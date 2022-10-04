import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

def preord(n):
    if n:
        print(chr(n+64), end="")
        preord(ch1[n])
        preord(ch2[n])

def inord(n):
    if n:
        inord(ch1[n])
        print(chr(n + 64), end="")
        inord(ch2[n])

def postord(n):
    if n:
        postord(ch1[n])
        postord(ch2[n])
        print(chr(n + 64), end="")

N = int(sys.stdin.readline())

ch1 = [0] * (N+1)
ch2 = [0] * (N+1)

for _ in range(N):
    tmp = sys.stdin.readline().split()
    n = ord(tmp[0]) - 64

    if tmp[1] != '.':
        ch1[n] = ord(tmp[1]) - 64

    if tmp[-1] != '.':
        ch2[n] = ord(tmp[-1]) - 64

preord(1)
print()
inord(1)
print()
postord(1)
