from frases import *
from personagem import Personagem
from vilao import Vilao
from heroi import Herói
from curandeiro import Curandeiro
from sabio import Sabio
import random
import time

def main():
    titulo_elarion()
    limpar_tela()
    print('Vamos criar o seu personagem!\n')
    nome=input('Digite um nome para o seu personagem: ')
    nome = nome.capitalize()
    while True:
        try:
            idade=int(input('Qual a idade do seu personagem?'))
            break
        except ValueError:
            print('Erro! Digite um número!')
    input('\nTecle ENTER para sortearmos a sua quantidade de vida\n')
    vida= random.randint(100, 201)
    time.sleep(2)
    print(f'A sua vida será:{vida}')
    if vida < 150:
        print('Sua sorte não foi das melhores, mas sempre se pode melhorar!\n')
    elif vida > 180:
        print('WOW! Que sorte, mas se lembre "Com grandes poderes vem grandes responsabilidades!".\n')
    else:
        print('Uma boa quantidade de vida para ser um exímio guerreiro\n')
    passar()
    while True:
        limpar_tela()
        print('Classes:\n\n[1] Herói\n[2] Curandeiro\n[3] Sábio\n[4] Mais informações sobre cada classe\n')
        classe = input('Digite a qual classe seu personagem pertencerá: ')
        if classe == '1':
            heroi = Herói(nome, idade, vida)
            break
        elif classe == '2':
            curandeiro = Curandeiro(nome, idade, vida)
            break
        elif classe == '3':
            sabio = Sabio(nome, idade, vida)
            break
        elif classe == '4':
            limpar_tela()
            print('Classe Herói: Voltado mais para o ataque, um herói possui uma força e habilidade manual sem igual, consegue domar a Luz da Alvorada - a espada mais afiada dos 7 reinos - como ninguém, possuindo um ataque especial chamado "Luz da Alvorada" (Quem diria?), que afeta Morfor de maneira mais letal podendo causar 25 pontos de dano (não podendo ser usado em rodadas consecutivas).\n\nClasse Curandeiro: Voltado mais para os atributos de cura, um curandeiro possui facilidade com poções e plantas medicinais, muito úteis em meio a uma batalha. Possui uma habilidade especial chamada "Super-cura", onde(de maneira aleatória) pode conceder até 40 pontos de cura à sua própria vida(não podendo ser usado em rodadas consecutivas).\n\nClasse Sábio: Classe mais equilibrada, um sábio dominou todos os livros disponíveis em Elarion, e a partir deles desenvolveu uma técnica especial, chamada "Regen", que pode garantir uma recuperação simples de pontos de vida e um ataque simples a Morfor, mesmo não causando tanto dano quanto um Herói, nem trazendo cura como um Curandeiro, sua habilidade pode ser bem útil, até porque ela não se limita.\n\n')
        else:
            print('Opção inválida, tente novamente')

        
    # Criando personagens e vilões
    vilao = Vilao('Morfor', 2000000, 300, 'Alta')

    historia(nome)
    limpar_tela()
    while vilao.vida > 0:
        if classe == '1':
            if heroi.vida > 0:
                print('[1] Atacar\n[2] Curar\n[3] Luz da Alvorada')
                escolha = input('\nQual será sua próxima ação?')
                limpar_tela()
                while True:
                    if heroi.vida == 0:
                        break
                    if vilao.vida == 0:
                        break
                    if escolha == '1':
                        heroi.ataque(vilao)
                        vilao.ataque(heroi)
                        print('[1] Atacar\n[2] Curar\n[3] Luz da Alvorada')
                        escolha = input('\nQual será sua próxima ação?')
                        limpar_tela()
                    elif escolha == '2':
                        heroi.upgrade_vida()
                        vilao.ataque(heroi)
                        print('[1] Atacar\n[2] Curar\n[3] Luz da Alvorada')
                        escolha = input('\nQual será sua próxima ação?')
                        limpar_tela()
                    elif escolha == '3':
                        heroi.luz_alvorada(vilao)
                        vilao.ataque(heroi)
                        while True :
                            if heroi.vida == 0:
                                break
                            if vilao.vida == 0:
                                break
                            print('[1] Atacar\n[2] Curar\n[3] Luz da Alvorada (Indisponível)')
                            escolha = input('\nQual será sua próxima ação?')
                            limpar_tela()
                            if escolha == '3':
                                print ('Opção inválida nesse round, tente novamente')
                            elif escolha == '2':
                                break
                            elif escolha =='1':
                                break
                            else:
                                print ('Opção inválida, tente novamente')
                    else:
                        print('Opção inválida, tente novamente')
                        break
            elif heroi.vida == 0:
                historiader(nome)
                break
        elif classe == '2':
            if curandeiro.vida != 0:
                print('[1] Atacar\n[2] Curar\n[3] Super-Cura')
                escolha = input('\nQual será sua próxima ação?')
                limpar_tela()
                while True:
                    if curandeiro.vida == 0:
                        break
                    if vilao.vida == 0:
                        break
                    if escolha == '1':
                        curandeiro.ataque(vilao)
                        vilao.ataque(curandeiro)
                        print('[1] Atacar\n[2] Curar\n[3] Super-Cura')
                        escolha = input('\nQual será sua próxima ação?')
                        limpar_tela()
                    elif escolha == '2':
                        curandeiro.upgrade_vida()
                        vilao.ataque(curandeiro)
                        print('[1] Atacar\n[2] Curar\n[3] Super-Cura')
                        escolha = input('\nQual será sua próxima ação?')
                        limpar_tela()
                    elif escolha == '3':
                        curandeiro.supercura()
                        vilao.ataque(curandeiro)
                        while True :
                            if curandeiro.vida == 0:
                                break
                            if vilao.vida == 0:
                                break
                            print('[1] Atacar\n[2] Curar\n[3] Super-Cura (Indisponível)')
                            escolha = input('\nQual será sua próxima ação?')
                            limpar_tela()
                            if escolha == '3':
                                print ('Opção inválida nesse round, tente novamente')
                            elif escolha == '2':
                                break
                            elif escolha =='1':
                                break
                            else:
                                print ('Opção inválida, tente novamente')
                    else:
                        print('Opção inválida, tente novamente')
                        break
            elif curandeiro.vida == 0:
                historiader(nome)
                break
        elif classe == '3':
            if sabio.vida != 0:
                while True:
                    if sabio.vida == 0:
                        break
                    if vilao.vida == 0:
                        break
                    print('[1] Atacar\n[2] Curar\n[3] Regen')
                    escolha = input('\nQual será sua próxima ação?')
                    limpar_tela()
                    if escolha == '1':
                        sabio.ataque(vilao)
                        vilao.ataque(sabio)
                    elif escolha == '2':
                        sabio.upgrade_vida()
                        vilao.ataque(sabio)
                    elif escolha == '3':
                        sabio.regen(vilao)
                        vilao.ataque(sabio)
                    else:
                        print('Opção inválida, tente novamente')
            elif sabio.vida == 0:
                historiader(nome)
                break
    else:
        historiavit(nome)
    
    final_elarion()

if __name__ == "__main__":
    main()
