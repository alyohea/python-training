def person_listener(f):
    def wrapper(people):
        people = sorted(people, key=lambda x: x[1])
        return list(map(f, people))

    return wrapper


@person_listener
def name_format(person):
    return f'Mr. {person[0]}' if person[2] == 'M' else f'Ms. {person[0]}'


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        people = [tuple(line.rsplit(maxsplit=2)) for line in f]
    with open('output.txt', 'w') as f:
        f.writelines('\n'.join(name_format(people)))
