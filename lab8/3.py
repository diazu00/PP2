import pygame

pygame.init()

fps = 60
timer = pygame.time.Clock()
width = 800
height = 600
active_size = 0
active_color = 'white'

win = pygame.display.set_mode([width, height])
pygame.display.set_caption("Paaint")
painting = []


def draw_menu(size, color):
    pygame.draw.rect(win, 'gray', [0, 0, width, 70])
    pygame.draw.line(win, 'black', (0, 70), (width, 70), 3)
    xl_brush = pygame.draw.rect(win, 'black', [10, 10, 50, 50])
    pygame.draw.circle(win, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(win, 'black', [70, 10, 50, 50])
    pygame.draw.circle(win, 'white', (95, 35), 15)
    m_brush = pygame.draw.rect(win, 'black', [130, 10, 50, 50])
    pygame.draw.circle(win, 'white', (155, 35), 10)
    s_brush = pygame.draw.rect(win, 'black', [190, 10, 50, 50])
    pygame.draw.circle(win, 'white', (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    if size == 20:
        pygame.draw.rect(win, 'green', [10, 10, 50, 50], 3)
    if size == 15:
        pygame.draw.rect(win, 'green', [70, 10, 50, 50], 3)
    if size == 10:
        pygame.draw.rect(win, 'green', [130, 10, 50, 50], 3)
    if size == 5:
        pygame.draw.rect(win, 'green', [190, 10, 50, 50], 3)

    pygame.draw.circle(win, color, (400, 35), 30)
    pygame.draw.circle(win, 'dark grey', (400, 35), 3)

    blue = pygame.draw.rect(win, (0, 0, 255), [width - 35, 10, 25, 25])
    red = pygame.draw.rect(win, (255, 0, 0), [width - 35, 35, 25, 25])
    green = pygame.draw.rect(win, (0, 255, 0), [width - 60, 10, 25, 25])
    yellow = pygame.draw.rect(win, (255, 255, 0), [width - 60, 35, 25, 25])
    teal = pygame.draw.rect(win, (0, 255, 255), [width - 85, 10, 25, 25])
    purple = pygame.draw.rect(win, (255, 0, 255), [width - 85, 35, 25, 25])
    white = pygame.draw.rect(win, (0, 0, 0), [width - 110, 10, 25, 25])
    black = pygame.draw.rect(win, (255, 255, 255), [width - 110, 35, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                (255, 255, 255)]

    return brush_list, color_rect, rgb_list


def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(win, paints[i][0], paints[i][1], paints[i][2])


run = True
while run:
    timer.tick(fps)
    win.fill('white')
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if mouse[1] > 70:
        pygame.draw.circle(win, active_color, mouse, active_size)

    draw_painting(painting)
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))

    brushes, colors, rgbs = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

    pygame.display.flip()
pygame.quit()