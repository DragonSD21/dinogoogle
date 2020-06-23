import pygame as pg
import os

import Backend.dinosaur as dino

DIC_PATH = os.path.abspath(os.path.dirname(__file__))

def loadImage(imageName):
    try:
        image = pg.image.load(DIC_PATH + imageName)
    except pg.error:
        print("Cannot load image: ", imageName)
        raise SystemExit
    return image, image.get_rect()

def animation(screen, TRex):
    screen.fill((255, 255, 255)) # preenche a tela com a cor branca
    screen.blit(TRex.image, [TRex.x, TRex.y])
    pg.display.update()

def render():
    pg.init()

    close = False
    isJump = False
    jumpCount = 10
    
    screen = pg.display.set_mode((1200, 600)) # largura / altura
    pg.display.set_caption("T-Rex Running")

    image, dimensions = loadImage("/assets/dino.png")
    imageSmall = pg.transform.scale(image, [72, 72])
    imageCut = imageSmall.subsurface([0, 0, 32, 32])

    # 443, 480, 514, 548, 582, 616, 651, 702, 751, 803, 850, 952
    imageAll, dimensionsAll = loadImage("/assets/imageGeneral.png")
    imageCactus = []
    imageCactus.append(imageAll.subsurface([443, 0, 37, 72]))
    imageCactus.append(imageAll.subsurface([480, 0, 34, 72]))
    imageCactus.append(imageAll.subsurface([514, 0, 34, 72]))
    imageCactus.append(imageAll.subsurface([548, 0, 34, 72]))
    imageCactus.append(imageAll.subsurface([582, 0, 34, 72]))
    imageCactus.append(imageAll.subsurface([616, 0, 35, 72]))
    imageCactus.append(imageAll.subsurface([651, 0, 51, 102]))
    imageCactus.append(imageAll.subsurface([702, 0, 49, 102]))
    imageCactus.append(imageAll.subsurface([751, 0, 52, 102]))
    imageCactus.append(imageAll.subsurface([803, 0, 47, 102]))
    imageCactus.append(imageAll.subsurface([850, 0, 102, 102]))

    TRex = dino.Dinosaur(0, 350, imageSmall)

    while close != True:
        pg.time.delay(20)
        # animation(screen, TRex)
        screen.fill((255, 255, 255)) # preenche a tela com a cor branca
        i = 0
        for cactu in imageCactus:
            screen.blit(cactu, [i,0])
            i += 20
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                close = True

        keys = pg.key.get_pressed()
        
        if keys[pg.K_ESCAPE]:
            close = True

        if keys[pg.K_UP]:
            isJump = True

        if isJump:
            if jumpCount >= -10:
                TRex.jump(jumpCount)
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False

    pg.quit()

render()
