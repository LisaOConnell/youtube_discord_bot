import feedparser
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

# Replace with your desired YouTubers
CHANNELS = {
    "Monster Hunter": "UCVS0xBpOtXBAl12rdG67-OQ",
    "RageGamingVideos": "UC2nMSE3t71qC8sG06WSJnMg",
}

posted_video_ids = set()

def check_new_videos():
    for name, channel_id in CHANNELS.items():
        feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
        feed = feedparser.parse(feed_url)
        if not feed.entries:
            continue
        latest_video = feed.entries[0]
        video_id = latest_video.yt_videoid
        if video_id not in posted_video_ids:
            posted_video_ids.add(video_id)
            message = f"🍕🍕🍕 **{name}** just served us a new video!\n Watch it while it is piping hot! \n👨‍🍳 **{latest_video.title}**\n🍕🍕🍕 {latest_video.link}"
            requests.post(WEBHOOK_URL, json={"content": message})
            print(f"Posted: {latest_video.title}")

def run_bot():
    while True:
        check_new_videos()
        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    print("Bot is running...")
    run_bot()