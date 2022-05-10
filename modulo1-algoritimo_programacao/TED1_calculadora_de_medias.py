from time import sleep


def calc_medias():
    try:
        print('---------------------------------------------------------')
        print('-------------------- Bem-vindo(a) -----------------------')
        print('------------- Programa de calculo de médias! ------------')
        print('Digite três valores e o tipo de média que deseja calcular')
        print('---------------------------------------------------------')

        sleep(1)

        cont = True

        while cont:

            # Entrada de dados pelo usuário:
            num1: int = int(input('\nDigite o primeiro número inteiro: '))
            num2: int = int(input('Digite o segundo número inteiro: '))
            num3: int = int(input('Digite o terceiro número inteiro: '))
            print('\n---------------------------------------------------------------')
            print('Selecione qual operação deseja efetuar com os numero digitados:')
            print('---------------------------------------------------------------')
            op: str = input(
                'A - Média Aritmética'
                '\nP - Média Ponderada'
                '\nH - Média Harmônica\n'
                )

            # Média Aritmética:
            if op == 'a' or op == 'A':
                m_a = (num1 + num2 + num3) / 3
                print(f'A média aritmética dos numeros {num1}, {num2}, e {num3} é {m_a:.2f}')

                menu: str = input('\nDeseja realizar outra operação? (s/n) ')

                if menu == 's' or menu == 'S':
                    continue

                elif menu == 'n' or menu == 'N':
                    cont = False

                else:
                    print('\nDigite uma opção valida')
                    continue

            # Média Ponderada:
            elif op == 'p' or op == 'P':
                m_p = ((num1 * 5) + (num2 * 3) + (num3 * 2)) / ( num1 + num2 + num3)
                print('OBS: Os pesos da média ponderada são respectivamente 5, 3 e 2!')
                print(f'A média aritmética dos numeros {num1}, {num2}, e {num3} é {m_p:.2f}')

                menu: str = input('\nDeseja realizar outra operação? (s/n) ')

                if menu == 's' or menu == 'S':
                    continue

                elif menu == 'n' or menu == 'N':
                    cont = False

                else:
                    print('\nDigite uma opção valida')
                    continue

            # Média Harmônica:
            elif op == 'h' or op == 'H':
                m_h = 3 / ((1 /num1) + (1 / num2) + (1 / num3))
                print(f'A média harmônica dos numeros {num1}, {num2}, e {num3} é {m_h:.2f}')

                menu: str = input('\nDeseja realizar outra operação? (s/n) ')

                if menu == 's' or menu == 'S':
                    continue

                elif menu == 'n' or menu == 'N':
                    cont = False

                else:
                    print('\nDigite uma opção valida')
                    continue
            else:
                print('Digite uma opção valida')

                menu: str = input('\nDeseja tentar novamente?(s/n) ')

                if menu == 's' or menu == 'S':
                    continue

                elif menu == 'n' or menu == 'N':
                    cont = False

                else:
                    print('\nDigite uma opção valida')
        else:
            print('\nObrigada por usar meu programa! Volte sempre ;)')

    except ValueError:
        print('\nDigite valores inteiros')
        sleep(2)
        calc_medias()

calc_medias()


