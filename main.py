import random
import requests

def generate_sets():
  first_group = random.sample(range(1, 732), 5)
  remaining = list(set(range(1, 732)) - set(first_group))
  second_group = random.sample(remaining, 5)
  return first_group, second_group

def get_hero_info(id):
  data = requests.get(f"https://superheroapi.com/api/2183127771827858/{id}").json()
  powerstats = data.get("powerstats")
  strength = powerstats.get("strength")
  speed = powerstats.get("speed")
  power = powerstats.get("power")
  combat = powerstats.get("combat")
  intelligence = powerstats.get("intelligence")
  stamina = random.randint(0,10)
  durability = powerstats.get("durability")

  return data.get("name"), intelligence, durability, strength, speed, power, combat

def get_hp(id):
  name, intelligence, durability, strength, speed, power, combat = get_hero_info(id)


  



a, b = generate_sets()
get_hero_info(a[0])
