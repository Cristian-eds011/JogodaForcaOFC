def escolha_menu():
    escolha = ''
    while escolha != 'R' and escolha != 'I' and escolha != 'S':
        escolha = input('Escolha: ').upper().strip()
    return escolha


def cria_2_usuarios():
    lista_jogadores = []
    for i in range(1, 3):
        print(f'Adicionando {i}° jogador.')
        usuario = dict()
        usuario['nome'] = input('Informe o seu nome: ').title().strip()
        usuario['pontos'] = 0
        usuario['desafiado'] = False
        lista_jogadores.append(usuario)
    return lista_jogadores


def input_definicao_palavra(jogador):
    print(f"{jogador.get('nome')}, "
          f"informe a palava que deseja desafiar o seu adversário. "
          f"Tome cuidado para que ele não veja! "
          f"OBS: INFORME A PALAVRA SEM ACENTOS.")
    while True:
        possue_acentos = False
        palavra = input('Qual palavra deseja usar? (Ex.: Abelha, Cachorro...): ').upper().strip()
        if palavra.isnumeric():
            print('Informe uma palavra, não números!')
        else:
            for c in palavra:
                if c in ['Á','À','Ã','Â','Ó','Õ','Ô','Ò','Ê','É','È','Í','Ì','Ú','Ù','Û',]:
                    print('Por favor, não digitar os acentos.')
                    possue_acentos = True
            if not possue_acentos and palavra:
                break
    return palavra


def input_dica_palavra(jogador):
    print(f'{jogador["nome"]}, informe uma dica para seu adversário.')
    while True:
        dica = input('Qual dica vai mostrar? (Ex.: Esporte, Comida...): ').upper().strip()
        if dica:
            break
    return dica


def input_letra(jogador, letrascertas, letraserradas, palavra):
    while True:
        letra = input(f'{jogador.get("nome")}, informe uma letra ou (Digite "CHUTE" para chutar a palavra): ').upper().strip()
        if letra == 'CHUTE':
            chute = input('Seu chute é: ').upper().strip()
            return 'Ganhou' if chute == palavra else 'Perdeu'
        else:
            if letra in letrascertas or letra in letraserradas:
                print('Letra já foi usada. Informe uma letra que não foi usada!')
            else:
                if len(letra) > 1 or len(letra) < 1:
                    print('É apenas uma letra, seu apedeuta!')
                elif letra.isnumeric():
                    print('Por favor, informe uma letra e não um número, seu apedeuta!')
                else:
                    break
    return letra.upper()


def input_jogar_outra_rodada():
    continuar = 'x'
    while continuar not in 'SN':
        continuar = input('Jogar outra rodada? [S/N]: ').upper().strip()
    return continuar
