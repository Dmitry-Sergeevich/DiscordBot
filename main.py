import asyncio
from datetime import datetime

import requests
import discord
from discord.ext import commands

TOKEN = '{токен}'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.command(name='погода')
async def weather(ctx, city: str):
    try:
        url = f"https://api.api-ninjas.com/v1/weather?city={city}"

        headers = {
            'X-Api-Key': '0PNG7AUgyjT5fmJeKkiWeQ==QBYPx9rneDMTlNaY'
        }

        response = requests.request("GET", url, headers=headers)
        data = response.json()
        cur_temp = data["temp"]
        feels_temp = data["feels_like"]

        await ctx.message.reply(
            f"Сегодня {datetime.now().strftime('%d.%m.%Y %H:%M')} \nПогода в городе: {city}\nТемпература: {cur_temp}°C \nОщущается как: {feels_temp}°C\n")
    except:
        await ctx.reply("Что-то не так с названием города...")


async def main():
    await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())