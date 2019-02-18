class Fraction:
    def __init__(self, nominator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        self.nominator = nominator
        self.denominator = denominator

    def __eq__(self, other):
        return self.nominator / self.denominator == other.nominator / other.denominator

    def __ne__(self, other):
        return self.nominator / self.denominator != other.nominator / other.denominator

    def __lt__(self, other):
        return self.nominator / self.denominator < other.nominator / other.denominator

    def __le__(self, other):
        return self.nominator / self.denominator <= other.nominator / other.denominator

    def __gt__(self, other):
        return self.nominator / self.denominator > other.nominator / other.denominator

    def __ge__(self, other):
        return self.nominator / self.denominator >= other.nominator / other.denominator

    def __str__(self):
        return f'Fraction ({self.nominator}, {self.denominator})'

    def __repr__(self):
        return f'Fraction ({self.nominator}, {self.denominator})'

    def __hash__(self):
        return hash(self.nominator / self.denominator)


def main():
    m = 1
    d = {Fraction(0.8): 'asd'}
    print(d[Fraction(8, 10)])
    print(d[Fraction(4, 5)])


if __name__ == '__main__':
    main()
