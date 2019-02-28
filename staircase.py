def staircase(n):
    counter = 1
    while counter <= n:
        print(("#"*counter).rjust(n))
        counter += 1


def double_staircase(n):
    counter = 1
    while counter <= n:
        string = "#"*counter
        print((string+" "+string).center((n*2)+1))
        counter += 1


if __name__ == '__main__':
    n = int(input())
    #staircase(n)
    double_staircase(n)
