votes = {}

print("Enter your votes (Press Ctrl+D to stop):")

while True:
    try:
        # Prompt user for a name and normalize it to uppercase
        candidate = input("Vote for: ").strip().upper()
        
        if not candidate:
            continue

        # Logic: If name exists, add 1. If not, start at 1.
        votes[candidate] = votes.get(candidate, 0) + 1

    except EOFError:
        print("\n--- Final Results ---")
        break

# Sort alphabetically by candidate name
for name in sorted(votes):
    print(f"{name}: {votes[name]} votes")