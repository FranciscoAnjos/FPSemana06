import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def especial(self, *args):
        pass

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    def especial(self, enemy):
        total_dmg = self.ataque + 15
        enemy.vida -= total_dmg
        print(f"{self.nome} usa Golpe Poderoso em {enemy.nome} e Causa {total_dmg} de Dano!")

class Mago(Personagem):
    def especial(self):
        self.vida += 25
        print(f"{self.nome} usa Cura e Ganha 25 Pontos de Vida!")

class Arqueiro(Personagem):
    def especial(self, enemies):
        for en in enemies:
            if en != self:
                en.vida -= 15
        print(f"{self.nome} usa Chuva de Flechas e Causa 15 de Dano a Todos os Inimigos!")

def importar_personagens(caminho):
    """
        Função que importa personagens a partir de um ficheiro JSON.
        O ficheiro contém uma lista de personagens com informações de nome, vida, ataque e classe.
        - caminho: Caminho para o ficheiro JSON que contém os dados dos personagens.
        Retorna:
        - lista de personagens.
        - quantidade total de personagens importados.
    """
    personagens = []

    try:
        with open(caminho, 'r') as f:
            dados = json.load(f)

            for personagem in dados:
                classe = personagem['classe']
                nome = personagem['nome']
                vida = personagem['vida']
                ataque = personagem['ataque']

                if classe == "Guerreiro":
                    personagens.append(Guerreiro(nome, vida, ataque))
                elif classe == "Mago":
                    personagens.append(Mago(nome, vida, ataque))
                elif classe == "Arqueiro":
                    personagens.append(Arqueiro(nome, vida, ataque))

        return personagens, len(personagens)
    except:
        print("Erro ao ler personagens.json")
        return


def ordenar_personagens_por_vida(personagens):
    """
        Função que ordena a lista de personagens de acordo com os pontos de vida (do menor para o maior).
        - personagens: Lista de personagens.
        Retorna:
        - lista de personagens ordenada por vida.
    """
    return sorted(personagens, key=lambda p: p.vida)


personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])
