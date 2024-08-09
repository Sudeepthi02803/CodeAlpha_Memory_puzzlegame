import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Memory Puzzle Game')  # Corrected function name

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Font
font = pygame.font.Font(None, 36)

class Card:
    def __init__(self, value, x, y):
        self.value = value
        self.rect = pygame.Rect(x, y, 100, 100)
        self.flipped = False

    def draw(self, screen):
        if self.flipped:
            pygame.draw.rect(screen, green, self.rect)
            text = font.render(str(self.value), True, black)
            screen.blit(text, (self.rect.x + 35, self.rect.y + 35))
        else:
            pygame.draw.rect(screen, blue, self.rect)

def create_board():
    values = list(range(8)) * 2  # Create pairs of values
    random.shuffle(values)
    cards = []
    for i in range(4):
        for j in range(4):
            card = Card(values.pop(), j * 110 + 50, i * 110 + 50)
            cards.append(card)
    return cards

def main():
    cards = create_board()
    running = True
    first_card = None
    second_card = None
    start_time = time.time()
    time_limit = 60  # 60 seconds time limit

    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for card in cards:
                    if card.rect.collidepoint(pos) and not card.flipped:
                        card.flipped = True
                        if first_card is None:
                            first_card = card
                        elif second_card is None:
                            second_card = card

        if first_card and second_card:
            if first_card.value == second_card.value:
                first_card = None
                second_card = None
            else:
                pygame.display.update()
                pygame.time.wait(1000)
                first_card.flipped = False
                second_card.flipped = False
                first_card = None
                second_card = None

        for card in cards:
            card.draw(screen)

        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            running = False
            print("Time's up! Game Over.")

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
