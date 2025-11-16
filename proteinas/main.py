from funcoes import *

while True:
    menu()
    opcao = input("escolha a opção")
    if opcao == '1':
        menu_objetivo()
        objetivo =int(input("Qual o seu objetivo?"))
        peso =float(input("Qual o seu peso(kg)"))
        
        resultado_proteinas = calc_proteinas(peso,objetivo)
        print("Você precisa de",round(resultado_proteinas,2))
        # usei round para arredondar
    elif opcao == '2':
         peso =float(input("Qual o seu peso(kg)"))
         altura =float(input("Qual a sua altura em metros"))

         resultado_imc = calcu_imc(peso,altura)
         print("Seu Imc é de", resultado_imc)
    
         valor_imc = calcu_imc(peso, altura) # Atribui o resultado (um número)
         print(f"Seu Imc é de {valor_imc:.2f}") # Agora funciona porque valor_imc é um número

         mensagem_usuario = imc(valor_imc)
         print(mensagem_usuario)
    else:
        print("Tchau") 
        break    
