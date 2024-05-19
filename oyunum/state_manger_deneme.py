import pygame
import sys
import button
import random
import time

pygame.init()
pygame.font.init()

ekran_en=1000
ekran_boy=700
screen=pygame.display.set_mode((ekran_en,ekran_boy))


pygame.display.set_caption("Adventures of The Bard")
house_img = pygame.image.load("buildings/classichouse.png").convert_alpha()
press_start = pygame.image.load("buttons/press_start.png").convert_alpha()
no_xp_img= pygame.image.load("buttons/no_xp.png").convert_alpha()

#ARKA FON
grass_background=pygame.transform.scale(pygame.image.load("backgrounds/grasscanva03.png"),(ekran_en,ekran_boy))

opening=pygame.transform.scale(pygame.image.load("backgrounds/opening2.jpg"),(ekran_en,ekran_boy))
fight_scene=pygame.transform.scale(pygame.image.load("backgrounds/fight.png"),(ekran_en,ekran_boy))
fight_scene1=pygame.transform.scale(pygame.image.load("backgrounds/fight.png"),(ekran_en,ekran_boy))
fight_scene2=pygame.transform.scale(pygame.image.load("backgrounds/fight.png"),(ekran_en,ekran_boy))
fight_scene3=pygame.transform.scale(pygame.image.load("backgrounds/fight.png"),(ekran_en,ekran_boy))
defeat_bg=pygame.transform.scale(pygame.image.load("backgrounds/defeat.png"),(ekran_en,ekran_boy))
victory_bg=pygame.transform.scale(pygame.image.load("backgrounds/victory.jpg"),(ekran_en,ekran_boy))
av_ve_topla=pygame.transform.scale(pygame.image.load("backgrounds/opening3.webp"),(ekran_en,ekran_boy))
showcase=pygame.transform.scale(pygame.image.load("backgrounds/showcase.jpg"),(ekran_en,ekran_boy))
menu_bg=pygame.transform.scale(pygame.image.load("backgrounds/menu_bg.png"),(900,ekran_boy+200))
tablo=pygame.transform.scale(pygame.image.load("backgrounds/tablo.png"),(550,250))
tablo_yatay=pygame.transform.scale(pygame.image.load("backgrounds/tablo_yatay.png"),(750,450))
name_tablosu=pygame.transform.scale(pygame.image.load("backgrounds/name_tablo.png"),(420,200))
welcome=pygame.transform.scale(pygame.image.load("backgrounds/welcome.png"),(310,150))

#karakterler
char_multiplier=12
char_multiplier2=10

main_char=pygame.transform.scale(pygame.image.load("chars/main_char.png"),(300,320))

main_char_ana_ekran=pygame.transform.scale(pygame.image.load("chars/main_char.png"),(300,320))

haydut_easy=pygame.transform.scale(pygame.image.load("chars/haydut_easy.png"),(36*char_multiplier2,40*char_multiplier2))
haydut_mid=pygame.transform.scale(pygame.image.load("chars/haydut_mid.png"),(300,380))
haydut_hard=pygame.transform.scale(pygame.image.load("chars/haydut_hard.png"),(39*char_multiplier,50*char_multiplier2))

#can barları
full_life=pygame.transform.scale(pygame.image.load("backgrounds/lifebars/full_life2.png"),(320,100))
almost_full_life=pygame.transform.scale(pygame.image.load("backgrounds/lifebars/almost_full2.png"),(320,100))
half_life=pygame.transform.scale(pygame.image.load("backgrounds/lifebars/half_life2.png"),(320,100))
almost_over_life=pygame.transform.scale(pygame.image.load("backgrounds/lifebars/almost_over_life2.png"),(320,100))
over_life=pygame.transform.scale(pygame.image.load("backgrounds/lifebars/life_over2.png"),(320,100))


#BİNALAR
kamp_alani_img=pygame.image.load('buildings/classichouse.png').convert_alpha()
kamp_alani_img=button.Button(95, 50, kamp_alani_img, 0.6)
macera_img=pygame.image.load('buildings/classichouse.png').convert_alpha()
macera_img=button.Button(95, 350, macera_img, 0.6)
han_img=pygame.image.load('buildings/classichouse.png').convert_alpha()
han_img=button.Button(700, 50, han_img, 0.6)
sifahane_img=pygame.image.load('buildings/classichouse.png').convert_alpha()
sifahane_img=button.Button(700, 350, sifahane_img, 0.6)

#BUTTONS

#menü butonları
scale=0.6
level_up_button= pygame.image.load("buttons/levelup.png").convert_alpha()
level_up_button=button.Button(500-(level_up_button.get_width()*scale/2),590, level_up_button,scale)
menu_button= pygame.image.load("buttons/menu.png").convert_alpha()
menu_button=button.Button(500-(menu_button.get_width()*scale/2),10, menu_button,scale)

#mekan butonları
scale2=0.45
kamp_alani_button= pygame.image.load("buttons/kamp_alani.png").convert_alpha()
kamp_alani_button=button.Button(90, 250, kamp_alani_button,scale2)
macera_button= pygame.image.load("buttons/macera.png").convert_alpha()
macera_button=button.Button(90, 550, macera_button,scale2)
han_button= pygame.image.load("buttons/han.png").convert_alpha()
han_button=button.Button(700, 250, han_button,scale2)
sifahane_button= pygame.image.load("buttons/sifahane.png").convert_alpha()
sifahane_button=button.Button(700, 550, sifahane_button,scale2)

#menü için olan butonlar
scale3=0.4
menu_buton_hiza=400
menu_buton_hiza_y=120
ozellikler_button=pygame.image.load("buttons/ozellikler_button.png").convert_alpha()
ozellikler_button=button.Button(menu_buton_hiza+15, menu_buton_hiza_y,ozellikler_button,0.35)
kamp_alani_button1= pygame.image.load("buttons/kamp_alani.png").convert_alpha()
kamp_alani_button1=button.Button(menu_buton_hiza, menu_buton_hiza_y+70, kamp_alani_button1,scale3)
han_button1= pygame.image.load("buttons/han.png").convert_alpha()
han_button1=button.Button(menu_buton_hiza, menu_buton_hiza_y+140, han_button1,scale3)
sifahane_button1= pygame.image.load("buttons/sifahane.png").convert_alpha()
sifahane_button1=button.Button(menu_buton_hiza, menu_buton_hiza_y+220, sifahane_button1,scale3)
macera_button1= pygame.image.load("buttons/macera.png").convert_alpha()
macera_button1=button.Button(menu_buton_hiza, menu_buton_hiza_y+300, macera_button1,scale3)
town_button= pygame.image.load("buttons/town_button.png").convert_alpha()
town_button=button.Button(menu_buton_hiza+50, menu_buton_hiza_y+370, town_button,0.3)

