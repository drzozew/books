class Res():
    'tworzy obiekt restaurant'

    def __init__(self, restaurant_name, cuisine_type):
        '''inicjalizacja atrybutów name i cuisine'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} i {self.cuisine_type}")

    def open_restaurant(self):
        print("Restauracja jest otwarta o 18:00")

    def read_served(self):
        print(f"Ilość obsłużonych {self.number_serverd}")

    def served_update(self, person):
        self.number_serverd += person

    def set_served(self, update_persona):
        self.number_serverd = update_persona
