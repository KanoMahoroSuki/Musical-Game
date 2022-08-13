from random import randint
from sys import exit

import pygame

########################################################################################################################
pygame.init()
screen = pygame.display.set_mode((1200, 640))
pygame.display.set_caption('Pymon')
icon = pygame.image.load('icon.PNG')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
game_active = False
pygame.mixer.music.load('Sound/Sky_High.mp3')
beat_sound = pygame.mixer.Sound('Sound/Beat.mp3')
num_combo = 0
num_good = 0
num_perfect = 0
########################################################################################################################
background_surf = pygame.image.load('Picture/Classroom1.png')
classroom_surf = pygame.image.load('Picture/Classroom2.png')
my_font240 = pygame.font.Font('Pixeltype.ttf', 240)
my_font80 = pygame.font.Font('Pixeltype.ttf', 80)
K1_surf = my_font80.render('S', False, (219, 77, 109))
K1_rect = K1_surf.get_rect(center=(446, 550))
K2_surf = my_font80.render('D', False, (233, 139, 42))
K2_rect = K1_surf.get_rect(center=(547, 550))
K3_surf = my_font80.render('J', False, (34, 125, 81))
K3_rect = K1_surf.get_rect(center=(648, 550))
K4_surf = my_font80.render('K', False, (81, 168, 221))
K4_rect = K1_surf.get_rect(center=(749, 550))


def display_combo():
    state_surf = my_font80.render(f'{num_combo} COMBO', False, (106, 76, 156))
    state_rect = state_surf.get_rect(center=(600, 150))
    screen.blit(state_surf, state_rect)


def display_hit(hit):
    hit_surf = my_font80.render(hit, False, (119, 66, 141))
    hit_rect = hit_surf.get_rect(center=(600, 350))
    screen.blit(hit_surf, hit_rect)


def note_movement(note_list):
    if note_list:
        for note_rect in note_list:
            note_rect.y += 10
            screen.blit(note_surf, note_rect)
        note_list = [note for note in note_list if note.y <= 870]
        return note_list
    else:
        return []


def collisions(k, notes):
    if notes:
        for note_rect in notes:
            if k.colliderect(note_rect):
                notes.remove(note_rect)
                return True


