def validate(f):
    def wrapper(*args):
        for i in args:
            int(i)
        return f(*args)
    return wrapper


@validate
def non_builtin_sum(*args):
    return sum(args)


def main():
    print(non_builtin_sum(1, 2, 'asd'))


if __name__ == "__main__":
    main()
