from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("meme(2).jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", 160)

def drawTextWithOutline(text, x, y):
    draw.text((x-2, y-2), text,(0,0,0),font=font)
    draw.text((x+2, y-2), text,(0,0,0),font=font)
    draw.text((x+2, y+2), text,(0,0,0),font=font)
    draw.text((x-2, y+2), text,(0,0,0),font=font)
    draw.text((x, y), text, (255,255,255), font=font)
    return

text = "Are we centered yet?"

drawTextWithOutline(text, img.width/2-250 , img.height*4/6)

img.save("out.jpg")