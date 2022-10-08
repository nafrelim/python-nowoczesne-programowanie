import os


h = 'read and write'
print(f'\n{h:*^50}')

fout = open('oops.txt', 'wt')
fout.close()

fout = open('oops.txt', 'wt')
print('Utworzyłem plik.', file=fout)
fout.close()

poem = '''Pewien zbrojarz-betoniarz spod Limy
wolał lato ciut bardziej od zimy.
Syn go pytał: "O, tato!
Czemuż ty wolisz lato...?!"
Na pytaniu tym utwór kończymy.'''
print('len(poem):', len(poem))
fout = open('oops.txt', 'wt')
print(fout.write(poem))
fout.close()

fout = open('oops2.txt', 'wt')
print(poem, file=fout)
fout.close()

fout = open('oops3.txt', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('wiersz.txt', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(poem[offset:offset+chunk]))  # wyświetla liczbę zapisanych znaków
    offset += chunk
fout.close()

try:  # ochrona istniejącego pliku
    fout = open('oops.txt', 'xt') # zgłosi wyjątek jak ploik istnieje
    fout.write('raz, dwa, trzy')
    fout.close()
except FileExistsError:
    print('Plik już istnieje.')

print('*'*50)
fin = open('wiersz.txt', 'rt' )
poem = fin.read()
fin.close()
print(poem)

print('*'*50)
poem = ''
fin = open('wiersz.txt', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print(poem)

print('*'*50)
poem = ''
fin = open('wiersz.txt', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(poem)

print('*'*50)
poem = ''
fin = open('wiersz.txt', 'rt')
for line in fin:  # jako iterator
    poem += line
fin.close()
print(poem)

print('*'*50)
fin = open('wiersz.txt', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'linii')
for line in lines:
    print(line, end='')

bdata = bytes(range(0, 256))
print('bdata:', bdata)
print('liczba bajtów bdata:', len(bdata))
fout = open('bdata.bin', 'wb')
print('liczba zapisanych bajtów:', fout.write(bdata))
fout.close()

bdata = bytes(range(0, 256))
fout = open('bdata.bin', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(bdata[offset:offset+chunk]))  # wyświetla liczbę zapisanych bajtów
    offset += chunk
fout.close()

fin = open('bdata.bin', 'rb')
bdata = fin.read()
fin.close()
print('len bdata:', len(bdata), bdata)

fin = open('bdata.bin', 'rb')
print('wskaźnik po otwarciu:', fin.tell())
fin.seek(255)
bdata = fin.read()
print(bdata)

