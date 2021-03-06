Jualan Gan
======

Alternatif tools untuk jualan di instagram, tools untuk auto upload gambar ke instagram dengan rentan waktu yang dibutuhkan

### Requirement 

- python 2.7
- pip

### Instalation 

1. pip install -r r.txt
2. bikin folder bersebelahan dengan run.py "batch"
3. bikin folder "senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu" didalam folder batch

```python
	- run.py
	- batch
	   |-senin
	   |-selasa
	   |-rabu
	   |-kamis
	   |-jumat
	   |-sabtu
	   |-minggu
```

### Format ENV file

```python
USERNAME = 
PASSWORD = 
IDLE = 
```

USERNAME diisi dengan username instagram
PASSWORD diisi dengan password instagram
IDLE adalah waktu standby sebelum cek jadwal

### Konfigurasi jadwal

- Didalam folder hari terdapat 2 tipe format file yang mewakili 1 posting
- Filter tersebut adalah file gambar (berupa jpg dengan aspect ratiomax 4:5) 
- dan file dengan extension lol dengan isi filenya adalah 
- pada baris pertama gunakan waktu yang akan di post pada hari tersebut
- dan barus kedua adalah text yang akan di sertakan di gambar

Contoh Listing Direktori :

```python
	- run.py
	- batch
	|-senin
	   |- 1.jpg
	   |- 1.lol
	   |- 2.jpg
	   |- 2.lol
	|-selasa
	|-rabu
	|-kamis
	|-jumat
	|-sabtu
	   |- 1.jpg
	   |- 1.lol
	|-minggu
```

Contoh Format dari lol file :

```text
10:08
mau tas keren ini ? muat laptop14 inch, anti air, high capacity, cocok untuk dailly order/tanya product ? whatsapp 080808080808 (RESELLER & DROPSHIP WELLCOME) : MJOLNIR NAVY 239.OOO (free ongkir ) (PENGIRIMAN BANDUNG) order bisa langsung hubungi
```

### Penggunaan Penjadwalan file upload

```python
python run.py
```

### Penggunaan Delete mass file

Fungsinya adalah menghapus massal post instagram paling akhir dari belakang, sebanyak nilai yang di inputkan
*note: fungsi ini akan ada delay setiap penghapusan post, untuk menghindari teridentifikasi spam oleh instagram
**note: gunakan fungsi ini terpisah dengan fungsi penjadwalan 

```python
python del.py banyakpost
```

### Referensi Gambar Aspect Ratio yang di perbolehkan oleh Instagram

image aspect ratio max 4:5

ex 

1.91:1 Ratio – 1200 x 628

2:3 Ratio – 800 x 1200 

1080px in width by 1080px in height

1080px in width by 1350px in height

1080px in width by 566px in height

refference untuk image aspect ratio : https://medium.com/@mikemurphyco/163-the-complete-guide-to-sizing-photos-videos-for-instagram-instagram-stories-71e089d5bd29

## Fitur Selanjutnya

- Touch up Readme
- Auto Like dari feed home [code=GBLK]
- GBLK confuse spam filter, Auto like ini bakal dipasang di si belegug, pada saat si belegug ga ada kerjaan, dia bakal cek feed pertama dan selain post dia, dia bakal like, lalu dia bakal cek lagi kerjaan, kalo ga ada kerjaan lagi, dia bakal like post ke dua.
- Auto follow 
- Auto comment dari salah satu akun setiap kali orang tersebut melakukan posting baru
- Mantengin salah satu akun, cek salah 5 post terbaru nya kalo commentnya lebih dari 100 biji posting auto comment [code=CCD]
- CCD confuse spam filter, comment pertama ga langsung di post, next comment ada delay (1-15 detik)
- Mantengin 
[DONE] Auto delete posting lama