#perks butonları
strenght_button=pygame.image.load("buttons/guc_button.png").convert_alpha()
strenght_button=button.Button(100, 80, strenght_button,0.5)
agility_button=pygame.image.load("buttons/ceviklik_button.png").convert_alpha()
agility_button=button.Button(450, 120, agility_button,0.35)
charisma_button=pygame.image.load("buttons/karizma_button.png").convert_alpha()
charisma_button=button.Button(720, 120, charisma_button,0.3)
gathering_button=pygame.image.load("buttons/toplayiclik_button.png").convert_alpha()
gathering_button=button.Button(270, 360, gathering_button,0.3)
resist_button=pygame.image.load("buttons/dayaniklilik_button.png").convert_alpha()
resist_button=button.Button(590, 400, resist_button,0.6)

#kamp butonları
sarki_button=pygame.image.load("buttons/sarkı_button.png").convert_alpha()
sarki_button=button.Button(50, 350, sarki_button,0.6)


banyo_button=pygame.image.load("buttons/bath_button.png").convert_alpha()
banyo_button=button.Button(340, 350, banyo_button,0.6)
uyku_button=pygame.image.load("buttons/uyku_button.png").convert_alpha()
uyku_button=button.Button(580, 300, uyku_button,0.8)
#şifahane butonları
merhem_button=pygame.image.load("buttons/merhem_button.png").convert_alpha()
merhem_button=button.Button(180, 100, merhem_button,0.7)
yara_sar_button=pygame.image.load("buttons/yara_sar_button.png").convert_alpha()
yara_sar_button=button.Button(500, 100, yara_sar_button,0.7)
#han butonları
yiyecek_button=pygame.image.load("buttons/food_button.png").convert_alpha()
yiyecek_button=button.Button(380, 350, yiyecek_button,0.6)
icecek_button=pygame.image.load("buttons/drink_button.png").convert_alpha()
icecek_button=button.Button(680, 350, icecek_button,0.6)
#macera butonları
av_button=pygame.image.load("buttons/av_button.png").convert_alpha()
av_button=button.Button(200, 60, av_button,0.5)
orman_button=pygame.image.load("buttons/forest_button.jpg").convert_alpha()
orman_button=button.Button(580, 100, orman_button,0.2)
kayalik_button=pygame.image.load("buttons/kayaliklar_button.png").convert_alpha()
kayalik_button=button.Button(200, 320, kayalik_button,0.13)
vadi_button=pygame.image.load("buttons/valley_button.jpg").convert_alpha()
vadi_button=button.Button(580, 310, vadi_button,0.4)

ok_button=pygame.image.load("buttons/done.png").convert_alpha()
ok_button=button.Button(250, 200,ok_button,0.8)
very_ok_button=pygame.image.load("buttons/very_ok.png").convert_alpha()
very_ok_button=button.Button(380, 500,very_ok_button,0.3)
yes_button=pygame.image.load("buttons/yes_button.png").convert_alpha()
yes_button=button.Button(220, 330,yes_button,0.3)
no_button=pygame.image.load("buttons/no_button.png").convert_alpha()
no_button=button.Button(550, 330,no_button,0.35)
no_xp_button=pygame.image.load("buttons/no_xp.png").convert_alpha()
no_xp_button=button.Button(250, 200,no_xp_button,0.8)

exit_button=pygame.image.load("buttons/exit_button.png").convert_alpha()
exit_button=button.Button(0, 0,exit_button,0.2)

#savaş butonları
kacma_button=pygame.image.load("buttons/kacma_dene.png").convert_alpha()
kacma_button=button.Button(360, 500,kacma_button,0.5)
start_fight_button=pygame.image.load("buttons/start_the_fight.png").convert_alpha()
start_fight_button=button.Button(370, 50,start_fight_button,1)
attack_button=pygame.image.load("buttons/attack.png").convert_alpha()
attack_button=button.Button(380, 340,attack_button,0.8)

#FONTLAR:
text_font=pygame.font.SysFont("arial",30,bold=True,italic=False)
text_font2=pygame.font.SysFont("timesnewroman",30,bold=True,italic=False)
text_font3=pygame.font.SysFont("timesnewroman",20,bold=True,italic=False)
text_font4=pygame.font.SysFont("timesnewroman",20,bold=True,italic=False)
text_font5=pygame.font.SysFont("timesnewroman",40,bold=True,italic=False)
text_font6=pygame.font.SysFont("timesnewroman",20,bold=True)

# OYUNCU BİLGİLERİ
class Karakter:
    def __init__(self, can, guc, ceviklik, dayaniklilik):
        # temel nitelikler
        self.can = can
        # beceriler
        self.guc = guc
        self.ceviklik = ceviklik
        self.dayaniklilik = dayaniklilik

