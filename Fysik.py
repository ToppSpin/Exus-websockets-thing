start = 12000
MonthlyCont = 1376


def räntaräkna(start, cont):
    x = start
    for i in range(36):
        x = (x + cont) * 1.04
    print(x)

räntaräkna(start, MonthlyCont)