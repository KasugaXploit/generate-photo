1. ✅ Buka Termux dan update dulu
pkg update && pkg upgrade

2. ✅ Install Python & pip
pkg install python
pip install --upgrade pip

3. ✅ Install module yang dibutuhkan
pip install python-telegram-bot requests

4. ✅ Buat file bot-nya
nano bot_gambar_telegraph.py

-Paste script bot di atas ke dalamnya
-Ganti bagian:
"BOT_TOKEN = "GANTI_DENGAN_TOKEN_KAMU""
→ dengan token bot kamu dari @BotFather

Simpan:
Tekan CTRL + O lalu Enter
Tekan CTRL + X untuk keluar

5. ✅ Jalankan bot
python bot_gambar_telegraph.py

Kalau muncul:

🤖 Bot aktif dan berjalan...
Artinya bot kamu sudah aktif dan siap terima gambar.

6. ✅ Tes kirim gambar ke bot kamu

-Buka Telegram
-Cari bot kamu (dengan username yang kamu buat)
-Kirim gambar
-Bot akan balas dengan link https://telegra.ph/.

🧠 Tambahan (opsional):
Kalau mau bot jalan terus walau Termux ditutup:
pkg install tmux
tmux
python bot_gambar_telegraph.py
# Untuk keluar tmux tanpa matikan bot: tekan CTRL + B, lalu D
