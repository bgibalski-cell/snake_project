import pygame
import random
import os

pygame.init()

import math
import array

pygame.mixer.init()

def make_beep(freq=880, duration_ms=120, volume=0.3, sample_rate=44100):
    n_samples = int(sample_rate * duration_ms / 1000)
    buf = array.array("h")  # signed short
    amplitude = int(32767 * volume)
    for i in range(n_samples):
        t = i / sample_rate
        sample = int(amplitude * math.sin(2 * math.pi * freq * t))
        buf.append(sample)
    return pygame.mixer.Sound(buffer=buf)

eat_sound = make_beep()

# --- stałe gry ---
WIDTH, HEIGHT = 600, 600
CELL = 20
FPS = 10

# --- okno ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# --- fonty ---
font = pygame.font.SysFont(None, 64)
small_font = pygame.font.SysFont(None, 28)

def draw_grid():
    # pionowe linie
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, HEIGHT))
    # poziome linie
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, (30, 30, 30), (0, y), (WIDTH, y))

def random_food():
    return (
        random.randrange(0, WIDTH, CELL),
        random.randrange(0, HEIGHT, CELL)
    )

def reset_game():
    snake = [(100, 60), (80, 60), (60, 60)]
    dx, dy = CELL, 0
    food = random_food()
    score = 0
    return snake, dx, dy, food, score

# --- start ---
running = True
game_over = False
snake, dx, dy, food, score = reset_game()

while running:
    # =========================
    # TRYB: GAME OVER (czekamy)
    # =========================
    if game_over:
        screen.fill((0, 0, 0))
        draw_grid()

        text = font.render("GAME OVER", True, (255, 0, 0))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, rect)

        hint = small_font.render(
            "Aby zagrać jeszcze raz, kliknij na dowolną strzałkę (lub R)",
            True, (200, 200, 200)
        )
        hint_rect = hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(hint, hint_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_r):
                    snake, dx, dy, food, score = reset_game()
                    game_over = False
                    pygame.event.clear()  # czyści “nadmiarowe” kliknięcia

        clock.tick(FPS)
        continue

    # =========================
    # EVENTY (normalna gra)
    # =========================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # zmiana kierunku (bez cofania w siebie)
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL, 0

            elif event.key == pygame.K_r:
                snake, dx, dy, food, score = reset_game()
                game_over = False

    # =========================
    # LOGIKA RUCHU
    # =========================
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    # kolizja ze ścianą -> game over
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        game_over = True
        continue

    # kolizja z ciałem (bez głowy) -> game over
    if new_head in snake[1:]:
        game_over = True
        continue

    # ruszamy węża
    snake.insert(0, new_head)

    # jedzenie
    if new_head == food:
        eat_sound.play()
        food = random_food()
        score += 1
    else:
        snake.pop()

    # =========================
    # RYSOWANIE
    # =========================
    screen.fill((0, 0, 0))
    draw_grid()

    score_text = small_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], CELL, CELL))

    for (sx, sy) in snake:
        pygame.draw.rect(screen, (0, 255, 0), (sx, sy, CELL, CELL))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()