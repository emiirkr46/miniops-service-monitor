# MiniOps – Servis İzleme Sistemi

## 1. Proje Hakkında

MiniOps, web servislerinin erişilebilirliğini ve yanıt sürelerini kontrol etmek amacıyla geliştirilen Python tabanlı bir servis izleme uygulamasıdır.

Uygulama, kullanıcıların takip etmek istedikleri web servislerini sisteme eklemelerine ve bu servislerin çalışma durumlarını manuel olarak kontrol etmelerine olanak sağlar.

## 2. Projenin Amacı

Web servislerinde meydana gelebilecek erişim problemlerinin tespit edilmesi ve servislerin durum bilgilerinin kullanıcıya anlaşılır şekilde sunulması amaçlanmaktadır.

## 3. Hedef Kullanıcılar

- Yazılım geliştiriciler
- Sistem ve ağ yöneticileri
- Web servislerinin erişilebilirliğini takip etmek isteyen kullanıcılar

## 4. Kullanılan Teknolojiler

- Python
- Streamlit
- Requests
- JSON
- GitHub ve GitHub Projects

## 5. Geliştirilen Özellikler

**1. Servis Ekleme**

Kullanıcı, takip etmek istediği web servisinin adını ve URL adresini sisteme ekleyebilir. Eklenen servisler JSON dosyasında saklanır.

**2. HTTP Durum Kodu ve Yanıt Süresi Kontrolü**

Kullanıcı, kayıtlı servisleri manuel olarak kontrol edebilir. HTTP durum kodu ve yanıt süresi milisaniye cinsinden görüntülenir. Erişim hataları kullanıcıya bildirilir.

## 6. Proje Takip Panosu

Projenin görevleri, geliştirme aşamaları ve çalışma durumları GitHub Projects üzerinden takip edilmektedir.

[MiniOps Geliştirme Takip Panosu](https://github.com/users/emiirkr46/projects/1/views/1)

## 7. Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için Python kurulu olmalıdır.

Depoyu bilgisayarınıza indirin:

```bash
git clone https://github.com/emiirkr46/miniops-service-monitor.git
cd miniops-service-monitor
```

Gerekli Python paketlerini yükleyin:

```bash
pip install -r requirements.txt
```

Uygulamayı başlatın:

```bash
streamlit run app.py
```

## 8. Uygulama Özelliklerinin Test Edilmesi

**Test 1 – Servis Ekleme**

1. Uygulamayı başlatın.
2. Servis adı alanına "Örnek Servis" yazın.
3. URL alanına `https://example.com` adresini girin.
4. Servis Ekle butonuna basın.
5. Servisin kayıtlı servisler listesinde görüntülendiğini kontrol edin.
6. Uygulamayı yeniden başlatarak kaydın korunup korunmadığını kontrol edin.

Beklenen sonuç: Servis başarıyla eklenmeli ve `services.json` dosyasında saklanmalıdır.

**Test 2 – HTTP Durum Kodu ve Yanıt Süresi**

1. Kayıtlı servisler arasından test etmek istediğiniz servisi seçin.
2. Kontrol Et butonuna basın.
3. Görüntülenen HTTP durum kodunu ve yanıt süresini inceleyin.

Beklenen sonuç: Servisin HTTP durum kodu ve yanıt süresi milisaniye cinsinden gösterilmelidir. Erişim hatalarında kullanıcıya hata mesajı sunulmalıdır.

## 9. Geliştirme Planı

Projenin sonraki aşamalarında aşağıdaki özelliklerin geliştirilmesi planlanmaktadır:

- Servis kontrol geçmişinin kaydedilmesi
- Otomatik periyodik servis kontrolü
- Başarısız servisler için uyarı sistemi

Bu özellikler mevcut sürümde henüz tamamlanmamıştır.
