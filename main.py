import random


class Map():
    def __init__(self):
        self.distance = self.random_spawn_distance()

    def distance_value(self):
        print(self.distance)

    def random_spawn_distance(self):
        return random.randint(1, 8)

    def attack_distance_check(self, attack_range):
        return self.distance <= attack_range

    def random_spawn_distance(self):
        return random.randint(1, 8)

    def character_move_further(self, character):
        character_move = random.randrange(0, character.max_speed)
        self.distance += character_move
        return character_move

    def character_move_closer(self, character):
        character_move = 0
        if self.distance > character.max_speed:
            character_move = random.randrange(0, (character.max_speed))
        elif self.distance > 1:
            character_move = random.randrange(0, self.distance)
        self.distance -= character_move
        return character_move
class Weapon():
    def __init__(self):
        self.name = self.weapon_name
        self.damage = self.base_damage
        self.range = self.base_range


class Sword(Weapon):
    weapon_name = "Sword"
    base_damage = [2, 11]
    base_range = 2

class Axe(Weapon):
    weapon_name = "Axe"
    base_damage = [3, 12]
    base_range = 1

class Bow(Weapon):
    weapon_name = "Bow"
    base_damage = [2, 9]
    base_range = 12

class Dagger(Weapon):
    weapon_name = "Dagger"
    base_damage = [2, 7]
    base_range = 1



class Entity:
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = self.base_health
        self.weapon = self.base_weapon
        self.damage_range = self.weapon.damage
        self.attack_range = self.weapon.base_range
        self.max_speed = self.base_max_speed

    def give_random_damage(self):
        return random.randrange(self.damage_range[0], self.damage_range[1])

    def take_damage(self, damage):
        self.health = self.health - damage
        return self.health

    def is_alive(self) -> bool:
        return self.health > 1

    def description(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nWeapon: {self.weapon.name}\nDamage: {self.weapon.damage}\nAttack range: {self.attack_range}, \n")

    def attack_entety(self,target: "Entity", map) -> None:
        print(f'\n{self.name} attacs {target.name}')
        if map.attack_distance_check(self.attack_range):
            damage = self.give_random_damage()
            target.take_damage(damage)
            print(f'with damage: {damage}\n{target.name} health: {target.health}')
        else:
            print("Miss, too far")

    def move_closer(self, map):
        character_move = map.character_move_closer(self)
        print(f'\n{self.name} moves on {character_move}\nDistance: {map.distance}')

    def move_further(self, map):
        character_move = map.character_move_further(self)
        print(f'\n{self.name} moves on {character_move}\nDistance: {map.distance}')

class Knight(Entity):
    base_health = 50
    base_weapon = Sword()
    base_max_speed = 5

class Archer(Entity):
    base_health = 35
    base_weapon = Bow()
    base_max_speed = 7

class Goblin(Entity):
    base_health = 15
    base_weapon = Dagger()
    base_max_speed = 8

class Elf(Entity):
    base_health = 30
    base_weapon = Bow()
    base_max_speed = 9

class Ork(Entity):
    base_health = 45
    base_weapon = Axe()
    base_max_speed = 6



class Game:
    def __init__(self):
        self.playing = True


    def create_character(self, name, chosen_class):
        if chosen_class == "Knight":
            character = Knight(name)
        else:
            character = Archer(name)
        return character

    def ask_character_name(self):
        name = input("Lets create a character!\nName:")
        return name
    def ask_character_class(self):
        chosen_class = input(f"Choose your Class Knight or Archer\nClass: ")
        return chosen_class

    def random_enemy(self):
        return random.choice([Elf("Elf"), Ork("Ork"), Goblin("Goblin")])

    def ask_what_to_do(self):
        return input("\nWhat do you want to do:\nAttack, Move closer, Move further\n")

    def character_action(self, what_to_do, character, enemy, map):
        if what_to_do == "Attack":
            character.attack_entety(enemy, map)
        if what_to_do == "Move closer":
            character.move_closer(map)
        elif what_to_do == "Move further":
            character.move_further(map)

    def enemy_action(self, enemy, character, map):
        if map.attack_distance_check(enemy.attack_range):
            enemy.attack_entety(character, map)
        else:
            enemy.move_closer(map)

    def fighting_process(self, character, enemy, map):
        counter = 1
        while character.is_alive() and enemy.is_alive():
            if counter % 2 != 0:
                self.character_action(self.ask_what_to_do(), character, enemy, map)
            else:
                self.enemy_action(enemy, character, map)
            counter += 1

    def begin_fight(self, character, enemy) -> None:
        map = Map()
        print(f"You are fighting with {enemy.name}\nDistance: {map.distance}\n")
        character.description()
        enemy.description()
        self.fighting_process(character, enemy, map)

    def start_journey(self, character):
        day = 1
        while character.is_alive():
            print(f"\n\nDay {day}:")
            activity = random.choice(["fight"])
            if activity == "fight":
                self.begin_fight(character, self.random_enemy())
            day += 1

    def start(self):
        name = self.ask_character_name()
        chosen_class = self.ask_character_class()
        character = self.create_character(name, chosen_class)
        self.start_journey(character)



