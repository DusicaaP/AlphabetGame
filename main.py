import pygame
import random

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption ("Alphabet Game")

black = (0, 0, 0)
white = (255, 255, 255)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

shuffled_alphabet = list(alphabet)
random.shuffle(shuffled_alphabet)

chosen_letters = random.sample(shuffled_alphabet, 10)

player_letters = []
player_word = ""

valid_words = ["CAT", "DOG", "HAT", "LOG", "MAT", "RAT"]

def reshuffle_letters():
    random.shuffle(chosen_letters)
    player_letters.clear()
    player_word = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if player_word in valid_words:
                    print("Valid word:", player_word)
                else:
                    print("Invalid word:", player_word)
                player_letters = []
                player_word = ""
            elif event.key ==pygame.K_SPACE:
                reshuffle_letters()
            else:
                letter = pygame.key.name(event.key).upper()
                if letter in chosen_letters:
                    player_letters.append(letter)
                    player_word = "".join(player_letters)

    window.fill(white)

    welcome_caption = "Welcome to the Alphabet Game!"
    guide_message = "Try to create words using the chosen letters. " \
                    "Press ENTER to submit a word. " \
                    "Press SPACE to reshuffle the letters."

    welcome_caption_font = pygame.font.Font(None, 48)
    welcome_caption_surface = welcome_caption_font.render(welcome_caption, True, black)
    window.blit(welcome_caption_surface, (100, 50))

    guide_font = pygame.font.Font(None, 28)
    guide_surface = guide_font.render(guide_message, True, black)
    window.blit(guide_surface, (100, 150))

    font = pygame.font.Font(None, 36)
    for i, letter in enumerate(chosen_letters):
        letter_surface = font.render(letter, True, black)
        window.blit(letter_surface, (100 + i * 50, 100))

    word_surface = font.render(player_word, True, black)
    window.blit(word_surface, (100, 200))

    pygame.display.update()

pygame.quit()

