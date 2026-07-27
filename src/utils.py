def get_positive_int(text):
    while True:
        try:
            value=int(input(text))
            if value <= 0:
                print("podana wartosc jest mniejsza lub zero")
                continue
            return value
        except ValueError:
            print("podana wartosc nie jest liczba")

