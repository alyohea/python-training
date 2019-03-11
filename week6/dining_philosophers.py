from dinner_helper import Philosopher
from multiprocessing import Event


def main():
    forks_events = [Event() for i in range(5)]

    for i in range(5):
        Philosopher(i, forks_events[i % 5], forks_events[(i + 1) % 5]).start()


if __name__ == '__main__':
    main()
