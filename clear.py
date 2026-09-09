import os
import shutil
import time
import threading
import requests
from apscheduler.schedulers.background import BackgroundScheduler

# 🔁 Function to clear cache
def clear_cache_and_sessions():
    folders_to_clear = ['.cache', '__pycache__', '.git']
    for folder in folders_to_clear:
        print(f"Checking folder: {folder}")
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"✅ Cleared folder: {folder}")
            except Exception as e:
                print(f"❌ Error clearing {folder}: {e}")
        else:
            print(f"⚠️ Folder not found: {folder}")

# 🔁 Function to self-ping every 1 min
def self_ping():
    while True:
        try:
            print("🌐 Self-pinging...")
            # Replace with your actual hosted URL if available
            requests.get("https://tinyurl.com/3nzw3ffe")  # or your deployed URL
            print("✅ Ping successful")
        except Exception as e:
            print(f"❌ Ping failed: {e}")
        time.sleep(60)

# 🕒 Start scheduler
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(clear_cache_and_sessions, 'interval', minutes=60)
    scheduler.start()

# Start scheduler
start_scheduler()

# Start self-ping in a separate thread
threading.Thread(target=self_ping, daemon=True).start()

# Keep the script running
while True:
    time.sleep(60)
