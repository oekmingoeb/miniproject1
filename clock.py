import pygame
import math
from datetime import datetime
import sys

# Initialisering
pygame.init()

width, height = 400, 400
center_x, center_y = width // 2, width // 2
clock_radius = width // 2
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
last_second = datetime.now().second
pygame.display.set_caption(":D")

# Farver
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

############### Load mp3 #############################################
pygame.mixer.music.load("among.mp3")

def start_music():
    pygame.mixer.music.play()

############### Load Per #############################################

Per_original = pygame.image.load(
    "Per.png"
).convert_alpha()

# pers næses position i OG-billedet
nose_original_x = 900
nose_original_y = 500

###########################################################################
############### main loop #############################################

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fyld med hvid så den gamle streg slettes
    screen.fill(white)
    #cirkel i midten
    pygame.draw.circle(screen, black, (center_x, center_y), radius=7)

    # hent sekunder og mikrosekunder til beregningen
    now = datetime.now()

############### forstørrer Per hvert 15. sekund #############################################

    if now.second % 15 == 0:
        scale = 1
    else:
        scale = 0.3

    Per = pygame.transform.smoothscale(
        Per_original,
        (
            int(Per_original.get_width() * scale),
            int(Per_original.get_height() * scale)
        )
    )
############### pers næse på viserne #############################################

    nose_x = int(nose_original_x * scale)
    nose_y = int(nose_original_y * scale)

    Per_x = center_x - nose_x
    Per_y = center_y - nose_y

############################################################

    second = now.second + now.microsecond / 1_000_000
    angle = math.radians(second * 6 - 90)


    #music
    if now.second != last_second:
        last_second = now.second

        if now.second % 15 == 0:
            start_music()
            

    #Per
    screen.fill(white)

    screen.blit(Per, (Per_x, Per_y))

############### tegner viserne #############################################
    # Linjens længde ud fra centrum
    line_length = 150

    # beregner slutpunktet (x, y) for linjen
    end_x = center_x + math.cos(angle) * line_length
    end_y = center_y + math.sin(angle) * line_length

    # tegner den røde linje fra centrum til slutpunktet
    pygame.draw.line(screen, black, (center_x, center_y), (end_x, end_y), 3)
    pygame.draw.line(screen, red, (center_x, center_y), (end_x, end_y), 3)


    #minut viser
    # beregn vinklen (-90 grader for at starte i toppen kl. 12)
    minute = now.minute + second / 60
    angle = math.radians(minute * 6 - 90)

    # linjens længde ud fra centrum
    minute_line_length = 150

    # beregn slutpunktet (x, y) for linjen
    end_x = center_x + math.cos(angle) * minute_line_length
    end_y = center_y + math.sin(angle) * minute_line_length

    # tegner den enkelte sorte linje fra centrum til slutpunktet
    pygame.draw.line(screen, black, (center_x, center_y), (end_x, end_y), 6)

    #time viser
    hour = now.hour % 12 + minute / 60
    angle = math.radians(hour * 30 - 90)

    # linjens længde ud fra centrum
    hour_line_length = 100

    # beregner slutpunktet (x, y) for linjen
    end_x = center_x + math.cos(angle) * hour_line_length
    end_y = center_y + math.sin(angle) * hour_line_length

    # tegner den sorte linje fra centrum til slutpunktet
    pygame.draw.line(screen, black, (center_x, center_y), (end_x, end_y), 6)

    #tegn 12 markører
    for i in range(12):
        # 360 degrees / 12 hours = 30 degrees
        angle = math.radians(i * 30 - 90)

        start_x = center_x + math.cos(angle) * (clock_radius - 15)
        start_y = center_y + math.sin(angle) * (clock_radius - 15)

        end_x = center_x + math.cos(angle) * clock_radius
        end_y = center_y + math.sin(angle) * clock_radius

        pygame.draw.line(
            screen,
            red,
            (start_x, start_y),
            (end_x, end_y),
            4
        )

    pygame.display.flip()
    clock.tick(60)  # 60 FPS 



pygame.quit()
sys.exit()
