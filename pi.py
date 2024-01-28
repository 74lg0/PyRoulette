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
    def print_banner():
        print(Colorate.Horizontal(Colors.red_to_blue, banner))

    vidasp1 = 1
    vidasp2 = 1
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
    option_1 = int(input(Colorate.Horizontal(Colors.green_to_yellow, '==> ')))
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
            posicion_gatillo = random.randint(1, cilindre) # Digamos que hay 6 cilindros
            kill = random.randint(bullets, cilindre) # 4, 6 => Genera una cantidad de solo 2 cilindros vacion, 4 balas, 6 cilindros
            time.sleep(1)
            print(Colorate.Horizontal(Colors.red_to_blue, f'{bot} a apretado el gatillo'))
            time.sleep(2)
            if posicion_gatillo <= kill:
                vidasp1 = vidasp1 - 1
                print(Colorate.Horizontal(Colors.red_to_blue, f'Vidas de {bot} => {vidasp1}'))
            else:
                print(Colorate.Horizontal(Colors.red_to_blue, f'{bot} => Cámara vacía. Sigues vivo'))
            
            #Jugador
            posicion_gatillo = random.randint(1, cilindre)
            kill = random.randint(bullets, cilindre)
            input(Colorate.Horizontal(Colors.green_to_yellow, (f'{player} presiona enter para jalar el gatillo ')))
            time.sleep(4)
            if posicion_gatillo <= kill:
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
            
            else:
                pass
    if option_1 == 2:
        clear_console()
        print(Colorate.Horizontal(Colors.red_to_blue, banner))
        p1 = input(Colorate.Horizontal(Colors.blue_to_green, 'Elije tu nombre jugador 1 => '))
        p2 = input(Colorate.Horizontal(Colors.blue_to_green, 'Elije tu nombre jugador 2 => '))
        if p1 == p2:
            print(Colorate.Horizontal(Colors.blue_to_purple, 'Los nombres de los jugadores no pueden ser igual'))

        else:
            apuesta_r = input(Colorate.Horizontal(Colors.blue_to_green, "Desean apostar dinero de verdad Y/N\n=> "))
            apuesta_r1 = 0
            apuesta_r2 = 0
            ronda = 0
            if apuesta_r == "Y" or apuesta_r == "y":
                while True:
                    clear_console()
                    ronda += 1
                    inicio_a = int(input(Colorate.Horizontal(Colors.blue_to_green, f'Jugador {p1} cuanto vas a apostar en esta ronda ronda => ')))
                    inicio_a2 = int(input(Colorate.Horizontal(Colors.blue_to_green, f'Jugador {p2} cuanto vas a apostar en esta ronda ronda => ')))
                    apuesta_r1 += inicio_a
                    apuesta_r2 += inicio_a2
                    print(Colorate.Horizontal(Colors.red_to_white, 'Recuerda, estas apuestas son acumulativas\n Al final el ganador recibira la cantidad que allan apostado en todas las rondas'))
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'Jugador {p1} has apostado ${apuesta_r1} en la ronda {ronda}\nJugador {p2} has apostado ${apuesta_r2} en la ronda {ronda}'))
                    time.sleep(7)
                    clear_console()
                    print_banner()
                    posicion_gatillo = random.randint(1, cilindre)
                    kill = random.randint(bullets, cilindre)
                    input(Colorate.Horizontal(Colors.red_to_blue, f'Jugador {p1} presiona enter para jalar el gatillo...'))
                    time.sleep(3)
                    if posicion_gatillo <= kill:
                        vidasp1 = vidasp1 - 1
                        print(Colorate.Horizontal(Colors.red_to_purple, f"Vidas de {p1} => {vidasp1}"))
                        time.sleep(1)
                    else:
                        print(Colorate.Horizontal(Colors.green_to_yellow, "Camara Vacia. Sigues vivo"))
                        time.sleep(2)
                # Jugador
                    posicion_gatillo = random.randint(1, cilindre)
                    kill = random.randint(bullets, cilindre)
                    input(Colorate.Horizontal(Colors.green_to_blue, f'Jugador {p2} presiona enter para jalar el gatillo...'))
                    time.sleep(3)
                    if posicion_gatillo <= kill:
                        vidasp2 = vidasp2 - 1
                        print(Colorate.Horizontal(Colors.red_to_blue, f"Vidas de {p2} => {vidasp2}"))
                        time.sleep(2)
                    else:
                        print(Colorate.Horizontal(Colors.green_to_blue, "Camara Vacia. Sigues vivo"))
                        time.sleep(4)
# Verificacion de vidas
                    if vidasp1 == 0:
                        clear_console()
                        print_banner()
                        print(Colorate.Horizontal(Colors.green_to_blue, f'El jugador {p2} ha ganado\n[!] Recompensa de => {apuesta_r1}'))
                        os.sys.exit()
                    else:
                        pass
                    
                    if vidasp2 == 0:
                        clear_console()
                        print_banner()
                        print(Colorate.Horizontal(Colors.green_to_blue, f'El jugador {p1} ha ganado\n[!] Recompensa de => {apuesta_r2}'))
                        os.sys.exit()
                    
                    else:
                        pass

            else:
                print()

except KeyboardInterrupt:
    os.sys.exit()
