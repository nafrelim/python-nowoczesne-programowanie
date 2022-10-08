import os

h = ' id procesu, użytkowników '
print(f'\n{h:*^50}')
print('id procesu (pid):', os.getpid())
print('katalog aktualny:', os.getcwd())
# nie działają pod windows
# print('id użytkownika (uid):', os.getuid())
# print('id grupy (gid):', os.getgid())

h = ' tworzenie procesów przez subprocess '
print(f'\n{h:*^50}')
import subprocess
ret = subprocess.getoutput('dir') # getoutput() zwraca string z przechwyconych danych komendy powłoki systemowe
print(ret)

h = ' tworzenie procesów przez check_output '
print(f'\n{h:*^50}')
# ret = subprocess.check_output(['cmd', 'dir']) # zwraca bajty z przechwyconych danych komendy powłoki systemowe, ale coś nie tak
# print(ret)

h = ' kod zakończenia procesu getstatusoutput '
print(f'\n{h:*^50}')
ret = subprocess.getstatusoutput('dir') # zwraca kod zakończenia i string z przechwyconych danych komendy powłoki systemowe
print(ret)
ret = subprocess.call('dir') # zwraca kod zakończenia, nie zwraca stringu z przechwyconych danych komendy powłoki systemowej
print(ret)
