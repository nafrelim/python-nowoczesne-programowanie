import multiprocessing as mp


def washer(dishes, output):
    for dish in dishes:
        print(f'Myję talerz na {dish}')
        output.put(dish)


def dryer(input):
    while True:
        dish = input.get()
        print(f'Wycieram talerz na {dish}')
        input.task_done()


if __name__ == '__main__':
    mp.freeze_support()
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['sałatkę', 'pieczywo', 'danie główne', 'deser']
    washer(dishes, dish_queue)
    dish_queue.join()

    dishes = ['sałatkę2', 'pieczywo2', 'danie główne2', 'deser2']
    washer(dishes, dish_queue)
    dish_queue.join()

    dryer_proc.terminate()

