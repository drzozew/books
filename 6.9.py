favorite_places = {
    "badzi": ["gdańsk", "wrocław", "toruń"],
    "stefan": ["kujawy", "stawy", "mazury"],
    "zigi": ["poznan", "stany", "mazurkujaqyy"],
  }

for name, places in favorite_places.items():
    print(f"Ulubinoe miejsca {name.title()} to: ")
    for place in places:
        print(f"  {place.title()}")
