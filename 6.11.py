cities = {
    "kartuzy": {
        "country": "Polska",
        "population": 14_000,
        "fact": "Znajduje się tutaj stary klasztor"
    },
    "gdańsk": {
        "country": "Polska",
        "population": 250_000,
        "fact": "Kiedyś wolne miasto gdańsk",
    },
    "ostrowice": {
        "country": "Polska",
        "population": 111,
        "fact": "Madzia pochodzi z tąd",
    },
}

for citi, citi_info in cities.items():
    print(f"Miasto {citi.title()} leży w {citi_info['country'].title()}."
          f"Jego populacja to {citi_info['population']} "
          f"ludzi a faktem jest, że {citi_info['fact']}")
