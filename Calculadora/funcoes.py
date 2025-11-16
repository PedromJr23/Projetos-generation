def soma (num1, num2):
    return num1+num2
# return é um comando similiar ao print
# ele retorna a informação de um função

def subtracao (num1,num2):
    return num1-num2

def multiplicação (num1,num2):
    return num1 *num2

def divisao (num1,num2):
    if num2 ==0:
      return "Erro, não posso dividir por 0"
    return num1/num2


def potencia(num1,num2):
    return num1 ** num2

def raiz(num1,num2):
    if num2 < 0:
        return "Erro ao calcular"
    return num1 ** (1/num2)