import re
url = input("URL: ").strip()

username = re.sub(r"^((http|https)://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")