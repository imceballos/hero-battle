import random
from typing import List, Tuple, Dict, Any

from api import request_info_hero

class Team:
    def __init__(self, members):
        self.members = members
        self.active_members = self.get_active_members()
        self.team_alignment = self.get_aligment()
        self.set_fb()

    def get_active_members(self):
        self.active_members = [hero for hero in self.members if hero.hp > 0]
        self.active = len(self.active_members)
        return self.active_members

    def get_aligment(self):
        alignments = [hero.alignment for hero in self.members]
        return max(alignments, key=alignments.count)

    def set_fb(self):
        for hero in self.members:
            coef = 1 + random.randint(0, 9)
            hero.fb = (
                coef if hero.alignment == self.team_alignment else coef**-1
            )
        self.set_attack()

    def set_attack(self):
        for hero in self.members:
            hero.mental_attack = (
                0.7 * hero.intelligence + 0.2 * hero.speed + 0.1 * hero.combat
            ) * hero.fb
            hero.strong_attack = (
                0.6 * hero.strength + 0.2 * hero.power + 0.2 * hero.combat
            ) * hero.fb
            hero.fast_attack = (
                0.55 * hero.speed + 0.25 * hero.durability + 0.2 * hero.strength
            ) * hero.fb

    def __str__(self):
        members = " - ".join(
            f"{hero.name} ({hero.alignment})" for hero in self.members
        )
        return f"Team ({self.team_alignment}): {members}"


class Battle:
    def __init__(self):
        self.teams = self.generate_teams()
        self.activity = []

    def generate_teams(self) -> List[Team]:
        first_group = random.sample(range(1, 732), 5)
        remaining = list(set(range(1, 732)) - set(first_group))
        second_group = random.sample(remaining, 5)
        return self.create_teams(first_group, second_group)

    def create_teams(self, first_group: List, second_group: List) -> List[Team]:
        first_team = self.create_team(first_group)
        second_team = self.create_team(second_group)
        return [first_team, second_team]

    def create_team(self, group: List) -> Team:
        return Team([Hero(i) for i in group])

    def start_battle(self):
        start, before = self.get_order()
        while len(start.get_active_members()) and len(
            before.get_active_members()
        ):
            self.attack(start, before)
            start, before = before, start
        
        active_members = start.get_active_members() if start.get_active_members() else before
        self.activity.append({"name": "wins", "action": {"sender": str(active_members), "receiver": None, "damage": 0}})

    def get_order(self) -> Tuple[str, str]:
        number = random.randint(0, 1)
        return self.teams[number], self.teams[1 - number]

    def attack(self, team_1: Team, team_2: Team):
        attacker = random.choice(team_1.get_active_members())
        receiver = random.choice(team_2.get_active_members())
        return self.execute_attack(attacker, receiver)

    def execute_attack(self, attacker, receiver):
        damage = random.choice(
            [
                attacker.mental_attack,
                attacker.strong_attack,
                attacker.fast_attack,
            ]
        )
        self.activity.append({"name": "attack", "action": {"sender": attacker.name, "receiver": receiver.name, "damage": damage}})
        receiver.hp = receiver.hp - damage if damage < receiver.hp else 0
        if receiver.hp == 0:
            self.activity.append({"name": "eliminated", "action": {"sender": None, "receiver": receiver.name, "damage": 0}})

class Hero:
    def __init__(self, id: int):
        self.id = id
        self.set_properties()


    def set_properties(self) -> None:
        data = request_info_hero(self.id)
        powerstats = data.get("powerstats")
        self.name = data.get("name")

        self.alignment = data.get("biography").get("alignment")
        self.strength = self.sanitize(powerstats.get("strength"))
        self.speed = self.sanitize(powerstats.get("speed"))
        self.power = self.sanitize(powerstats.get("power"))
        self.combat = self.sanitize(powerstats.get("combat"))
        self.intelligence = self.sanitize(powerstats.get("intelligence"))
        self.durability = self.sanitize(powerstats.get("durability"))
        self.stamina = random.randint(0, 10)
        self.hp = self.get_hp()

    def sanitize(self, value: Any) -> int:
        if value == "null":
            return random.randint(0, 100)
        return int(value)

    def get_hp(self) -> int:
        return (
            int(
                (0.8 * self.strength + 0.7 * self.durability + self.power)
                * (1 + self.stamina / 10)
                / 2
            )
            + 100
        )

    def __str__(self) -> str:
        return f"{self.name}, hp: {self.hp}, stamina: {self.stamina}"


battle = Battle()
battle.start_battle()
print(battle.activity)
