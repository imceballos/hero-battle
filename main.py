import random
import requests

def generate_sets():
  first_group = random.sample(range(1, 732), 5)
  remaining = list(set(range(1, 732)) - set(first_group))
  second_group = random.sample(remaining, 5)
  return first_group, second_group

def get_hero_info(id):
  data = requests.get(f"https://superheroapi.com/api/2183127771827858/{id}").json()
  print(data)
  powerstats = data.get("powerstats")
  strength = int(powerstats.get("strength"))
  speed = int(powerstats.get("speed"))
  power = int(powerstats.get("power"))
  combat = int(powerstats.get("combat"))
  intelligence = int(powerstats.get("intelligence"))
  durability = int(powerstats.get("durability"))
  stamina = random.randint(0,10)

  return data.get("name"), intelligence, durability, strength, speed, power, combat, stamina

def get_hp(id):
  name, inte, dura, stre, spee, powe, comb, stam = get_hero_info(id)
  HP =  int((0.8*stre + 0.7*dura + powe)*(1 + stam/10)/2) + 100
  return HP

def get_attack(id):
  


a, b = generate_sets()
print(get_hero_info(a[0]))
print(get_hp(a[0]))
