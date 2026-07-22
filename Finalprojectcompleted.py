import pygame
import random
pygame.init()
diff = input("what difficulty do you want this game to be, easy,normal,hard,impossible").strip().lower()
GRID = 9
CELL = 60
TOP = 170

WIDTH = GRID * CELL
HEIGHT = GRID * CELL + TOP

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Digger")

font = pygame.font.SysFont(None, 28)

YELLOW = (235, 210, 70)
TAN = (210, 180, 140)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 50, 50)
GREEN = (40, 180, 40)
GRAY = (180, 180, 180)

board = [["empty" for _ in range(GRID)] for _ in range(GRID)]
revealed = [[False for _ in range(GRID)] for _ in range(GRID)]

spots = [(r, c) for r in range(GRID) for c in range(GRID)]
random.shuffle(spots)
if diff == "easy":
    bomb = 1
    treasure = 3
elif diff == "normal":
    bomb = 2
    treasure = 5
elif diff == "hard":
    bomb = 4
    treasure = 7
else:
    bomb = 71
    treasure = 10
for _ in range(treasure):
    r, c = spots.pop()
    board[r][c] = "treasure"

for _ in range(bomb):
    r, c = spots.pop()
    board[r][c] = "bomb"

lives = 1
treasures = 0
power1_used = False
power2_used = False
game_over = False
message = ""

power1_rect = pygame.Rect(40,85,180,42)
power2_rect = pygame.Rect(260,85,180,42)


def reveal_cell(r, c, count_bombs=True):
    global treasures, lives
    if not revealed[r][c]:
        revealed[r][c] = True
        if board[r][c] == "treasure":
            treasures += 1
        elif board[r][c] == "bomb" and count_bombs:
            lives -= 1


def reveal_all():
    for r in range(GRID):
        for c in range(GRID):
            revealed[r][c] = True


def draw():
    title_font=pygame.font.SysFont(None,42,bold=True)
    screen.fill((110,190,255))
    pygame.draw.rect(screen,(235,220,170),(0,0,WIDTH,TOP))
    screen.blit(title_font.render("🏴‍☠️ Treasure Digger",True,(120,70,20)),(WIDTH//2-150,10))
    screen.blit(font.render(f"💰 Treasures: {treasures}/{treasure}",True,BLACK),(180,55))
    pygame.draw.rect(screen,GRAY,power1_rect)
    pygame.draw.rect(screen,GRAY,power2_rect)
    label1 = "reveal cross" if not power1_used else "Used"
    label2 = "Reveal 3x3" if not power2_used else "Used"
    screen.blit(font.render(label1,True,BLACK),(power1_rect.x+10,power1_rect.y+10))
    screen.blit(font.render(label2,True,BLACK),(power2_rect.x+20,power2_rect.y+10))
    
    if message:
        pygame.draw.rect(screen,WHITE,(20,135,WIDTH-40,28),border_radius=8)
        screen.blit(font.render(message,True,RED),(30,140))
    for r in range(GRID):
        for c in range(GRID):
            x=c*CELL; y=TOP+r*CELL
            pygame.draw.rect(screen,TAN if revealed[r][c] else YELLOW,(x,y,CELL,CELL))
            pygame.draw.rect(screen,BLACK,(x,y,CELL,CELL),2)
            if revealed[r][c]:
                if board[r][c]=="treasure":
                    screen.blit(font.render("$",True,GREEN),(x+22,y+18))
                elif board[r][c]=="bomb":
                    screen.blit(font.render("X",True,RED),(x+22,y+18))

running=True
while running:
    draw()
    pygame.display.flip()
    if treasures==treasure:
        message="YOU WIN!"
        game_over=True
    if lives<=0 and not game_over:
        message="GAME OVER"
        game_over=True
        reveal_all()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            mx,my=pygame.mouse.get_pos()
            if power1_rect.collidepoint((mx,my)) and not power1_used:
                power1_used=True
                row = random.randint(0, GRID - 1)
                col = random.randint(0, GRID - 1)
                for c in range(GRID):
                    reveal_cell(row, c, count_bombs=False)
                for r in range(GRID):
                    reveal_cell(r, col, count_bombs=False)
                message = "Row and column revealed!"
            elif power2_rect.collidepoint((mx,my)) and not power2_used:
                power2_used=True
                top = random.randint(0, GRID - 3)
                left = random.randint(0, GRID - 3)
                for r in range(top, top + 3):
                    for c in range(left, left + 3):
                        reveal_cell(r, c, count_bombs=False)
                message = "3x3 square revealed!"
            elif my>=TOP:
                row=(my-TOP)//CELL
                col=mx//CELL
                reveal_cell(row, col)
pygame.quit()
