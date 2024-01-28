try:
    from pystyle import *
    import time
    import random
    import os
    from colorama import Fore

    def clear_console():
        osystem = os.sys.platform
        if osystem == 'linux':
            os.system('clear')
        else:
            os.system('cls')
    vidasp1 = 10
    vidasp2 = 10

    banner = '''
 (             (
 )\ )          )\ )                (              )      )
(()/(   (     (()/(           (    )\     (    ( /(   ( /(     (
 /(_))  )\ )   /(_))   (     ))\  ((_)   ))\   )\())  )\())   ))\ 
(_))   (()/(  (_))     )\   /((_)  _    /((_) (_))/  (_))/   /((_)
| _ \   )(_)) | _ \   ((_) (_))(  | |  (_))   | |_   | |_   (_))
|  _/  | || | |   /  / _ \ | || | | |  / -_)  |  _|  |  _|  / -_)
|_|     \_, | |_|_\  \___/  \_,_| |_|  \___|   \__|   \__|  \___|
        |__/
    '''
    clear_console()
    print(Colorate.Horizontal(Colors.red_to_blue, banner))
    cilindre = int(input(Colorate.Horizontal(Colors.green_to_blue, 'Cantidad de cilindros ==> ')))
    bullets = int(input(Colorate.Horizontal(Colors.green_to_blue, 'Cantidad de balas ==> ')))

    clear_console()
    print(Colorate.Horizontal(Colors.red_to_blue, banner))
    print(Colorate.Horizontal(Colors.red_to_blue, '[1] Jugar con bot\n[2] 2 Jugadores'))
    option_1 = int(input(Colorate.Horizontal(Colors.green_to_yellow, '==>')))
    if option_1 == 1:
        bot = '74lg0'
        player = input(Colorate.Horizontal(Colors.green_to_blue, 'Nombre del jugador ==> '))
        if player == bot:
            bot = 'HACK_BOT'
        clear_console()
        print(Colorate.Horizontal(Colors.red_to_blue, banner))
        print(Fore.GREEN+'Cargando', end='')
        txt = '......'
        for letras in txt:
            print(letras, end='')
            time.sleep(0.5)
            os.sys.stdout.flush()
        
        
        while True:
            clear_console()
            print(Colorate.Horizontal(Colors.red_to_blue, banner))
            kill = random.randint(bullets, cilindre)
            time.sleep(1)
            print(Colorate.Horizontal(Colors.red_to_blue, f'{bot} a apretado el gatillo'))
            time.sleep(2)
            if kill == cilindre:
                vidasp1 = vidasp1 - 1
                print(Colorate.Horizontal(Colors.red_to_blue, f'Vidas de {bot} => {vidasp1}'))
            else:
                print(Colorate.Horizontal(Colors.red_to_blue, f'{bot} => Cámara vacía. Sigues vivo'))
            
            #Jugador
            kill = random.randint(bullets, cilindre)
            p2 = input(Colorate.Horizontal(Colors.green_to_yellow, (f'{player} presiona enter para jalar el gatillo ')))
            time.sleep(4)
            if kill == cilindre:
                vidasp2 = vidasp2 - 1
                print(Colorate.Horizontal(Colors.green_to_yellow, f'Vidas de {player} => {vidasp2}'))
            else:
                print(Colorate.Horizontal(Colors.green_to_yellow, f'{player} => Cámara vacía. Sigues vivo'))
            
            time.sleep(4)

# Verificacion de vidas
            if vidasp1 == 0:
                clear_console()
                print(Colorate.Horizontal(Colors.red_to_blue, banner))
                print(Colorate.Horizontal(Colors.green_to_yellow, f'\n{player} => Haz ganado'))
                os.sys.exit()
            else:
                pass

            if vidasp2 == 0:
                clear_console()
                print(Colorate.Horizontal(Colors.red_to_blue, banner))
                print(Colorate.Horizontal(Colors.red_to_blue, f'\n{player} => Haz Perdido'))
                os.sys.exit
    if option_1 == 2:
        clear_console()
        print(Colorate.Horizontal(Colors.red_to_blue, '\n\nPronto estara disponible.....'))


except KeyboardInterrupt:
    os.sys.exit()