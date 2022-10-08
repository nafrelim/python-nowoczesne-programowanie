import threading as th
import os


def whoami(what):
    print(f'Wątek {th.current_thread()}: {what}')


if __name__ == '__main__':
    whoami('Jestem głównym programem')
    for n in range(4):
        p = th.Thread(target=whoami, args=(f'jestem funkcję {n}',))
        p.start()
