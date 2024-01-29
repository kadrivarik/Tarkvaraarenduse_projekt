import pygame # impordin  pygame mooduli
pygame.init()  # kutsun ellu mooduli

screen=pygame.display.set_mode([300,300])  # määran ekraani suuruse
pygame.display.set_caption("Valgusfoor - Kadri Varik")  # loon ekraani pealkirja

pygame.draw.circle(screen, [255, 0, 0], [150,60], 40, 0)   # Punane ring
pygame.draw.circle(screen, [255, 255, 0], [150,145], 40, 0)  # kollane ring
pygame.draw.circle(screen, [0, 255, 1], [150,230], 40, 0) # roheline ring
pygame.draw.rect(screen, [134, 132, 133], [100, 10, 100, 270], 2)  # hall kast ümber
pygame.display.flip()  # värskendab ekraanil kuvatava


# Hoiab ekraani avatuna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False   #