from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generateImage(sentence):
  
  amongFont = ImageFont.truetype('myFont.otf', 55)
  img = Image.open('dailyAmongus.png')
  I1 = ImageDraw.Draw(img)
  I1.text((330, 515), sentence, font=amongFont, fill=(255, 0, 0))
  img.save("currentAmong.png")