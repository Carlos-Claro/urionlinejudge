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


# https://www.urionlinejudge.com.br/judge/en/problems/view/1014
def t_1014(x,y):
    media = int(x) / float(y)
    return "{:0.3f} km/l".format(media)


def test_1014():
    assert t_1014("500", "35.0") == "14.286 km/l"
    assert t_1014("2254", "124.4") == "18.119 km/l"
    assert t_1014("4554", "464.6") == "9.802 km/l"


# https://www.urionlinejudge.com.br/judge/en/problems/view/1015
def t_1015(x,y):
    a = x.split()
    map_a = map(float, a)
    list_a = list(map_a)
    b = y.split()
    map_b = map(float,b)
    list_b = list(map_b)
    c = ( ( (list_b[0] - list_a[0]) ** 2 ) + ( (list_b[1] - list_a[1]) ** 2 ) ) ** 0.5
    return float("{:0.4f}".format(c))


def test_1015():
    assert t_1015("1.0 7.0","5.0 9.0") == 4.4721
    assert t_1015("-2.5 0.4", "12.1 7.3") == 16.1484
    assert t_1015("2.5 -0.4", "-12.2 7.0") == 16.4575


# https://www.urionlinejudge.com.br/judge/en/problems/view/1016
def t_1016(x):
    a = 60
    b = 90
    x = int(x)
    t = (x / (b - a)) * 60
    return "{:0.0f} minutos".format(t)


def test_1016():
    assert t_1016("30") == "60 minutos"
    assert t_1016("110") == "220 minutos"
    assert t_1016("7") == "14 minutos"


# https://www.urionlinejudge.com.br/judge/en/problems/view/1017
def t_1017(a,b):
    x = 12
    litros = (int(a) * int(b))/x
    return "{:0.3f}".format(litros)


def test_1017():
    assert t_1017("10","85") == "70.833"
    assert t_1017("2", "92") == "15.333"
    assert t_1017("22", "67") == "122.833"

from math import floor
# https://www.urionlinejudge.com.br/judge/en/problems/view/1018
def t_1018(a):
    notas = [100,50,20,10,5,2,1]
    qtde_notas = {}
    sobra = int(a)
    for nota in notas:
        valor = sobra // nota
        qtde_notas[nota] = 0
        if valor > 0:
            qtde_notas[nota] = valor
            sobra = sobra % nota
    retorno = '{:0.0f}\n'.format(a)
    for c,v in qtde_notas.items():
        if c == 1:
            retorno += "{:0.0f} nota(s) de R$ {},00".format(v,c)
        else:
            retorno += "{:0.0f} nota(s) de R$ {},00\n".format(v, c)
    return retorno


def test_1018():
    assert t_1018(576) == "576\n5 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n1 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n0 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00"
    assert t_1018(11257) == "11257\n112 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n0 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n1 nota(s) de R$ 2,00\n0 nota(s) de R$ 1,00"
    assert t_1018(503) == "503\n5 nota(s) de R$ 100,00\n0 nota(s) de R$ 50,00\n0 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n0 nota(s) de R$ 5,00\n1 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00"


# https://www.urionlinejudge.com.br/judge/en/problems/view/1019
def t_1019(a):
    x = int(a)
    if x < 60:
        return "0:0:{:0.0f}".format(x)
    horas = 0
    segundos = 0
    minutos = x / 60
    if minutos > 59:
        horas = floor(minutos/60)
        minutos = floor((x - (horas * 3600))/60)
    else:
        minutos = floor(minutos)
    segundos = floor(x - (horas * 3600) - (minutos * 60))
    return "{:0.0f}:{:0.0f}:{:0.0f}".format(horas,minutos,segundos)

from time import gmtime
from time import strftime
def t_1019_o(a):
    x = int(a)
    return strftime("%-H:%-M:%-S", gmtime(x))

def t_1019_sem_imp(a):
    x = int(a)
    h = x//3600
    m = (x%3600)//60
    s = (x%3600)%60
    return "{:0.0f}:{:0.0f}:{:0.0f}".format(h,m,s)


def test_1019():
    assert t_1019(556) == "0:9:16"
    assert t_1019(1) == "0:0:1"
    assert t_1019(140153) == "38:55:53"
    assert t_1019_o(556) == "0:9:16"
    assert t_1019_o(1) == "0:0:1"
    assert t_1019_sem_imp(556) == "0:9:16"
    assert t_1019_sem_imp(1) == "0:0:1"
    assert t_1019_sem_imp(140153) == "38:55:53"


# https://www.urionlinejudge.com.br/judge/en/problems/view/1020
def t_1020(a):
    x = int(a)
    ano = x//365
    mes = (x%365)//30
    dias = (x%365)%30
    return "{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, mes, dias)


def test_1020():
    assert t_1020(400) == "1 ano(s)\n1 mes(es)\n5 dia(s)"
    assert t_1020(800) == "2 ano(s)\n2 mes(es)\n10 dia(s)"
    assert t_1020(30) == "0 ano(s)\n1 mes(es)\n0 dia(s)"