class Oyuncu(Karakter):
    def __init__(self, name, calgi):
        super().__init__(can=100, guc=1, ceviklik=1, dayaniklilik=1)
        # alınan bilgiler
        self.name = name
        self.calgi = calgi
        # temel nitelikler max100
        self.tokluk = 100
        self.hijyen = 100
        self.eglence = 100
        self.uykusuzluk = 100
        # beceriler max25
        self.karizma = 1
        self.toplayıcılık = 1
        # extra
        self.para = 10
        self.tecrube = 0
        self.seviye = 0
        self.xp_puan = 0
    # kamp alanı kodları
    def sarkı_soyle(self):

        if self.uykusuzluk >= 30:
            if self.hijyen >= 10:

                if self.eglence <= 80:
                    self.eglence += 20
                else:
                    self.eglence = 100
                if self.tecrube <= 90:
                    self.tecrube += 10
                if self.tecrube>=100:
                    pass

                self.uykusuzluk -= 10
                self.hijyen -= 10

            else:
                print("uyarı hijyen low")
        else:
            print("uyarı dinlenmen lazım")
    def yıkanma(self):
        if oyuncum.uykusuzluk > 90:
            if oyuncum.tokluk > 90:
                if oyuncum.eglence > 90:

                    oyuncum.hijyen = 100

                else:
                    pass
            else:
                pass
        else:
            pass
    def uyu(self):
        if oyuncum.tokluk > 30:
            # can yükseltme kısmı
            self.uykusuzluk = min(100, self.uykusuzluk + 20)

            self.tokluk = max(0, self.tokluk - 30)
            self.eglence = max(0, self.eglence - 30)
            self.hijyen = max(0, self.hijyen - 30)

            return 1
        else:
            print("açken uyuyamazsın")
            return 0  # pass
    # şifahane kodları
    def yaraları_sarma(self):
        if oyuncum.tokluk > 10:
            if oyuncum.hijyen > 10:
                if oyuncum.eglence > 10:
                    if oyuncum.uykusuzluk > 10:
                        # can yükseltme kısmı
                        self.can = min(100, self.can + 20)
                        oyuncum.tokluk -= 10
                        oyuncum.eglence -= 10
                        oyuncum.hijyen -= 10
                        oyuncum.uykusuzluk -= 10
                    else:
                        print("uyarı dinlenmen lazım")  # return 0  # pass
                else:
                    print("eğlencen düşük")  # return 0  # pass
            else:
                print("uyarı hijyen low")  # return 0  # pass
        else:
            print("açken çalamazsın")  # return 0  # pass
    def merhem(self):

        if oyuncum.tokluk > 10:
            if oyuncum.hijyen > 10:
                if oyuncum.eglence > 10:
                    if oyuncum.uykusuzluk > 10:
                        # can yükseltme kısmı
                        self.can = min(100, self.can + 50)
                        oyuncum.tokluk-=10
                        oyuncum.eglence-=10
                        oyuncum.hijyen-=10
                        oyuncum.uykusuzluk-=10
                    else:
                        print("uyarı dinlenmen lazım")#return 0  # pass
                else:
                    print("eğlencen düşük")#return 0  # pass
            else:
                print("uyarı hijyen low")#return 0  # pass
        else:
            print("açken çalamazsın")#return 0  # pass
    # HAN kodları
    def yiyecek_al_ve_ye(self):

        if self.uykusuzluk >= 10:
            if self.hijyen >= 10:
                if self.eglence>=10:
                    if self.para>=10:

                        self.tokluk = min(100, self.tokluk + 50)
                        self.para -= 10
                        self.uykusuzluk -= 10
                        self.hijyen -= 10
                        self.eglence -= 10

                    else:
                        print("yetersiz bakiye")
                else:
                    print("eğlencen düşük")
            else:
                print("uyarı hijyen low")
        else:
            print("uyarı dinlenmen lazım")
    def icecek_al_ve_ye(self):
        if self.uykusuzluk >= 10:
            if self.hijyen >= 10:
                if self.eglence >= 10:
                    if self.para >= 5:

                        self.tokluk = min(100, self.tokluk + 10)
                        self.para -= 5
                        self.uykusuzluk -= 10
                        self.hijyen -= 10
                        self.eglence -= 10

                    else:
                        print("yetersiz bakiye")
                else:
                    print("eğlencen düşük")
            else:
                print("uyarı hijyen low")
        else:
            print("uyarı dinlenmen lazım")
    def cal_ve_sarki_soyle(self):

        if self.uykusuzluk >= 10:
            if self.hijyen >= 10:
                if self.tokluk>=10 or self.tokluk!=0:
                    if self.eglence <= 80:
                        self.eglence += 20
                    elif self.eglence >= 80:
                        self.eglence = 100

                    if self.tecrube <= 90:
                        self.tecrube += 10
                    elif self.tecrube >= 90:
                        self.tecrube = 100

                    self.uykusuzluk -= 10
                    self.hijyen -= 10
                    self.tokluk -= 10
                else:
                    print("açken çalamazsın")
            else:
                print("uyarı hijyen low")
        else:
            print("uyarı dinlenmen lazım")
    # macera kodları
    def bitki_topla_ve_avlan(self):
        if random.randint(0, (self.toplayıcılık * 4) / 100) > 0.5:
            # bitki bulunur
            self.can = min(100, self.can + 10)
        if random.randint(0, (self.toplayıcılık * 4) / 100) > 0.5:
            # meyve bulunur
            self.can = min(100, self.can + 20)
        if random.randint(0, (self.toplayıcılık * 4) / 100) * 2 > 0.5:
            # avlanır
            self.tokluk = min(100, self.tokluk + 50)
        else:
            print("no")
    def orman_kesif(self):  # kolay haydut
        if oyuncum.tecrube <= 70:
            oyuncum.tecrube += 30
        else:
            oyuncum.tecrube = 100

        oyuncum.para += 30
        oyuncum.uykusuzluk -= 10
        oyuncum.tokluk -= 10
        oyuncum.eglence -= 10
        oyuncum.hijyen -= 10
    def kayalik_kesfi(self):  # orta haydut
        if oyuncum.tecrube <= 40:
            oyuncum.tecrube += 60
        else:
            oyuncum.tecrube = 100

        oyuncum.para += 30
        oyuncum.uykusuzluk -= 10
        oyuncum.tokluk -= 10
        oyuncum.eglence -= 10
        oyuncum.hijyen -= 10
    def vadi_gez(self):  # zor haydut

        oyuncum.tecrube = 100
        oyuncum.para += 30
        oyuncum.uykusuzluk -= 10
        oyuncum.tokluk -= 10
        oyuncum.eglence -= 10
        oyuncum.hijyen -= 10
    def isim_al(self):
        oyuncum.name = info_alma()
    def calgi_al(self):
        oyuncum.calgi = info_alma2()
    def seviye_atla(self):
        pass
    def __str__(self):
        return (f'Oyuncunun özellikleri\nİsim:{self.name}\nÇalgı:{self.calgi}\n'
                f'Temel Nitelikler:\nCan:{self.can}\n'
                f'Tokluk:{self.tokluk}\nHijyen:{self.hijyen}\n'
                f'Eğlence:{self.eglence}\nUykusuzluk:{self.uykusuzluk}\nBECERİLER:\nGüç:{self.guc}\n'
                f'Çeviklik:{self.ceviklik}\nDayanıklılık:{self.dayaniklilik}\n'
                f'Karizma:{self.karizma}\nToplayıcılık:{self.toplayıcılık}\n')
    def oyundan_cik(self):
        pass

def draw_text(text,font,text_color,x,y):
    img=font.render(text,True,text_color)
    screen.blit(img,(x,y))
def info_alma():
    # info alma kısmı
    base_font = pygame.font.Font(None, 45)
    user_text = " "
    input_rect = pygame.Rect(400, 350, 150, 40)#x,y,-,boy

    box_color = pygame.Color("darkblue")
    box_color2 = pygame.Color("lightyellow")

    var = True
    while var:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                var = False

        #screen.fill((100, 100, 50))
        screen.blit(opening, (0, 0))

        pygame.draw.rect(screen, box_color, input_rect, 0)
        pygame.draw.rect(screen, box_color2, input_rect, 5)

        draw_text("İSİM:",text_font2,"white",320,355)
        draw_text("OYUNCUNUN İSMİNİ GİRİNİZ",text_font2,"white",270,305)
        draw_text("PRESS RİGHT ARROW TO CONTİNUE",text_font3,"white",300,660)


        text_surface = base_font.render(user_text, True, (150, 0,0))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()
    return user_text
