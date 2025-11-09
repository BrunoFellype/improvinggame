import os
import time

def passar():
    input('Tecle ENTER para continuar')

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def frase1():
    limpar_tela()
    print('O reino de Elarion viveu séculos de paz sob a proteção dos Cristais da Aurora, relíquias antigas capazes de manter afastadas as forças do caos. Mas agora, uma sombra voltou a se erguer dos confins das Montanhas Negras: Morfor, o Devorador de Almas — uma entidade imortal que se alimenta do medo e da magia dos vivos. Os cristais começaram a se apagar um a um, e o céu de Elarion se tingiu de cinza. O equilíbrio do mundo está prestes a ruir.\n')
    passar()

def frase2(nome):
    limpar_tela()
    print(f'O Grandioso {nome}, o último descendente dos Guardiões da Aurora. Após anos vagando como mercenário, ele retorna ao reino ao ouvir o chamado do destino — e o eco do nome de Morfor.')
    passar()

def frase3(nome):
    limpar_tela()
    print(f'O vento rugia como uma fera faminta enquanto {nome} subia os últimos degraus da escadaria em espiral. Cada passo ecoava entre as paredes negras da fortaleza, cobertas de runas que pulsavam com uma luz vermelha — viva, maléfica. O ar era denso, pesado, cheirava a ferro e morte.')
    passar()

def frase4():
    limpar_tela()
    print('No salão principal, um trono esculpido em ossos esperava. Atrás dele, uma brecha no teto deixava entrar a luz pálida da lua, cortando a escuridão em faixas prateadas.')
    passar()

def frase5():
    limpar_tela()
    print('E ali, sentado com a tranquilidade de um deus entediado, estava Morfor.')
    passar()

def frase6():
    limpar_tela()
    print('Sua forma era humana, mas imperfeita: olhos que ardiam como brasas, pele rachada como pedra, e uma sombra que parecia se mover com vontade própria.')
    passar()

def frase7():
    limpar_tela()
    print('Quando falou, sua voz soou em mil tons — como se o próprio ar o obedecesse.\nMorfor: — "O herdeiro da Aurora... veio me oferecer sua alma?"')
    passar()

def frase8(nome):
    limpar_tela()
    print(f'{nome}: — "Vim pôr fim ao que você começou."')
    passar()

def frase9():
    limpar_tela()
    print('Morfor se levantou devagar.\nMorfor: — "Fim?" — murmurou, caminhando pelo salão. — "Não existe fim, pequeno guerreiro. Eu sou o medo que move reis, o desespero que alimenta deuses. Mate-me, e outro tomará meu lugar."')
    passar()

def frase10(nome):
    limpar_tela()
    print(f'O chão rachou sob seus pés. Sombras se ergueram como serpentes, tentando envolver {nome}. Ficou claro que a batalha começaria.')
    passar()


def frasevitoria1(nome):
    limpar_tela()
    print(f'O salão da fortaleza estava em ruínas.\nChamas azuis devoravam as sombras deixadas por Morfor, enquanto {nome}, ferido, fincava a espada no chão para se manter de pé.')
    passar()

def frasevitoria2():
    limpar_tela()
    print('O corpo do vilão começava a se despedaçar em fragmentos de trevas que se desfaziam no ar, como fumaça sendo sugada pela luz nascente.')
    passar()

def frasevitoria3():
    limpar_tela()
    print('Morfor o fitava com ódio e incredulidade.\nMorfor: — “Você... é só um homem...”')
    passar()

def frasevitoria4(nome):
    limpar_tela()
    print(f'{nome} respirou com dificuldade, mas manteve o olhar firme.\n{nome}— “Um homem... é tudo o que precisa ser... quando a luz o chama.”')
    passar()

def frasevitoria5():
    limpar_tela()
    print('Com um último golpe, ele cravou a Luz da Alvorada no peito de Morfor. Um clarão cegante inundou a fortaleza — e, por um instante, o mundo ficou em silêncio absoluto.')
    passar()

def frasevitoria6(nome):
    limpar_tela()
    print(f'Quando a claridade se dissipou, {nome} estava ajoelhado entre as ruínas. A espada havia se desfeito em pó dourado, que subia lentamente aos céus.\nNo horizonte, os Cristais da Aurora voltavam a brilhar, espalhando luz por todo o reino.')
    passar()