note_surf = pygame.image.load('note.png')
note_rect_list = []
note_timer = pygame.USEREVENT + 1
pygame.time.set_timer(note_timer, 500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    beat_sound.play()
                if event.key == pygame.K_d:
                    beat_sound.play()
                if event.key == pygame.K_j:
                    beat_sound.play()
                if event.key == pygame.K_k:
                    beat_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.mixer.music.play(0)
                num_combo = 0
                num_good = 0
                num_perfect = 0
                note_rect_list.clear()
                game_active = True
        if event.type == note_timer and game_active:
            if randint(0, 2):
                if randint(0, 2):
                    note_rect_list.append(note_surf.get_rect(midtop=(446, -100)))
                else:
                    note_rect_list.append(note_surf.get_rect(midtop=(547, -100)))
            else:
                if randint(0, 2):
                    note_rect_list.append(note_surf.get_rect(midtop=(648, -100)))
                else:
                    note_rect_list.append(note_surf.get_rect(midtop=(749, -100)))

    if game_active:
        if not pygame.mixer.music.get_busy():
            game_active = False
        K1_Perfect = pygame.draw.rect(screen, '#ff9d9d', (396, 450, 101, 100))
        K2_Perfect = pygame.draw.rect(screen, '#ff9d9d', (497, 450, 101, 100))
        K3_Perfect = pygame.draw.rect(screen, '#ff9d9d', (598, 450, 101, 100))
        K4_Perfect = pygame.draw.rect(screen, '#ff9d9d', (699, 450, 101, 100))
        K1_Good = pygame.draw.rect(screen, '#ff9d9d', (396, 400, 101, 50))
        K2_Good = pygame.draw.rect(screen, '#ff9d9d', (497, 400, 101, 50))
        K3_Good = pygame.draw.rect(screen, '#ff9d9d', (598, 400, 101, 50))
        K4_Good = pygame.draw.rect(screen, '#ff9d9d', (699, 400, 101, 50))
        screen.blit(background_surf, (0, 0))
        screen.blit(K1_surf, K1_rect)
        screen.blit(K2_surf, K2_rect)
        screen.blit(K3_surf, K3_rect)
        screen.blit(K4_surf, K4_rect)
        if num_combo >= 5:
            display_combo()
        note_rect_list = note_movement(note_rect_list)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            if collisions(K1_Good, note_rect_list):
                display_hit('GOOD')
                num_combo += 1
                num_good += 1
            if collisions(K1_Perfect, note_rect_list):
                display_hit('PERFECT')
                num_combo += 1
                num_perfect += 1
        if keys[pygame.K_d]:
            if collisions(K2_Good, note_rect_list):
                display_hit('GOOD')
                num_combo += 1
                num_good += 1
            if collisions(K2_Perfect, note_rect_list):
                display_hit('PERFECT')
                num_combo += 1
                num_perfect += 1
        if keys[pygame.K_j]:
            if collisions(K3_Good, note_rect_list):
                display_hit('GOOD')
                num_combo += 1
                num_good += 1
            if collisions(K3_Perfect, note_rect_list):
                display_hit('PERFECT')
                num_combo += 1
                num_perfect += 1
        if keys[pygame.K_k]:
            if collisions(K4_Good, note_rect_list):
                display_hit('GOOD')
                num_combo += 1
                num_good += 1
            if collisions(K4_Perfect, note_rect_list):
                display_hit('PERFECT')
                num_combo += 1
                num_perfect += 1

    else:
        screen.blit(classroom_surf, (0, 0))
        welcome_message = my_font80.render('PRESS SPACE TO START', False, (255, 255, 255))
        welcome_message_rect = welcome_message.get_rect(center=(600, 320))
        welcome_message2 = my_font80.render('PRESS SPACE TO START AGAIN', False, (255, 255, 255))
        welcome_message2_rect = welcome_message2.get_rect(center=(600, 500))
        result_message = my_font80.render('RESULT', False, (255, 255, 255))
        result_message_rect = result_message.get_rect(center=(600, 100))
        perfect_message = my_font80.render(f'PERFECT: {num_perfect}', False, (255, 255, 255))
        perfect_message_rect = perfect_message.get_rect(midleft=(200, 200))
        good_message = my_font80.render(f'GOOD: {num_good}', False, (255, 255, 255))
        good_message_rect = good_message.get_rect(midleft=(200, 300))
        combo_message = my_font80.render(f'COMBO: {num_combo}', False, (255, 255, 255))
        combo_message_rect = combo_message.get_rect(midleft=(200, 400))
        sync_rate = int((num_combo / 320) * 100)
        sync_rate_message = my_font80.render(f'SYNC_RATE: {sync_rate}%', False, (255, 255, 255))
        sync_rate_message_rect = sync_rate_message.get_rect(center=(900, 400))
        if sync_rate >= 80:
            accuracy = 'S+'
        elif sync_rate >= 70:
            accuracy = 'S'
        elif sync_rate >= 60:
            accuracy = 'A'
        else:
            accuracy = 'B'
        accuracy_message = my_font240.render(str(accuracy), False, (239, 187, 36))
        accuracy_message_rect = accuracy_message.get_rect(center=(900, 275))

        if num_combo == 0:
            screen.blit(welcome_message, welcome_message_rect)
        else:
            screen.blit(result_message, result_message_rect)
            screen.blit(perfect_message, perfect_message_rect)
            screen.blit(good_message, good_message_rect)
            screen.blit(combo_message, combo_message_rect)
            screen.blit(sync_rate_message, sync_rate_message_rect)
            screen.blit(accuracy_message, accuracy_message_rect)
            screen.blit(welcome_message2, welcome_message2_rect)

    pygame.display.update()
    clock.tick(60)
