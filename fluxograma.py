from projeto_prova import telaInicial
#Elton e Wagner, eu tentei transformar o fluxograma em condicional, só pra irmos organizando as ideias de quais classes e funções vamos usar
#deem feedback hehe
#aqui é o inicio do jogo

telaInicial()
print('''
Você é um jovem programador e o seu superior te deu a oportunidade que você estava esperando!
Você precisa entregar um projeto SUPER importante e tem apenas 24:00 horas para isso!
Entregue o projeto e conquiste sua promoção!
''')
print('-='*30)
# aqui vamos apresentar as opções ( troquei as funções por prints para melhorar a lógica enquanto desenvolvemos essas funções)
while True:
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Fazer café da manhã")
        print("3 - Pedir café da manhã")
        print("4 - Tomar café da manhã")
        print("5 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")
        if opcao == "1":
            print('Você tomou banho!') #Esta consome tempo
        elif opcao == "2":
            print('Fez café da manhã!')#Esta consome tempo e gasta 1 energia
        elif opcao == "3":
            print('Pediu café da manha')#Esta consome tempo
        elif opcao == "4":
            print('Tomou café')#esta consome tempo e dá +2 de energia
        elif opcao == "5":
            print('''
            Você vai trabalhar de:
            1 - Carro
            2 - Ônibus
            3 - Uber
            ''')
            opcao2 = input('Escolha seu transporte:')
            if opcao2 == '1':
                print('Carro') #aqui podemos inserir um random com falha/normal/sorte
            elif opcao2 == '2':
                print('Ônibus') #aqui podemos inserir um random com falha/normal/sorte
            elif opcao2 == '3':
                print('Uber') #aqui podemos inserir um random com falha/normal/sorte
            else:
                print('Erro')
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
