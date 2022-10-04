import sys
sys.stdin = open("input.txt", 'rt', encoding='UTF8')

st = input().upper()        # 대문자로 변환
st_dict = dict()            # 문자를 넣을 딕셔너리

for x in st:
    if x not in st_dict.keys():     # key에 해당 문자가 없다면
        st_dict[x] = 1              # 추가
    else:
        st_dict[x] += 1             # 있다면 value +1

V = []
for v in st_dict.values():
    V.append(v)

if V.count(max(V)) > 1:
    print('?')
else:
    for k, v in st_dict.items():
        if v == max(V):
            print(k)