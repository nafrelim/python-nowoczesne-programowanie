import re

source = 'Młody Frankenstein'
result = re.match('Mło', source)
print(result)

youpattern = re.compile('Mło')
result = youpattern.match(source)
print(result)
if result:
    print(result.group())

result = re.match('^Mło', source)  # to samo
if result:
    print(result.group())

if result := re.match('Fra', source):  # czy na początku
    print(result.group())

if result := re.search('Fra', source):  # czy gdziekolwiek, pierwsze wystąpienie
    print(result.group())

if result := re.search('.*Fra', source):
    # pierwsze występienie, czy gdziekolwiek dowolna ilość (*) dowoknych znaków(.) zakończonych 'Fra'
    print(result.group())

result = re.findall('n', source)  # zwraca listę wszystkich wystąpień
print(result)

result = re.findall('n.', source)  # zwraca listę wszystkich wystąpień 'n' z jakąś literą po
print(result)

result = re.findall('n.?', source)  # zwraca listę wszystkich wystąpień 'n' z jakąś literą po opcjonanie
print(result)

result = re.split('n', source)  # zwraca listę z podzielonego tekstu wzrocem
print(result)

result = re.sub('n', '?', source)  # zastąpienie wzroca innym wzorcem
print(result)

import string
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])
print(re.findall(r'\d', printable))  # dowolna cyfra
print(re.findall(r'\w', printable))  # dowolny znak alfanumeryczny
print(re.findall(r'\s', printable))  # dowolny znak biały

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall(r'\w', x))

source = '''Siała baba mak,
nie wiedziała jak.'''
print(re.findall(r'ak', source))
print(re.findall(r'ła|ak', source))  # 'ła' lub 'ak'
print(re.findall(r'^baba', source))  # czy zaczyna się od 'baba
print(re.findall(r'^Siała', source))  # czy zaczyna się od 'Siała'
print(re.findall(r'wiedziała$', source))   # czy kończy się na 'wiedziała'
print(re.findall(r'jak\.$', source))  # czy kończy się na 'jak.
print(re.findall(r'[mj]ak', source))  # czy zawiera 'mak' lub 'jak'
print(re.findall(r'[akm]+', source))  # wszystkie kombinacje z tymi literami
print(re.findall(r'ak\W', source))  # czy zawiera 'ak' i dowolny znak nie alfanumeryczny
print(re.findall(r'ała (?=jak)', source))  # czy zawiera 'ała' i po którym jest 'jak'
print(re.findall(r'(?<=ała) jak', source))  #  'jak' poprzedzone 'ała'
