#biblioteca///////////////////////////////////////
import random

#memoria///////////////////////////////////////
numero = 0
numeroMat1= float
numeroMat2= float
texto = str
enter =str
textoMat =str
k=0
b4 ='zero'
b5=0
ppt=0
#memoria matematica///////////////////////////////////////////////////////////////////////////////////////////////////
m1=0
m2=0
m3=0
m4=0
#união de numero/////////////////////////////////////////////////////////////////////////////////////////////////////
ma=[numero,m1,m2,m3,m4]
#volta de numero/////////////////////////////////////////////////////////////////////////////////////////////////////
numpt1 = float(input('recuperar do reste de ciclos de matemáticos > '))
numero =numpt1/2987
#volta de texto//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
textpt1 =str(input('recuperar do apagão de ciclos de texto > '))
a1=textpt1.replace('1','a')
a2=a1.replace('2','b')
texto=a2.replace('3','i')
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
print('\033[4;33;40m MODELOS OPERACIONAIS\ndepositar numero\ndepositar texto\nextrair numero\nextrair texto\nconta\nespandir')
for k in range(0,11):
    # ponto de pedido///////////////////
    print('\033[4;33;40mciclos({}/10)'.format(k))
    print('\033[4;32;40m====='*20)
    enter = str(input('> '))
    #parte de entradas////////////////////////
    #caide de numeros entrada/////////////////////////
    if enter=='depositar numero':
        numero=float(input('>>> '))
    #caixa de texto entrada ///////////////////////////
    if enter=='depositar texto':
        texto=str(input('>>> '))   
    #parte de saida//////////////////////////
    #caxa de numero saida/////////////////////////
    if enter=='extrair numero':
        print(numero)
    #caixa de texto saida///////////////////////
    if enter=='extrair texto':
        print(texto)
    #calculo//////////////////////////////////////////////
        #caculo de adição/////////////////////////////////
    if enter=='conta':
        print('CONTAS OPERACIONAIS\nadição\nsubitração\nmultiplicação\ndivição')
        print('(lenbrete)colóque o numero maior primeiro')   
        textoMat =str(input('digite o tipo de comta > '))
        if textoMat == 'adição':
            numeroMat1=float(input('>>'))
            numeroMat2=float(input('>>'))
            m1=numeroMat1+numeroMat2
            print('O resultado da conta é {}'.format(m1))
        #caculo de subitração/////////////////////////////
        if textoMat =='subitração':
            numeroMat1=float(input('>>'))
            numeroMat2=float(input('>>'))
            m2=numeroMat1-numeroMat2
            print('O resultado da conta é {}'.format(m2))
        #calculo de multiplicação    
        if textoMat== 'multiplicação':
            numeroMat1=float(input('>>'))
            numeroMat2=float(input('>>'))
            m3=numeroMat1*numeroMat2
            print('o resultado da conta é {}'.format(m3))
        #calculo de divição/////////////////////////////
        if textoMat=='divição':
            numeroMat1=float(input('>>'))
            numeroMat2=float(input('>>'))
            m4=numeroMat1/numeroMat2
            print('O resultado da conta é {}'.format(m4))
    #espandir/////////////////////////////////////////////////////////////////
    if enter =='espandir':
        print('O espandir é o lugar onde numeros ficam armazenados\n[1]adição\n[2]subitração\n[3]multiplicação\n[4]divição')
        enter=(input('>>'))
        if enter=='1':
            print('{}'.format(m1))
            enter=(input('precione para fechar'))
        elif enter=='2':
            print('{}'.format(m2))
            enter=(input('precione para fechar'))
        elif enter=='3':
            print('{}'.format(m3))
            enter=(input('precione para fechar'))
        elif enter=='4':
            print('{}'.format(m4))
            enter=(input('precione para fechar'))
    #pedra papel tesoura//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if enter=='jogo':
        print('Jogo de pedra papel tesoura')
        print('[1]pedra\n[2]papel\n[3]tesoura')
        enter=input('>>>')
        ppt=(int(random.random()*11))
        if enter==1 and ppt in range(0,3):
            print('você ganhou!!')
        elif enter==2 and ppt in range(4,7):
            print('você ganhou!!')
        elif enter==2 and ppt in range(8,10):
            print('você ganhou!!')
        else:
            print('você perdeu!!')
        if ppt in range(0,3):
            print('Eu escoli papel')
        elif ppt in range(4,7):
            print('Eu escoli tesoura')
        elif ppt in range(8,10):
            print('Eu escoli pedra')       




        k+1
#valvamento esterno de memoria/////////////////////////
b2=texto.replace('a','1')
b3 =b2.replace('b','2')
b4=b3.replace('i','3')
print('arquivo de texto {}'.format(b4))
b5=numero*2987
print('arquivo de matematico {}'.format(b5))

enter=(input('precione para fechar'))
