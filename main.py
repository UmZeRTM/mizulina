import pygame

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mizulina")
    clock = pygame.time.Clock()
    running = True

    square_size = 30
    STEP = 5
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    square_x2 = 0
    square_y2 = HEIGHT - square_size

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        square_x1 = mouse_x - square_size // 2
        square_y1 = mouse_y - square_size // 2

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, (square_x1, square_y1, square_size, square_size))
        pygame.draw.rect(screen, BLACK, (square_x2, square_y2, square_size, square_size))

        if square_x2 > WIDTH:
            square_x2 -= STEP
        else:
            square_x2 += STEP

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
