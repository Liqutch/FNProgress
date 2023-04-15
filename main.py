from PIL import Image, ImageDraw, ImageFont
import datetime
import json

with open("settings.json") as settings:
  load = json.load(settings)
  seasonBegin = load['seasonBegin']
  seasonEnd = load['seasonEnd']

# Season Dates
beginDate = datetime.datetime.strptime(seasonBegin, '%Y-%m-%dT%H:%M:%SZ')
endDate = datetime.datetime.strptime(seasonEnd, '%Y-%m-%dT%H:%M:%SZ')
today = datetime.datetime.today()
img = Image.open('./assets/background.png')
total = (endDate - beginDate).days
progress = (today - beginDate).days

draw = ImageDraw.Draw(img)
x1, y1 = 100, 100
x2, y2 = 1900, 300

# Progress bar
bar_x1, bar_y1 = x1, y1
bar_x2 = bar_x1 + int((x2 - x1) * progress / total)
bar_y2 = y2 - 1
draw.rectangle([(bar_x1, bar_y1), (bar_x2, bar_y2)], outline=None, fill=(30, 75, 180))
percent = ('%{:.2f}'.format((progress / total) * 100))
print(f"4. Bölüm 2. Sezon {percent} tamamlandı. Bitmesine {total - progress} gün var.")
img.save(f"./outputs/{percent}.png")
input("Çıkmak için enter'a basın...\n")
