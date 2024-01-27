from tabuleiro import Tabuleiro


tabuleiro = Tabuleiro()

tabuleiro.preencher_tabuleiro()

tabuleiro.print_tabuleiro()

# print(tabuleiro.get_json_tabuleiro()['data']))

numbers = tabuleiro.get_json_tabuleiro()['data']

cont = 0
for number in numbers:
    print(number['number'], end=' ')
    cont += 1

    if cont % 9 == 0:
        print()
    elif cont % 3 == 0:
        print(end='  ')
    if cont % 27 == 0:
        print()
