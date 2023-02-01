import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption("GameGameGameGame")
    clock = pygame.time.Clock()

    sky_surface = pygame.image.load('graphics/sky_background.png')
    sky_surface = pygame.transform.scale(sky_surface, (800,300))

    ground_surface = pygame.image.load('graphics/ground.png').convert()
    ground_surface = pygame.transform.scale(ground_surface,(800,100))

    text_font = pygame.font.Font('Font/Pixeltype.ttf', 60)

    text_surface = text_font.render('Penguin Jumping Game', False, 'Black')
    #Penguin Sprite
    penguin_surface = pygame.image.load('graphics/penguin.png').convert_alpha()
    penguin_surface = pygame.transform.scale(penguin_surface, (100,100))
    #Snake Sprite
    snake_surface = pygame.image.load("graphics/snake.png").convert()
    snake_surface = pygame.transform.scale(snake_surface, (100,100))

    penguin_x = 0
    penguin_y = 250

    snake_x = 400
    snake_y = 250

    MOVE_UP = 220
    MOVE_DOWN = 300
    MOVE_MIDDLE = 250

    while True:
        for event in pygame.event.get():
            #Quit the game in case of closing it
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            #React to the keys inputs as they are pressed
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    if penguin_y == MOVE_MIDDLE:
                        penguin_y = MOVE_UP
                        print(1)
                    if penguin_y == MOVE_DOWN:
                        penguin_y = MOVE_MIDDLE
                        print(2)
                #FIX KEY DOWN
                if keys[pygame.K_DOWN]:
                    if penguin_y == MOVE_UP:
                        penguin_y = MOVE_MIDDLE
                        print(3)
                    if penguin_y == MOVE_MIDDLE:
                        penguin_y = MOVE_DOWN
                        print(4)
        
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
        #52:34

if __name__ == "__main__":
    main()