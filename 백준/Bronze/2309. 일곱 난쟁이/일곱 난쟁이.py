Dwarf = []
SUM = 0

for _ in range(9):
    Dwarf.append(int(input()))
    SUM += Dwarf[_]
for i in Dwarf:
    for j in Dwarf:
        if i != j and SUM - (i + j) == 100:
            a = i
            b = j
Dwarf.remove(a)
Dwarf.remove(b)
Dwarf.sort()
for k in Dwarf:
    print(k)