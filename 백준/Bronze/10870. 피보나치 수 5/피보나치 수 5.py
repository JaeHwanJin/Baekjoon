def fi(num):
    if num <= 1:
        return num
    return fi(num-1) + fi(num-2)

print(fi(int(input())))