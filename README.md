# Fortnite Sezon İlerlemesi
Bu program, mevcut Fortnite sezonunun bitiş tarihine ne kadar kaldığını günüyle, yüzdesiyle hesaplar ve size bu ilerlemeyi resim olarak çıkartır.

# Nasıl Kullanılır:
- [Python](https://www.python.org/downloads/) 3.6 ve üstü bir sürümün yüklü ve PATH'e eklenmiş olduğundan emin olun.
- `packages.bat` adlı dosyayı çalıştırarak gerekli modülleri yükleyin.
- `start.bat` adlı dosyayı çalıştırarak programı başlatın
- Program çalıştıktan sonra resimler `/outputs` klasöründe olacak.
# Yapılandırma:
- Sezonun başlangıç ve bitiş tarihlerini otomatik olarak tespit etmek için `"auto_mode": true` olarak ayarlanmıştır. Eğer manuel olarak tarihleri girmek isterseniz `settings.json` adlı dosyayı açın, değeri false olarak ayarlayın ve başlangıç ve bitiş tarihlerini yazın. Not: Sezon bittiğinde yeni sezonun tarihlerini girmeyi unutmayın.
- Not: [background.psd](assets/background.psd) ile sezonun adını güncelleyip, eski olan [background.png](assets/background.png) ile değiştirebilirsiniz.

# Destek
Eğer bir problemle karşılaşıyorsanız, aşağıdaki bağlantılardan yardım alabilirsiniz.

[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/341886629142593537)
[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Liqutch)
[![Website](https://img.shields.io/badge/🔗%20LIQUTCH.DEV-white.svg?style=for-the-badge&logo=link&logoColor=black&color=EDF2F7)](https://liqutch.dev)

# Kaynaklar
- Arkaplan görüntüsü [@FNProgress](https://twitter.com/FNProgress) tarafından alınmış ve değiştirilmiştir.
- Sezon başlangıç-bitiş tarihleri için [NiteStats API](https://nitestats.com/) kullanılmıştır.
