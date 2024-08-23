import aiohttp
import asyncio

async def get_pokemon_with_ability(session, ability_url):
    async with session.get(ability_url) as resp:
        data = await resp.json()
        # ดึง Pokémon ที่มีความสามารถ "battle-armor"
        pokemon_list = data['pokemon']
        return [pokemon['pokemon']['name'] for pokemon in pokemon_list]

async def main():
    url = 'https://pokeapi.co/api/v2/ability/battle-armor'
    
    async with aiohttp.ClientSession() as session:
        pokemon_names = await get_pokemon_with_ability(session, url)
        # พิมพ์ชื่อ Pokémon ในบรรทัดเดียวกัน
        print("Pokémon with ability 'battle-armor':", ', '.join(pokemon_names))

asyncio.run(main())
