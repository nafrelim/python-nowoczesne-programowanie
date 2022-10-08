import os
h = ' czy istnieje '
print(f'\n{h:*^50}')
print('czy oops.txt istnieje:', os.path.exists('oops.txt'))
print('czy ./oops.txt istnieje:', os.path.exists('./oops.txt'))
print('czy dups.txt istnieje:', os.path.exists('dups.txt'))
print('czy . istnieje:', os.path.exists('.'))
print('czy ./ istnieje:', os.path.exists('./'))

h = ' czy to plik '
print(f'\n{h:*^50}')
print('czy oops.txt to plik:', os.path.isfile('oops.txt'))
print('czy oops.txt to folder:', os.path.isdir('oops.txt'))
print('czy . to folder:', os.path.isdir('.'))
print('czy .. to folder:', os.path.isdir('..'))

h = ' kopiowanie plikow przy pomocy modulu shutil '
print(f'\n{h:*^50}')
import shutil
shutil.copy('oops.txt', 'ohno.txt')

h = ' zmiana nazwy plikow '
print(f'\n{h:*^50}')
# os.rename('ohno.txt', 'ohwell.txt')

h = ' tworzenie odnosnikow '
print(f'\n{h:*^50}')
# os.link('oops.txt', 'yikes.txt')
print('czy yikes.txt istnieje:', os.path.isfile('yikes.txt'))
print('czy yikes.txt jest linkiem:', os.path.islink('yikes.txt'))
# os.symlink('oops.txt', 'jeepers.txt')
print('czy jeepers.txt jest linkiem:', os.path.islink('jeepers.txt'))


