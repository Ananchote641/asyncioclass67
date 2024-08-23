import aiohttp
import asyncio
import time

async def get_pokemon_with_ability(session, ability_url):
    async with session.get(ability_url) as resp:
        data = await resp.json()
        # ดึง Pokémon ที่มีความสามารถจาก API
        pokemon_list = data['pokemon']
        return [pokemon['pokemon']['name'] for pokemon in pokemon_list]

async def fetch_and_time(session, ability_url, label):
    # เริ่มจับเวลา
    start_time = time.perf_counter()
    
    # ดึงข้อมูล Pokémon
    names = await get_pokemon_with_ability(session, ability_url)
    
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    
    # คำนวณจำนวน Pokémon
    number_of_pokemon = len(names)
    
    # พิมพ์ผลลัพธ์
    print(f"Number of Pokémon with ability '{label}': {number_of_pokemon}")
    print(f"Pokémon with ability '{label}':", ', '.join(names))
    print(f"Time taken for '{label}': {elapsed_time:.2f} seconds")

async def main():
    battle_armor_url = 'https://pokeapi.co/api/v2/ability/battle-armor'
    speed_boost_url = 'https://pokeapi.co/api/v2/ability/speed-boost'
    
    async with aiohttp.ClientSession() as session:
        # สร้าง tasks 
        battle_armor_task = asyncio.create_task(fetch_and_time(session, battle_armor_url, 'battle-armor'))
        speed_boost_task = asyncio.create_task(fetch_and_time(session, speed_boost_url, 'speed-boost'))
        
        # รอให้ tasks เสร็จสิ้น
        await battle_armor_task
        await speed_boost_task

asyncio.run(main())
