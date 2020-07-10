import sys, os
sys.path.append(os.path.abspath('.'))

import random

class Meal:
    db_connection = None
    veggie = None
    protein = None
    soup = None
    special_meal = None
    normal_or_special = None

    def __init__(self):
        self.db_connection = None
        self.normal_or_special = random.choice({1, 0})
        if self.normal_or_special == 0:
            self.veggie = self.init_dish("veggie")
            self.protein = self.init_dish("protein")
            self.soup = self.init_dish("soup")
        self.special_meal = self.init_dish("special_meal")

    def init_dish(self, dish):
        return self.db_connection.read_from_table("column", dish, "ORDER BY RANDOM() LIMIT 1") #get random from db 

    def add_veggie(self, veggie):
        self.db_connection.add_to_table("veggie", veggie)

    def add_protein(self, protein):
        self.db_connection.add_to_table("protein", protein)

    def add_soup(self, soup):
        self.db_connection.add_to_table("soup", soup)

    def add_special_meal(self, special_meal):
        self.db_connection.add_to_table("special_meal", special_meal)

if __name__ == '__main__':
    new_meal = Meal()