import pygame
import sys
from button import ImageButton
import random

pygame.init()

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
MAX_FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (65, 105, 213)
grey = (192, 192, 192)
skyblue = (135, 206, 235)
colors = [(255, 110, 0), (255, 255, 102), (0, 255, 0), (65, 105, 213), (0, 191, 255), (139, 0, 255), (252, 15, 192), (192, 192, 192)]

pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Lucida Console", 30)
menu_font = pygame.font.SysFont("bahnschrift", 80)
menu_font_2 = pygame.font.SysFont("Lucida Console", 25)
record = []

# Загрузка и установка курсора
cursor = pygame.image.load("cursor.png")
pygame.mouse.set_visible(False)  # Скрываем стандартный курсор

def Your_score(score, recor):
    value = score_font.render("Ваш счёт: " + str(score), True, white)
    dis.blit(value, [0, 0])
    if score > recor:
        rec = score_font.render("Ваш рекорд: " + str(score), True, green)
    else:
        rec = score_font.render("Ваш рекорд: " + str(recor), True, white)
    dis.blit(rec, [550, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        color = random.choice(colors)
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def main_menu():
    # Создание кнопок
    start_button = ImageButton(dis_width/2-(252/2), 250, 252, 74, "Новая игра", "green_button2.jpg", "green_button2_hover.jpg")
    exit_button = ImageButton(dis_width/2-(252/2), 350, 252, 74, "Выйти", "green_button2.jpg", "green_button2_hover.jpg")

    running = True
    while running:
        dis.fill((0, 0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Игра Змейка", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(dis_width/2,150))
        dis.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                print("Кнопка 'Старт' была нажата!")
                fade()
                new_game()


            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(dis)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        dis.blit(cursor, (x-2, y-2))

        pygame.display.flip()

def new_game():
    # Создание кнопок
    restrictions_button = ImageButton(100, 200, 252, 74, "Без ограничений", "green_button2.jpg", "green_button2_hover.jpg")
    easy_button = ImageButton(450, 200, 252, 74, "Easy", "green_button2.jpg", "green_button2_hover.jpg")
    medium_button = ImageButton(100, 300, 252, 74, "Medium", "green_button2.jpg", "green_button2_hover.jpg")
    hard_button = ImageButton(450, 300, 252, 74, "Hard", "green_button2.jpg", "green_button2_hover.jpg")
    back_button = ImageButton(dis_width/2-(252/2), 400, 252, 74, "Назад", "green_button2.jpg", "green_button2_hover.jpg")

    running = True
    while running:
        dis.fill((0, 0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Выберете уровень", True, (255, 255, 255))
        dis.blit(text_surface, [180, 50])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Возврат в меню
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Возврат в меню
            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.USEREVENT and event.button == easy_button:
                def gameLoop():
                    game_over = False
                    game_close = False
                    x1 = dis_width / 2
                    y1 = dis_height / 2
                    x1_change = 0
                    y1_change = 0
                    snake_List = []
                    Length_of_snake = 1
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    while not game_over:
                        while game_close == True:
                            dis.fill(blue)
                            if len(record) != 0:
                                Your_score(Length_of_snake - 1, max(record))
                            else:
                                Your_score(Length_of_snake - 1, 0)
                            record.append(Length_of_snake - 1)
                            pro = score_font.render("Вы проиграли! Нажмите Q для выхода в меню", True, red)
                            dis.blit(pro, [0, 200])
                            prod = score_font.render("или C для повторной игры", True, red)
                            dis.blit(prod, [0, 250])
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_q:
                                        game_over = True
                                        game_close = False
                                        main_menu()
                                    if event.key == pygame.K_c:
                                        gameLoop()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game_over = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_RIGHT:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_UP:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_DOWN:
                                    y1_change = snake_block
                                    x1_change = 0
                                if event.key == pygame.K_a:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_d:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_w:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_s:
                                    y1_change = snake_block
                                    x1_change = 0
                        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                            game_close = True
                        x1 += x1_change
                        y1 += y1_change
                        dis.fill(black)
                        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
                        snake_Head = []
                        snake_Head.append(x1)
                        snake_Head.append(y1)
                        snake_List.append(snake_Head)
                        if len(snake_List) > Length_of_snake:
                            del snake_List[0]
                        for x in snake_List[:-1]:
                            if x == snake_Head:
                                game_close = True
                        our_snake(snake_block, snake_List)
                        if len(record) != 0:
                            Your_score(Length_of_snake - 1, max(record))
                        else:
                            Your_score(Length_of_snake - 1, 0)
                        pygame.display.update()
                        if x1 == foodx and y1 == foody:
                            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                            Length_of_snake += 1
                        clock.tick(snake_speed)
                    pygame.quit()
                    quit()

                gameLoop()

            if event.type == pygame.USEREVENT and event.button == restrictions_button:
                def No_restrictions():
                    game_over = False
                    game_close = False
                    x1 = dis_width / 2
                    y1 = dis_height / 2
                    x1_change = 0
                    y1_change = 0
                    snake_List = []
                    Length_of_snake = 1
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    while not game_over:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game_over = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_RIGHT:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_UP:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_DOWN:
                                    y1_change = snake_block
                                    x1_change = 0
                                if event.key == pygame.K_a:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_d:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_w:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_s:
                                    y1_change = snake_block
                                    x1_change = 0
                                if event.key == pygame.K_q:
                                    game_over = True
                                    game_close = False
                                    main_menu()

                        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                            if x1 >= dis_width:
                                x1 = 0.0
                            elif x1 < 0:
                                x1 = 800.0
                            elif y1 >= dis_height:
                                y1 = 0.0
                            elif y1 < 0:
                                y1 = 600.0
                        x1 += x1_change
                        y1 += y1_change
                        dis.fill(black)
                        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
                        rec = font_style.render("Для выхода в меню нажмите Q", True, white)
                        dis.blit(rec, [435, 560])
                        snake_Head = []
                        snake_Head.append(x1)
                        snake_Head.append(y1)
                        snake_List.append(snake_Head)
                        if len(snake_List) > Length_of_snake:
                            del snake_List[0]
                        our_snake(snake_block, snake_List)
                        if len(record) != 0:
                            Your_score(Length_of_snake - 1, max(record))
                        else:
                            Your_score(Length_of_snake - 1, 0)
                        pygame.display.update()
                        if x1 == foodx and y1 == foody:
                            if x1 == foodx and y1 == foody:
                                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                                Length_of_snake += 1
                            clock.tick(snake_speed)
                        clock.tick(snake_speed)
                    pygame.quit()
                    quit()

                No_restrictions()

            if event.type == pygame.USEREVENT and event.button == medium_button:
                def Medium():
                    game_over = False
                    game_close = False
                    x1 = dis_width / 2
                    y1 = dis_height / 2
                    x1_change = 0
                    y1_change = 0
                    snake_List = []
                    obstacles_x1 = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 for _ in
                                    range(10)]
                    obstacles_y1 = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 for _ in
                                    range(10)]
                    obstacles_x2 = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 for _ in
                                    range(10)]
                    obstacles_y2 = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 for _ in
                                    range(10)]

                    obs_x1 = list(map(int, obstacles_x1))
                    obs_y1 = list(map(int, obstacles_y1))
                    obs_x2 = list(map(int, obstacles_x2))
                    obs_y2 = list(map(int, obstacles_y2))

                    Length_of_snake = 1
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

                    for i in range(10):
                        while x1 in range(obs_x2[i], obs_x2[i] + 41) and y1 in range(obs_y2[i],
                                                                                     obs_y1[i] + 51) and x1 in range(
                                obs_x1[i], obs_x1[i] + 21) and y1 in range(obs_y1[i], obs_y1[i] + 31):
                            x1 = random.randint(0, 800) + 0.0
                            y1 = random.randint(0, 600) + 0.0
                        while foodx in range(obs_x2[i], obs_x2[i] + 41) and foody in range(obs_y2[i],
                                                                                     obs_y1[i] + 51) and foodx in range(
                                obs_x1[i], obs_x1[i] + 21) and foody in range(obs_y1[i], obs_y1[i] + 31):
                            x1 = random.randint(0, 800) + 0.0
                            y1 = random.randint(0, 600) + 0.0

                    while not game_over:
                        while game_close == True:
                            dis.fill(blue)
                            if len(record) != 0:
                                Your_score(Length_of_snake - 1, max(record))
                            else:
                                Your_score(Length_of_snake - 1, 0)
                            record.append(Length_of_snake - 1)
                            pro = score_font.render("Вы проиграли! Нажмите Q для выхода в меню", True, red)
                            dis.blit(pro, [0, 200])
                            prod = score_font.render("или C для повторной игры", True, red)
                            dis.blit(prod, [0, 250])
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_q:
                                        game_over = True
                                        game_close = False
                                        main_menu()
                                    if event.key == pygame.K_c:
                                        Medium()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game_over = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_RIGHT:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_UP:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_DOWN:
                                    y1_change = snake_block
                                    x1_change = 0
                                if event.key == pygame.K_a:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_d:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_w:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_s:
                                    y1_change = snake_block
                                    x1_change = 0
                        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                            game_close = True
                        for i in range(10):
                            obs_x1 = list(map(int, obstacles_x1))
                            obs_y1 = list(map(int, obstacles_y1))
                            obs_x2 = list(map(int, obstacles_x2))
                            obs_y2 = list(map(int, obstacles_y2))
                            if x1 in [i + 0.0 for i in range(obs_x1[i], obs_x1[i] + 21)] and y1 in [i + 0.0 for i in range(obs_y1[i], obs_y1[i] + 31)]:
                                game_close = True
                                dis.fill(blue)
                                if len(record) != 0:
                                    Your_score(Length_of_snake - 1, max(record))
                                else:
                                    Your_score(Length_of_snake - 1, 0)
                                record.append(Length_of_snake - 1)
                                pr = score_font.render("Вы проиграли! Нажмите Q для выхода в меню", True, red)
                                dis.blit(pr, [0, 200])
                                pro = score_font.render("или C для повторной игры", True, red)
                                dis.blit(pro, [0, 250])
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                            game_over = True
                                            game_close = False
                                            main_menu()
                                        if event.key == pygame.K_c:
                                            Medium()
                            if x1 in range(obs_x2[i], obs_x2[i] + 41) and y1 in range(obs_y2[i], obs_y2[i] + 51):
                                game_close = True
                                dis.fill(blue)
                                if len(record) != 0:
                                    Your_score(Length_of_snake - 1, max(record))
                                else:
                                    Your_score(Length_of_snake - 1, 0)
                                record.append(Length_of_snake - 1)
                                p = score_font.render("Вы проиграли! Нажмите Q для выхода в меню", True, red)
                                dis.blit(p, [0, 200])
                                prodi = score_font.render("или C для повторной игры", True, red)
                                dis.blit(prodi, [0, 250])
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                            game_over = True
                                            game_close = False
                                            main_menu()
                                        if event.key == pygame.K_c:
                                            Medium()
                        x1 += x1_change
                        y1 += y1_change
                        dis.fill(black)
                        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
                        for i in range(10):
                            pygame.draw.rect(dis, grey, [obstacles_x1[i], obstacles_y1[i], 20, 30])
                            pygame.draw.rect(dis, grey, [obstacles_x2[i], obstacles_y2[i], 40, 50])
                        snake_Head = []
                        snake_Head.append(x1)
                        snake_Head.append(y1)
                        snake_List.append(snake_Head)
                        if len(snake_List) > Length_of_snake:
                            del snake_List[0]
                        for x in snake_List[:-1]:
                            if x == snake_Head:
                                game_close = True
                        our_snake(snake_block, snake_List)
                        if len(record) != 0:
                            Your_score(Length_of_snake - 1, max(record))
                        else:
                            Your_score(Length_of_snake - 1, 0)
                        pygame.display.update()
                        if x1 == foodx and y1 == foody:
                            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                            Length_of_snake += 1
                        clock.tick(snake_speed)
                    pygame.quit()
                    quit()

                Medium()

            if event.type == pygame.USEREVENT and event.button == hard_button:
                def Hard():
                    snake_speed = 14
                    game_over = False
                    game_close = False
                    x1 = dis_width / 2
                    y1 = dis_height / 2
                    x1_change = 0
                    y1_change = 0
                    snake_List = []
                    obstacles_x1 = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 for _ in
                                    range(10)]
                    obstacles_y1 = [round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 for _ in
                                    range(10)]
                    obstacles_x2 = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 for _ in
                                    range(10)]
                    obstacles_y2 = [round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 for _ in
                                    range(10)]
                    ice_x = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 for _ in range(5)]
                    ice_y = [round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 for _ in range(5)]
                    Length_of_snake = 1
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

                    obs_x1 = list(map(int, obstacles_x1))
                    obs_y1 = list(map(int, obstacles_y1))
                    obs_x2 = list(map(int, obstacles_x2))
                    obs_y2 = list(map(int, obstacles_y2))
                    i_x = list(map(int, ice_x))
                    i_y = list(map(int, ice_x))

                    for i in range(10):
                        while x1 in range(obs_x2[i], obs_x2[i] + 41) and y1 in range(obs_y2[i],
                                                                                     obs_y1[i] + 51) and x1 in range(
                                obs_x1[i], obs_x1[i] + 21) and y1 in range(obs_y1[i], obs_y1[i] + 31):
                            x1 = random.randint(0, 800) + 0.0
                            y1 = random.randint(0, 600) + 0.0
                        while foodx in range(obs_x2[i], obs_x2[i] + 41) and foody in range(obs_y2[i],
                                                                                           obs_y1[
                                                                                               i] + 51) and foodx in range(
                            obs_x1[i], obs_x1[i] + 21) and foody in range(obs_y1[i], obs_y1[i] + 31):
                            foodx = random.randint(0, 800) + 0.0
                            foody = random.randint(0, 600) + 0.0

                    for i in range(5):
                        if x1 in [i + 0.0 for i in range(i_x[i], i_x[i] + 91)] and y1 in [i + 0.0 for i in
                                                                                          range(i_y[i], i_y[i] + 91)]:
                            x1 = random.randint(0, 800) + 0.0
                            y1 = random.randint(0, 600) + 0.0
                        if foodx in [i + 0.0 for i in range(i_x[i], i_x[i] + 91)] and foody in [i + 0.0 for i in
                                                                                                range(i_y[i],
                                                                                                      i_y[i] + 91)]:
                            foodx = random.randint(0, 800) + 0.0
                            foody = random.randint(0, 600) + 0.0

                    while not game_over:
                        while game_close == True:
                            dis.fill(blue)
                            if len(record) != 0:
                                Your_score(Length_of_snake - 1, max(record))
                            else:
                                Your_score(Length_of_snake - 1, 0)
                            record.append(Length_of_snake - 1)
                            pro = score_font.render("Вы проиграли! Нажмите Q для выхода в меню", True, red)
                            dis.blit(pro, [0, 200])
                            prod = score_font.render("или C для повторной игры", True, red)
                            dis.blit(prod, [0, 250])
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_q:
                                        game_over = True
                                        game_close = False
                                        main_menu()
                                    if event.key == pygame.K_c:
                                        Hard()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game_over = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_RIGHT:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_UP:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_DOWN:
                                    y1_change = snake_block
                                    x1_change = 0
                                if event.key == pygame.K_a:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_d:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_w:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_s:
                                    y1_change = snake_block
                                    x1_change = 0

                        for i in range(5):
                            if x1 in [i + 0.0 for i in range(i_x[i], i_x[i] + 91)] and y1 in [i + 0.0 for i in
                                                                                              range(i_y[i],
                                                                                                    i_y[i] + 91)]:
                                nap = random.choice(['down', 'right', 'left', 'up'])
                                if nap == 'left':
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif nap == 'right':
                                    x1_change = snake_block
                                    y1_change = 0
                                elif nap == 'up':
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif nap == 'down':
                                    y1_change = snake_block
                                    x1_change = 0
                                snake_speed += 0.5

                        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                            game_close = True
                        for i in range(10):
                            obs_x1 = list(map(int, obstacles_x1))
                            obs_y1 = list(map(int, obstacles_y1))
                            obs_x2 = list(map(int, obstacles_x2))
                            obs_y2 = list(map(int, obstacles_y2))
                            if x1 in [i + 0.0 for i in range(obs_x1[i], obs_x1[i] + 21)] and y1 in [i + 0.0 for i in
                                                                                                    range(obs_y1[i],
                                                                                                          obs_y1[
                                                                                                              i] + 31)]:
                                game_close = True
                                dis.fill(blue)
                                if len(record) != 0:
                                    Your_score(Length_of_snake - 1, max(record))
                                else:
                                    Your_score(Length_of_snake - 1, 0)
                                record.append(Length_of_snake - 1)
                                pr = score_font.render("Вы проиграли! Нажмите Q для выхода в меню", True, red)
                                dis.blit(pr, [0, 200])
                                pro = score_font.render("или C для повторной игры", True, red)
                                dis.blit(pro, [0, 250])
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                            game_over = True
                                            game_close = False
                                            main_menu()
                                        if event.key == pygame.K_c:
                                            Hard()
                            if x1 in range(obs_x2[i], obs_x2[i] + 41) and y1 in range(obs_y2[i], obs_y2[i] + 51):
                                game_close = True
                                dis.fill(blue)
                                if len(record) != 0:
                                    Your_score(Length_of_snake - 1, max(record))
                                else:
                                    Your_score(Length_of_snake - 1, 0)
                                record.append(Length_of_snake - 1)
                                p = score_font.render("Вы проиграли! Нажмите Q для выхода в меню", True, red)
                                dis.blit(p, [0, 200])
                                prodi = score_font.render("или C для повторной игры", True, red)
                                dis.blit(prodi, [0, 250])
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                            game_over = True
                                            game_close = False
                                            main_menu()
                                        if event.key == pygame.K_c:
                                            Hard()
                        x1 += x1_change
                        y1 += y1_change
                        dis.fill(black)
                        for i in range(5):
                            pygame.draw.rect(dis, skyblue, [ice_x[i], ice_y[i], 120, 120])
                        for i in range(10):
                            pygame.draw.rect(dis, grey, [obstacles_x1[i], obstacles_y1[i], 20, 30])
                            pygame.draw.rect(dis, grey, [obstacles_x2[i], obstacles_y2[i], 40, 50])
                        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
                        snake_Head = []
                        snake_Head.append(x1)
                        snake_Head.append(y1)
                        snake_List.append(snake_Head)
                        if len(snake_List) > Length_of_snake:
                            del snake_List[0]
                        for x in snake_List[:-1]:
                            if x == snake_Head:
                                game_close = True
                        our_snake(snake_block, snake_List)
                        if len(record) != 0:
                            Your_score(Length_of_snake - 1, max(record))
                        else:
                            Your_score(Length_of_snake - 1, 0)
                        pygame.display.update()
                        if x1 == foodx and y1 == foody:
                            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                            snake_speed += 2
                            Length_of_snake += 1
                        clock.tick(snake_speed)
                    pygame.quit()
                    quit()

                Hard()

            for btn in [back_button, hard_button, easy_button, medium_button, restrictions_button]:
                btn.handle_event(event)

        for btn in [back_button, hard_button, easy_button, medium_button, restrictions_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(dis)

        # Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        dis.blit(cursor, (x-2, y-2))

        pygame.display.flip()

# затемнение
def fade():
    running = True
    fade_alpha = 0  # Уровень прозрачности для анимации

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Анимация затухания текущего экрана
        fade_surface = pygame.Surface((dis_width, dis_height))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        dis.blit(fade_surface, (0, 0))

        # Увеличение уровня прозрачности
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)  # Ограничение FPS

if __name__ == "__main__":
    main_menu()