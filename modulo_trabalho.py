import random
def falarcomchefe():
    pericia = 0
    chefe = random.randint(1, 6)
    if chefe == 1:
        print('-='*10,'MENSAGEM','-='*10,'\nO chefe parece não estar de bom humor, melhor voltar mais tarde!')
    elif chefe > 2 and chefe < 5:
        print('-='*10,'MENSAGEM','-='*10,'\nO chefe deu poucas informações sobre o projeto, mas ajudou um pouco')
        pericia = 1
    else:
        print('-='*10,'MENSAGEM','-='*10,'\nO chefe estava animado! As informações vao ajudar você!')
        pericia = 3
    return pericia

def senhadopc():
    senha = 'python'
    pin = 0
    trava_senha = 0
    while pin != senha and trava_senha < 3:
        pin = input('Digite sua senha: ').lower()
        if pin != senha:
            print('Senha incorreta! Tente novamente!')
            trava_senha += 1
            if trava_senha == 3:
                print ('ACHO QUE ALGUÉM MUDOU SUA SENHA!')
        else:
            print('Senha Correta! Seja bem vindo!')
            return True


def ajudarestagiario():
    print('\nEu acabei trocando a senha de todos os computadores!\nColoquei o nome de uma Linguagem de programação e não consigo me lembrar')
    ajudar=input('Ajudar a lembrar da senha? S/N: ').upper()
    if ajudar == 'S':
        senha = 'python'
        acertos = 0
        letras_descobertas = ''

        while len(letras_descobertas) != len(senha):
            mensagem = ''
            for letra in senha:
                if letra in letras_descobertas:
                    mensagem += letra + ' '
                else:
                    mensagem += '_'
            print(mensagem)
            
            letra = input('Chute uma letra').lower()

            if letra in senha:
                print('É, acho que tem essa letra!')
                letras_descobertas += letra
                acertos += 1
            else:
                print('Hm... acho que não...')
    else:
        print ('Que feio! você já foi estagiário um dia!')




def cafeteria():
    m = random.randint(1, 6)
    if m == 1:
        print('Café pra codar!')
        return -5
    elif m == 2:
        print('Esse café ta meio estranho...')
        return -1
    elif m ==3:
        print('...')
        return -3
    elif m ==4:
        print('Estava precisando...')
        return -6
    elif m ==5:
        print('Quero Caféeeee')
        return -10
    elif m ==6:
        print('Um café quentinho pra acordar!')
        return -3

def codar():
    print('Você está codando!')
    return 5