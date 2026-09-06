import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".jpg") and not sys.argv[1].endswith(".jpeg") and not sys.argv[1].endswith(".png"):
    sys.exit("Invalid input")
if not sys.argv[2].endswith(".jpg") and not sys.argv[2].endswith(".jpeg") and not sys.argv[2].endswith(".png"):
    sys.exit("Invalid output")
while True:
    if sys.argv[1].endswith(".jpeg") and not sys.argv[2].endswith(".jpeg"):
                sys.exit("Input and output have different extensions")
    elif sys.argv[1].endswith(".jpg") and not sys.argv[2].endswith(".jpg"):
        sys.exit("Input and output have different extensions")
    elif sys.argv[1].endswith(".png") and not sys.argv[2].endswith(".png"):
               sys.exit("Input and output have different extensions")
    else:
        break

try:
     shirt = Image.open("shirt.png")
     photo = Image.open(sys.argv[1])
except FileNotFoundError:
     sys.exit("Input does not exist")
fittedpho = ImageOps.fit(photo, shirt.size)
fittedpho.paste(shirt, shirt)
fittedpho.save(sys.argv[2])
