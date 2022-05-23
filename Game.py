from random import randint
from time import sleep

pl = int(input('''(1) Pedra
(2) Papel
(3) Tesoura
Vamos jogar JockenPo, escolha sua opçao: '''))
if pl != 1 and  pl != 2 and pl != 3:
    print('\033[1;31mOpçao Invalida recomeçe!!')
else:
    print('Deixa eu pensar...')
    sleep(2)
    print('Ja sei')
    jg = randint(1, 3)

    if pl == jg:
        print('\033[1;36mDeu empate!!')

    elif pl == 1 and jg == 3:
        print('O computador escolheu Tesoura')
        print('O jogador escolheu Pedra')
        print('Voce \033[1;92mganhou!!')

    elif pl == 3 and jg == 2:
        print('O computador escolheu Papel')
        print('O jogador escolheu Tesoura')
        print('Voce \033[1;92mganhou!!')

    elif pl == 2 and jg == 1:
        print('O computador escolheu Pedra')
        print('O jogador escolheu Papel')
        print('Voce \033[1;92mGanhou!!')

    elif jg == 1 and pl == 3:
        print('O computador escolheu Pedra')
        print('O jogador escolheu Tesoura')
        print('O computador \033[1;96mganhou!!')
    elif jg == 3 and pl == 2:
        print('O computador escolheu Tesoura')
        print('O jogador escolheu Papel')
        print('Computador \033[1;96mganhou!!')
    elif jg == 2 and pl == 1:
        print('O computador escolheu Papel')
        print('O jogador escolheu Pedra')
        print('O Computador \033[1;96mGanhou!!')
        
