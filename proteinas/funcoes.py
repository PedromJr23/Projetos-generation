def menu():
    print("Bem vindo ao protein- cal- gen")
    print("Escolha a opção")
    print("1- Calcular proteinas")
    print("2 - Calcular IMC")
    print("Qualquer outro numero - sair")

## -- função para saber o objetivo do usuario
def menu_objetivo():
    print("Qual a sua meta") 
    print("1- Perder peso")
    print("2 - Manter peso") 
    print("3 - Ganhar peso")   

def calc_proteinas(peso, objetivo):
    if objetivo == 1:
        return peso * 1.2
    elif objetivo == 2:
        return peso * 1.6
    elif objetivo == 3:
        return peso *1.8
    else:
        return None
    # o comando None, é para não fazer nada
def calcu_imc(peso,altura):
    return peso/(altura**2)

def imc(valor_imc):
    if valor_imc <18.5:
        return "abaixo do peso"
    elif valor_imc < 24.9:
        return "peso normal"
    elif valor_imc < 29.9:
        return "Para de comer hamburguer"
    else:
        return "Po, já te disse tá foda né ?"