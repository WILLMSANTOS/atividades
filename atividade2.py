# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário.
def multiplo_de_5e3(numero):
    if numero % 5 == 0: 
        print("e multiplo de 5")
        if numero % 3 == 0:
            print("e multiplo de 3")
            return True
        else:
            print("nao e multiplo de 3")

    else:
        print("nao e multiplo de 5")
        return False


    
    
numero = (int(input("Insira um número inteiro: ")))

print(multiplo_de_5e3(numero))