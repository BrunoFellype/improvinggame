from personagem import Personagem
import random

class Sabio(Personagem):

    def __init__(self, nome, idade, vida):
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def ataque(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()
    
    def regen(self, personagem):
        """
        Aumenta a vida do personagem e ataca ao mesmo tempo.
        """
        incremento = random.randint(1,6)
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')
        personagem.downgrade_vida()
