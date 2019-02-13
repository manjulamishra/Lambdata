#!/usr/bin/env python
"""
Python module for simulation Aquariums.
"""

from collections import defaultdict

class Aquarium:
    """Example class to model an aquarium
    """
    def __init__(self, name="Pierre's Underwater World"):
        self.name = name
        # self.fish = {}
        self.fish = defaultdict(int)

    def add_fish(self, fish_species):
        """Incrementing count for fish_species in fish dict."""
        # assert type(fish_species) == str
        if isinstance(fish_species, str):
            self.fish[fish_species] += 1
        else:
            print("That doesn't look like a fish!")

    def generate_fish_report(self):
        """Iterate over and summarize self.fish dictionary."""
        for species, count in self.fish.items():
            print(f'{species}: {count}')

class Habitat:
    """General class to represent a habitat with species in it."""
    def __init__(self, name="Habitat Name"):
        self.name = name
        self.animals = defaultdict(int)
        self.plants = defaultdict(int)

    def generate_animal_report(self):
        """Iterate over and summarize self.animal dictionary."""
        print('ANIMALS IN ' + self.name)
        for species, count in self.animals.items():
            print(f'{species}: {count}')

    def generate_plant_report(self):
        """Iterate over and summarize self.plant dictionary."""
        print('PLANTS IN ' + self.name)
        for species, count in self.plants.items():
            print(f'{species}: {count}')


class Zoo(Habitat):
    """Class to represent data and behavior of a zoo."""
    def clean_zoo(self):
        print('Better call in the cleaners!')

    def generate_animal_report(self):
        print('This is the *Zoo* report!')
        for species, count in self.animals.items():
            print(f'{species}: {count}')