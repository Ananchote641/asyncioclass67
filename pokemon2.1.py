import aiohttp
import asyncio

async def get_pokemon_with_ability(session, ability_url):
    async with session.get(ability_url) as resp:
        data = await resp.json()
        # ดึง Pokémon ที่มีความสามารถจาก API
        pokemon_list = data['pokemon']
        return [pokemon['pokemon']['name'] for pokemon in pokemon_list]

async def main():
    # URLs สำหรับความสามารถต่างๆ
    battle_armor_url = 'https://pokeapi.co/api/v2/ability/battle-armor'
    speed_boost_url = 'https://pokeapi.co/api/v2/ability/speed-boost'
    
    async with aiohttp.ClientSession() as session:
        # ดึงชื่อ Pokémon สำหรับแต่ละความสามารถ
        battle_armor_names = await get_pokemon_with_ability(session, battle_armor_url)
        speed_boost_names = await get_pokemon_with_ability(session, speed_boost_url)
        
        # พิมพ์ชื่อ Pokémon ทั้งสองความสามารถในบรรทัดเดียวกัน
        print("Pokémon with ability 'battle-armor':", ', '.join(battle_armor_names))
        print("Pokémon with ability 'speed-boost':", ', '.join(speed_boost_names))

asyncio.run(main())
