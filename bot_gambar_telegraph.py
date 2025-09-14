import logging
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# GANTI dengan token bot kamu dari @BotFather
BOT_TOKEN = "GANTI_DENGAN_TOKEN_KAMU"

# Logging (buat debug kalau error)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Ambil file gambar resolusi tertinggi
        photo = update.message.photo[-1]
        file = await context.bot.get_file(photo.file_id)

        # Simpan sementara
        file_path = f"temp_{photo.file_id}.jpg"
        await file.download_to_drive(file_path)

        # Upload ke telegra.ph
        with open(file_path, 'rb') as img:
            response = requests.post(
                'https://telegra.ph/upload',
                files={'file': ('file.jpg', img, 'image/jpeg')}
            )

        # Hapus file lokal
        os.remove(file_path)

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and 'src' in result[0]:
                link = "https://telegra.ph" + result[0]['src']
                await update.message.reply_text(f"✅ Gambar berhasil diupload:\n{link}")
            else:
                await update.message.reply_text("❌ Gagal mendapatkan link.")
        else:
            await update.message.reply_text("❌ Upload gagal, server error.")

    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text("❌ Terjadi error saat proses upload.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handler untuk gambar
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("🤖 Bot aktif dan berjalan...")
    app.run_polling()
