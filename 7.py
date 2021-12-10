"""
Rozdział 7 - krotki i listy
"""
krotka1 = 'tekst1',
krotka2 = ('tekst2',)  # koniecznie przecinek, żeby zdefiniował jednoelementową krotkę, bo inaczej będzie to str
print(krotka1)
print(krotka2)
print()

marx_tuple = ('Groucho', 'Chico', 'Groucho')
a, b, c = marx_tuple
print(a)
print(b)
print(c)
print()

# zamiana wskazań zmiennych poprzez krotkę
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)
print()

marxes = ['Groucho', 'Chico', 'Harpo']
print(id(marxes))
marxes = marxes[::-1]
print(id(marxes))
print(marxes)
print()

marxes.append('Zeppo')
print(marxes)
print()

marxes.insert(2, 'Gummo')
print(marxes)
print()

others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)
print()

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)
print()

numbers[1:3] = []
print(numbers)
print()

numbers[1:3] = (98, 99, 100)
print(numbers)
print()

numbers[1:3] = 'co?'
print(numbers)
print()
