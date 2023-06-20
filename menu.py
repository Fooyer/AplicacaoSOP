from firstfit import alocarMemoria_f, desalocarMemoria_f, list_allocated_blocks_f, list_unallocated_blocks_f
from bestfit import alocarMemoria_b, desalocarMemoria_b, list_allocated_blocks_b, list_unallocated_blocks_b
import os
import time

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Menu:") 
    print("")
    print("1- Alocação First Fit")
    print("2- Alocação Best Fit")
    print("")

    opcao = int(input("Digite uma opção: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:

        case 1:
            
            print("Funções: ")
            print("")
            print("1- Alocar Memória")
            print("2- Desalocar Endereço")
            print("3- Listar Blocos Alocados")
            print("4- Listar Blocos Desalocados")
            print("")

            funcao = int(input("Digite uma função: "))

            match funcao:

                case 1:

                    print("")

                    valor = int(input("Valor a ser alocado: "))

                    print("")

                    print("Carregando...")

                    print("")

                    alocarMemoria_f(valor)

                    time.sleep(3)

                case 2:

                    print("")

                    valor = int(input("Valor a ser alocado: "))

                    print("")

                    print("Carregando...")

                    print("")

                    desalocarMemoria_f(valor)

                    time.sleep(3)

                case 3:
                    
                    os.system('cls' if os.name == 'nt' else 'clear')

                    list_allocated_blocks_f()

                    print("")
                    input("Precione Enter Para Continuar...")

                case 4:
                    
                    os.system('cls' if os.name == 'nt' else 'clear')

                    list_unallocated_blocks_f()

                    print("")
                    input("Precione Enter Para Continuar...")

                case _:

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("Função inválida!")

                    time.sleep(3)
        
        case 2:

            print("Funções: ")
            print("")
            print("1- Alocar Memória")
            print("2- Desalocar Endereço")
            print("3- Listar Blocos Alocados")
            print("4- Listar Blocos Desalocados")
            print("")

            funcao = int(input("Digite uma função: "))

            match funcao:

                case 1:
                    print("")

                    valor = int(input("Valor a ser alocado: "))

                    print("")

                    print("Carregando...")

                    print("")

                    alocarMemoria_b(valor)

                    time.sleep(3)

                case 2:

                    print("")

                    valor = int(input("Valor a ser alocado: "))

                    print("")

                    print("Carregando...")

                    print("")

                    desalocarMemoria_b(valor)

                    time.sleep(3)

                case 3:
                    
                    os.system('cls' if os.name == 'nt' else 'clear')

                    list_allocated_blocks_b()

                    print("")
                    input("Precione Enter Para Continuar...")

                case 4:
                    
                    os.system('cls' if os.name == 'nt' else 'clear')

                    list_unallocated_blocks_b()

                    print("")
                    input("Precione Enter Para Continuar...")

                case _:

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("Função inválida!")

                    time.sleep(3)

        case _:

            print("Opção inválida!")

            time.sleep(3)