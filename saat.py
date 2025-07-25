from pyrubi import Client
import time
import datetime
import pytz
import socket

GUID = "g0GH2ZC084be310ee810a251ae776d9b"
CLIENT_TOKEN = "توکن-حساب-روبیکا-شما"
BASE_TITLE = ""

def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(f"❌ خطای اتصال اینترنت: {ex}")
        return False

def update_group_title(client):
    try:
        tehran_time = datetime.datetime.now(pytz.timezone("Asia/Tehran"))
        current_time = tehran_time.strftime("VIPZEXNET%H:%M:%S")
        fancy_numbers = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
        fancy_time = current_time.translate(fancy_numbers)

        title = f"{BASE_TITLE} {fancy_time}".strip()
        client.edit_group_info(object_guid=GUID, title=title)
        print(f"🔄 عنوان گروه آپدیت شد: {title} ({tehran_time.strftime('%Y-%m-%d %H:%M:%S')})")
    except Exception as e:
        print(f"❌ خطا در به‌روزرسانی: {e}")

def main():
    print("🤖 ربات شروع به کار کرد...")
    
    if not check_internet():
        print("❌ اینترنت وصل نیست. لطفاً اتصال را بررسی کنید و مجدداً اجرا کنید.")
        return
    
    try:
        client = Client(CLIENT_TOKEN)
    except Exception as e:
        print(f"❌ خطا در ساخت کلاینت روبیکا: {e}")
        return

    try:
        while True:
            update_group_title(client)
            time.sleep(1)  # هر ۱ ثانیه آپدیت
    except KeyboardInterrupt:
        print("❎ ربات توسط کاربر متوقف شد.")
    except Exception as e:
        print(f"❌ خطای ناگهانی: {e}")

if name == "main":
    main()