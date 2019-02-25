def strip_chars(chars):
    def wrapper(s):
        for char in s:
            if char in chars:
                s = s.replace(char, '')
        return s

    return wrapper


if __name__ == '__main__':
    strip_punctuations = strip_chars(',;:.?!')
    s = 'Please, strip punctuations from this string!'
    print(strip_punctuations(s))
