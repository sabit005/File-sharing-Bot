from pyrogram import Client

class Bot(Client):
    def __init__(self):
        super().__init__(
            "my_bot",
            bot_token="YOUR_BOT_TOKEN",
            api_id=123456,  # তোমার API ID বসাও
            api_hash="YOUR_API_HASH"  # তোমার API HASH বসাও
        )

    async def start(self):
        if hasattr(self, "me") and self.me:  # ✅ Bot কানেক্টেড থাকলে আবার চালু করবে না
            print("⚡ Bot is already running!")
            return
        
        await super().start()
        self.me = await self.get_me()  # Bot তথ্য সেভ করছি
        print(f"✅ Bot started as {self.me.username}")
from bot import Bot  # 'Bot' ক্লাস ইমপোর্ট করছি
import asyncio

async def main():
    bot = Bot()  # Bot অবজেক্ট তৈরি করছি
    
    if not bot.is_connected:  # ✅ Bot আগে কানেক্টেড কিনা চেক করছি
        await bot.start()  
        print("✅ Bot started successfully!")
    else:
        print("⚡ Bot is already running!")

# 🔹 Ensure the script runs only when executed directly
if __name__ == "__main__":
    asyncio.run(main())
