from funcoes import *
# * = all = tudo

def menu():
    opcao = input("Escolha uma opção de 1 a 6 ou outra coisa para sair):")
    if opcao not in["1","2","3","4","5","6"]:
        print("Tchau") 
    
    # As linhas problemáticas (if input > 6 / return == "Tchau") foram removidas/adaptadas
    # pois o bloco acima já faz a validação e a saída.

    # Fix: Pedimos os números SOMENTE se a opção for válida (eficiência).
    # Fix: O prompt do num2 foi corrigido para "Digite o numero 2".
    try:
        num1 = float(input("Digite o numero 1: "))
        num2 = float(input("Digite o numero 2: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        return

    # A lógica de cálculo foi corrigida e indentada corretamente.
    if opcao =="1":
        print(soma(num1,num2))
    elif opcao == "2": 
        print(subtracao(num1,num2)) 
    elif opcao == "3": 
        print(multiplicação (num1,num2)) 
    elif opcao == "4": 
        # Fix: Adicionado tratamento para Divisão por Zero (Prática Essencial de Dados)
        if num2 != 0:
            print(divisao(num1,num2)) 
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif opcao == "5": 
        print(potencia(num1,num2))
    elif opcao == "6": 
        print(raiz(num1,num2))
    # O 'else' final foi removido, pois a saída já é tratada no início da função.

# Criação de função principal
if __name__ == "__main__":
 # if __name__ == "__main__":
 # garante que o código só rode quando
 # você executar o main    
    
    menu()