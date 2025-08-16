# Student Data Analyzer

Bu proje, öğrencilerin temel bilgilerini (ad, soyad, yaş, şehir, not) kaydedip analiz eden bir Python uygulamasıdır. Ayrıca özet istatistikler ve grafikler üreterek veri görselleştirmesi yapar.

## Özellikler

- JSON formatında öğrenci verisi kaydetme ve okuma
- Not ve yaş bilgilerine göre filtreleme
- Ortalama, en yüksek ve en düşük notların hesaplanması
- CSV formatında sonuçların kaydedilmesi
- Not dağılımı ve yaş-not ilişkisi için görselleştirme

## Kurulum

1. Projeyi klonlayın veya indirin.
2. Gerekli kütüphaneleri yükleyin:
pip install -r requirements.txt

3. Verilerin bulunduğu klasörü oluşturun:
mkdir -p student_data/data

4. `data.json` dosyasını boş olarak oluşturabilirsiniz:
echo "[]" > student_data/data/data.json

## Kullanım

1. Programı çalıştırın:
python main.py

2. Veri girişi yapmak isteyip istemediğiniz sorulacak (Y/N):
   - Y girerseniz, ad, soyad, yaş, şehir ve not bilgilerini girebilirsiniz.
   - N girerseniz, mevcut verilerle analize geçilir.

3. Analiz sonuçları `student_data/results.csv` dosyasına kaydedilecektir.

4. Grafikler görmek isteyip istemediğiniz sorulacak (Y/N):
   - 1 -> Not dağılımı
   - 2 -> Yaş ve not dağılımı
   - 3 -> Not dağılımı ve ortalama çizgisi
   - Başka bir sayı girerseniz, uyarı mesajı verilir ve tekrar sorulur.

## Gereksinimler

- Python 3.8 veya üstü
- Pandas
- Matplotlib
- Seaborn
