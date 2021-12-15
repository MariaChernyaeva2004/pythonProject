x = int(input())
k = 0
r = 9
y = x % 10
while x > 0:
 k = k + 1
 if r > (x % 10):
  r = x % 10
 x = x // 10
r = y - r
print(k, r)