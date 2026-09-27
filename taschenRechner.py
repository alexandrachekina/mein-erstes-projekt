def addition(zahlen):
    sum = 0
    for zahl in zahlen:
        sum += zahl
        return sum

def substraktion(zahlen):
    sub = zahlen[0]
    for zahl in zahlen[1:]:
        sub -= zahl
        return sub


def division(zahlen):
    div = zahlen[0]
    for zahl in zahlen[1:]:
        div /= zahl
        return div

def Multiplikation(zahlen):
    mul = 1
    for zahl in zahlen:
        mul*= zahl
        return mul
