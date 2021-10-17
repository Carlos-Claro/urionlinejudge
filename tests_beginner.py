# https://www.urionlinejudge.com.br/judge/en/problems/view/1012
def t_1012(x):
    a = x.split()
    triangulo = (float(a[0]) * float(a[2])) / 2
    circulo = 3.14159*(float(a[2])*float(a[2]))
    trapezio = ((float(a[0])+float(a[1]))*float(a[2]))/2
    quadrado = float(a[1])*float(a[1])
    retangulo = float(a[0])*float(a[1])
    return "TRIANGULO: {:0.3f}\n" \
           "CIRCULO: {:0.3f}\n" \
           "TRAPEZIO: {:0.3f}\n" \
           "QUADRADO: {:0.3f}\n" \
           "RETANGULO: {:0.3f}".format(triangulo, circulo, trapezio, quadrado, retangulo)


def test_1012():
    print(t_1012("3.0 4.0 5.2"))
    assert t_1012("3.0 4.0 5.2") == "TRIANGULO: 7.800\nCIRCULO: 84.949\nTRAPEZIO: 18.200\nQUADRADO: 16.000\nRETANGULO: 12.000"
    assert t_1012("12.7 10.4 15.2") == "TRIANGULO: 96.520\nCIRCULO: 725.833\nTRAPEZIO: 175.560\nQUADRADO: 108.160\nRETANGULO: 132.080"

# https://www.urionlinejudge.com.br/judge/en/problems/view/1013
def t_1013(x):
    a = x.split()
    map_ = map(int,a)
    list_ = list(map_)
    maior = (list_[0]+list_[1]+abs(list_[0]-list_[1]))/2
    maior_ = (maior + list_[2] + abs(maior - list_[2])) / 2
    return "{:0.0f} eh o maior".format(maior_)

def t_1013_o(x):
    a = x.split()
    map_ = map(int,a)
    list_ = list(map_)
    maior = 0
    for i in list_:
        if maior == 0:
            maior = i
        maior = (maior+i+abs(maior-i))/2
    return "{:0.0f} eh o maior".format(maior)


def test_1013():
    assert t_1013("7 14 106") == "106 eh o maior"
    assert t_1013_o("7 14 106") == "106 eh o maior"
    assert t_1013_o("7 14 106 105") == "106 eh o maior"
    assert t_1013("217 14 6") == "217 eh o maior"
    assert t_1013_o("217 14 6") == "217 eh o maior"