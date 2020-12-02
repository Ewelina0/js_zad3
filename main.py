def what_word(key, attempt):
    i=0
    print("Zgadnijmy jakie słowo wpisałeś!")
    while  i < attempt:
        word1 =str(input())
        if word1!=key:
            print("Spróbuj ponownie.")
        else:
            print("Gratulacje!")
            break
        i+=1
    if(i==attempt):
            print("Przegrywasz! Skończyła się liczba prób.")
print("Wpisz słowo klucz:\n")
key = str(input())
print("Wpisz liczbę prób:\n")
attempt = int(input())
what_word(key, attempt)