class Player:
    def __init__(self,name,health,damage,inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory
        
    def restore_health(self):
        if "life poition" in self.inventory:
            if self.health <= 0:
                print("Restoring health is not possible, please re-alive first!")
            elif self.health >=100:
                print("You have maximum health!") 
            else:
                self.health = 100
        else:
            print("You don't have Life Poition!")
    
    def add_health(self,health):
        if "health poition" in self.inventory:
            if self.health <= 0:
                print("Adding health is not possible, please re-alive first!")
            elif self.health >=100:
                print("You have maximum health!")
            else:
                self.health += health
        else:
            print("You don't have Health Poition!")
    
    def __repr__(self):
        print("\n Name: {} \n Health: {} \n Damage: {} \n Inventory: {}".format(self.name,self.health,self.damage,self.inventory))
            
    
          
          
      
class Soldier(Player):
    
    def __init__(self,name,health,damage,inventory,armor,weapon):
        super().__init__(name,health,damage,inventory)
        self.armor = armor
        self.weapon = weapon
    
    def deal_damage(self,damage,dragon):
        if self.damage <= 0:
            print("Adding damage is not possible! you dont have enough damage points!")
        elif dragon.health <= 0:
            print('Dragon is Dead!')
        else:
            dragon.health -= damage
            print('You launched a {} damage point on the dragon and he has {} health points now.'.format(damage,dragon.health))
            
    def __repr__(self):
        super().__repr__()
        print(" Armor: {} \n Weapon: {} \n".format(self.armor,self.weapon)) 
        
    
class Wizard(Player):
    
    def __init__(self,name,health,damage,inventory,spells):
        super().__init__(name,health,damage,inventory)
        self.spells = spells
    
    def deal_damage(self,damage,dragon):
        if self.damage <= 0:
            print("Adding damage is not possible! you dont have enough damage points!")
        elif dragon.health <= 0:
            print('Dragon is Dead!')
        else:
            dragon.health -= damage
            print('You launched a {} damage point on the dragon and he has {} health points now.'.format(damage,dragon.health))

class Dragon:
    def __init__(self,health,damage,fire):
        self.health = health
        self.damage = damage
        self.fire = fire
    
    def deal_damage(self,damage,soldier):
        if soldier.armor == 'y':
            soldier.health -= int(damage/2)
            print("The dragon just attacked you! only have the damage tho cuz you wore an armor!")    
        else:
            soldier.health -= damage
            print("The dragon just attacked you!")
     
    def deal_damage_to_wizard(self,damage,wizard):
        if 'damage protection' in wizard.spells:
            wizard.health -= 0
            print("The dragon tried to attack you! but you have a damage protection spell!")    
        else:
            wizard.health -= damage
            print("The dragon just attacked you!")        
    
    def attack_fire(self,fire,soldier):
        if soldier.armor == 'y':
            soldier.health -= int(fire/2)
            print("The dragon just flamed fire at you! only half the damage tho cuz you wore an armor!")
        else:
            soldier.health -= fire
            print("The dragon just flamed fire at you!")
    
    def attack_fire_to_wizard(self,fire,wizard):
        if 'fire protection' in wizard.spells:
            wizard.health -= 0
            print("The dragon just tried to attack you but failed because you have fire protection!")    
        else:
            wizard.health -= fire
            print("The dragon just flamed fire at you!")
            
    def __repr__(self):
        print("\n Health: {} \n Damage: {} \n Fire: {}".format(self.health,self.damage,self.fire))
    
import random

def game(dragon,player):
    
        print('''Now you will fight the most powerful dangerous dragon of all time ! be carful with what your choices!
        Choose 1, 2, or 3
        1. Attack
        2. Use health poition
        3. Restore health
        4. Exit ''')

        while(dragon.health > 0):
                choice = int(input("Make a choice Now! "))
                
                if choice == 1:
                    damage = int(input("How much damage do you want to inflict? "))
                    player.deal_damage(damage,dragon)
                elif choice == 2:
                    health = int(input("How much health do you want to recover? "))
                    player.add_health(health)
                elif choice == 3:
                    player.restore_health()
                else:
                    break
                
                num = random.randint(1, 3)
                
                if num == 1:
                    continue
                elif num == 2:
                    if isinstance(player, Wizard):
                        dragon.attack_fire_to_wizard(50,player)
                           
                    else:
                        dragon.attack_fire(50,player)
                    
                else:
                    if isinstance(player, Wizard):
                        dragon.deal_damage_to_wizard(40,player) 
                    else:
                        dragon.deal_damage(40,player)
        print("You have won!!!")
        
dragon = Dragon(100,70,50)
print('''\n\t\t\t∘₊✧──────✧₊∘ Welcome to Age of Dragons ∘₊✧──────✧₊∘ 
      A game where you fight against the most powerful dragon in the world! ''')
player_name = str(input('What\'s your name? '))
player_choice = str(input('Hello {}! Please choose your player: Soldier or Wizard ? '.format(player_name))).lower()
inventory = []
spells = []
if player_choice == 'soldier':
    print('Great! Now plase Enter your soldier infromation such as name, health, damage, inventory, armor, and weapon!' )
    name = str(input('name? '))
    health = int(input('health? (0-100) '))
    damage = int(input('damage? (0-100) '))
    print('inventory? please note you are allowed only 3 elements of Life Poition or Health Potion! enter - if you have none')
    for i in range(0, 3):
        ele = str(input()).lower()
        inventory.append(ele)
    armor = str(input('armor? (Y/N) ')).lower()
    weapon = str(input('weapon? (Y/N) ')).lower()
    soldier = Soldier(name,health,damage,inventory,armor,weapon)
    game(dragon,soldier)
    
if player_choice == 'wizard':
    print('Great! Now plase Enter your wizard infromation such as name, health, damage, inventory, and spells!' )
    name = str(input('name? '))
    health = int(input('health? (0-100) '))
    damage = int(input('damage? (0-100) '))
    print('inventory? please note you are allowed only 3 elements of Life Poition or Health Potion! enter - if you have none')
    for i in range(0, 3):
        ele = str(input()).lower()
        inventory.append(ele)
    print('spells? please note you are allowed only 2 elements of Damage Increaser or Fire Spell or Fire Protection! enter - if you have none')
    for i in range(0, 2):
        ele = str(input()).lower()
        spells.append(ele)
    wizard = Wizard(name,health,damage,inventory,spells)
    game(dragon,wizard)