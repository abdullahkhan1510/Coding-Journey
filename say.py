import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    text = input("Input: ")
    font_choice = random.choice(fonts)
    figlet.setFont(font=font_choice)
    print("Output: ")
    print(figlet.renderText(text))
elif len(sys.argv) == 3:
    font = sys.argv[2]
    if font in fonts:
            font_choice = sys.argv[2]
    else:
        sys.exit("Invalid usage")
    text = input("Input: ")
    figlet.setFont(font=font_choice)
    print("Output: ")
    print(figlet.renderText(text))
