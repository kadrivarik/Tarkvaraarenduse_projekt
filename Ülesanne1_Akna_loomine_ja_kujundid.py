import pygame # impordin  pygame mooduli
pygame.init()  # kutsun ellu mooduli

screen=pygame.display.set_mode([300,300])  # määran ekraani suuruse
pygame.display.set_caption("Lumemees - Kadri Varik")  # loon ekraani pealkirja

pygame.draw.circle(screen, [255, 255, 255], [150,75], 30, 0)   # Lumememmme pea , värv, asukoht x ja y teljel, palli suurus
pygame.draw.circle(screen, [0, 0, 0], [140,70], 5, 0)  # Lumememme vasak silm
pygame.draw.circle(screen, [0, 0, 0], [160,70], 5, 0) # Lumememme parem silm
pygame.draw.polygon(screen, [255, 0, 0], [[145,80],[155,80],[150,95],[145,80]], 0)  # Lumememme nina, värv, asukoht x ja  y telgede suhtes
pygame.draw.circle(screen, [255, 255, 255], [150,140], 40, 0)  # Lumememme keha
pygame.draw.circle(screen, [255, 255, 255], [150,225], 50, 0)  # lumememme kolma pall
pygame.display.flip()  # värskendab ekraanil kuvatava


# Hoiab ekraani avatuna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False   #