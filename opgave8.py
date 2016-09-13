def gevoelsCalc(t, b, l) :
    som = 0
    calc = (13 + 0.62*t -14*(b**0.24) + 0.47*l**0.24)
    heleCalc = som +calc
    print(heleCalc)

gevoelsCalc(20,2,40)