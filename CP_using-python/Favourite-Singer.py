singer = {}

n = int(input())
# print(n)
for i in range(n):
    val = int(input())
    if val in singer:
        singer[val] += 1
    else:
        singer[val] = 1
count = 0
print1 = 0
for key,val in singer.items():
        count = max(count, val)
        print1 = key if val == count else print1
print(print1)
