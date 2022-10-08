import threading as th
import queue
import time


def washer(dishes, output):
    for dish in dishes:
        print(f'Myję talerz na {dish}')
        output.put(dish)


def dryer(input):
    while True:
        dish = input.get()
        print(f'\nWycieram talerz na {dish}')
        input.task_done()


dish_queue = queue.Queue()
for n in range(2):
    dryer_thread = th.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()
dishes = ['sałatkę', 'pieczywo', 'danie główne', 'deser']
washer(dishes, dish_queue)
dish_queue.join()
dishes = ['sałatkę2', 'pieczywo2', 'danie główne2', 'deser2']
washer(dishes, dish_queue)
dish_queue.join()
