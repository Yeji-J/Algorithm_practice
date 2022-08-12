str_input = input()
new = ''
# for i in range(len(str_input)-1, -1, -1):
#     new += str_input[i]

for x in str_input:
    new = x + new

print(new)