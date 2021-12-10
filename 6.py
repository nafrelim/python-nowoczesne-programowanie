"""
Rozdział 6 - pętle
"""
while True:
    value = input("Podaj liczbę [lub q, aby zakończyć]: ")
    if value == 'q':  # Wyjście
        break
    number = int(value)
    if number % 2 == 0:  # Liczba parzysta
        continue
    print(number, "do kwadratu to", number * number)

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Znaleziona liczba parzysta', number)
        break
    position += 1
else:  # Instrukcja break nie została użyta
    print('Nie ma liczb parzystych')
