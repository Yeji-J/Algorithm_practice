# str => int
str1 = '1234'
sm = 0
for ch in str1:
    sm = sm * 10 + ord(ch) - ord('0')
print(sm, type(sm))

# int => str
i = 123
st = ''
while i > 0:
    st = chr(i % 10 + ord('0')) + st # 기존 문자열의 앞에 하나씩 붙이기
    i //= 10
print(st, type(st))

# 음수일 경우에는 ?
# 기존에 - 곱해서 양수로 만들어 주고 시작

