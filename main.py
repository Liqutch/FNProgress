from PIL import Image, ImageDraw, ImageFont
import datetime

# Season Dates
beginDate = datetime.datetime.strptime("2023-03-09T13:00:00Z", '%Y-%m-%dT%H:%M:%SZ')
endDate = datetime.datetime.strptime("2023-06-3T12:00:00Z", '%Y-%m-%dT%H:%M:%SZ')
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
img.save("./outputs/progress.png")

# Fullscreen
background = Image.new('RGB', (3840, 2160), (4, 12, 59))
x = int((3840 - 2000) / 2)
y = int((2160 - 400) / 2)
background.paste(img, (x, y), img)
background.save("./outputs/fullscreen.png")
input("Çıkmak için enter'a basın...\n")