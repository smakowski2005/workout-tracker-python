from src import workouts
from src import storage
from src import utils
from src import database


database.create_table()
list=database.get_workouts()

def menu():
    print("Menu!")
    print("1. Dodaj trening")
    print("2. Pokaz trening")
    print("3. Usun trening")
    print("4. Edytuj trening")
    print("5. Wyszukaj trening")
    print("6. Pokaz statystyki")
    print("7. Usun baze")
    print("8. Wyszukaj trening po ID")
    print("9. Zamiana treningu")
    print("10. Wyszukaj trening po nazwie")
    print("11. Wyjsc")

while True:
    menu()
    choice = utils.get_positive_int("Podaj liczbe: ")
    if choice == 1:
        workouts.add_workout(list)
        storage.save_workouts(list)
    elif choice == 2:
        workouts.show_workouts(list)
    elif choice == 3:
        workouts.delete_workout(list)
        storage.save_workouts(list)
    elif choice == 4:
        workouts.edit_workouts(list)
        storage.save_workouts(list)
    elif choice == 5:
        workouts.search_workouts(list)
    elif choice == 6:
        workouts.show_stats(list)
    elif choice == 7:
        database.delete_database()
    elif choice == 8:
        workout_id = int(input("Podaj ID treningu: "))
        workout = database.get_workout_by_id(workout_id)
        if workout:
            print(workout)
        else:
            print("Nie znaleziono treningu.")
    elif choice == 9:
        workout_id = int(input("Podaj ID treningu: "))
        column = input(
            "Co chcesz zmienic (cwiczenie/ciezar/powtorzenia/serie): "
        )
        value = input("Podaj nowa wartosc: ")
        database.update_workout(
            workout_id,
            column,
            value
        )
    elif choice == 10:
        workout_name = input("Podaj nazwe cwiczenia: ")
        database.search_workout_by_name(workout_name)
    elif choice == 11:
        break
    else:
        print("Nie poprawne.")
    input("Naciśnij Enter, aby kontynuować...")