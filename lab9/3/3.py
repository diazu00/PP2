import pygame
pygame.init()

fps = 120
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 0
active_color = 'white'
active_shape = 'circle'

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paaint')
painting = []


def draw_menu():
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Draw buttons for brush types
    square_brush = pygame.draw.rect(screen, 'black', [250, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [260, 20, 30, 30])
    rt_brush = pygame.draw.rect(screen, 'black', [310, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(335, 20), (335, 50), (360, 50)])
    rhombus_brush = pygame.draw.rect(screen, 'black', [370, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(395, 20), (370, 35), (395, 50), (420, 35)])
    brush_type_list = [square_brush, rt_brush, rhombus_brush]

    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    brush_size_list = [xl_brush, l_brush, m_brush, s_brush]

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 60, 35, 25, 25])
    color_rect = [blue, red, green, white]

    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 255)]

    return brush_size_list, brush_type_list, color_rect, rgb_list


def draw_painting(paints):
    for paint in paints:
        color, position, size, shape = paint
        if shape == 'circle':
            pygame.draw.circle(screen, color, position, size)
        elif shape == 'square':
            pygame.draw.rect(screen, color, (position[0] - size // 2, position[1] - size // 2, size, size))
        elif shape == 'right_triangle':
            pygame.draw.polygon(screen, color, [position, (position[0], position[1] + size), (position[0] + size, position[1] + size)])
        elif shape == 'rhombus':
            pygame.draw.polygon(screen, color, [(position[0], position[1] - size // 2), (position[0] - size // 2, position[1]), (position[0], position[1] + size // 2), (position[0] + size // 2, position[1])])


run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if mouse[1] > 70:
        if active_shape == 'circle':
            pygame.draw.circle(screen, active_color, mouse, active_size)
        elif active_shape == 'square':
            pygame.draw.rect(screen, active_color, (mouse[0] - active_size // 2, mouse[1] - active_size // 2, active_size, active_size))
        elif active_shape == 'right_triangle':
            pygame.draw.polygon(screen, active_color, [mouse, (mouse[0], mouse[1] + active_size), (mouse[0] + active_size, mouse[1] + active_size)])
        elif active_shape == 'rhombus':
            pygame.draw.polygon(screen, active_color, [(mouse[0], mouse[1] - active_size // 2), (mouse[0] - active_size // 2, mouse[1]), (mouse[0], mouse[1] + active_size // 2), (mouse[0] + active_size // 2, mouse[1])])
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size, active_shape))
    draw_painting(painting)
    brush_sizes, brush_type, colors, rgbs = draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brush_sizes)):
                if brush_sizes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for i, brush in enumerate(brush_type):
                if brush.collidepoint(event.pos):
                    if i == 0:
                        active_shape = 'square'
                    elif i == 1:
                        active_shape = 'right_triangle'
                    elif i == 2:
                        active_shape = 'rhombus'

    pygame.display.flip()
pygame.quit()