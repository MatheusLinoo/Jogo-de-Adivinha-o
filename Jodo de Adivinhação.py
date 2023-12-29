import random

def jogo_de_adivinhacao():
    while True:
        print("Bem-vindo ao Jogo de Adivinhação!")
        print("Eu escolhi um número aleatório entre 1 e 100. Tente adivinhar!")

        numero_secreto = random.randint(1, 100)
        tentativas_maximas = 10
        tentativas_realizadas = 0

        while tentativas_realizadas < tentativas_maximas:
            palpite = int(input("Digite o seu palpite: "))

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas_realizadas + 1} tentativas.")
                break
            elif palpite < numero_secreto:
                print("Tente um número mais alto.")
            else:
                print("Tente um número mais baixo.")

            tentativas_realizadas += 1

        if tentativas_realizadas == tentativas_maximas:
            print(f"Fim do jogo! Você não conseguiu adivinhar o número. O número correto era {numero_secreto}.")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar. Até a próxima!")
            break

if __name__ == "__main__":
    jogo_de_adivinhacao()
