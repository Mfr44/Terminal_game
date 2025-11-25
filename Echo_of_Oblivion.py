# Терминальная игра "Эхо Забвения" 

from random import randint

class Character():
    def __init__(self, name):
        self.name = name 
        self.hp = 3 # здоровье персонажа
        self.key_found = False # ключ найден - означает возможность перехода на следующий уровень
        self.artifact_activated = False # артифакт - нужен для выхода из игры 
        self.symbol_remembered = False #символ запомнет - нужен для подтверждения прочтения карты 
        self.torch_fire = False # факел - нужен чтобы переплыть подземное озеро
        self.flint = False # кремень - нужен чтобы зажечь факел
        self.medicinal_herb = False # Лечебная трава (+ 1 к здоровью)

player_one = Character("player") 

class Location:
    def enter(self):
        raise NotImplementedError("Каждая локация должна реализовывать метод enter()")
    
 
class Death():
    qusips = [
        "О боже мой...",
        "Как тебя вообще так угораздило???",
        "Пу пу пу, мой маленький щенок соображает лучше",
        "GAME OVER"
    ]
    noy_hp = [
        "Надо смотреть за здоровьем!",
        "HP НА НУЛЕ",
        "Живой мертвец, РH ноооооль......"
     ]

    def enter(self):
        if player_one.hp <= 0:
            rand = randint(0,2)
            print(Death.noy_hp[rand])
            exit(1)
        else:
            rand = randint(0,3)
            print(Death.qusips[rand])
            exit(1)
    

class StartGame(Location):
    def enter(self):
        print(player_one.name)
        print("\n\t-----Добро пожаловать в \"Эхо Забвения: Пробуждение\"!-----\n" )
        print("Вы очнулись на холодном каменном полу. \n" \
        "Вокруг — тьма и запах сырости. Где вы? \nПоследнее, что вы помните — свет, вспышка и тишина.\n\n" \
        "Перед вами — три направления:\n" \
        "1) Север: узкий проход, откуда веет ледяным воздухом.\n" \
        "2) Восток: приглушённое свечение — возможно, выход.\n" \
        "3) Юг: темнота, но там слышен звук капающей воды.\n" \
        "Что вы выберете? (СЕВЕР / ВОСТОК / ЮГ)")
        
        choice = input("> ").strip().lower()

        if choice in ("1", "север"):
            return "sever"
        elif choice in ("2", "восток"):
            return "vostok"
        elif choice in ("3", "юг"):
            return "yug"
        else:
            print("Странно, попробуй еще раз!")
            return "start_game"

class Sever(Location):
    def enter(self):
        print ("\n\t---ЛОКАЦИЯ: Сырой Проход---")
        print("Вы спускаетесь вниз. Здесь холоднее. \n" \
        "На стене — высеченные символы и потухший факел." \
            "\n1) Осмотреть символы." \
            "\n2) Взять факел." \
            "\n3) Вернуться назад.")
        
        choice = input(">").strip().lower()
    

        if choice.lower() in ("1"):

            player_one.symbol_remembered = True
            print("Вы замечаете знак, похожий на тот, что видели во сне. Он словно пульсирует.\n" \
            "*** Состояние Игрока: символ запомнен = %r ***" % (player_one.symbol_remembered))
            print("отправляешься на локацию \"сырой проход\"")
            return "sever"

        elif choice == '2':
            print("Вы берёте факел со стены. Он влажный, но если у вас есть кремень — можно зажечь.")


            if player_one.flint == False:
                print("Факел мокрый, нужно чем-то зажечь.\n" \
                      "***  Состояние кремния = %r  ***" % (player_one.flint))
                print("отправляешься на начальную локацию \"сырой проход\"")
                return "sever"


            elif player_one.flint == True:
                print(" Искры вспыхивают — факел горит\n" \
                "***  Состояние факела = %r  ***" % (player_one.torch_fire))
                print("отправляешься на начальную локацию \"сырой проход\"")
                
                return "sever"
            else:
             print("Странно, попробуй еще раз!")
             return "sever"
            
        elif choice == '3':
            return "start_game"

        else:
            print("Странно, попробуй еще раз!")
            return "sever"
    

