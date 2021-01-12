def what_word(key, attempt):
    succeded = False
    print("Zgadnijmy jakie słowo wpisałeś!")

    for i in range(attempt):
        word = str(input())
        if word != key:
            print("Spróbuj ponownie")
        else:
            succeded = True
            break
    print("Gratulacje! Odgadłeś/aś słowo klucz!") if succeded else print("Przegrałeś! Liczba dostępnych prób wygasła")



print("Wpisz słowo klucz:")
key = str(input())
print("Wpisz liczbę prób:")
attempt = int(input())
what_word(key, attempt)