def info_alma2():
    # info alma kısmı
    base_font = pygame.font.Font(None, 45)
    user_text = " "
    input_rect = pygame.Rect(400, 350, 150, 40)#x,y,-,boy

    box_color = pygame.Color("darkblue")
    box_color2 = pygame.Color("lightyellow")
    var = True

    while var:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                var = False

        #screen.fill((100, 100, 50))
        screen.blit(opening, (0, 0))

        pygame.draw.rect(screen, box_color, input_rect, 0)
        pygame.draw.rect(screen, box_color2, input_rect, 5)

        draw_text("ÇALGI:",text_font2,"white",290,355)
        draw_text("OYUNCUNUN ÇALGISINI GİRİNİZ",text_font2,"white",240,305)
        draw_text("PRESS RİGHT ARROW TO CONTİNUE",text_font3,"white",300,660)


        text_surface = base_font.render(user_text, True, (50, 155, 100))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()
    return user_text

class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((ekran_en,ekran_boy))
        self.clock=pygame.time.Clock()

        self.gameStateManager=GameStateManager("start")
        self.start = Start(self.screen, self.gameStateManager)
        self.town = Town(self.screen, self.gameStateManager)
        self.sifahane = Sifahane(self.screen, self.gameStateManager)
        self.han = Han(self.screen, self.gameStateManager)
        self.kamp_alani = Kamp_alani(self.screen, self.gameStateManager)
        self.menu = Menu(self.screen, self.gameStateManager)
        self.level_atla = Level_atla(self.screen, self.gameStateManager)
        self.macera= Macera(self.screen, self.gameStateManager)
        self.howtoplay = HowToPlay(self.screen, self.gameStateManager)
        self.showcase = Showcase(self.screen, self.gameStateManager)
        self.done = Done(self.screen, self.gameStateManager)

        self.fight = Fight(self.screen, self.gameStateManager)
        self.fight2 = Fight2(self.screen, self.gameStateManager)
        self.fight3 = Fight3(self.screen, self.gameStateManager)
        self.av_topla = AvVeToplama(self.screen, self.gameStateManager)
        self.no_xp = NO_XP(self.screen, self.gameStateManager)
        self.defeat = Defeat(self.screen, self.gameStateManager)
        self.victory = Victory(self.screen, self.gameStateManager)
        self.emin_misin = EminMisin(self.screen, self.gameStateManager)
        self.emin_misin2= EminMisin2(self.screen, self.gameStateManager)
        self.emin_misin3 = EminMisin3(self.screen, self.gameStateManager)
        self.exit_ekrani = ExitEkranı(self.screen, self.gameStateManager)
        self.seviye_atla_uyari = SeviyeAtlaUyari(self.screen, self.gameStateManager)

        self.states={"start":self.start,"sifahane":self.sifahane,"han":self.han,"kamp_alani":self.kamp_alani,"menu":self.menu,
                     "level_atla":self.level_atla,"fight":self.fight,"macera":self.macera,"town":self.town,"howtoplay":self.howtoplay,
                     "showcase":self.showcase,"done":self.done,"fight2":self.fight2,"fight3":self.fight3,
                     "av_topla":self.av_topla,"no_xp":self.no_xp,"defeat":self.defeat,"victory":self.victory,
                     "emin_misin":self.emin_misin, "emin_misin2":self.emin_misin2, "emin_misin3":self.emin_misin3,
                     "exit_ekrani":self.exit_ekrani,"seviye_atla_uyari":self.seviye_atla_uyari}
    def run(self):
        oyuncum.isim_al()
        oyuncum.calgi_al()
        clock = pygame.time.Clock()
        start_time = time.time()
        while True:
            clock.tick(60)
            elapsed_time = time.time()-start_time

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if event.type==pygame.KEYDOWN:
                    if keys[pygame.K_ESCAPE]:
                        self.gameStateManager.set_state("town")
            self.states[self.gameStateManager.get_state()].run()
            ##ÇOK ÇOK ÖNEMLİ HER CLASSDADA RUN DİYE FONSKİYON OLMALI YOKSA OLMAZ
            time_text = text_font.render(f"Time :{round(elapsed_time)}s", 1, "white")
            screen.blit(time_text, (10, 650))
            pygame.draw.rect(screen,"white",(880,20,110,100))
            draw_text(f"PARA:{oyuncum.para} ",text_font4,"black",890,30)
            draw_text(f"XP:{oyuncum.tecrube}",text_font4,"black",890,60)#TECRUBE
            draw_text(f"SEVİYE:{oyuncum.seviye}",text_font4,"black",890,90)
            pygame.display.update()

################
class Start:
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):#bu levelde isen olan şeyler yani
        bg = pygame.transform.scale(pygame.image.load("backgrounds/opening5.jpg"), (ekran_en, ekran_boy))
        self.display.blit(bg,(0,0))
        screen.blit(press_start,(180,480))

        screen.blit(name_tablosu, (300, 230))
        screen.blit(welcome, (350,120))
        ########
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] :
            self.gameStateManager.set_state("town")

class Town:
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
        self.clock = pygame.time.Clock()
    def run(self):

         screen.blit(grass_background, (0, 0))

         #######

         screen.blit(main_char_ana_ekran, (360, 175))

         if exit_button.draw(screen):
             self.gameStateManager.set_state("exit_ekrani")

         if 100 >= oyuncum.can>85:
             screen.blit(full_life, (360, 470))
         if  85>= oyuncum.can >60:
             screen.blit(almost_full_life, (360, 470))
         if 60>= oyuncum.can >50:
             screen.blit(half_life, (360, 470))
         if 50 >= oyuncum.can >0:
             screen.blit(almost_over_life, (360, 470))
         if oyuncum.can==0:
             screen.blit(over_life, (360, 470))

         draw_text(f"{oyuncum.can:.2f}",text_font6,"white",505,510)
         draw_text(f"{oyuncum.name}", text_font5, "white", 420, 145)

         if han_button.draw(screen):
            self.gameStateManager.set_state("han")

         if sifahane_button.draw(screen):
            self.gameStateManager.set_state("sifahane")

         if macera_button.draw(screen):
            self.gameStateManager.set_state("macera")

         if kamp_alani_button.draw(screen):
            self.gameStateManager.set_state("kamp_alani")

         if level_up_button.draw(screen):
             if oyuncum.tecrube==100:
                 #oyuncum.xp_puan+=3#bu puanlar birikebilirse olur bu
                 oyuncum.xp_puan= min(3, oyuncum.xp_puan + 3)
                 self.gameStateManager.set_state("level_atla")
             else:
                 print("yeteri tecrübe yok")#buraya yetersiz işareti getir
                 self.gameStateManager.set_state("no_xp")
         if menu_button.draw(screen):
            self.gameStateManager.set_state("menu")


         if han_img.draw(screen):
            pass
            #self.gameStateManager.set_state("han")
         if sifahane_img.draw(screen):
             pass
             #self.gameStateManager.set_state("sifahane")
         if macera_img.draw(screen):
             pass
             #self.gameStateManager.set_state("macera")
         if kamp_alani_img.draw(screen):
             pass
             #self.gameStateManager.set_state("kamp_alani")


         if oyuncum.seviye==15:
             pass#buraya hikaye anaçlı gelen final boss gelebilir

         if oyuncum.tecrube==100:
             self.gameStateManager.set_state("seviye_atla_uyari")#pass#buraya seviye atla diye uyarı gelmesi lazım

