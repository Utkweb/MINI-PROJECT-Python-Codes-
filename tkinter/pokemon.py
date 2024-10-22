import tkinter as tk
from random import randint

# Define a simple Pokemon class
class Pokemon:
    def __init__(self, name, max_health, attack_power):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power

    def attack(self, opponent):
        damage = randint(1, self.attack_power)
        opponent.health -= damage
        if opponent.health < 0:
            opponent.health = 0
        return damage

# Create the Game App class with tkinter
class PokemonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Battle")

        # Create two Pokemon for battle
        self.pokemon1 = Pokemon("Pikachu", 100, 20)
        self.pokemon2 = Pokemon("Charmander", 100, 18)

        # Health labels
        self.pokemon1_health_label = tk.Label(root, text=f"{self.pokemon1.name} HP: {self.pokemon1.health}/{self.pokemon1.max_health}")
        self.pokemon1_health_label.pack()

        self.pokemon2_health_label = tk.Label(root, text=f"{self.pokemon2.name} HP: {self.pokemon2.health}/{self.pokemon2.max_health}")
        self.pokemon2_health_label.pack()

        # Attack button for Pokémon 1
        self.attack_button = tk.Button(root, text="Pikachu Attack!", command=self.pokemon1_attack)
        self.attack_button.pack()

        # Attack button for Pokémon 2
        self.attack_button2 = tk.Button(root, text="Charmander Attack!", command=self.pokemon2_attack)
        self.attack_button2.pack()

        # Result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def update_health_labels(self):
        self.pokemon1_health_label.config(text=f"{self.pokemon1.name} HP: {self.pokemon1.health}/{self.pokemon1.max_health}")
        self.pokemon2_health_label.config(text=f"{self.pokemon2.name} HP: {self.pokemon2.health}/{self.pokemon2.max_health}")

    def pokemon1_attack(self):
        damage = self.pokemon1.attack(self.pokemon2)
        self.result_label.config(text=f"{self.pokemon1.name} dealt {damage} damage!")
        self.update_health_labels()
        self.check_game_over()

    def pokemon2_attack(self):
        damage = self.pokemon2.attack(self.pokemon1)
        self.result_label.config(text=f"{self.pokemon2.name} dealt {damage} damage!")
        self.update_health_labels()
        self.check_game_over()

    def check_game_over(self):
        if self.pokemon1.health == 0:
            self.result_label.config(text=f"{self.pokemon1.name} fainted! Charmander wins!")
            self.attack_button.config(state=tk.DISABLED)
            self.attack_button2.config(state=tk.DISABLED)
        elif self.pokemon2.health == 0:
            self.result_label.config(text=f"{self.pokemon2.name} fainted! Pikachu wins!")
            self.attack_button.config(state=tk.DISABLED)
            self.attack_button2.config(state=tk.DISABLED)

# Set up the tkinter window
root = tk.Tk()
game = PokemonGame(root)
root.mainloop()