def frasevitoria7(nome):
    limpar_tela()
    print(f'{nome} estava salvo.\nMas o herói jamais voltou a ser visto.')
    passar()

def frasevitoria8(nome):
    limpar_tela()
    print(f'Dizem que, nas noites claras, um raio dourado corta o céu sobre as Montanhas Negras — o espírito de {nome}, vigiando o reino que jurou proteger.')
    passar()

def frasevitoria9():
    limpar_tela()
    print('A lenda passou a ser contada como “O Amanhecer do Último Guardião.”')
    passar()


def frasederrota1(nome):
    limpar_tela()
    print(f'O golpe de Morfor atravessou o peito de {nome}, e a Luz da Alvorada caiu de sua mão, apagada.\nO salão mergulhou em trevas.')
    passar()

def frasederrota2(nome):
    limpar_tela()
    print(f'{nome} tentou se erguer, mas as sombras o envolveram. A voz de Morfor soou, fria e triunfante:\nMorfor: — “Você lutou contra o inevitável. Agora será parte dele.”')
    passar()

def frasederrota3():
    limpar_tela()
    print('A luz dos cristais distantes se apagou, um a um. Elarion chorava.')
    passar()

def frasederrota4(nome):
    limpar_tela()
    print(f'Morfor ergueu o guerreiro caído, e seu corpo começou a se distorcer, consumido por trevas.\nAos poucos, os olhos de {nome} brilharam com o mesmo vermelho profundo do inimigo.')
    passar()

def frasederrota5():
    limpar_tela()
    print('— “Não tema,” disse Morfor. “A luz ainda brilha — dentro da escuridão que você me ajudará a espalhar.”')
    passar()

def frasederrota6(nome):
    limpar_tela()
    print(f'Quando a lua se ergueu sobre a fortaleza, dois tronos aguardavam no salão.\nUm para Morfor.\nE o outro, ao lado, para {nome}, o Cavaleiro Sombrio — o novo senhor das trevas, guardião do caos.')
    passar()

def frasederrota7():
    limpar_tela()
    print('O nome do herói foi esquecido.\nSomente o medo permaneceu.')
    passar()

def frasederrota8():
    limpar_tela()
    print('Daquele dia em diante, o povo passou a chamar o tempo que se seguiu de “A Era das Sombras.”')
    passar()


def historia(nome):
    frase1()
    frase2(nome)
    frase3(nome)
    frase4()
    frase5()
    frase6()
    frase7()
    frase8(nome)
    frase9()
    frase10(nome)

def historiavit(nome):
    frasevitoria1(nome)
    frasevitoria2()
    frasevitoria3()
    frasevitoria4(nome)
    frasevitoria5()
    frasevitoria6(nome)
    frasevitoria7(nome)
    frasevitoria8(nome)
    frasevitoria9()

def historiader(nome):
    frasederrota1(nome)
    frasederrota2(nome)
    frasederrota3()
    frasederrota4(nome)
    frasederrota5()
    frasederrota6(nome)
    frasederrota7()
    frasederrota8()

def titulo_elarion():
    limpar_tela()
    titulo = "ELARION"
    subtitulo = "A LUZ E A SOMBRA"
    versao = "Versão 1.0"
    linha = "=" * 60
    print(linha)
    print(f"{titulo:^60}")
    print(f"{subtitulo:^60}")
    print(linha)
    print(f"{versao:^60}")
    print(linha)
    print()
    print("Bem-vindo ao Reino de Elarion.")
    print("As sombras despertam... e o destino o aguarda.")
    print()
    input("Pressione ENTER para iniciar sua jornada... ")

def final_elarion():
    limpar_tela()
    titulo = "ELARION"
    subtitulo = "O FIM DA JORNADA"
    linha = "=" * 60
    print(linha)
    print(f"{titulo:^60}")
    print(f"{subtitulo:^60}")
    print(linha)
    print()
    print("A luz da Aurora sempre renasce sobre o Reino de Elarion.")
    print("As trevas nunca recuam, mas o nome do herói ecoa na eternidade...")
    print()
    print("✨  ELARION  ✨")
    print()
    print(linha)
    print(f"{'Obrigado por jogar!':^60}")
    print(f"{'Desenvolvido por: Bruno Fellype':^60}")
    print(linha)
    print()
    input("Pressione ENTER para encerrar... ")
    limpar_tela()