class Sifahane:
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        bg = pygame.transform.scale(pygame.image.load("backgrounds/sifahane.webp"), (ekran_en, ekran_boy))
        self.display.blit(bg, (0, 0))

        #buralara class içindeki mödüller return ekle

        if merhem_button.draw(screen):
            #sonuc=oyuncum.merhem()
            oyuncum.merhem()
            self.gameStateManager.set_state("done")
            """
            if sonuc==0:
                self.gameStateManager.set_state("done")
            else:
                self.gameStateManager.set_state("done")
"""

        if yara_sar_button.draw(screen):
            #sonuc=oyuncum.yaraları_sarma()
            oyuncum.yaraları_sarma()
            self.gameStateManager.set_state("done")
            """
            if sonuc == 0:
                self.gameStateManager.set_state("done")
            else:
                self.gameStateManager.set_state("done")
                 """

class Han:
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        bg = pygame.transform.scale(pygame.image.load("backgrounds/han.png"), (ekran_en, ekran_boy))
        self.display.blit(bg, (0, 0))

        if yiyecek_button.draw(screen):
            print("yiyecek aldım")
            oyuncum.yiyecek_al_ve_ye()
            self.gameStateManager.set_state("done")

        if icecek_button.draw(screen):
            print("icecek aldım")
            oyuncum.icecek_al_ve_ye()
            self.gameStateManager.set_state("done")

        if sarki_button.draw(screen):
            print("sarkı söyledim")
            oyuncum.cal_ve_sarki_soyle()
            self.gameStateManager.set_state("done")

class Kamp_alani:
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        bg = pygame.transform.scale(pygame.image.load("backgrounds/kamp_alani.jpg"), (ekran_en, ekran_boy))
        self.display.blit(bg, (0, 0))

        if sarki_button.draw(screen):
            oyuncum.sarkı_soyle()
            self.gameStateManager.set_state("done")
        if banyo_button.draw(screen):
            oyuncum.yıkanma()
            self.gameStateManager.set_state("done")
        if uyku_button.draw(screen):
            oyuncum.uyu()
            self.gameStateManager.set_state("done")
class Macera:
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        bg = pygame.transform.scale(pygame.image.load("backgrounds/macera.jpg"), (ekran_en, ekran_boy))
        self.display.blit(bg, (0, 0))

        if av_button.draw(screen):


            if bitki_bulma_ihtimal:
                oyuncum.can = min(100, oyuncum.can + 10)
            if meyve_bulma_ihtimal:
                oyuncum.can = min(100, oyuncum.can + 20)
            if av_bulma_ihtimal:
                oyuncum.tokluk=min(100, oyuncum.can + 50)

            self.gameStateManager.set_state("av_topla")

        if orman_button.draw(screen):
            #oyuncum.orman_kesif()

            global haydut_kolay
            haydut_kolay=Karakter(50, random.randint(1, 5), random.randint(1, 5), random.randint(1, 5))

            self.gameStateManager.set_state("emin_misin")

        if kayalik_button.draw(screen):
            #oyuncum.kayalik_kesfi()

            global haydut_orta
            haydut_orta = Karakter(70, random.randint(6, 10), random.randint(6, 10), random.randint(6, 10))

            self.gameStateManager.set_state("emin_misin2")

        if vadi_button.draw(screen):
            #oyuncum.vadi_gez()

            global haydut_zor
            haydut_zor = Karakter(90, random.randint(11, 15), random.randint(11, 15), random.randint(11, 15))
            self.gameStateManager.set_state("emin_misin3")

class Fight:
    #easy mod için
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        #self.haydut_kolay=Karakter(50,random.randint(1,5),random.randint(1,5),random.randint(1,5))
        screen.blit(fight_scene,(0,0))
        screen.blit(haydut_easy,(50,ekran_boy-haydut_easy.get_height()))
        screen.blit(main_char, (650, ekran_boy-main_char.get_height()))

        draw_text(f"DÜŞMAN GÜCÜ: {haydut_kolay.guc}", text_font3, "white", 10, 10)
        draw_text(f"DÜŞMAN DAYANIKLILIĞI: {haydut_kolay.dayaniklilik}", text_font3, "white", 10, 40)
        draw_text(f"DÜŞMAN ÇEVİKLİLİĞİ: {haydut_kolay.ceviklik}", text_font3, "white", 10, 70)
        draw_text(f"DÜŞMAN CANI: {haydut_kolay.can}", text_font, "white", 100,200)
        draw_text(f"GÜÇ: {oyuncum.guc}", text_font3, "white", 700, 10)
        draw_text(f"DAYANIKLILIK: {oyuncum.dayaniklilik}", text_font3, "white", 700, 40)
        draw_text(f"ÇEVİKLİLİK: {oyuncum.ceviklik}", text_font3, "white", 700, 70)
        draw_text(f"CAN: {oyuncum.can:.2f}", text_font, "white", 700, 200)

        turn = True
        alinan_hasar = (haydut_kolay.guc * 4) - ((haydut_kolay.guc * 4) * (4 * oyuncum.dayaniklilik / 100) - 1)
        rakibe_verilen_hasar=(4*oyuncum.guc)- ((oyuncum.guc * 4) * (4 * haydut_kolay.dayaniklilik / 100) - 1)

        if turn == True:
            if attack_button.draw(screen):
                haydut_kolay.can -= rakibe_verilen_hasar
                turn = False
            if kacma_button.draw(screen):
                if random.randint(2*oyuncum.ceviklik,100)>=50:
                    turn = False
                elif random.randint(2*oyuncum.ceviklik,100)<50:
                    self.gameStateManager.set_state("town")
                    turn = False


        if turn == False:
            oyuncum.can -= alinan_hasar
            turn = True


        if haydut_kolay.can<=0:
            oyuncum.orman_kesif()
            self.gameStateManager.set_state("victory")

        if oyuncum.can <= 0:
            self.gameStateManager.set_state("defeat")
            screen2 = pygame.display.set_mode((1000, 700))
            run = True
            while run:
                screen2.fill((202, 228, 241))
                screen.blit(defeat_bg, (0, 0))
                draw_text("PRESS SPACE TO CLOSE",text_font,"white",350,350)
                # event handler
                for event in pygame.event.get():
                    # quit game
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        run = False
                    if keys[pygame.K_SPACE]:
                        run = False

                pygame.display.update()

            pygame.quit()
