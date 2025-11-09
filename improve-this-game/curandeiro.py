from personagem import Personagem
import random

class Curandeiro(Personagem):

    def __init__(self, nome, idade, vida):
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def ataque(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo curandeiro.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()
    
    def supercura(self):
        """
        Aumenta a vida do personagem de maneira maior. O valor de incremento pode variar de 20 a 30.
        """
        incremento = random.randint(30,41)
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')