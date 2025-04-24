import random


class Palavra:
    def __init__(self, lista_palavras):
        self.secreta = random.choice(lista_palavras).lower() #Seleciona aleatoriamente uma das palavras e deixa em minusculo
        self.letras_descobertas = ["_" for _ in self.secreta] #Troca as letras nao encontradas por um traço

    def mostrar_progresso(self):
        return " ".join(self.letras_descobertas) #Junta os elementos da lista 

    def tentar_letra(self, letra):
        acerto = False #Setado inicialmente no Falso
        for i, l in enumerate(self.secreta):
            if l == letra: #Se encontrar letra correspondente, troca o traço, pela letra
                self.letras_descobertas[i] = letra
                acerto = True
        return acerto

    def foi_completada(self):
        return "_" not in self.letras_descobertas


class JogoDaForca:
    def __init__(self):
        self.tentativas_restantes = 6
        self.letras_usadas = set() #Cria um conjunto para nao permitir duplicação
        lista_de_palavras = ["paralelepipedo", "python", "computador", "github", "internet", "orientacao", "objeto"]
        self.palavra = Palavra(lista_de_palavras)

    def jogar(self):
        print("🎮 Bem-vindo ao Jogo da Forca!")
        while self.tentativas_restantes > 0: #Roda enquanto houver tentativas
            print("\nPalavra: ", self.palavra.mostrar_progresso())
            print("Letras usadas:", " ".join(self.letras_usadas))
            print(f"Tentativas restantes: {self.tentativas_restantes}")
            letra = input("Digite uma letra: ").lower()

            if not letra.isalpha() or len(letra) != 1: #Erros de digitação (mais de uma letra, letra maiuscula)
                print("Digite apenas uma letra.")
                continue

            if letra in self.letras_usadas:
                print("Você já tentou essa letra!")
                continue

            self.letras_usadas.add(letra)

            if self.palavra.tentar_letra(letra):
                print("Você acertou uma letra.")
                if self.palavra.foi_completada():
                    print("\nVocê venceu!")
                    print("A palavra era:", self.palavra.secreta)
                    break
            else:
                self.tentativas_restantes -= 1
                print("Letra incorreta.")

        else:
            print("\n💀 Fim de jogo!")
            print("A palavra era:", self.palavra.secreta)


# Roda o jogo
jogo = JogoDaForca()
jogo.jogar()
