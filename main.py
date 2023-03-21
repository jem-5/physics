import math, pygame, sys

def move_ball(time_passed):
    # x_pos = (1 - math.exp(- viscosity * time_passed)) * (init_vel * math.cos(math.radians(angle))) / viscosity
    # y_pos = -GRAVITY * time_passed / viscosity + (1/viscosity) * ((init_vel * math.sin(math.radians(angle))) + height + GRAVITY / viscosity) * (1 - math.exp(-viscosity * time_passed))
    x_pos = ((init_vel * math.cos((math.radians(angle)))) * time_passed)
    y_pos = (height + init_vel * math.sin(math.radians(angle)) * time_passed - 0.5 * GRAVITY * time_passed ** 2)
    return x_pos, y_pos

def create_button(x,y,w,h,text):
    text_surf = font2.render(text, True, WHITE)
    button_rect = pygame.Rect(x,y,w,h)
    text_rect = text_surf.get_rect(center=(button_rect.center))
    button = {
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': GREEN}
    return button

def draw_button(button, screen):
    pygame.draw.rect(screen,button['color'],button['rect'])
    screen.blit(button['text'], button['text rect'])

def DisplayStats():
    time_flight = round((init_vel * math.sin(math.radians(angle)) + math.sqrt((init_vel * math.sin(math.radians(angle)))** 2 + 2 * GRAVITY * height))/GRAVITY, 2)
    max_height = round(height + ((init_vel) ** 2 * (math.sin(math.radians(angle))) ** 2) / (2 * GRAVITY), 2)
    horizontal_range = round(((init_vel) * math.cos(math.radians(angle))/ GRAVITY) * (init_vel * math.sin(math.radians(angle)) + math.sqrt(init_vel**2 * math.sin(math.radians(angle))**2+2 * GRAVITY * height)), 2)
    stats= ("Time of flight: " + str(time_flight) + "  "
    "Max height: " + str(max_height) + "  "
    "Horizontal range: " + str(horizontal_range))
    stats_display = font.render(str(stats), True, BLACK)
    screen.blit(stats_display, (20, 20))

def PrintSettings(init_vel, angle, height):
    settings_vel = font.render(str("Initial Velocity: " + str(init_vel)), True, BLACK)
    settings_ang = font.render(str("Launch Angle: " + str(angle)), True, BLACK)
    settings_hei = font.render(str("Initial Height: " + str(height)), True, BLACK)
    # settings_res = font.render(str("Air Resistance: " + str(round(viscosity, 2))), True, BLACK)

    screen.blit(settings_vel, (40, 60))
    screen.blit(settings_ang, (225, 60))
    screen.blit(settings_hei, (475, 60))
    # screen.blit(settings_res, (675, 60))

pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 562
GRAVITY = 9.8
# viscosity = 0.45
FPS = pygame.time.Clock()
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
FLOOR = 0.95*SCREEN_HEIGHT
init_vel = 90
angle = 60
height = 100
time_passed = 0
font = pygame.font.Font(None, 23)
font2 = pygame.font.Font(None, 40)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Welcome to my physics program!")
bg = pygame.image.load(r'field.jpg')
ballimage = pygame.image.load(r'ball.png').convert_alpha()

button1 = create_button(50,90,30,30, '-')
button2 = create_button(100,90,30,30, '+')
button3 = create_button(250,90,30,30, '-')
button4 = create_button(300,90,30,30, '+')
button5 = create_button(500,90,30,30, '-')
button6 = create_button(550,90,30,30, '+')
# button7 = create_button(700,90,30,30, '-')
# button8 = create_button(750,90,30,30, '+')
buttons = [button1,button2,button3,button4,button5,button6]

while True:
    screen.blit(bg, (0,0))
    x_pos, y_pos = move_ball(time_passed)
    screen.blit(ballimage,(x_pos, (SCREEN_HEIGHT - y_pos)))
    time_passed += 1
    for button in buttons:
        draw_button(button,screen)
    DisplayStats()
    PrintSettings(init_vel,angle,height)
    pygame.display.flip()
    if x_pos > SCREEN_WIDTH or y_pos < 0:
        time_passed = 0
        x_pos, y_pos = move_ball(time_passed)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if button1['rect'].collidepoint(pos):
                init_vel -= 15
            if button2['rect'].collidepoint(pos):
                init_vel += 15
            if button3['rect'].collidepoint(pos):
                angle -= 10
            if button4['rect'].collidepoint(pos):
                angle += 10
            if button5['rect'].collidepoint(pos):
                height -= 50
            if button6['rect'].collidepoint(pos):
                height += 50
            # if button7['rect'].collidepoint(pos):
            #     viscosity -= 0.05
            # if button8['rect'].collidepoint(pos):
            #     viscosity += 0.05
    FPS.tick(20)
