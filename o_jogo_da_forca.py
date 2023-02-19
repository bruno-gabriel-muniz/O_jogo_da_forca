import getpass
# fazer uma função que mostre a forca


def mostra_forca(cont_erro):
    # imprimindo a forca caso o usuário tenha errado 0 vezes
    if cont_erro == 0:
        print('''   Forca
    +--------+
    |        |
             |
             |
             |
             |
             |
    ==========
    ''')
    # imprimindo a forca caso o usuário tenha errado 1 vezes
    elif cont_erro == 1:
        print('''   Forca
    +--------+
    |        |
    O        |
             |
             |
             |
             |
    ==========
    ''')
    # imprimindo a forca caso o usuário tenha errado 2 vezes
    elif cont_erro == 2:
        print('''   Forca
    +--------+
    |        |
    O        |
    |        |
             |
             |
             |
    ==========
    ''')
    # imprimindo a forca caso o usuário tenha errado 3 vezes
    elif cont_erro == 3:
        print('''   Forca
    +--------+
    |        |
    O        |
    |\\      |
             |
             |
             |
    ==========
    ''')
    # imprimindo a forca caso o usuário tenha errado 4 vezes
    elif cont_erro == 4:
        print('''   Forca
    +--------+
    |        |
    O        |
   /|\\      |
             |
             |
             |
    ==========
    ''')
    # imprimindo a forca caso o usuário tenha errado 5 vezes
    elif cont_erro == 5:
        print('''   Forca
    +--------+
    |        |
    O        |
   /|\\      |
     \\      |
             |
             |
    ==========
    ''')
    # imprimindo a forca caso o usuário tenha errado 6
    # vezes e anunciando a derrota
    elif cont_erro == 6:
        print('''   Forca
    +--------+
    |        |
    O        |
   /|\\      |
   / \\      |
             |
             |
    ==========
    AND game''')
# função que pede a próxima tentativa de letra e a quarda na
# lista das certas ou na das erradas dependendo do caso


def pede_letra(palavra_sort, li_letras_er, li_letras_cer):
    # pulando uma linha para facilitar a visualisação para
    # o usuário
    print()
    while True:
        # pedir para o usuário digitar uma letra
        letra = input("Próxima letrar: ").lower()
        if not ((letra in li_letras_er) or (letra in li_letras_cer)):
            break
        print("você já tentou esta letra. Tente novamente.")
    # variavel que verifica se a letra é certa e se for ela faz
    # a parte que adciona as erradas não funcionar
    v = 0
    # verificar se a letra está na palavra com a função in e
    # executa a quantidade de vezes que a letra está na palavra
    for a in range(palavra_sort.count(letra)):
        # verificando que a letra está correta e não deve ser
        # acionado a parte que adciona esta para a lista das
        # erradas
        v = 1
        # adicionando a letra nas casas certas
        li_letras_cer[palavra_sort.index(letra)] = letra
        # se sim adcionar a letra na lista da palavar no indice
        # certo na demosntração da palavra através das função
        # mostra palavra
        palavra_sort[palavra_sort.index(letra)] = []
    # caso não devolver a letra para a lista das erradas e
    # adicionar a variavel de erro
    if not v:
        li_letras_er.append(letra)
    # retornando as duas listas para o main
    return li_letras_er, li_letras_cer
# esta função pede a palavra que o usuário quer que seja
# adivinhada pela outra pessoas


def pede_palavra():
    # pedindo a palavra de forma oculta para o usuário que
    # escolhe a palavra para que o outro não veja a palavra
    palavra_escolhida = getpass.getpass(
        "Digite a palavra escolhida para ser advinhada: ").lower()
    # transformando a entrada do usuário em uma lista com os caracteres para
    # comparar as letras futuramente
    palavra_escolhida_li = list(palavra_escolhida)[:]
    # retornando a palavra e a lista da palavra para o programa
    return palavra_escolhida_li, palavra_escolhida
# esta função mostra quantas letras da palavra escolhida o
# usuário acertou


def mostra_letras_c(li_letras_cer):
    # mostra o o que são as letras que serão exibidas e ao
    # inves de pular uma linha no final a função print da um
    # espeço
    print("Letras certas até agora:", end=" ")
    # percorrendo os elementos da lista letras certas que
    # usuário marcou
    for i in li_letras_cer:
        # imprimindo cada letra (caso certa) ou _ (caso ainda
        # esteja indefinida) individualmente fazendoa função
        # print dar um espaço ao final para facilitar a visualição
        print(i, end=" ")
    # imprimindo uma linha vazia para facilitar a visualização da
    # palavra pelo o usuário
    print()
# esta as letra erradas sem espaço entre elas


def mostra_letras_er(li_letras_er):
    # printando uma linha vazia para dar um espaço entre a lista das
    # listas certas das erradas
    print()
    # anunciando quais são os dados que serão exibidos fazendo a função não
    # pular uma linha ao final para que os dados fiquem na mesma linha
    print(
        "As letras que foram digitadas até agora e estão erradas são:",
        end=" ")
    # percorrendo todas as letras erradas
    for i in li_letras_er:
        # mostrando cada letra errada na mesma linha
        print(i, end="")
# função que executa todas as outra e faz o jogo da forca acontecer


def main():
    # pedindo a palavra que será adivinhada para o outro usuário
    palavra_sort_a, palavra_sort = pede_palavra()
    # criando uma lista para colocar as letras certas do usuário
    li_letras_cer = []
    # criando uma lista para colocar as letras erradas do usuário
    li_letras_er = []
    # criando os espaços corretos das letras na lista de letras
    # certas para mostra a casas das letras
    for t in range(len(palavra_sort)):
        # adcionando o espaço para a cada letra da palavra
        li_letras_cer.append("_")
    # rodando o jogo em si e comparando se o usuário ganhou o jogo
    while list(palavra_sort) != li_letras_cer:
        # mostrando a forca para o usuário
        mostra_forca(len(li_letras_er))
        # verificando se o usuário perdeu o jogo
        if len(li_letras_er) >= 6:
            # se sim mostrando que o jogo acabou e a palavra certa
            print("Fim de jogo.")
            print("A palavra era: %s" % (palavra_sort))
            # perguntando se o usuário deseja jogar de novo
            if input('''
Você deseja jogar de novo? digite Sim para jogar/Não para não jogar: '''
                     ).upper().startswith("S"):
                # caso quiera retornando a função principal
                # para o jogo se repetir
                return main()
            # se não retornando nada para o jogo acabar
            else:
                return
        # caso ainda não tenha perdido mostrando as letras da palavra
        # acertadas a té o momento
        mostra_letras_c(li_letras_cer)
        # mostrando a lista das tentativas erradas até o momento
        mostra_letras_er(li_letras_er)
        # pedindo a próxima letra e atualizando as listas das letras certas
        # e erradas
        li_letras_er, li_letras_cer = pede_letra(
            palavra_sort_a, li_letras_er, li_letras_cer)
    # mostrando todas as letras corretas da palavra
    mostra_letras_c(li_letras_cer)
    # informando que o usuário ganhou já que só isso pode ter acontecido
    # para o programa chegar nesta parte, pois quando ele perde o
    # programa pergunta no ciclo
    # se ele quer jogar de novo ou não e encerra o programa caso ele não queira
    print("Você ganhou!!")
    # perguntando se o usuário quer jogar de novo ou não
    if input('''
Você deseja jogar de novo? digite Sim para jogar/Não para não jogar: '''
             ).upper().startswith("S"):
        # caso queira chamando a função para que o jogo ocorra novamente
        return main()


# chamando a função principal para o jogo ser iniciado
main()
