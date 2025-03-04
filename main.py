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
