### estudo caixa de seleção para definir qual a fórmula a ser executada FALTA INCLUIR AS FORMULAS#
##FAZER TEMPERATURA DE EQUILIBRIO

choice = 0
opçãodil = 0
eqter = 0
opçãovelo = 0
while choice != 5:
    while 0 <= choice <4 :
        while 0 <= opçãodil <= 5 :
            while 0 <= eqter <= 5 :
                  while 0 <= opçãovelo <= 5 :
        
##           
                    choice = int(input('''    Selecione a Fórmula que deseja:
                        [ 1 ] Cálculo de dilatação linear
                        [ 2 ] Cálculo de velocidade
                        [ 3 ] Cálculo de Equilíbrio Térmico
                        [ 4 ] Créditos do Sistema
                        [ 5 ] Sair do programa: ''' ))
                    print(choice)

                
                    if choice == 1:
                        opçãodil = int(input('''    Selecione o que quer descobrir:
                        NENHUM VALOR PODE SER = 0.0
                        [ 1 ] Descobrir a dilatação, possuindo-a em diferente escala.
                        [ 2 ] Descobrir o Delta L, diferença de tamanho.
                        [ 3 ] Descobrir o coeficiente de dil.
                        [ 4 ] Descobrir o L inicial
                        [ 5 ] Descobrir o Delta Temp: '''))
                        print(opçãodil)
                        
        #1 CHECK
                    if opçãodil == 1:
                        ti = float(input("Insira o tamanho inicial: "))
                        di = float(input("Insira a dilatação inicial(em mm): "))
                        tf = float(input("Insira o tamanho final: "))
                        dila1 = (di * tf) / ti
                        print ("a dilatação final é = %.1f mm" %dila1)
                        break

        #2 CHECK
                    elif opçãodil == 2:
                        Lo = float(input("Insira a L inicial (em cm): "))
                        C = float(input("Insira o Coeficiente de dilatação: "))
                        DT = float(input("Insira a Delta de Temperatura: "))
                        DeltaL = C * Lo * DT
                        print("O Delta L é = %.1f cm" %DeltaL)
                        break


        #3 CHECK
                    elif opçãodil == 3:
                        DL = float(input("Insira a Delta L (em cm): "))
                        Lo = float(input("Insira a L inicial(em cm): "))
                        DT = float(input("Insira a Delta Temperatura (em °C): "))
                        alfa = DL / (Lo * DT)
                        print ("o coeficiente de dilatação é = %.1f mm" %alfa)
                        break
        # CHECK
                    elif opçãodil == 4:
                        DL = float(input("Insira o Delta L (em cm): "))
                        C = float(input("Insira o Coef. de dilatação: "))
                        DT = float(input("Insira o Delta Temperatura(em °C): "))
                        LINI = DL / (C * DT)
                        print ("O tamanho inicial foi = %.1f cm"%LINI)
                        break
        # Check
                    elif opçãodil == 5:
                        Lo = float(input("Insira a L inicial(em cm): "))
                        DL = float(input("Insira a Delta L(em cm): "))
                        C = float(input("Insira o Coef. de Dilatação: "))
                        VARTEMP = DL / (C * Lo)
                        print ("A variação de temperatura %.1f °C" %VARTEMP)
                        exit()
        #VELOCIDADE CHOICE2

                    elif choice == 2:
                        print("Bem vinde! Insira as medidas utilizando metros e segundos respectivamente:")
                        print("Calculadora de Velocidade Média")

                        opçãovelo = int(input('''    Selecione a Fórmula que deseja:
                        [ 1 ] Descobrir espaço percorrido
                        [ 2 ] Descobrir espaço Inicial
                        [ 3 ] Descobrir Velocidade Média
                        [ 4 ] Descobrir tempo percorrido
                        [ 5 ] Sair do programa: ''' ))
                        print(opçãovelo)
              #Velo EM ANDAMENTO
                    
                    if opçãovelo == 1:
                        SI = float(input("Insira o Espaço Inicial(em m): "))
                        T = float(input("Insira o tempo(em s): "))
                        Vms = float(input("Insira a Velocidade em m/s: "))
                        SG = SI + (Vms*T)
                        print("O Espaço Total equivale à %.1f m " %SG)
                   
        #espaço
                    if opçãovelo == 2:
                        SG = float(input("Insira o Espaço percorrido(em m): "))
                        T = float(input("Insira o tempo(em s): "))
                        Vms = float(input("Insira a Velocidade Média em m/s: "))
                        SI = SG - (Vms*T)
                        print("O Espaço Inicial equivale à %.1f metro(s) " %SI)
                   
                    if opçãovelo == 3:
                        S0 = float(input("Insira o Espaço Inicial em m : "))
                        SF = float(input("Insira o Espaço Final: "))
                        DeltaS = S0 - SF
                        t0 = float(input("Insira o Tempo Inicial: em segundos"))
                        tF = float(input("Insira o Tempo Final: em segundos"))
                        Deltat = t0 - tF
                        Vm = DeltaS / Deltat
                        if Vm < 0:
                            print("O objeto está no sentido contrário a %.1f m/s" %Vm)
                        if Vm == 0:
                            print("O objeto está parado.")
                            
                        print ("A velocidade Média, é %.1f metro(s) por segundo(s)" %Vm)
                      
                    if opçãovelo == 4:
                        DS = float(input("Insira o Espaço percorrido(em m): "))
                        Vms = float(input("Insira a Velocidade em m/s: "))
                        DT = (DS/ Vms)
                        print ("O tempo gasto para percorrer o trajeto foi de %.1f segundo(s)" %DT)
                        
                    elif opçãovelo == 5:
                        exit()

                        
