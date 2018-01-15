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

image must be jpg, with aspect ratio 4:5