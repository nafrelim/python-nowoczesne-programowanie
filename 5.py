"""
Rozdział 5 - ciągi znaków
"""

rzeczownik = 'lokomotywa'
czasownik = 'Stoi'
zdanie1 = f'{czasownik = :>20} na stacji {rzeczownik.upper() = :^20.4}.'
print(zdanie1)

piosenka = """W żółtych płomieniach liści brzoza dopala się ślicznie.
...Grudzień ucieka za grudniem, styczeń mi stuka za styczniem."""
print(piosenka.replace(' s', ' S'))

pytania = ["Jaki kraj ma najwięcej jezior na świecie?", "Jaki kraj wytwarza najwięcej tlenu?",
           "Jaki kraj produkuje najwięcej energii elektrycznej ze źródeł odnawialnych?"]
odpowiedzi = ["Rosja", "Kanada", "Norwegia"]
p_o = ((0, 1), (1, 2), (2, 0))
for p, o in p_o:
    print("Pyt.:", pytania[p])
    print("Odp.:", odpowiedzi[o])
    print()

wiersz = '''Wróbelek jest mała %s,
wróbelek istotka %s,
on brzydką stonogę %s,
lecz nikt nie popiera %s.'''
słowa = ('ptaszyna', 'niewielka', 'pochłania', 'wróbelka')
print(wiersz % słowa)

reklamacja = '''
REKLAMACJA
Oświadczam, że produkt {produkt}, który kupiłem dn. {data} za kwotę {cena} zł
w ilości {liczba} sztuk, jest niezgodny z opisem.
Z poważaniem,
{klient}
'''
print(reklamacja.format(produkt='zegarek', data='2020-05-11', cena='49', liczba='3', klient='Jan Nowak'))

rzeczy = ["lamp", "wag", "butelk"]
for rzecz in rzeczy:
    z_wielkiej = rzecz.capitalize()
    print("%sa %sowa" % (z_wielkiej, z_wielkiej))
print()

for rzecz in rzeczy:
    z_wielkiej = rzecz.capitalize()
    print("{}a {}owa".format(z_wielkiej, z_wielkiej))
print()

for rzecz in rzeczy:
    z_wielkiej = rzecz.capitalize()
    print(f"{z_wielkiej}a {z_wielkiej}owa")
