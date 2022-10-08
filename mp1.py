import multiprocessing
import os


def whoami(what):
    print(f'Process {os.getpid()}: {what}')


if __name__ == '__main__':
    whoami('Jestem głównym procesem')
    for n in range(4):
        p = multiprocessing.Process(target=whoami, args=(f'jestem funkcję {n}',))
        p.start()
