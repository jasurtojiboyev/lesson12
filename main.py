num = int(input("son kriting :"))


def sonlar_kopaytmasi(n):
    number = 1
    for x in range(1, num + 1):
        number = number * x
    print(number)
sonlar_kopaytmasi(num)
