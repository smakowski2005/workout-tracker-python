import json
import datetime

try:
    with open('/Users/sebastian/PycharmProjects/PythonProject1/data/workouts.json') as json_file:
        workouts = json.load(json_file)
except FileNotFoundError:
    workouts = []
except json.decoder.JSONDecodeError:
    workouts = []

def get_positive_int(tekst):
    while True:
        try:
            zmienna=int(input(tekst))
            if zmienna <= 0:
                print("podana wartosc jest mniejsza lub zero")
                continue
            return zmienna
        except ValueError:
            print("podana wartosc nie jest liczba")

def add_workout():

    cwiczenie=input("Cwiczenie: ")
    ciezar=get_positive_int("ciezar: ")
    powtorzenia=get_positive_int("Powtorzenia: ")
    serie=get_positive_int("Serie: ")
    godzina=datetime.datetime.now()
    workout={
        "cwiczenie":cwiczenie,
        "ciezar":ciezar,
        "powtorzenia":powtorzenia,
        "serie":serie,
        "godzina":godzina.strftime("%H:%M")
    }
    workouts.append(workout)
    save_workouts()
def show_workouts():
    if not workouts:
        print("Nie ma takiego treningu.")
        return
    for x,workout in enumerate(workouts,start=1):
        print(x)
        print(
            f'{workout["cwiczenie"]} |'
            f'{workout["ciezar"]} |'
            f'{workout["powtorzenia"]} |'
            f'{workout["serie"]} |'
            f'{workout["godzina"]} |'
        )
        print("--------")
def delete_workout():
    choice = int(input("Wybierz: "))-1
    if 0 <= choice < len(workouts):
        workouts.pop(choice)
    else:
        print("Nie ma takiego treningu.")
    save_workouts()
def edit_workouts():
    print("Ktory trening chcesz edytowac?")
    x = 0
    godzina=datetime.datetime.now()
    for workout in workouts:
        x = x + 1
        print(x)
        print(
            f'{workout["cwiczenie"]} |'
        )
    choice = int(input("Wybierz: "))-1
    if 0 <= choice < len(workouts):
        for klucz in workouts[choice].keys():
            print(klucz)
        choice2 = int(input("Wybierz: "))
        if choice2 == 1:
            slowo="cwiczenie"
            nowy = input("Podaj")
        elif choice2 == 2:
            slowo="ciezar"
            nowy = get_positive_int("Podaj")
        elif choice2 == 3:
            slowo="powtorzenia"
            nowy = get_positive_int("Podaj")
        elif choice2 == 4:
            slowo="serie"
            nowy = get_positive_int("Podaj")
        else:
            print("Nie ma")
            return


        workouts[choice]["godzina"]=godzina.strftime("%H:%M")
        workouts[choice][slowo] = nowy
        save_workouts()


def save_workouts():
    with open('/Users/sebastian/PycharmProjects/PythonProject1/data/workouts.json', 'w') as outfile:
        json.dump(workouts, outfile)

def menu():
    print("Menu!")
    print("1. Dodaj trening")
    print("2. Pokaz trening")
    print("3. Usun trening")
    print("4. Edytuj trening")
    print("5. Wyjdz")

while True:
    menu()
    choice = int(input("Wybierz: "))
    if choice == 1:
        add_workout()
    elif choice == 2:
        show_workouts()
    elif choice == 3:
        delete_workout()
    elif choice == 4:
        edit_workouts()
    elif choice == 5:
        break
    else:
        print("Nie poprawne.")