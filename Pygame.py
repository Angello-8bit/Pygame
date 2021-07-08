import pygame, sys, random

def draw_surface():
    screen.blit(bg_surface,(bg_surface_x_pos,0))
    screen.blit(bg_surface,(bg_surface_x_pos + 1200,0))

def create_pipe():
    random_pipe = random.choice(pipe_height)
    new_pipe = pipe_surface.get_rect(midtop = (1000, random_pipe))
    other_pipe = pipe_surface.get_rect(midbottom= (1000, random_pipe - 300))
    return new_pipe , other_pipe

def move_pipes(pipes):
    for i in pipes:
        i.centerx -= 20
    return pipes

def draw_pipes(pipes):
    for i in pipes:
        if i.bottom >= 1000:
            screen.blit(pipe_surface, i)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False,True)
            screen.blit(flip_pipe, i)

def check_collision(pipes):
    for i in pipes:
        if dog_rect.colliderect(i):
            return False
    if dog_rect.top <= -100 or dog_rect.bottom >= 1000:
        return False
    else:
        return True

def rotate_dog(dog):
    new_dog = pygame.transform.rotozoom(dog, -dog_movemnt * 3,1)
    return new_dog

pygame.init()
screen = pygame.display.set_mode((600, 725))
clock = pygame.time.Clock()

# Game Variable
gravity = 0.22
dog_movemnt = 0 
game_active = True

bg_surface = pygame.image.load('C:/Desktop/Pygames/pictures/bg_1.jpg').convert()
# bg_surface = pygame.transform.scale2x(bg_surface)
bg_surface_x_pos = 0 
draw_surface

# animation 
# dog_down = pygame.transfrom.scale2x(pygame.image.load('C:/Desktop/Pygames/pictures/dog_down.jpg').convert_alpha)
# dog_mid = pygame.transfrom.scale2x(pygame.image.load('C:/Desktop/Pygames/pictures/dog_mid.jpg').convert_alpha)
# dog_up = pygame.transfrom.scale2x(pygame.image.load('C:/Desktop/Pygames/pictures/dog_up.jpg').convert_alpha)
# dog_frames = [dog_down,dog_mid,dog_up]
# dog_index = 0 
# dog_surface = dog_frames[bird_index]
# dog_rect = dog_surface.get_rect(center = (100,512))

# DOGFLAP = pygame.USEREVENT + 1 
# pygame.time.set_timer(DOGFLAP, 200)

dog_surface = pygame.image.load('C:/Desktop/Pygames/chracters/dog_2.png').convert_alpha()
dog_surface = pygame.transform.scale2x(dog_surface)
dog_rect = dog_surface.get_rect(center = (100,360))


pipe_surface = pygame.image.load('C:/Desktop/Pygames/chracters/pipe-red.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400,600,800]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active :
                dog_movemnt = 0
                dog_movemnt -=10 
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                dog_rect.center = (100,360)
                dog_movemnt = 0       
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        # if event.type == DOGFLPA:
        #   if bird_index < 2:
        #    dog_index += 1
        #   else:
        #       dog_index = 0 
    bg_surface_x_pos += -1 # can also do (-=)
    draw_surface()
    if game_active:
        # Dog
        dog_movemnt += gravity
        rotated_dog = rotate_dog(dog_surface)
        dog_rect.centery += dog_movemnt
        screen.blit(rotated_dog, dog_rect)
        game_active = check_collision(pipe_list)

        #pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        if bg_surface_x_pos <= -1200:
            bg_surface_x_pos = 0

    pygame.display.update()
    clock.tick(60)