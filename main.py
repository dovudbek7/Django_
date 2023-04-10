import pygame
import random

# o'yin oynaash uchun funksiya
def oyna():
    pygame.init()

    # o'yin oynasining hajmi
    ekran_hajmi = (600, 400)
    ekran = pygame.display.set_mode(ekran_hajmi)
    pygame.display.set_caption("Futbol topi")

    # ranglar
    qora = (255, 0, 0)
    yashil = (0, 255, 0)

    # topning o'lchami va joylashuvi
    top_olchami = 25
    top_x, top_y = 300, 200

    # boshlanish tezligi
    tezlik = 5

    # rasmni yuklash
    futbol_topi = pygame.image.load("futbol_topi.png")

    # topni random x, y tomondagi holatga joylashtrish
    def topni_joylash():
        nonlocal top_x, top_y
        top_x = random.randint(0, ekran_hajmi[0] - top_olchami)
        top_y = random.randint(0, ekran_hajmi[1] - top_olchami)

    # o'yin davomida harakat qilish funksiyasi
    def harakat():
        nonlocal top_x, top_y, tezlik

        for hodisada in pygame.event.get():
            if hodisada.type == pygame.QUIT:
                quit()

        tugma = pygame.key.get_pressed()
        if tugma[pygame.K_UP]:
            top_y -= tezlik
        elif tugma[pygame.K_DOWN]:
            top_y += tezlik
        elif tugma[pygame.K_LEFT]:
            top_x -= tezlik
        elif tugma[pygame.K_RIGHT]:
            top_x += tezlik

        if top_x < 0:
            top_x = 0
        elif top_x > ekran_hajmi[0] - top_olchami:
            top_x = ekran_hajmi[0] - top_olchami
        elif top_y < 0:
            top_y = 0
        elif top_y > ekran_hajmi[1] - top_olchami:
            top_y = ekran_hajmi[1] - top_olchami

        # topni chizish
        ekran.fill(yashil)
       
