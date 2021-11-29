n = int(input("請輸入聖誕樹大小 (大於3):"))
while n < 3:
  n = int(input("請輸入大於3的數字:"))

star = "*"
blank = " "
total = 2 * n

for i in range(n):
  layer_num = 2 * (i + 1) +1
  for j in range(layer_num):
    s = j
    b = total - s
    layer = blank * b + star * s + "*" + star * s + blank * b
    print(f"{layer}")