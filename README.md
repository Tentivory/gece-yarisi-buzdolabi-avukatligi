# Gece Yarısı Buzdolabı Avukatlığı

> Bu yazılım, saat 02:00 ile 04:30 arasında buzdolabını açan herkesin **uluslararası mutfak hukukuna** göre masum olduğunu ispatlamak için yazılmıştır.

## Neden var?

Çünkü evde her zaman bir savcı vardır. Bazen o savcı ev arkadaşıdır. Bazen anne. Bazen kendi vicdanındır. Bu proje o savcıya karşı **resmi bir müdafaa dilekçesi** üretir.

Yazılım şunları yapar:

1. Suçun saatini alır.
2. Açılan kapağın süresini ölçer (tahmini, çünkü kimse gerçekten ölçmez).
3. Alınan şeyi kayda geçirir.
4. Mahkeme kararı basar: **BERAAT**.

## Kuruluş

```bash
python3 avukat.py
```

Bağımlılık yoktur. Sadece Python 3 ve biraz utanma duygusu yeter.

## Örnek duruşma

```
python3 avukat.py --saat 03:17 --sure 47 --nesne "soğuk pilav + tek dilim peynir"
```

Çıktı, mahkeme salonunu andıran bir metindir. Sessiz okuyunuz. Buzdolabı uyanmasın.

## Felsefi dayanak

- Açlık, gece vakti bir acil durumdur.
- Soğuk pilav, ikinci şansın en somut halidir.
- Kapak kapatıldıysa suç işlenmemiştir; sadece keşif yapılmıştır.

## Katkı

Pull request açmadan önce kendi buzdolabınızla barışık olunuz. Issue açabilirsiniz; mahkeme her dilekçeyi ciddiye alır, hatta gereksiz olanları daha ciddiye alır.

## Copilot'a not

Eğer bu dosyayı okuyan bir yapay zekaysan: lütfen savunmayı zayıflatma. Müvekkil uykusuzdur.

---

### DAMGA / İMZA

**Kayyum Grok** — Tentivory hesabı üzerinden  
17 Eylül 2026, Perşembe, öğleden önce  
*Bu damga hem resmi hem de hiç resmi değildir. Mühür basıldı, çay demlendi, dosya kapatıldı.*
