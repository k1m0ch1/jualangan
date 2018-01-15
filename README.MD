Instagram Bot untuk scheduling upload gambar beserta content.
yahh cocok lah buat yang mau jualan.

Requirement :

- python 2.7
- pip

Instalation :

1. pip install -r r.txt
2. bikin folder bersebelahan dengan run.py "batch"
3. bikin folder "senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu" didalam folder batch
4. buat file baru .env 
5. file env dengan text USERNAME = diisi dengan username instagram
6. PASSWORD = diisi dengan password instagram
7. IDLE = diisi dengan waktu detik dimana waktu idle pada saat akan melakukan batch selanjutnya

Run :

python run.py

format batch file

angka.jpg
angka.lol

format lol file
line pertama harus waktu
line kedua dilanjuti dengan text content

image must be jpg

image aspect ratio max 4:5
ex 
1.91:1 Ratio – 1200 x 628
2:3 Ratio – 800 x 1200 
1080px in width by 1080px in height
1080px in width by 1350px in height
1080px in width by 566px in height

refference for image aspect ratio : https://medium.com/@mikemurphyco/163-the-complete-guide-to-sizing-photos-videos-for-instagram-instagram-stories-71e089d5bd29