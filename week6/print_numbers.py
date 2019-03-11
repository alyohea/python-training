import threading

mutex = threading.Lock()
number = 0


def odd(count):
    global number
    while number < count:
        with mutex:
            if number % 2 == 1:
                print(f'odd: {number}')
                number += 1


def even(count):
    global number
    while number < count:
        with mutex:
            if number % 2 == 0:
                print(f'evn: {number}')
                number += 1


def get_numbers(count):
    t1 = threading.Thread(target=even, args=(count,))
    t2 = threading.Thread(target=odd, args=(count,))
    t1.start()
    t2.start()


def main():
    get_numbers(100)


if __name__ == '__main__':
    main()
