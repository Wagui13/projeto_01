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

def stackoverflow():
    print('Você pesquisou no stack overflow')

def codar():
    print('Você está codando!')
