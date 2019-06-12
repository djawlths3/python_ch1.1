# hello.py
def add(m, n):
    s = m
    s += n
    return s


def mymax(m, n):
    if m > n:
        return m
    else:
        return n


a = 21
b = 1
if a > 1:
    print('a는 1보다 크다')
    for i in range(1, 10):
        print('-->', i)
print('end')