class Fight2:
    #mid mod için
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        #arka fon görseller
        screen.blit(fight_scene2,(0,0))
        screen.blit(haydut_mid,(50,ekran_boy-haydut_mid.get_height()))
        screen.blit(main_char, (650, ekran_boy-main_char.get_height()))
        #karakter özellikleri
        draw_text(f"DÜŞMAN GÜCÜ: {haydut_orta.guc}", text_font3, "white", 10, 10)
        draw_text(f"DÜŞMAN DAYANIKLILIĞI: {haydut_orta.dayaniklilik}", text_font3, "white", 10, 40)
        draw_text(f"DÜŞMAN ÇEVİKLİLİĞİ: {haydut_orta.ceviklik}", text_font3, "white", 10, 70)
        draw_text(f"DÜŞMAN CANI: {haydut_orta.can}", text_font, "white", 100, 200)

        draw_text(f"GÜÇ: {oyuncum.guc}", text_font3, "white", 700, 10)
        draw_text(f"DAYANIKLILIK: {oyuncum.dayaniklilik}", text_font3, "white", 700, 40)
        draw_text(f"ÇEVİKLİLİK: {oyuncum.ceviklik}", text_font3, "white", 700, 70)
        draw_text(f"CAN: {oyuncum.can:.2f}", text_font, "white", 700, 200)

        alinan_hasar=(haydut_orta.guc*4)-((haydut_orta.guc*4)*(4*oyuncum.dayaniklilik/100)-1)
        rakibe_verilen_hasar=(4*oyuncum.guc)- ((oyuncum.guc * 4) * (4 * haydut_orta.dayaniklilik / 100) - 1)
        turn=True

        if turn==True:
            if attack_button.draw(screen):
                haydut_orta.can -= rakibe_verilen_hasar
                turn = False
            if kacma_button.draw(screen):
                if random.randint(2 * oyuncum.ceviklik, 100) >= 50:
                    turn = False
                elif random.randint(2 * oyuncum.ceviklik, 100) < 50:
                    self.gameStateManager.set_state("town")
                    turn = False


        if turn==False:
            oyuncum.can-=alinan_hasar
            turn=True


        if haydut_orta.can<=0:
            oyuncum.kayalik_kesfi()
            self.gameStateManager.set_state("victory")

        if oyuncum.can<=0:
            self.gameStateManager.set_state("defeat")
            screen2=pygame.display.set_mode((1000,700))
            run = True
            while run:
                screen2.fill((202, 228, 241))
                screen.blit(defeat_bg,(0,0))
                draw_text("PRESS SPACE TO CLOSE", text_font, "white", 350, 350)
                # event handler
                for event in pygame.event.get():
                    # quit game
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        run = False
                    if keys[pygame.K_SPACE]:
                        run=False


                pygame.display.update()

            pygame.quit()
class Fight3:
    #zor mod için
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        screen.blit(fight_scene3,(0,0))
        screen.blit(haydut_hard,(-20,ekran_boy-haydut_hard.get_height()))
        screen.blit(main_char, (650, ekran_boy-main_char.get_height()))
        draw_text(f"DÜŞMAN GÜCÜ: {haydut_zor.guc}", text_font3, "white", 10, 10)
        draw_text(f"DÜŞMAN DAYANIKLILIĞI: {haydut_zor.dayaniklilik}", text_font3, "white", 10, 40)
        draw_text(f"DÜŞMAN ÇEVİKLİLİĞİ: {haydut_zor.ceviklik}", text_font3, "white", 10, 70)
        draw_text(f"DÜŞMAN CANI: {haydut_zor.can}", text_font, "white", 100, 200)
        draw_text(f"GÜÇ: {oyuncum.guc}", text_font3, "white", 700, 10)
        draw_text(f"DAYANIKLILIK: {oyuncum.dayaniklilik}", text_font3, "white", 700, 40)
        draw_text(f"ÇEVİKLİLİK: {oyuncum.ceviklik}", text_font3, "white", 700, 70)
        draw_text(f"CAN: {oyuncum.can:.2f}", text_font, "white", 700, 200)

        alinan_hasar = (haydut_zor.guc * 4) - ((haydut_zor.guc * 4) * (4 * oyuncum.dayaniklilik / 100) - 1)
        rakibe_verilen_hasar=(4*oyuncum.guc)- ((oyuncum.guc * 4) * (4 * haydut_zor.dayaniklilik / 100) - 1)
        turn = True

        if turn == True:
            if attack_button.draw(screen):
                haydut_zor.can -= rakibe_verilen_hasar
                turn = False
            if kacma_button.draw(screen):
                if random.randint(2 * oyuncum.ceviklik, 100) >= 50:
                    turn = False
                elif random.randint(2 * oyuncum.ceviklik, 100) < 50:
                    self.gameStateManager.set_state("town")
                    turn = False

        if turn == False:
            oyuncum.can -= alinan_hasar
            turn = True


        if haydut_zor.can<=0:
            oyuncum.vadi_gez()
            self.gameStateManager.set_state("victory")

        if oyuncum.can <= 0:
            self.gameStateManager.set_state("defeat")

            screen2 = pygame.display.set_mode((1000, 700))
            run = True
            while run:
                screen2.fill((202, 228, 241))
                screen.blit(defeat_bg, (0, 0))
                draw_text("PRESS SPACE TO CLOSE", text_font, "white", 350, 350)
                # event handler
                for event in pygame.event.get():
                    # quit game
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        run = False
                    if keys[pygame.K_SPACE]:
                        run = False

                pygame.display.update()

            pygame.quit()

