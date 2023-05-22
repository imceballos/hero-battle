class Team:
    def __init__(self, members):
        self.members = members
        self.active_members = self.get_active_members()
        self.alignment = self.get_aligment()


class Hero:
    def __init__(self, id):
        self.id = id
        self.set_properties(id)

    def request_info_hero(id):
        return requests.get(f"https://superheroapi.com/api/2183127771827858/{id}").json()

    def set_properties(self):
        data = self.request_info_hero(self.id)
        powerstats = data.get("powerstats")
        self.alignment = data.get("biography").get("alignment")
        self.strength = int(powerstats.get("strength"))
        self.speed = int(powerstats.get("speed"))
        self.power = int(powerstats.get("power"))
        self.combat = int(powerstats.get("combat"))
        self.intelligence = int(powerstats.get("intelligence"))
        self.durability = int(powerstats.get("durability"))
        self.stamina = random.randint(0,10)
        self.hp = self.get_hp()

    def get_hp(self):
        return  int((0.8*self.strength + 0.7*durability + power)*(1 + stami}/10)/2) + 100



