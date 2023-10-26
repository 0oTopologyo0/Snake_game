#導入pygame
import pygame , sys ,random , time

#利用變數設定基礎參數
FPS = 20
frame_size_x = 720
frame_size_y = 480
BLACK = (0,0,0)
WHITE = (255,255,255)
RED =(255,0,0)
BLUE =(0,0,255)
GREEN = (0,255,0)

#遊戲初始化 & 創建視窗
check_error = pygame.init()
if(check_error[1] > 0):
    print("Error"+check_error[1])
else:
    print("Game Succesfully initiailized")

game_window = pygame.display.set_mode((frame_size_x,frame_size_y))
pygame.display.set_caption("貪食蛇")
fps_controller = pygame.time.Clock()

#設定蛇的參數
square_size = 20

def init_vars():
    global head_pos,snake_body,food_pos,food_spawn ,score, direction
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body = [[120,60]]
    food_pos = [random.randrange(1,(frame_size_x//square_size))*square_size,
                random.randrange(1,(frame_size_y//square_size))*square_size,]
    food_spawn = True
    score = 0

init_vars()

def show_score(choice,color,font,size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render("Score: " + str(score) ,True ,color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x /10,15)
    else:
        score_rect.midtop = (frame_size_x/2 ,frame_size_y/1.25)
    
    game_window.blit(score_surface,score_rect)


#設定遊戲迴圈
running = True
while running:
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord("w")
                and direction != "DOWN"):
                direction = "UP"
            elif (event.key == pygame.K_DOWN or event.key == ord("s")
                and direction != "UP"):
                direction = "DOWN"
            elif (event.key == pygame.K_LEFT or event.key == ord("a")
                and direction != "RIGHT"):
                direction = "LEFT"
            elif (event.key == pygame.K_RIGHT or event.key == ord("d")
                and direction != "LEFT"):
                direction = "RIGHT"
    
    #設定蛇的方向
    if direction == "UP":
        head_pos[1] -= square_size
    elif direction =="DOWN":
        head_pos[1] += square_size
    elif direction =="LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size
    
    #設定邊界
    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    if head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    if head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

    #設定吃到飼料
    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    
    #生成食物
    if not food_spawn:
        food_pos = [random.randrange(1,(frame_size_x//square_size))*square_size,
                    random.randrange(1,(frame_size_y//square_size))*square_size,]
        food_spawn = True

    # 畫面顯示
    game_window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(game_window,GREEN,pygame.Rect(
            pos[0]+2,pos[1]+2,
            square_size,square_size))
        
    pygame.draw.rect(game_window,RED,pygame.Rect(
        food_pos[0],food_pos[1],
        square_size,square_size))
    
    show_score(1,WHITE,'consolas',20)

    pygame.display.update()
    fps_controller.tick(FPS)

pygame.quit()