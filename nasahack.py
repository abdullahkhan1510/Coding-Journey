data = {
    "sites": [
        {"name": "Shackleton", "sunlight": 12, "earth": True},
        {"name": "Malapert", "sunlight": 7, "earth": True},
        {"name": "Haworth", "sunlight": 15, "earth": False},
        {"name": "Nobile", "sunlight": 10, "earth": True}
    ]
}
count = 0
for site in data["sites"]:
    if site["sunlight"] >= 10 and site["earth"]:
        print(site["name"])
        count = count+1
print(f"Total suitable sites: {count}")