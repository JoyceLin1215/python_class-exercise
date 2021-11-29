money = int(input("你現有的錢:"))
cost = int(input("你的花費:"))
minus = money - cost
change = []

if minus > 0:
  change.append(minus % 5)
  minus = minus - change[0]

  change.append(minus % 10)
  minus = minus - change[1]
  change[1] = int(change[1] / 5)

  change.append(minus % 50)
  minus = minus - change[2]
  change[2] = int(change[2] / 10)

  change.append(minus % 100)
  minus = minus - change[3]
  change[3] = int(change[3] / 50)

  change.append(minus % 1000)
  minus = minus - change[4]
  change[4] = int(change[4] / 100)
  change.append(minus)
  change[5] = int(change[5] / 1000)

  print(f"1000元:{change[5]}個, 100元:{change[4]}個, 50元:{change[3]}個, 10元:{change[2]}個, 5元:{change[1]}個, 1元:{change[0]}個")
elif minus <0 : print(f"你超支了")
