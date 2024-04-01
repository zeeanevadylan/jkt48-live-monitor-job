import requests
from telegram import Bot

TELEGRAM_BOT_TOKEN = '7136457340:AAGMYpKlaByQPVppSrSP3Um6uLpP5S4KpSM'
TELEGRAM_CHANNEL_ID = '@idnshowroomJKT48'

def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)

def check_jkt48_live():
    try:
        response = requests.get('https://www.showroom-live.com/api/live/onair')
        live_data = response.json()
        for live in live_data['onairs']:
            if 'JKT48' in live['name']:
                member_name = live['name']
                viewers = live['viewers']
                active_viewers = live['activeViewers']
                comments = live['comments']
                participants = live['participants']
                new_followers = live['newFollowers']
                total_followers = live['totalFollowers']
                room_url = f"https://www.showroom-live.com/{live['roomUrl']}"
                
                message = f"{member_name} sedang siaran langsung! {room_url}\n👥 {viewers} penonton ({active_viewers} penonton aktif)*\n💬 {comments} komentar (oleh {participants} partisipan)\n💖 +{new_followers} followers baru ({total_followers} total)"
                send_telegram_message(message)
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        check_jkt48_live()
        sleep(300)  # 300 detik = 5 menit

if __name__ == "__main__":
    main()
