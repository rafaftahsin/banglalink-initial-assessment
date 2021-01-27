import datetime

T = int(input())

for t in range(T):
    # Ref: https://www.programiz.com/python-programming/datetime/strptime
    t1 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    # Ref: https://stackoverflow.com/a/43308104/4814427
    dt = int((t1 - t2).total_seconds())
    print(dt)


