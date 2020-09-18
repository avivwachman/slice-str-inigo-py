__author__ = "aviv"


def my_func():
    word = "Hello, my name is Inigo Montoya"
    print(word[:5])
    print(word[7:15])
    print(word[::2])
    print(word[2:19:2])


if __name__ == '__main__':
    my_func()
