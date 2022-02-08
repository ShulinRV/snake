import pygame

SIZE_BLOCK = 20  # константа
FRAME_COLOR = (0, 255, 204)  # Модель RGB заливка
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
size = [500, 600]  # size переменная, которую сохраняем как screen
COUNT_BLOCKS = 20
MARGIN = 1

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")  # модуль set_caption добавляет имя


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.QUIT()

        screen.fill(FRAME_COLOR)  # скрин наполняем (переменная FRAME_COLOR)

    for row in range(COUNT_BLOCKS):
        for column in range(
                COUNT_BLOCKS):  # в цикле будет делаться одна команта и к 10+колонку и множить на размер блока
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [10 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                             20 + row * SIZE_BLOCK + MARGIN * (row + 1),
                                             SIZE_BLOCK,
                                             SIZE_BLOCK])
              # draw, где будем рисовать, на screen + кортеж [из 4х значение] где 10, верхняя левая точка

            pygame.display.flip()  # метод который приминяем, все что сделали на screen
