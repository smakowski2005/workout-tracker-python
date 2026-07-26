import workouts
import storage

list=storage.load_workouts()

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
        workouts.add_workout(list)
    elif choice == 2:
        workouts.show_workouts(list)
    elif choice == 3:
        workouts.delete_workout(list)
    elif choice == 4:
        workouts.edit_workouts(list)
    elif choice == 5:
        break
    else:
        print("Nie poprawne.")