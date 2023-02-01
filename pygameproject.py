import pygame

def main():
    pygame.init()
    width = 100
    height = 200
    surface = pygame.Surface((width, height))

    screen = pygame.display.set_mode((800,400))
    
    pygame.display.set_caption("GameGameGameGame")
    clock = pygame.time.Clock()


    sky_surface = pygame.image.load('graphics/sky_background.png')
    sky_surface = pygame.transform.scale(sky_surface, (800,300))

    ground_surface = pygame.image.load('graphics/ground.png').convert()
    ground_surface = pygame.transform.scale(ground_surface,(800,100))

    text_font = pygame.font.Font('Font/Pixeltype.ttf', 60)

    text_surface = text_font.render('Penguin Jumping Game', False, 'Black')

    penguin_surface = pygame.image.load('graphics/penguin.png').convert_alpha()
    penguin_surface = pygame.transform.scale(penguin_surface, (100,100))

    snake_surface = pygame.image.load("graphics/snake.png").convert()
    snake_surface = pygame.transform.scale(snake_surface, (100,100))

    penguin_x = 0
    penguin_y = 250

    snake_x = 400
    snake_y = 250

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (300, 50))
        penguin_x += 1
        snake_x -= 4
        screen.blit(penguin_surface, (penguin_x, penguin_y ))
        screen.blit(snake_surface, (snake_x, snake_y))

        #Goes back if the snake goes out of the screen
        if snake_x == -100: snake_x = 800
        
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()