class Res():
    'tworzy obiekt restaurant'

    def __init__(self, restaurant_name, cuisine_type):
        '''inicjalizacja atrybutów name i cuisine'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}i {self.cuisine_type}")

    def open_restaurant(self):
        print("Restauracja jest otwarta o 18:00")


x = Res("Kania", "Włoska")
y = Res("Italiana", "Zagra")
z = Res("Alad", "Pizza")

x.describe_restaurant()
y.describe_restaurant()
z.describe_restaurant()