# https://www.urionlinejudge.com.br/judge/en/problems/view/1021
def t_1021(a):
    moedas = {
        100.00:'nota',
        50.00:'nota',
        20.00:'nota',
        10.00:'nota',
        5.00:'nota',
        2.00:'nota',
        1.00:'moeda',
        0.50:'moeda',
        0.25:'moeda',
        0.10:'moeda',
        0.05:'moeda',
        0.01:'moeda'
    }
    sobra = float(a) + 0.001
    retorno = 'NOTAS:\n'
    for m,tipo in moedas.items():
        moeda = m
        if moeda == 1.00:
            retorno += "MOEDAS:\n"
        valor = sobra//moeda
        retorno += "{:0.0f} {}(s) de R$ {:0.2f}".format(valor, tipo, moeda)
        sobra = sobra%moeda
        if moeda != 0.01:
            retorno += "\n"
    print(retorno)
    return retorno


def test_1021():
    assert t_1021(576.73) == "NOTAS:\n" \
                                "5 nota(s) de R$ 100.00\n" \
                                "1 nota(s) de R$ 50.00\n" \
                                "1 nota(s) de R$ 20.00\n" \
                                "0 nota(s) de R$ 10.00\n" \
                                "1 nota(s) de R$ 5.00\n" \
                                "0 nota(s) de R$ 2.00\n" \
                                "MOEDAS:\n" \
                                "1 moeda(s) de R$ 1.00\n" \
                                "1 moeda(s) de R$ 0.50\n" \
                                "0 moeda(s) de R$ 0.25\n" \
                                "2 moeda(s) de R$ 0.10\n" \
                                "0 moeda(s) de R$ 0.05\n" \
                                "3 moeda(s) de R$ 0.01"
    assert t_1021(4.00) == "NOTAS:\n" \
                                "0 nota(s) de R$ 100.00\n" \
                                "0 nota(s) de R$ 50.00\n" \
                                "0 nota(s) de R$ 20.00\n" \
                                "0 nota(s) de R$ 10.00\n" \
                                "0 nota(s) de R$ 5.00\n" \
                                "2 nota(s) de R$ 2.00\n" \
                                "MOEDAS:\n" \
                                "0 moeda(s) de R$ 1.00\n" \
                                "0 moeda(s) de R$ 0.50\n" \
                                "0 moeda(s) de R$ 0.25\n" \
                                "0 moeda(s) de R$ 0.10\n" \
                                "0 moeda(s) de R$ 0.05\n" \
                                "0 moeda(s) de R$ 0.01"
    assert t_1021(91.01) == "NOTAS:\n" \
                                "0 nota(s) de R$ 100.00\n" \
                                "1 nota(s) de R$ 50.00\n" \
                                "2 nota(s) de R$ 20.00\n" \
                                "0 nota(s) de R$ 10.00\n" \
                                "0 nota(s) de R$ 5.00\n" \
                                "0 nota(s) de R$ 2.00\n" \
                                "MOEDAS:\n" \
                                "1 moeda(s) de R$ 1.00\n" \
                                "0 moeda(s) de R$ 0.50\n" \
                                "0 moeda(s) de R$ 0.25\n" \
                                "0 moeda(s) de R$ 0.10\n" \
                                "0 moeda(s) de R$ 0.05\n" \
                                "1 moeda(s) de R$ 0.01"
    assert t_1021(44.55) == "NOTAS:\n" \
                            "0 nota(s) de R$ 100.00\n" \
                            "0 nota(s) de R$ 50.00\n" \
                            "2 nota(s) de R$ 20.00\n" \
                            "0 nota(s) de R$ 10.00\n" \
                            "0 nota(s) de R$ 5.00\n" \
                            "2 nota(s) de R$ 2.00\n" \
                            "MOEDAS:\n" \
                            "0 moeda(s) de R$ 1.00\n" \
                            "1 moeda(s) de R$ 0.50\n" \
                            "0 moeda(s) de R$ 0.25\n" \
                            "0 moeda(s) de R$ 0.10\n" \
                            "1 moeda(s) de R$ 0.05\n" \
                            "0 moeda(s) de R$ 0.01"
    assert t_1021(77.77) == "NOTAS:\n" \
                            "0 nota(s) de R$ 100.00\n" \
                            "1 nota(s) de R$ 50.00\n" \
                            "1 nota(s) de R$ 20.00\n" \
                            "0 nota(s) de R$ 10.00\n" \
                            "1 nota(s) de R$ 5.00\n" \
                            "1 nota(s) de R$ 2.00\n" \
                            "MOEDAS:\n" \
                            "0 moeda(s) de R$ 1.00\n" \
                            "1 moeda(s) de R$ 0.50\n" \
                            "1 moeda(s) de R$ 0.25\n" \
                            "0 moeda(s) de R$ 0.10\n" \
                            "0 moeda(s) de R$ 0.05\n" \
                            "2 moeda(s) de R$ 0.01"


# https://www.urionlinejudge.com.br/judge/en/problems/view/1035
def t_1035(a, b, c, d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if ( b > c and d > a and (c+d) > (a+b) and c >= 0 and d >= 0 and a%2 == 0):
        retorno = "Valores aceitos"
    else:
        retorno = "Valores nao aceitos"
    return retorno


def test_1035():
    assert t_1035(5,6,7,8) == "Valores nao aceitos"
    assert t_1035(2,3,2,6) == "Valores aceitos"
