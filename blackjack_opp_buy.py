from random import choice,randint
from time import sleep
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


karty = {'K':10,
         'Q':10,
         'W':10,
         'A':11,
         '2':2,
         '3':3,
         '4':4,
         '5':5,
         '6':6,
         '7':7,
         '8':8,
         '9':9,
         '10':10}

wynik_gracza = 0
wynik_krupiera = 0

kto_wygral = ''

gracz = []
krupier = []

budget = 100

d_widelka_jackpot = 2500
g_widelka_jackpot = 7500

d_widelka_default = 0
g_widelka_default = 2000

koszt_wykupienia_przeciwnika = 1000

def loso_gracz():
    gracz.append(choice(list(karty.keys())))

    
def loso_krupier():
    krupier.append(choice(list(karty.keys())))
    

def show_gracza():
    global wynik_gracza
    wynik_gracza = 0
    for i in gracz:
        wynik_gracza += karty.get(i)

    for i in gracz:
        if i == 'A' and wynik_gracza > 21:
            wynik_gracza -= 10

    sleep(1)          
    print(f'Karty gracza: {gracz} = {wynik_gracza}')
    

def show_krupiera():
    global wynik_krupiera
    wynik_krupiera = 0

    for i in krupier:
        wynik_krupiera += karty.get(i)
    
    for i in krupier:
        if i == 'A' and wynik_krupiera > 21:
            wynik_krupiera -= 10
    sleep(1)
    print(f'Karty krupiera: {krupier} = {wynik_krupiera}')
    

