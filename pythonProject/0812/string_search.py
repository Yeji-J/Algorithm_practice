import sys
sys.stdin = open("../input.txt", 'rt', encoding='UTF8')

T = 10
for test_case in range(1, T+1):
    def length(sentence):
        letter = 0
        for _ in sentence:
            letter += 1
        return letter

    _ = input()
    search = input()
    sen = input()
    cnts = 0

    for i in range(length(sen) - length(search) + 1):
        scan = ''
        for j in range(length(search)):
            scan += sen[i]
            i += 1
        if scan == search:
            cnts += 1


    print(f'#{test_case} {cnts}')
