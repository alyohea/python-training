import random

from multiprocessing import Process
from time import sleep


class Philosopher(Process):

    def __init__(self, id, left_fork_event, right_fork_event):
        super(Philosopher, self).__init__()
        self.id = id  # int
        left_fork_event.set()
        right_fork_event.set()
        self.left_fork = (Fork(self.id % 5), left_fork_event)
        self.right_fork = (Fork((self.id + 1) % 5), right_fork_event)
        self.eat_time = random.randint(0, 5)
        self.think_time = random.randint(0, 5)

    def think(self):
        print(f'Philosophy {self.id} is thinking')
        sleep(self.think_time)

    def eat(self):
        print(f'Philosophy {self.id} is eating')
        sleep(self.eat_time)

    def take(self, fork, timeout=None):
        print(f'{self} take {fork[0]}')
        fork[1].clear()

    def put(self, fork):
        print(f'{self} put {fork[0]}')
        fork[1].set()

    def run(self):
        while True:
            self.think()
            self.left_fork[1].wait()
            self.take(self.left_fork)
            self.right_fork[1].wait()
            self.take(self.right_fork)
            self.eat()
            self.put(self.left_fork)
            self.put(self.right_fork)

    def __str__(self):
        return f'Philosophy {self.id}'


class Fork:
    def __init__(self, id):
        self.id = id  # int

    def __str__(self):
        return f'Fork {self.id}'
