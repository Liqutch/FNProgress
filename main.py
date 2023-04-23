try:
  from PIL import Image, ImageDraw
  import coloredlogs
  import datetime
  import requests
  import logging
  import time
  import json
  import os
except ImportError as e:
  print(f'{e.name} modülü yüklü değil. Lütfen programı çalıştırmadan önce "packages.bat" ile gerekli modülleri yükleyin.')
  time.sleep(5)
  exit()

os.system('cls')
os.system('TITLE FNProgress by Liqutch')
coloredlogs.logging.basicConfig(level=coloredlogs.logging.INFO)
log = coloredlogs.logging.getLogger(__name__)
coloredlogs.install(fmt="[%(asctime)s][%(levelname)s] %(message)s", datefmt="%H:%M:%S", logger=log)

if not os.path.isfile('settings.json'):       
  log.error('Ayarlar dosyası bulunamadı, program kapatılıyor...')
  time.sleep(5)
  exit()
try:
  with open("settings.json") as settings:
    load = json.load(settings)
    autoMode = load["auto_mode"]
    seasonBegin = load['seasonBegin']
    seasonEnd = load['seasonEnd']
except:
  log.error("Yapılandırma ayarlarını alırken bir sorun oluştu. Lütfen dosyanın düzgün yapılandırıldığından emin olun.")
  time.sleep(5)
  exit()

try:
  # Season Dates
  if autoMode == False:
    beginDate = datetime.datetime.strptime(seasonBegin, '%Y-%m-%dT%H:%M:%SZ')
    endDate = datetime.datetime.strptime(seasonEnd, '%Y-%m-%dT%H:%M:%SZ')
  else:
    request = requests.get("https://api.nitestats.com/v1/epic/modes")
    seasonBegin = request.json()["channels"]["client-events"]["states"][0]["state"]["seasonBegin"]
    seasonDisplayedEnd = request.json()["channels"]["client-events"]["states"][0]["state"]["seasonDisplayedEnd"]
    beginDate = datetime.datetime.strptime(seasonBegin, '%Y-%m-%dT%H:%M:%SZ')
    endDate = datetime.datetime.strptime(seasonDisplayedEnd, '%Y-%m-%dT%H:%M:%SZ')

  today = datetime.datetime.today()
  img = Image.open('./assets/background.png')
  total = (endDate - beginDate).days
  progress = (today - beginDate).days
except FileNotFoundError as e:
  log.error(f'Arkaplan görüntüsü bulunamadı. lütfen "background.png" olarak /assets klasörüne eklediğinizden emin olun.')
  time.sleep(5)
  exit()
except:
  log.error("Bilinmeyen bir hata oluştu. Lütfen daha sonra tekrar deneyin veya destek alın.")

try:
  draw = ImageDraw.Draw(img)
  x1, y1 = 100, 100
  x2, y2 = 1900, 300

  # Progress bar
  bar_x1, bar_y1 = x1, y1
  bar_x2 = bar_x1 + int((x2 - x1) * progress / total)
  bar_y2 = y2 - 1
  draw.rectangle([(bar_x1, bar_y1), (bar_x2, bar_y2)], outline=None, fill=(30, 75, 180))
  percent = ('%{:.2f}'.format((progress / total) * 100))
  log.info(f"Mevcut sezon {percent} tamamlandı. Bitmesine {total - progress} gün kaldı.")
  img.save(f"./outputs/{percent}.png")
  input()
except:
  log.error("İlerleme oluşturulurken bir hata oluştu. Lütfen daha sonra tekrar deneyin veya destek alın.")