class Safe(Location):
    def enter(self):
        print("У вас 3 попытки")
        shans = 3

        while shans > 0:
            choice = input("Введите код от сейфа:").strip()
        
            if choice == "373":
                player_one.key_found = True
                player_one.flint = True 
                player_one.torch_fire = True
                print("Сундук ржавый, но поддаётся. Внутри: “Ржавый Ключ” и “Кремень”.\n")
                print("*** Состояние Игрока: Ключ = %r ***" % (player_one.key_found))
                print("*** Состояние Игрока: Кремень = %r ***" % (player_one.flint))
                print("*** Состояние Игрока: Факел = %r ***" % (player_one.torch_fire))
                print("отправляешься обратно на ЛОКАЦИЮ: \"Затопленный Коридор\"\n")
                return "vostok"
            else: 
                shans -= 1
                print("Замок сундука проворачивается и ничего не происходит.")
                print("Осталось %r попыток" % shans)
                
                if shans < 0:
                    print("Осталось попыток %r" % shans)

        print("\nСейф заблокирован. Вы больше не можете открыть его.\n")
        return "death"
         
class Vostok(Location):
    def enter(self):
        print("---ЛОКАЦИЯ: Затопленный Коридор---")
        print("Вода по щиколотку. Вдоль стены виден ржавый сундук. Вдалеке — массивная дверь.\n" \
        "1) Открыть сундук (нужен код).\n" \
        "2) Подойти к двери.\n" \
        "3) Вернуться.")

        choice = input(">")
    
        if choice == '1':
            return "sefe"
        
        elif choice == "2":
            print("Дверь заперта. На ней выгравирован символ глаза.\n")
            if player_one.symbol_remembered == True:
                print("И тут ты вспоминаешь сивол который ты запомнил. \n" \
                "Символ вспыхивает, и дверь тихо открывается. За ней лестница вниз." \
                "\nВы переходите в ЛОКАЦИЮ: Подземное Святилище.\n")
                return "underground"
                

            elif player_one.symbol_remembered == False:
                print("Символ остаётся мёртвым. Дверь не поддаётся.")
                print("отправляешься обратно на ЛОКАЦИЮ: \"Восток\"")
                return "vostok"
            else:
                print("Странно, попробуй еще раз!")
                print("отправляешься обратно на ЛОКАЦИЮ: \"Восток\"")
                return "vostok"
            
        elif choice == "3":
            
            print("отправляешься обратно на стартовую локацию")
            return "start_game"

class Yug(Location):
    def enter(self):
        print("---ЛОКАЦИЯ: Подземное Озеро---")
        print("Темно. Без света вы едва видите берег. В центре озера — островок с чем-то блестящим.\n" \
        "1) Попробовать переплыть.\n" \
        "2) Осмотреть берег.\n" \
        "3) Вернуться.")

        choice = input(">")
    
        if choice == "1":
            player_one.hp -= 1
            print("Вода ледяная, вы не видите куда плывёте. Что-то хватает вас за ногу. \n" \
            "*** здоровье -1 ***\n" \
            "Здоровья осталось %r\n" \
            "Вы едва выбираетесь назад.\n\n" % player_one.hp)

            if player_one.torch_fire == True:
                player_one.artifact_activated = True
                print("Но тебя спасает горящий факел\n")
                print("Свет факела отражается в воде, и вы замечаете деревянную лодку сбоку.\n" \
                "С её помощью вы переправляетесь на остров. На острове — Серебряный Амулет.\n"
                "*** В инвентарь добавлен \"Серебряный Амулет\" ***\n\n")
                print("Возвращаешся обратно на лоуацию ЛОКАЦИЯ: Подземное Озеро")
                return "yug"
            
            elif player_one.torch_fire == False:
                print("Факел не горит по этому в темоте ничего не видно...\n" \
                "Дальше плыть невозможно")
                print("Возвращаешся обратно на лоуацию ЛОКАЦИЯ: Подземное Озеро")
                return "yug"
            
            else:
                print("Странно, попробуй еще раз!")
                print("Возвращаешся обратно на лоуацию ЛОКАЦИЯ: Подземное Озеро")
                return "yug"

        elif choice == "2":
            if player_one.medicinal_herb == False:
                player_one.hp += 1
                player_one.medicinal_herb = True

                print("Под камнями вы находите записку, в ней написынно три цифры \"373\"\n"\
                      "рядом с запиской маленький мешочек с сушёными травами.\n" \
                      "*** здоровье +1 (но не больше 3) ***" )
                print("Здоровье =", player_one.hp)
                return "yug"
                
            elif player_one.medicinal_herb == True:
                print("Эх похоже здесь больше ничего нет...")
                print("Отправляешся обратно на локацию ЮГ")
                return "yug"
            
        elif choice == "3":
            print("отправляешься обратно на стартовую локацию")
            return "start_game"