class AvVeToplama:
    #zor mod için
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        screen.blit(av_ve_topla,(0,0))
        pygame.draw.rect(screen, (222, 184, 135), (330, 100, 350, 400))
        draw_text("       BULUNANLAR:",text_font,"white",320,130)

        if bitki_bulma_ihtimal==True:
            draw_text("           CAN +10", text_font, "white", 300, 160)
        if meyve_bulma_ihtimal==True:
            draw_text("           TOKLUK +20", text_font, "white", 300, 220)
        if av_bulma_ihtimal==True:
            draw_text("           TOKLUK +50", text_font, "white", 300, 270)
        elif meyve_bulma_ihtimal==False and bitki_bulma_ihtimal==False and av_bulma_ihtimal==False:
             draw_text(f"           BAŞARISIZ", text_font, "white", 300, 300)

        if very_ok_button.draw(screen):
            self.gameStateManager.set_state("town")

#menü butonları

class Menu:
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        self.display.fill("lightyellow")
        screen.blit(menu_bg, (50, -110))

        if ozellikler_button.draw(screen):
            print(oyuncum)
            self.gameStateManager.set_state("showcase")
        if town_button.draw(screen):
            self.gameStateManager.set_state("town")
        if kamp_alani_button1.draw(screen):
            self.gameStateManager.set_state("kamp_alani")
        if han_button1.draw(screen):
            self.gameStateManager.set_state("han")
        if sifahane_button1.draw(screen):
            self.gameStateManager.set_state("sifahane")
        if macera_button1.draw(screen):
            self.gameStateManager.set_state("macera")
        if exit_button.draw(screen):
            self.gameStateManager.set_state("exit_ekrani")

class Level_atla:
    def __init__(self,display,gameStateManager):
        self.display=display
        self.gameStateManager=gameStateManager
    def run(self):
        self.display.fill("lightblue")
        screen.blit(tablo,(-20,100))
        screen.blit(tablo, (250,100))
        screen.blit(tablo, (500,100))

        screen.blit(tablo, (100,350))
        screen.blit(tablo, (350,350))


        draw_text(f"Kalan Hakkın:{oyuncum.xp_puan}",text_font,"red",400,600)

        if oyuncum.tecrube == 100:
            if oyuncum.xp_puan >0:
                draw_text("Hangi Becerileri Geliştirmek İstersin?", text_font2, (150, 155, 155), 150, 20)

                if strenght_button.draw(screen):
                    oyuncum.guc = min(25,oyuncum.guc + 1)
                    oyuncum.xp_puan -= 1

                if agility_button.draw(screen):
                    oyuncum.dayaniklilik = min(25, oyuncum.dayaniklilik + 1)
                    oyuncum.xp_puan -= 1

                if charisma_button.draw(screen):
                    oyuncum.karizma = min(25, oyuncum.karizma + 1)

                    oyuncum.xp_puan -= 1

                if gathering_button.draw(screen):
                    oyuncum.toplayıcılık = min(25, oyuncum.toplayıcılık + 1)
                    oyuncum.xp_puan -= 1

                if resist_button.draw(screen):
                    oyuncum.dayaniklilik = min(25, oyuncum.dayaniklilik + 1)
                    oyuncum.xp_puan -= 1

                # elif sec==5:
                # self.toplayıcılık+=1

                # else:
                # print("yanlış giriş ")
                # self.xp_puan-=1
            else:
                #if oyuncum.tecrube==0:
                oyuncum.seviye +=1

                oyuncum.tecrube=0
                self.gameStateManager.set_state("done")

        else:
            self.gameStateManager.set_state("no_xp")

class HowToPlay:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        self.display.fill((150,30,10))

        pygame.draw.rect(screen, (0, 150, 150), (200, 100, 150, 150))

class Showcase:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager


    def run(self):
        self.display.fill("lightpink")
        line=600#x
        col=150#y
        line2 = 150#x
        col2= 150#y
        multiply=40


        showcase_text_color=(0,0,0)
        screen.blit(showcase,(0,0))

        draw_text(f"*İSİM: {oyuncum.name}",text_font,showcase_text_color,line2,col2-multiply)
        draw_text(f"*CALGI: {oyuncum.calgi}", text_font, showcase_text_color, line2,col2)

        draw_text("Temel nitelikler",text_font,showcase_text_color,line2,col2+multiply*1)
        draw_text(f"*CAN: {oyuncum.can:.2f}", text_font, showcase_text_color, line2, col2+multiply*2)
        draw_text(f"*TOKLUK: {oyuncum.tokluk}", text_font, showcase_text_color, line2, col2+multiply*3)
        draw_text(f"*HİJYEN: {oyuncum.hijyen}", text_font, showcase_text_color, line2, col2+multiply*4)
        draw_text(f"*EGLENCE: {oyuncum.eglence}", text_font, showcase_text_color, line2, col2+multiply*5)
        draw_text(f"*UYKUSUZLUK: {oyuncum.uykusuzluk}", text_font, showcase_text_color, line2, col2+multiply*6)

        draw_text("Beceriler",text_font,showcase_text_color,line,col+multiply*1)
        draw_text(f"*GUC: {oyuncum.guc}", text_font, showcase_text_color, line, col+multiply*2)
        draw_text(f"*CEVİKLİK: {oyuncum.ceviklik}", text_font, showcase_text_color, line, col+multiply*3)
        draw_text(f"*DAYANIKLILIK: {oyuncum.dayaniklilik}", text_font, showcase_text_color, line, col+multiply*4)
        draw_text(f"*KARİZMA: {oyuncum.karizma}", text_font, showcase_text_color, line, col+multiply*5)
        draw_text(f"*TOPLAYICILIK: {oyuncum.toplayıcılık}", text_font, showcase_text_color, line, col+multiply*6)

        if very_ok_button.draw(screen):
            self.gameStateManager.set_state("town")

class Done:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        ok_button.draw(screen)
        if very_ok_button.draw(screen):
            self.gameStateManager.set_state("town")

class NO_XP:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        no_xp_button.draw(screen)
        if very_ok_button.draw(screen):
            self.gameStateManager.set_state("town")

