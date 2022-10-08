from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('żółty', 'długi')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {'bill': 'żółty', 'tail': 'długi'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='imponujący', bill='szeroki')
print(duck3)


