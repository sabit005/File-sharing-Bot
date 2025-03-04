from bot import Bot  # এখানে 'Bot' ইমপোর্ট করছি
import asyncio

if __name__ == "__main__":
    bot = Bot()  # এখানে 'Bot' অবজেক্ট তৈরি করছি
    asyncio.run(bot.start())