class EminMisin:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        screen.fill((30,0,0))
        screen.blit(haydut_easy,(10,100))

        if haydut_kolay.ceviklik>oyuncum.ceviklik:
            draw_text("   Savaşa  ",text_font5,"white",680,200)
            draw_text("   Düşman ", text_font5, "white", 680, 250)
            draw_text("Başlayacaktır", text_font5, "white", 680, 300)
        if haydut_kolay.ceviklik<oyuncum.ceviklik:
            draw_text("Savaşa Sen Başlayacaksın",text_font,"white",400,100)
        if haydut_kolay.ceviklik==oyuncum.ceviklik:
            draw_text("Savaş Rastgele Başlayacaktır",text_font,"white",400,100)


        draw_text(f"DÜŞMAN CAN: {haydut_kolay.can:.2f}", text_font, "white", 400, 400)
        draw_text(f"DÜŞMAN GUC: {haydut_kolay.guc}", text_font,"white", 400, 450)
        draw_text(f"DÜŞMAN CEVİKLİK: {haydut_kolay.ceviklik}", text_font, "white", 400,500)
        draw_text(f"DÜŞMAN DAYANIKLILIK: {haydut_kolay.dayaniklilik}", text_font, "white", 400,550)

        if start_fight_button.draw(screen):
            if haydut_kolay.ceviklik > oyuncum.ceviklik:
                oyuncum.can -= haydut_kolay.guc * 4
            if random.randint(1, 3) == 1:
                if haydut_kolay.ceviklik == oyuncum.ceviklik:
                    oyuncum.can -= haydut_kolay.guc * 4
            self.gameStateManager.set_state("fight")

class EminMisin2:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        screen.fill((30,0,0))
        screen.blit(haydut_mid, (10, 100))

        if haydut_orta.ceviklik>oyuncum.ceviklik:
            draw_text("   Savaşa  ",text_font5,"white",680,200)
            draw_text("   Düşman ", text_font5, "white", 680, 250)
            draw_text("Başlayacaktır", text_font5, "white", 680, 300)

        if haydut_orta.ceviklik<oyuncum.ceviklik:
            draw_text("Savaşa Sen Başlayacaksın",text_font,"white",400,100)
        if haydut_orta.ceviklik==oyuncum.ceviklik:
            draw_text("Savaş Rastgele Başlayacaktır",text_font,"white",400,100)


        draw_text(f"DÜŞMAN CAN: {haydut_orta.can:.2f}", text_font, "white", 400, 400)
        draw_text(f"DÜŞMAN GUC: {haydut_orta.guc}", text_font,"white", 400, 450)
        draw_text(f"DÜŞMAN CEVİKLİK: {haydut_orta.ceviklik}", text_font, "white", 400,500)
        draw_text(f"DÜŞMAN DAYANIKLILIK: {haydut_orta.dayaniklilik}", text_font, "white", 400,550)

        if start_fight_button.draw(screen):
            if haydut_orta.ceviklik > oyuncum.ceviklik:
                oyuncum.can -= haydut_orta.guc * 4
            if random.randint(1,3)==1:
                if haydut_orta.ceviklik == oyuncum.ceviklik:
                    oyuncum.can -= haydut_orta.guc * 4

            self.gameStateManager.set_state("fight2")

class EminMisin3:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        screen.fill((30,0,0))
        screen.blit(haydut_hard, (-50, 100))

        if haydut_zor.ceviklik>oyuncum.ceviklik:
            draw_text("   Savaşa  ",text_font5,"white",680,200)
            draw_text("   Düşman ", text_font5, "white", 680, 250)
            draw_text("Başlayacaktır", text_font5, "white", 680, 300)

        if haydut_zor.ceviklik<oyuncum.ceviklik:
            draw_text("Savaşa Sen Başlayacaksın",text_font,"white",400,100)
        if haydut_zor.ceviklik==oyuncum.ceviklik:
            draw_text("Savaş Rastgele Başlayacaktır",text_font,"white",400,100)

        draw_text(f"DÜŞMAN CAN: {haydut_zor.can}", text_font, "white", 400, 400)
        draw_text(f"DÜŞMAN GUC: {haydut_zor.guc}", text_font,"white", 400, 450)
        draw_text(f"DÜŞMAN CEVİKLİK: {haydut_zor.ceviklik}", text_font, "white", 400,500)
        draw_text(f"DÜŞMAN DAYANIKLILIK: {haydut_zor.dayaniklilik}", text_font, "white", 400,550)

        if start_fight_button.draw(screen):
            if haydut_zor.ceviklik > oyuncum.ceviklik:
                oyuncum.can -= haydut_zor.guc * 4
            if random.randint(1, 3) == 1:
                if haydut_zor.ceviklik == oyuncum.ceviklik:
                    oyuncum.can -= haydut_zor.guc * 4

            self.gameStateManager.set_state("fight3")

class Defeat:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        screen.blit(defeat_bg, (0, 0))

        anahtar = pygame.key.get_pressed()
        if anahtar[pygame.K_SPACE]:
            pygame.quit()
            sys.exit()

class Victory:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        screen.blit(victory_bg, (0, 0))

        anahtar = pygame.key.get_pressed()
        if anahtar[pygame.K_SPACE]:
            self.gameStateManager.set_state("town")

class ExitEkranı:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        screen.fill("lightyellow")
        draw_text("OYUNDAN ÇIKMAK İSTEDİĞİNE ",text_font5,"black",190,200)
        draw_text("EMİN MİSİN?", text_font5, "black", 350, 250)
        if yes_button.draw(screen):
            pygame.quit()
            sys.exit()
        if no_button.draw(screen):
            self.gameStateManager.set_state("town")

class SeviyeAtlaUyari:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        screen.blit(tablo_yatay,(120,70))
        draw_text("      seviye atlaman lazım".upper(),text_font,"white",250,120)
        draw_text("şimdi seviye atlamazsan 10xp kaydeceksin".upper(),text_font,"white",200,170)
        draw_text("      seviye atlayacak mısın?".upper(), text_font, "white", 250, 220)

        if yes_button.draw(screen):
            if oyuncum.tecrube == 100:
                # oyuncum.xp_puan+=3#bu puanlar birikebilirse olur bu
                oyuncum.xp_puan = min(3, oyuncum.xp_puan + 3)
                self.gameStateManager.set_state("level_atla")
            else:
                print("yeteri tecrübe yok")  # buraya yetersiz işareti getir
                self.gameStateManager.set_state("no_xp")
        if no_button.draw(screen):
            oyuncum.tecrube-=10
            self.gameStateManager.set_state("town")

class GameStateManager:
    def __init__(self,currentState):
        self.currentState=currentState
    def get_state(self):
        return self.currentState
    def set_state(self,state):
        self.currentState=state



if __name__=="__main__":

    oyuncum=Oyuncu("","")
    bitki_bulma_ihtimal =random.randint(1, 100) <= oyuncum.toplayıcılık * 4
    meyve_bulma_ihtimal =random.randint(1, 100) <= oyuncum.toplayıcılık * 4
    av_bulma_ihtimal = random.randint(1, 100) <= oyuncum.toplayıcılık * 2

    game=Game()
    game.run()