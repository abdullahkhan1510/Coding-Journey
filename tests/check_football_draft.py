"""Run game logic regressions using macOS JavaScriptCore, without a browser."""
from pathlib import Path
import json,re,subprocess,tempfile
root=Path(__file__).resolve().parents[1]
html=(root/'football_draft.html').read_text()
source=re.search(r'<script>(.*?)</script>',html,re.S)[1]
source=source[:source.index("    $('#playerCount').onchange=")]
prefix='''const nodes=new Map();
const document={addEventListener(){},querySelector(selector){if(!nodes.has(selector))nodes.set(selector,{value:'',innerHTML:'',querySelectorAll(){return []},classList:{add(){},remove(){},toggle(){},contains(){return true}}});return nodes.get(selector)}};
function assert(value,message){if(!value)throw new Error(message)}
'''
tests=r'''
const realRenderCards=renderCards;
renderGame=()=>{};renderTeams=()=>{};renderSeason=()=>{};toast=()=>{};
let drafts=0;
for(const category of categories){
 for(let count=2;count<=5;count++){
  const pool=availableFor(category.id);
  if(!canStartHistoricalDraft(pool,count))continue;
  for(let trial=0;trial<50;trial++){
   state.category=category.id;state.count=count;state.round=0;state.turn=0;state.finished=false;
   state.available=pool.map((p,i)=>({...p,identity:i}));
   state.teams=Array.from({length:count},(_,i)=>({name:`Manager ${i}`,clubName:premierClubs[i],formation:'4-3-3',picks:[]}));
   refreshRoundPool();
   for(let round=0;round<11;round++){
    const drawn=state.roundTeam;
    assert(state.roundPool.length>=count,'Insufficient real squad players');
    for(let pick=0;pick<count;pick++){
     const player=state.roundPool[Math.floor(Math.random()*state.roundPool.length)];
     assert(player.editions.length===1,'Alternate season offered');
     assert(player.editions[0].season===seasonKey(drawn.season),'Season mismatch');
     assert(player.editions[0].rating===drawn.ratings[player.name],'Wrong rating');
     document.querySelector(`#edition-${player.identity}`).value='999'; // DOM tampering must not affect edition.
     const team=currentTeam();
     draft(player.identity);
     assert(team.picks.at(-1).edition.season===seasonKey(drawn.season),'Draft accepted wrong season');
     assert(team.picks.at(-1).edition.club===drawn.name,'Wrong club');
    }
   }
   assert(state.teams.every(t=>t.picks.length===11),'Incomplete XI');
   assert(new Set(state.teams.flatMap(t=>t.picks.map(p=>p.name))).size===count*11,'Duplicate player');
   drafts++;
  }
 }
}
const savedDraftTeams=state.teams;
// Batch playback: one fixture per club, bounded by manager count, no lost games.
for(let count=2;count<=5;count++){
 state.teams=Array.from({length:count},(_,i)=>({clubName:`User ${i}`}));
 const fixtures=[];
 for(let round=0;round<3;round++)for(let i=0;i<count;i++)fixtures.push({home:`User ${i}`,away:`Opponent ${i}`,round});
 state.matchQueue=[...fixtures];
 const shown=[];
 while(state.matchQueue.length){
  const batch=takeBroadcastBatch();
  assert(batch.length===count,'Expected one simultaneous match per manager');
  assert(new Set(batch.flatMap(f=>[f.home,f.away])).size===batch.length*2,'Club appears twice in broadcast');
  shown.push(...batch);
 }
 assert(shown.length===fixtures.length&&new Set(shown).size===fixtures.length,'Fixture lost or replayed');
}
state.teams=[{clubName:'Aston Villa'},{clubName:'Arsenal'}];
const duplicateVilla=[{home:'Aston Villa',away:'Chelsea'},{home:'Liverpool',away:'Aston Villa'},{home:'Arsenal',away:'Everton'}];
state.matchQueue=[...duplicateVilla];
let batch=takeBroadcastBatch();
assert(batch.length===2&&batch[0]===duplicateVilla[0]&&batch[1]===duplicateVilla[2],'Repeated Aston Villa fixture was not deferred');
assert(state.matchQueue.length===1&&state.matchQueue[0]===duplicateVilla[1],'Deferred fixture lost');
state.matchQueue=[{home:'Aston Villa',away:'Arsenal'},{home:'Arsenal',away:'Chelsea'}];
batch=takeBroadcastBatch();assert(batch.length===1,'Head-to-head duplicated across managers');
state.matchQueue=[{home:'Aston Villa',away:'Chelsea'},{home:'Arsenal',away:'Chelsea'},{home:'Arsenal',away:'Everton'}];
batch=takeBroadcastBatch();assert(batch.length===1,'Conflicting or out-of-order fixture broadcast');
// Restore a completed draft for the full-season regression below.
state.teams=savedDraftTeams;
const united=historicalTeams.find(s=>s.name==='Manchester United'&&s.season==='2008/2009');
assert(editionForTeam(players.find(p=>p.name==='Cristiano Ronaldo'),united).season==='2008-09','Missing 2008-09 Ronaldo');
let rejected=false;try{editionForTeam(players.find(p=>p.name==='Lionel Messi'),united)}catch(e){rejected=true}assert(rejected,'Ineligible player accepted');
for(const [club,excluded] of [['Real Madrid','Iker Casillas'],['Barcelona','Thierry Henry'],['Barcelona','Cesc Fàbregas'],['Manchester City','Sergio Agüero'],['Liverpool','Steven Gerrard'],['Liverpool','Xabi Alonso'],['Chelsea','Eden Hazard'],['Chelsea','Nicolas Anelka']])assert(!historicalTeams.find(s=>s.name===club).members.includes(excluded),`Anachronistic player ${excluded}`);
state.roundTeam=united;state.roundPool=[{...players.find(p=>p.name==='Cristiano Ronaldo'),identity:0,editions:[editionForTeam(players.find(p=>p.name==='Cristiano Ronaldo'),united)]}];
document.querySelector('#search').value='';realRenderCards();
assert(document.querySelector('#cards').innerHTML.includes('disabled'),'Season dropdown is not locked');
assert(!document.querySelector('#cards').innerHTML.includes('2003-04'),'Unrelated edition rendered');
// Exercise a full simulation with the last completed draft.
state.season=createSeason();state.season.playerStats=new Map();state.seasonMonth=0;state.janDone=false;
state.teams.forEach(t=>t.picks.forEach(statFor));setupSeasonFixtures();
for(let month=0;month<12;month++){
 if(month===5){for(const team of state.teams)completeTransfer(team,0,'random',true);state.janDone=true}
 playMonth(month,true);
}
assert(state.seasonMonth===12,'Season simulation incomplete');
assert(state.season.winners['Champions League'],'Missing UCL winner');
assert(state.season.winners['FA Cup'],'Missing FA Cup winner');
assert(state.season.log.length>500,'Season fixtures did not run');
print(`PASS: ${drafts} complete randomized drafts, broadcast batch regressions, locked editions, roster exclusions, season simulation (${state.season.log.length} matches).`);
print(JSON.stringify({clubs:[...new Set([...premierClubs,...europeanClubs.filter(n=>!n.startsWith('Fictional')),...extraCupClubs,...historicalTeams.map(s=>s.name)])],categories:categories.map(c=>({category:c.id,players:availableFor(c.id).length,managers:[2,3,4,5].filter(n=>canStartHistoricalDraft(availableFor(c.id),n))}))}));
'''
with tempfile.NamedTemporaryFile('w',suffix='.js') as f:
 f.write(prefix+source+tests);f.flush()
 result=subprocess.run(['/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc',f.name],check=True,capture_output=True,text=True)
 print(result.stdout.splitlines()[0])
 report=json.loads(result.stdout.splitlines()[1])
manifest=json.loads((root/'assets/club-badges/sources.json').read_text())
assert {entry['club'] for entry in manifest.values()}==set(report['clubs']),'Incomplete real club badge coverage'
for slug in manifest:
 assert (root/f'assets/club-badges/{slug}.png').read_bytes().startswith(b'\x89PNG\r\n\x1a\n'),slug
print(f'PASS: {len(manifest)} real club badge PNG assets verified.')
