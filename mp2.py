import multiprocessing
import os
import time


def whoami(what):
    print(f'Process {os.getpid()}: {what}')


def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print(f'\t Obieg {num} z {stop}')
        time.sleep(1)


if __name__ == '__main__':
    whoami('Jestem głównym procesem')
    p = multiprocessing.Process(target=loopy, args=('Jestem loopy',))
    p.start()
    time.sleep(5)
    p.terminate()