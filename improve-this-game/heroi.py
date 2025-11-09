from personagem import Personagem

class Herói(Personagem):

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

    def luz_alvorada(self, personagem):
        
        if personagem.vida > 25:
            personagem.vida -= 25
        else:
            personagem.vida = 0
        print(f'Vida de {personagem.nome} após downgrade: {personagem.vida}')