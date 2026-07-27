import workouts
import storage
import utils

list=storage.load_workouts()

def menu():
    print("Menu!")
    print("1. Dodaj trening")
    print("2. Pokaz trening")
    print("3. Usun trening")
    print("4. Edytuj trening")
    print("5. Wyszukaj trening")
    print("6. Pokaz statystyki")
    print("7. Wyjdz")

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
        break
    else:
        print("Nie poprawne.")
    input("Naciśnij Enter, aby kontynuować...")