import datetime

from utils import get_positive_int

def add_workout(workouts):

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
def show_workouts(workouts):
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
def delete_workout(workouts):
    choice = int(input("Wybierz: "))-1
    if 0 <= choice < len(workouts):
        workouts.pop(choice)
    else:
        print("Nie ma takiego treningu.")
    save_workouts()
def edit_workouts(workouts):
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

