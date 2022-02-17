def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

massive1 = list()
inter_cell = list()
massive2 = list()
s = input().split()
n = int(s[0])
m = int(s[1])
last_element = int()

for i in range(1, n+1):
    massive1.append(i)

iterator = cycle(massive1)
while last_element != 1:
    while len(inter_cell) != m:
        j = next(iterator)
        inter_cell.append(j)
        last_element = j
    massive2.append(inter_cell)
    inter_cell = []
    inter_cell.append(last_element)

for i in massive2:
    print(i[0], end='')