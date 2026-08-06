import datetime

from src import database
from src.utils import get_positive_int

data=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def add_workout(workouts):

    cwiczenie=input("Cwiczenie: ")
    ciezar=get_positive_int("ciezar: ")
    powtorzenia=get_positive_int("Powtorzenia: ")
    serie=get_positive_int("Serie: ")
    workout={
        "cwiczenie":cwiczenie,
        "ciezar":ciezar,
        "powtorzenia":powtorzenia,
        "serie":serie,
        "data": data
    }
    database.add_workout(workout)
def show_workouts(workouts):
    if not workouts:
        print("Nie ma takiego treningu.")
        return
    for x,workout in enumerate(workouts,start=1):
        print(
            f'ID: {workout[0]}'
        )
        print(
            f'{workout[1]} |'
            f'{workout[2]} |'
            f'{workout[3]} |'
            f'{workout[4]} |'
            f'{workout[5]} |'
        )
        print("--------")
def delete_workout(workouts):
    choice = int(input("Podaj ID treningu: "))-1
    if 0 <= choice < len(workouts):
        for workout in workouts:
            if workouts[workout]["id"] == choice:
                del workouts[workout]
    else:
        print("Nie ma takiego treningu.")
def edit_workouts(workouts):
    print("Ktory trening chcesz edytowac?")
    x = 0
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


        workouts[choice]["data"]=data
        workouts[choice][slowo] = nowy
def search_workouts(workouts):
    text=input("Wyszukaj po nazwie: ")
    value=True
    for workout in workouts:
        if text.lower() == workout["cwiczenie"].lower():
            value = False
            print(
                f'ID: {workout["id"]}'
            )
            print(
                f'{workout["cwiczenie"]} |'
                f'{workout["ciezar"]} |'
                f'{workout["powtorzenia"]} |'
                f'{workout["serie"]} |'
                f'{workout["data"]} |'
            )
    if value:print("Nie ma takiego treningu.")
def show_stats(workouts):
    print("Liczba treningow: ",len(workouts))
    max=workouts[0]["ciezar"]
    ciezar=workouts[0]
    for workout in workouts:
        if workout["ciezar"] > max:
            ciezar=workout
    print(
        f'Najwiekszy ciezar:'
        f'{ciezar["cwiczenie"]}  {ciezar["ciezar"]}'
    )
    suma=0
    for workout in workouts:
        suma=suma+workout["serie"]
    print("Laczna liczba serii: ",suma)



