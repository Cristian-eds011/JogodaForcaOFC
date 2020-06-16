from componentes_tela.modulo_inputs import input_definicao_palavra, input_letra, \
    input_jogar_outra_rodada, input_dica_palavra, cria_2_usuarios
from componentes_tela.modulo_print_janelas import desenha_jogo, menu, print_linha, mostrar_pontos, \
    dica_tamanho_palavra, ganhador_rodada, print_palavra_forca
from jogo.modulo_regras_jogo import define_jogador_desafiado_desafiador, obtem_jogador_desafiado, obtem_jogador_desafiador,\
    erro_ou_acerto, ganhador_jogo, caracteres_nulos
from time import sleep
import os

menu()
print_linha(30)
lista = cria_2_usuarios()
print_linha(30)
jogador1 = lista[0]
jogador2 = lista[1]

while True:
    lista_letras_certas = []
    lista_letras_erras = []
    erro = acerto = 0
    define_jogador_desafiado_desafiador(jogador1, jogador2)
    mostrar_pontos(jogador1, jogador2)
    jogador_desafiador = obtem_jogador_desafiador(jogador1, jogador2)
    jogador_desafiado = obtem_jogador_desafiado(jogador1, jogador2)
    palavra = input_definicao_palavra(jogador_desafiador)
    print_linha(4)
    dica = input_dica_palavra(jogador_desafiador)
    print_linha(30)
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    resultado_nulos = caracteres_nulos(palavra)
    acerto += resultado_nulos
    desenha_jogo(erro)
    print_palavra_forca(palavra, lista_letras_certas)
    while True:
        print()
        dica_tamanho_palavra(dica, palavra)
        print()
        letra = input_letra(jogador_desafiado, lista_letras_certas, lista_letras_erras, palavra)
        if letra == 'Perdeu':
            print('\033[33mVocê infelizmente errou!\033[m')
            erro += 6
        elif letra == 'Ganhou':
            print('\033[33mUAU! Você acertou!\033[m')
            acerto += len(palavra)
        else:
            if erro_ou_acerto(letra, palavra) == 'Acertou':
                for c in palavra:
                    if c == letra:
                        if letra not in lista_letras_certas:
                            lista_letras_certas.append(letra)
                        acerto += 1
                    if c == '-':
                        lista_letras_certas.append('-')
            else:
                erro += 1
                lista_letras_erras.append(letra)
            desenha_jogo(erro)
            print_palavra_forca(palavra, lista_letras_certas)
        if acerto >= len(palavra):
            ganhador_rodada(jogador_desafiado.get('nome'))
            jogador_desafiado['pontos'] += 1
            break
        elif erro >= 6:
            print()
            print(f'A palavra era \033[34m{palavra}\033[m')
            ganhador_rodada(jogador_desafiador.get('nome'))
            jogador_desafiador['pontos'] += 1
            break
    continuar = input_jogar_outra_rodada()
    if continuar == 'N':
        print()
        ganhador_jogo(jogador_desafiador, jogador_desafiado)
        mostrar_pontos(jogador1, jogador2)
        break
    os.system('cls' if os.name == 'nt' else 'clear')