def blackjack():

    def again():
        global gracz,krupier,wynik_gracza,wynik_krupiera

        print()
        for i in range(3,-1,-1):
            sleep(1)
            print(f'Następna gra za: {i}') 
        gracz = []
        krupier = []
        wynik_gracza = 0
        wynik_krupiera = 0
        blackjack()

    global budget, kto_wygral, koszt_wykupienia_przeciwnika, d_widelka_jackpot, g_widelka_jackpot, g_widelka_default

    sleep(0.4)
    print('\nGra: Blackjack!\n')

    
    loso_gracz()
    show_gracza()

    loso_krupier()
    show_krupiera()

    loso_gracz()
    show_gracza()
    
             
    print('\n🕗 Chwila na postawienie betów!🕗')
    sleep(0.7)

    wybory = ['Gracz','Krupier','Remis','Pass']
   
    bet = input('🤔 Postaw na kogo uważasz że wygra (Krupier(x1.9) / Gracz(x2.3) / Remis(x10) / Pass)🤔: ')

    if bet.capitalize() not in wybory:
        pass
        print()

    elif bet.capitalize() == 'Pass':
        pass
        print()

    else:
        sleep(0.25)
        while True:
            kesz = float(input(f'💸 Ile chcesz obstawić? Masz:{budget}$💸: '))
            print()
            
            if kesz <= budget:
                break

            else:
                sleep(0.3)
                print('😞 Nie masz tyle kasy mordo.😞')


    while wynik_gracza < 17:
        loso_gracz()
        show_gracza()

        if wynik_gracza > 21:
            sleep(1)
            print()
            print('Bust!')
            print()
            show_gracza()
            show_krupiera()
            print('😞 Gracz przegrał.😞  🤑 Wygrana krupiera!🤑')
            kto_wygral = 'Krupier'
            sleep(1)
            break


    while wynik_krupiera < 17:

        if wynik_gracza == 21 and len(gracz) == 2 and wynik_krupiera < 10:
            break

        elif wynik_gracza > 21:
            break

        loso_krupier()
        show_krupiera()

        if wynik_gracza == 21 and len(gracz) == 2:
                break
        
        elif wynik_krupiera > 21:
            sleep(1)
            print()
            print('Bust!')
            print()
            show_gracza()
            show_krupiera()
            print('😞 Krupier przegrał.😞  🤑 Wygrana gracza!🤑')
            kto_wygral = 'Gracz'
            sleep(1)
            break

    if wynik_gracza > 21:
        pass
    
    elif wynik_krupiera > 21:
        pass
    
    elif wynik_gracza == 21 and wynik_krupiera == 21 and len(gracz) == 2 and len(krupier) == 2:
        print()
        show_gracza()
        show_krupiera()
        print("⚖️  Remis poprzez blackjack'a!⚖️")
        sleep(1)
        kto_wygral = 'Remis'

    elif wynik_gracza == 21 and len(gracz) == 2:
        print()
        show_gracza()
        show_krupiera()
        print("🤑 Wygrana gracza poprzez blackjack'a!🤑")
        sleep(1)
        kto_wygral = 'Gracz'

    elif wynik_krupiera == 21 and len(krupier) == 2:
        print()
        show_gracza()
        show_krupiera()
        print("🤑 Wygrana krupiera poprzez blackjack'a!🤑")
        sleep(1)
        kto_wygral = 'Krupier'

    elif wynik_krupiera == wynik_gracza:
        print()
        show_gracza()
        show_krupiera()
        print('⚖️  Remis!⚖️')
        sleep(1)
        kto_wygral = 'Remis'
    
    elif wynik_gracza > wynik_krupiera:
        print()
        show_gracza()
        show_krupiera()
        print('😞 Krupier przegrał.😞  🤑 Wygrana gracza!🤑')
        sleep(1)
        kto_wygral = 'Gracz'
        
    elif wynik_krupiera > wynik_gracza:
        print()
        show_gracza()
        show_krupiera()
        print('😞 Gracz przegrał.😞  🤑 Wygrana krupiera!🤑')
        sleep(1)
        kto_wygral = 'Krupier'


    if bet.capitalize() == 'Gracz' and kto_wygral == 'Gracz':
        budget = round((budget - float(kesz)) + float(kesz)*2.3)

    elif bet.capitalize() == 'Krupier' and kto_wygral == 'Krupier':
        budget = round((budget - float(kesz)) + float(kesz)*1.9)
        
    elif bet.capitalize() == 'Remis' and kto_wygral == 'Remis':
        budget = round((budget - float(kesz)) + float(kesz)*10)

    elif bet.capitalize() == 'Pass':
        pass

    elif bet.capitalize() not in wybory:
        pass
    
    else:
        budget -= float(kesz)

    print(f'\n💸 Hajs po tej grze:{int(budget)}$💸')
    sleep(1)
    
 
    if budget >= koszt_wykupienia_przeciwnika:
        
        wykupienie = input('\nMożesz wykupić przeciwnika, odbierze to jego pozostałe pieniądze (Y/N): ').title()
        print()

        if wykupienie == 'Y':

            budget -= koszt_wykupienia_przeciwnika

            szansa = randint(1,10)

            if szansa == 7:
                hajs_wykupionego_jackpot = randint(d_widelka_jackpot, g_widelka_jackpot)
                budget += hajs_wykupionego_jackpot
                print(f'Pieniądze które zostały przeciwnikowi:{hajs_wykupionego_jackpot}$')
                
            else:
                hajs_wykupionego = randint(d_widelka_default, g_widelka_default)
                budget += hajs_wykupionego
                print(f'Pieniądze które zostały przeciwnikowi:{hajs_wykupionego}$')
                
            sleep(0.6)
            print(f'\n💸 Hajs po wykupieniu przeciwnika {int(budget)}$💸')

            koszt_wykupienia_przeciwnika *= 2
            
            g_widelka_default *= 2

            d_widelka_jackpot *= 2
            g_widelka_jackpot *= 2

        else:
            pass
    

    if budget <= 0:
        print('👋 Witamy w nałogu.👋')
        exit()


    sleep(1)

    print(f'\nKoszt wykupienia przeciwnika:{koszt_wykupienia_przeciwnika}$')
    sleep(1)


    def czy_pre_end():
        if budget < 10:
            koniec = input('Chcesz skończyć grę?(Y/N): ')
            if koniec.capitalize() == 'Y':
                print(f'💸 Skończyłeś grę z {budget}$ na koncie!💸')
                exit()

            elif koniec.capitalize() == 'N':
                pass

            else:
                czy_pre_end()
    czy_pre_end()
    
    again()

blackjack()