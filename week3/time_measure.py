from time import perf_counter


def measure_execution_time(f):
    def wrapper():
        start = perf_counter()
        f()
        end = perf_counter()
        return end - start
    return wrapper


@measure_execution_time
def big_loop():
    for _ in range(100_000_000):
        pass


def main():
    print(big_loop())


if __name__ == "__main__":
    main()
