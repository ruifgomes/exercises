resultado = 0
for multiple in range(0,10):
    if multiple%3 == 0 or multiple%5 == 0:
        resultado = resultado + multiple
        print("multiple: " + str(multiple) + " res: " + str(resultado))
        print("multiple: {} res: {}".format(multiple, resultado))