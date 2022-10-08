from datetime import date

h = 'datetime.date'
print(f'\n{h:*^50}')

helloween = date(2020, 10, 31)
print(helloween)
# helloween.isoformat()
print(helloween.day)
print(helloween.month)
print(helloween.year)

h = 'datetime.date.today'
print(f'\n{h:*^50}')
now = date.today()
print('today:', now)

h = 'datetime.date.timedelta'
print(f'\n{h:*^50}')
from datetime import timedelta
one_day = timedelta(days=1)
tommorow = now + one_day
print('tommorow:', tommorow)
print('in 17 days:', now + 17*one_day)
yesterday = now - one_day
print('yesterday:', yesterday)

h = 'datetime.time'
print(f'\n{h:*^50}')
from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

h = 'datetime.datetime'
print(f'\n{h:*^50}')
from datetime import datetime
someday = datetime(2020, 1, 2, 3, 4, 5, 6)
print(someday)

h = 'datetime.now'
print(f'\n{h:*^50}')
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

h = 'combine date and time'
print(f'\n{h:*^50}')
noon = time(12)
this_day = date.today()
noon_tooday = datetime.combine(this_day, noon)
print(noon_tooday)

h = 'time'
print(f'\n{h:*^50}')
import time
now = time.time()
print('now=time.time():', now)
print('ctime(now):', time.ctime(now))
print('localtime(now):', time.localtime(now))
print('gmtime(now):', time.gmtime(now))
print('localtime():', time.localtime())
print('gmtime():', time.gmtime())

print('\n')
now = time.localtime()
print('now=time.localtime():', now)
print('now[0]:', now[0])
print('now.tm_year:', now.tm_year)
print('list of tm_:', list(now[x] for x in range(0, 9)))

tm = time.localtime()
print('mktime:', time.mktime(tm))

h = 'strftime'
print(f'\n{h:*^50}')
fmt = "Dzisiaj jest %Y-%m-%d, godzina %H:%M:%S"
t = time.localtime()
print('t = time.localtime():', t)
print('time.strftime(fmt, t):', time.strftime(fmt, t))

some_day = date(2022, 4, 22)
print('some_day = date(2022, 4, 22):', some_day)
print('some_day.strftime(fmt):', some_day.strftime(fmt))

from datetime import time
some_time = time(10, 35)
print('some_time = time(10, 35):', some_time)
print('some_time.strftime(fmt):', some_time.strftime(fmt))

h = 'strptime'
print(f'\n{h:*^50}')
import time
fmt = "%Y-%m-%d"
print('time.strptime("2022-04-22", "%Y-%m-%d"):', time.strptime("2022-04-22", fmt))


h = 'locale'
print(f'\n{h:*^50}')
import locale
from datetime import date
halloween = date(2019, 10, 31)
print('locale.LC_TIME:', locale.LC_TIME)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is', 'pl_pl']:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime("%A, %B %d"))

names = locale.locale_alias.keys()
print('locale.locale_alias.keys():', names)
good_names = [name for name in names if len(name) == 5 and name[2] == '_']
print('first of 5 good_names:', good_names[:5])
de = [name for name in names if name.startswith('de')]
print('starts with de:', de)