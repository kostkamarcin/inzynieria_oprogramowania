def trojkat(bok_a, bok_b, bok_c, wys_h):
    pole = bok_a * wys_h / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod

def romb(bok_a, wys_h):
    pole = bok_a * wys_h
    obwod = 4 * bok_a
    return pole, obwod

def trapez(bok_a, bok_b, bok_c, bok_d, wys_h):
    pole = (bok_a + bok_b) * wys_h / 2
    obwod = bok_a + bok_b + bok_c + bok_d
    return pole, obwod

print(f'Pole i obwod trojkata wynosza: {trojkat(10, 10, 10, 10)}')
print(f'Pole i obwod rombu: {romb(10, 10)}')
print(f'Pole i obwod trapeza wynosza: {trapez(10, 10, 10, 10, 10)}')
