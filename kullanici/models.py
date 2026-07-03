from django.db import models
# 1. MARKA TABLOSU
class Marka(models.Model):
    ad = models.CharField(max_length=100, verbose_name="Marka Adı")
    iletisim_kisi = models.CharField(max_length=100, verbose_name="İletişim Kurulacak Kişi")
    eposta = models.EmailField(unique=True, verbose_name="E-Posta Adresi")
    aktif_mi = models.BooleanField(default=True, verbose_name="Aktif Müşteri mi?")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad

# 2. İÇERİK ÜRETİCİSİ (CREATOR) TABLOSU
class Uretici(models.Model):
    ad_soyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    instagram_kullanici_adi = models.CharField(max_length=50, blank=True, null=True)
    tiktok_kullanici_adi = models.CharField(max_length=50, blank=True, null=True)
    portfolyo_linki = models.URLField(blank=True, null=True, verbose_name="Portfolyo / Medya Kiti")
    
    def __str__(self):
        return self.ad_soyad

# 3. PROJE / KAMPANYA TABLOSU (İlişkisel Tablo)
class Proje(models.Model):
    # Foreign Key (Yabancı Anahtar) ile diğer tabloları buraya bağlıyoruz
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, related_name='projeler')
    uretici = models.ForeignKey(Uretici, on_delete=models.SET_NULL, null=True, related_name='projeler')
    
    baslik = models.CharField(max_length=150, verbose_name="Proje Başlığı")
    teslim_tarihi = models.DateField(verbose_name="Son Teslim Tarihi")
    butce = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Bütçe (TL)")
    tamamlandi_mi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marka.ad} - {self.uretici.ad_soyad} Projesi"
# Create your models here.
