import pygame
from random import uniform, randint


def background():
    maze = pygame.image.load('grounds/space.jpg').convert()
    return maze


def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(loops=-1, start=0.0)


def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mizulina")
    clock = pygame.time.Clock()
    running = True

    pygame.mixer.init()
    play_music('sound/level_song.mp3')

    square_size = 50
    WHITE = (255, 255, 255)
    bullet = pygame.Surface((5, 10))
    bullet.fill((255, 0, 0))

    bullet_list = []
    bullet_speed = 5

    num_enemies = 7
    enemies_list = []
    for _ in range(num_enemies):
        enemies_list.append([randint(0, WIDTH - 50), randint(-100, -40), uniform(0.3, 0.5)])


    score = 0
    missed = 0

    enemy_image = pygame.image.load('skins/enemy.png')
    player_img = pygame.image.load('skins/v1_sprite.png')
    player_img = pygame.transform.scale(player_img, (square_size, square_size))

    background_img = background()

    square_x, square_y = 30, 30

    font = pygame.font.Font(None, 36)
    start_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_list.append([square_x, square_y])

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[2]:
            square_x = mouse_x - square_size // 2
            square_y = mouse_y - square_size // 2

        for enemy in enemies_list:
            enemy[1] += enemy[2]
            if enemy[1] > HEIGHT:
                missed += 1
                enemy[0] = randint(0, HEIGHT - 50)
                enemy[1] = randint(-100, HEIGHT -40)
                enemy[2] = uniform(0.3, 0.5)


        new_bullet = []
        for bull in bullet_list:
            bull[1] -= bullet_speed
            if bull[1] > 0:
                new_bullet.append(bull)
        bullet_list = new_bullet


        past_time = (pygame.time.get_ticks() - start_time) // 1000
        timer_text = font.render(f"{past_time} sec", True, WHITE)

        screen.blit(background_img, (0, 0))

        screen.blit(player_img, (square_x, square_y))

        screen.blit(timer_text, (10, 10))

        for enemy in enemies_list:
            screen.blit(enemy_image, (enemy[0], enemy[1]))

        for bull in bullet_list:
            screen.blit(bullet, (bull[0], bull[1]))


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
