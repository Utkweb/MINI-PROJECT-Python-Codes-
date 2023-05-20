import random
import time
## TODO: import Hero class here
from characters import Hero
def driver():
    ## TODO: Get first monster's name, health, description, basicAttackDamange,specialAttackDamage, defenseDamage, defenseName here.
    # Instantiate a Hero using that info.
    name1 = str(input("Enter monster 1 name: "))
    print("")
    health1 = int(input("Enter a number for monster 1 health: "))
    print("")
    description1 = str(input("Enter monster 1 description: "))
    print("")
    basicAttackDamage1 = int(input("Enter a number for monster 1 basic attack damage: "))
    print("")
    specialAttackDamage1 = int(input("Enter a number for monster 1 special attack damage: "))
    print("")
    defenseDamage1 = int(input("Enter a number for monster 1 defense damage: "))
    print("")
    basicAttackName1 = str(input("Enter monster 1 basic attack name: "))
    print("")
    specialAttackName1 = str(input("Enter monster 1 special attack name: "))
    print("")
    basicDefenseName1 = str(input("Enter monster 1 defense name: "))
    first = Hero(name1, health1, description1, basicAttackDamage1,specialAttackDamage1, defenseDamage1,basicAttackName1, specialAttackName1,basicDefenseName1) 
    # this should be an instance of your Hero class
    # TODO: Get second monster's name, health, description, basicAttack Damange,specialAttackDamage, defenseDamage, defenseName here.
    # Instantiate a Hero using that info.
    name2 = str(input("Enter monster 2 name: "))
    print("")
    health2 = int(input("Enter a number for monster 2 health: "))
    print("")
    description2 = str(input("Enter monster 2 description: "))
    print("")
    basicAttackDamage2 = int(input("Enter a number for monster 2 basic attack damage: "))
    print("")
    specialAttackDamage2 = int(input("Enter a number for monster 2 special attack damage: "))
    print("")
    defenseDamage2 = int(input("Enter a number for monster 2 defense damage: "))
    print("")
    basicAttackName2 = str(input("Enter monster 2 basic attack name: "))
    print("")
    specialAttackName2 = str(input("Enter monster 2 special attack name: "))
    print("")
    basicDefenseName2 = str(input("Enter monster 2 defense name: "))
    second = Hero(name2, health2, description2, basicAttackDamage2,specialAttackDamage2, defenseDamage2,basicAttackName2, specialAttackName2,basicDefenseName2) 
    # this should be an instance of your Hero class
    winner = monster_battle(first, second)
    # This function has two monsters fight and returns the winner
def monster_battle(m1, m2):
    # first reset everyone's health!
    #####TODO######
    m1.resetHealth()
    m2.resetHealth()
    # next print out who is battling
    print("Starting Battle Between")
    print(m1.getName() + ": " + m1.getDescription())
    print(m2.getName() + ": " + m2.getDescription())
 # Whose turn is it?
 # Select Randomly whether m1 or m2 is the initial attacker
 # the other is the initial defender
 ######TODO######
    random_decide = random.randint(0, 1)
    if random_decide == 0:
        attacker = m1
        defender = m2
    else:
        attacker = m2
        defender = m1
    print(attacker.getName() + " goes first.")
    # Loop until either monster is unconscious (health < 1) or choose to stop.
    while (m1.getHealth() > 0 and m2.getHealth() > 0):
 # Ask the user a move among special attack, basic attack, defense or the stop.
        move = input('Pick one of these (s)pecial attack, (b)asic attack, (d)efense or sto(p):')
 # It will be nice for output to record the damage done
        before_health = defender.getHealth()
 # for easy reference
        attacker_name = attacker.getName()
        defender_name = defender.getName()
 # for each of the options above, apply the appropriate attack and
 # print out who did what attack on whom
 # basic attack
        if (move.lower() == "b"):
 # Attacker uses basic attack on defender
 # and print results by calling print_results function
 ######TODO######
            basic_attack = Hero.basicAttack(defender)
            print_line = "{} used {} on {}".format(attacker_name,attacker.getBasicName(), defender_name)
            print(print_line)
            attacker.basicAttack(defender)
            attack_amount = attacker.getBasicAttackDamage()
            healthchange = defender.getHealth()
            print_results(attacker, defender, attack_amount, healthchange)
    # defense attack
        elif move.lower() == "d":
 # Defend! and print results by calling print_results function
 ######TODO######
            print_line = "{} used {} on {}".format(attacker_name,attacker.getDefenseName(), defender_name)
            print(print_line)
            attacker.defenseAttack(defender)
            attack_amount = attacker.getDefenseAttackDamage()
            healthchange = defender.getHealth()
            print_results(attacker, defender, attack_amount, healthchange)
 # special attack
        elif move.lower() == "s":
 # Special Attack! and print results by calling print_results function
 ######TODO######
            print_line = "{} used {} on {}".format(attacker_name,attacker.getSpecialName(), defender_name)
            print(print_line)
            attacker.specialAttack(defender)
            attack_amount = attacker.getSpecialAttackDamage()
            healthchange = defender.getHealth()
            print_results(attacker, defender, attack_amount, healthchange)
        elif move.lower() == 'p':
 # stop the fight
            break
 # Swap attacker and defender
 ######TODO######
        if attacker == m1:
            attacker = m2
            defender = m1
        elif attacker == m2:
            attacker = m1
            defender = m2
 # Print the names and healths after this round
 ######TODO######
 # Print out who won.
 # Return who won
 ######TODO######
    print("")
    print("Battle is over. let's see who has won...")
    if m1.getHealth() > m2.getHealth():
        print("{} is victorious!".format(m1.getName()))
        return m1
    else:
        print("{} is victorious!".format(m2.getName()))
        return m2
# Print status updates
####TODO####
def print_results(attacker, defender, attack, hchange):
 ####TODO####
 # Get the name of the attacker and the defender. hchange is health
 # then give status updates based on the the attack. For more
 # info refer to the example trace.
 # res=""
 # print(res)
    print("The attack did {} damage.".format(attack))
    print("{} at {}".format(attacker.getName(), attacker.getHealth()))
    print("{} at {}".format(defender.getName(), hchange))
# ----------------------------------------------------
if __name__ == "__main__":
 # Ideally every battle will be different
 # But for reproducability, we'll seed the random number generator as 0
 random.seed(0)
 driver()