###EQUILIBRIO TERMICO - INCOMPLETO                    

                    if choice == 3:
                      print("ESTA SEÇÃO ESTÁ INCOMPLETA!")
                      print("Você escolheu Equilíbrio Térmico!!")
                      eqter = int(input(('''Selecione a Fórmula que deseja:
                      [ 1 ] Descobrir o Q(qntd. de calor) dos elementos
                      [ 2 ] Já tenho dois Q's
                      [ 3 ] Preciso somar mais de dois materiais.
                      [ 4 ] Fechar Programa.
                       ''')))
                      print (eqter)
                      if  eqter == 1:
                                print("Escreva somente os valores do primeiro  elemento: ")
                                C1= float(input("Insira o calor específico em cal: "))
                                M1= float(input("Insira a massa em gramas: "))
                                DT1= float(input("Insira o Delta Temperatura em °C: "))
                                Q1 = (M1 * C1 * DT1)
                                print("O Q do primeiro é igual a %.1f" %Q1)
                                print("Insira somente os dados do 2o elemento, agora: ")
                                C2= float(input("Insira o calor específico em cal: "))
                                M2= float(input("Insira a massa em gramas: "))
                                DT2= float(input("Insira o Delta Temperatura em °C: "))
                                Q2 = (M2 * C2 * DT2)
                                print("O Q do segundo é igual a %.1f" %Q2)
                               #    equilibrio = float(Q1 + Q2 = 0)
                                print ("O Equilíbrio Térmico ocorrerá em %.1f °C" %equilibrio)
                                break
                                    
                                    
                                if eqter == 2:
                                    eleum = float(input("Qual é o Q em cal do primeiro elemento: "))
                                    eledois = float(input("Qual é o Q em cal do segundo elemento: "))
                                   # equi = eleum + eledois = 0

                                elif eqter == 3:
                                    eleum = float(input("Qual é o Q em cal do primeiro elemento: "))
                                    eledois = float(input("Qual é o Q em cal do segundo elemento: "))
                                    ele3 = float(input("Qual é o Q em cal do terceiro elemento: "))
                                elif choice == 5:
                                    exit()

                    elif choice == 4 :
                        print(" Código elaborado durante a aula Espiadela na Caixa Preta")
                        print(" Profª Renata")
                        print(" Construído por Antonio Haddad e Fernando Murachco, 2022.")
                    elif choice == 5:
                        exit()

                           #     equi = eleum + eledois + ele3 = 0
                            

                 #   opcão = int(input('Qual fórmula você deseja calcular? '))

            #if opção == 1 (True):
             #   print("iu")
            #else:
            #    print("aaa")
                    #    elif opção == "2":
                            
                    #    elif opção == 3:

                    #    elif opção == 4:

                #    elif opção == 5:
         # print("Fim do Programa")




