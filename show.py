import os
import time

device = os.getenv('DEVICE', 'unknown device')

f = open('update_count.txt', 'r')
updates = int(f.readline())

print 'Device type: %s' % device
print 'Hello, you are the user who pushed update #%d' % updates
print 'Welcome to ELCE'

if device == 'raspberrypi':
    import pygame
    import signal

    def handler():
        raise KeyboardInterrupt

    signal.signal(signal.SIGALRM, handler)

    WHITE = (255,255,255)

    os.putenv('SDL_FBDEV', '/dev/fb1')

    pygame.init()
    pygame.mouse.set_visible(False)
    signal.alarm(1)
    display = pygame.display.set_mode((240, 320))

    font_big = pygame.font.Font(None, 100)
    font_small = pygame.font.Font(None, 40)

    surface = font_big.render('#%d' % updates, True, WHITE)
    display.blit(surface, surface.get_rect(center=(120, 220)))

    surface = font_small.render('Welcome to DockerCon', True, WHITE)
    display.blit(surface, surface.get_rect(center=(120, 280)))

    image = pygame.image.load('/usr/src/app/image.jpg')
    display.blit(pygame.transform.smoothscale(image, (240, 160)), (0, 0))

    pygame.display.update()

# Sleep for a year
time.sleep(60 * 60 * 24 * 365)
