# task1
p1 = '/Users/ross/Desktop/p1.txt'
p2 = '/Users/ross/Desktop/p2.txt'

p1file = open(p1, 'r')
p2file = open(p2, 'w')

for li in p1file.readlines():
    p2file.write(li)

# task2
p1 = '/Users/ross/Desktop/p1.txt'
p2 = '/Users/ross/Desktop/p2.txt'

p1file = open(p1, 'r')
p2file = open(p2, 'w')

cnt = 0
for li in p1file.readlines():
    if cnt == 0:
        p2file.write(li)
    else:
        items = li.split(',')
        p2file.write(items[0]+','+items[1] + ',' + items[2])