class UndergroundSanctuary (Location):
    def enter(self):
        print("---Локация: \"ПОДЗЕМНОЕ СВЯТИЛИЩЕ\"")
        print("Вы спускаетесь в зал, освещённый тусклым голубым светом. В центре — Алтарь.\n" \
        "Он пульсирует тем же символом глаза.\n" \
        "1) Подойти к алтарю.\n" \
        "2) Осмотреть стены.\n" \
        "3) Вернуться к двери.\n")

        choice = input(">")
    
        if choice == "1":
            if player_one.key_found == True:
                print("В основании алтаря вы находите выемку для ключа. Вставляете его.\n" \
                      "Алтарь открывает нишу — внутри место для амулета.")
                if player_one.artifact_activated == True:
                    print("У тебе есть артифакт, ты его вставляешь и ...")
                    print("ПОЯВЛЯЕТСЯ ПОРТАЛ НА ВЫХОД\n\n" \
                    "Вы можете уйти.\n" \
                    "1) Войти в портал.\n" \
                    "2) Забрать амулет обратно (рискуя).")

                    choice = input(">")

                    if choice == "1":
                        print("Свет поглощает вас, и вы просыпаетесь у входа в руины. " \
                              "Солнце ослепительно, но вы живы." \
                                "*** Амулет исчез. ***")
                        return "finished"
                    
                    elif choice == "2":
                        print("Когда вы касаетесь амулета, энергия пронзает вас.")
                        player_one.hp = 0 
                        print("Здоровье =", player_one.hp)
                        return "death"
                    
                elif player_one.artifact_activated == False:
                    print("В инфенторе нет артифакта, осмотрись еще")
                    print("Отправляешся обратно в ЛОКАЦИЮ: \"Подземное святилище\"")
                    return "underground"
                
            elif player_one.key_found == False:
                print("Так, тут замочная скважена, в инвенторе отсутствует ключ.")
                return "underground"
            
        elif choice == "2":
            print("На стенах изображены сцены: люди приносят амулет к глазу, а затем уходят в свет." \
            "\nПохоже, амулет должен быть помещён на алтарь.")
            print("Отправляешся обратно на локацию Подземное святилище\n")
            return "underground"
        
        elif choice == "3":
            print("отправляешся обратно на ЛОКАЦИЮ: Затопленный Коридор")
            return "vostok"

class Finished (Location):
 def enter(self):
        print ("Вы победили! Отличная работа!")
        return 'finished' 

class Engine():
    
    def __init__(self, scenes_mapa):
        self.scenes_mapa = scenes_mapa

    def play(self):
        current_scene = self.scenes_mapa.opening_scene()
        last_scener = self.scenes_mapa.next_csene('finished')

        while current_scene !=last_scener:
            if player_one.hp <= 0:
                death_scene = self.scenes_mapa.next_csene("death")
                death_scene.enter()
            nev_scens = current_scene.enter()
            current_scene = self.scenes_mapa.next_csene(nev_scens)

        last_scener.enter()

class Mapa():

    scenes ={
    "start_game": StartGame(),
    "sever": Sever(),
    "vostok": Vostok(),
    "yug": Yug(),
    "death": Death(),
    "finished": Finished(),
    "underground": UndergroundSanctuary(),
    "sefe": Safe()
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    # замена с имени сцены на название сцены
    def next_csene(self,scene_name):
        return Mapa.scenes.get(scene_name)

    # запуск первой сцены (как движек понимает какую сценцу запускать первой)
    def opening_scene(self):
        return self.next_csene(self.start_scene)

a_map = Mapa("start_game")
a_game = Engine(a_map)
a_game.play()