table_booking = input("Na ile osób chciał byś zarezerwoać stół:? ")

ppls = int(table_booking)

if ppls > 8:
    print("Przykro mi trzeba poczkeąc nie ma na tą chwilę wolnych stołów.")
else:
    print("Mamy wolny stół, już prowadzę")
