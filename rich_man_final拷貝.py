# -*- coding: utf-8 -*-
"""
Created on Tue May 28 00:03:44 2024

@author: user
"""

import pygame
import sys
import random

NamesToPrice = {
    "小傑辦公室": [850, 625],
    "管一": [700, 500],
    "管二": [600, 350],
    "禮賢樓": [500, 300],
    "管圖": [350, 200],
    "教研": [400, 260],
    "總圖": [750, 550],
    "社科圖": [675, 450],
    "普通": [572, 374],
    "博雅": [460, 278],
    "新生": [380, 262],
    "共同": [300, 175],
    "小福": [512, 306],
    "小小福": [375, 258],
    "女九餐廳": [320, 180],
    "活大": [685, 482],
    "118巷": [590, 340],
    "小木屋鬆餅": [770, 570],
    "醉月湖": [608, 354],
    "新體": [342, 190],
    "水源BOT": [800, 575],
    "傅鐘": [405, 265],
    "大考中心": [490, 290],
    "捷運公館站": [715, 515],
}

################################ 機會命運
chance_cards = {"跟小傑老師打高爾夫球後去吃熱炒 等老師喝醉趁機詢問期中考題目 最後還貼心地幫老師叫uber回家 積分也跟著增加800分":800,
    '期中考偷看別人且沒被抓到 玩家的積分500分':500,
    '期中報告隊友超強 躺分躺得恰到好處 積分加600分':600,
    '55688發計程車折價券!!! 玩家積分增加400分':400,
    '管二大廳整修完畢 旋轉樓梯讓管院大樓高級感加倍 玩家積分加500':500,
    '雖然玩家平常課業繁重 但該玩的還是不能少 玩家揪三五好友去台大音樂節放鬆充電 度過美好的一週!積分加700':700,
    '小木屋鬆餅買一送一 玩家花十分鐘排隊買了藍莓鬆餅 心情超滿足，加300分':300,
    '學生證弄丟第七次:( 花費200點積分得到新的學生證!!':-200,
    '學生證弄丟第18次 但有順利找回來 加500點積分':500,
    '520看到小傑在跟多慧約會 心情大受打擊，一整天上課都提不起勁 積分扣100分':-100,
    '在醉月湖餵食禽鳥 被工友伯伯看到被訓斥一頓 上課還遲到，扣150分':-150,
    '你忘記了重要的報告截止日期 被組員白眼，扣100分':-100,
    '在總圖讀書打瞌睡 錯過開會的時間，扣50分':-50,
    '你為了參加台大杜鵑花節與音樂節 忘記完成作業，罰款 $300':-300,
    '你在小福買牛奶的期間 水源阿北把你的腳踏車拖到水源拖吊場 玩家氣到不行!!!! 積分扣200':-200,
    '教育部通過以後體恤老師與行政人員 決定教師節與勞動節大專院校皆放假 玩家的積分加500分':500,
    '你參加聚會過多 學業受到影響，罰款 $50':-50,
    '你在宿舍因為一時貪玩 弄壞了公共設施，賠償 $200':-200,
    '寫實習履歷熬夜爆肝 但獲得投顧暑假實習 加300分':300,
    '你的作業遲交 又因為受夠台北陰晴不定的天氣錯過公車 遲進教室，被微積分老師狠狠記住， 扣200分':-200,
    '該玩家參加體育課時受傷 意外被漂亮的校花帶去保健室 雖然受傷但內心超快樂，加500分':500,
    '學會邊騎腳踏車邊撐傘 上下學超方便，加300分':300,
    '週三施工不能走舟山路，繞道而行 積分減100':-100,
    '台大以後聖誕節與平安夜皆放假 積分加200分':200,
    # Add more cards as needed
}

#將自己商管程的作業給別人抄把自己積分50分隨機給另一人(或是給下一個玩家)。
#YouBike借不到自己下一回合暫停動作。
#YouBike滿車，無法還車自己下一回合暫停動作。


Chance_cards = list(chance_cards.keys())
# 移到後面 random.shuffle(Chance_cards)
# selected_Chance_cards = Chance_cards[0]

# 敘述太長需要依照空白鍵換行 
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    current_width = 0
    
    for word in words:
        word_width, _ = font.size(word + ' ')
        if current_width + word_width > max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            current_line.append(word)
            current_width += word_width
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

def draw_text(screen, text, rect, font, color, padding):
    x, y, width, height = rect
    line_height = font.get_linesize()
    lines = wrap_text(text, font, width - 2*padding)

    for line in lines:
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x + padding, y + padding))
        y += font.get_linesize() 




################################機會命運


GridToInfo = list(NamesToPrice.keys())
random.shuffle(GridToInfo)

class boardattr:
    def __init__(self, name, price, fine, playerId, color, x=0, y=0):
        self.name = name
        self.price = price
        self.fine = fine
        self.who = playerId
        self.x = x
        self.y = y
        self.color = color


class Button: 
    def __init__(self, text, position, color, hover_color, size=(100, 50)): #文字 位置 顏色 陰暗面 大小
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont('arialunicode', 20)
        self.rect = pygame.Rect(position, size)
        self.text_surf = self.font.render(text, True, BLACK)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen): 
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
            self.draw(screen)
        else:
            self.current_color = self.color
            self.draw(screen)


dice = [pygame.transform.scale(pygame.image.load('骰子拷貝/1.png'), (75, 75)),
        pygame.transform.scale(pygame.image.load('骰子拷貝/2.png'), (75, 75)),
        pygame.transform.scale(pygame.image.load('骰子拷貝/3.png'), (75, 75)),
        pygame.transform.scale(pygame.image.load('骰子拷貝/4.png'), (75, 75)),
        pygame.transform.scale(pygame.image.load('骰子拷貝/5.png'), (75, 75)),
        pygame.transform.scale(pygame.image.load('骰子拷貝/6.png'), (75, 75))]

# 初始化 Pygame
pygame.init()


# 设置游戏窗口
width, height = 800, 800
grid_size = 10  # 每边的格子数量
cell_size = width/10  # 格子的大小
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("臺大富翁")
dice_rect = pygame.Rect(width / 2-40, cell_size*2.5, 80, 80)
GridInfo = list()


# 设置颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CHANCE_COLOR=(198,78,78)
OPPORTUNITY_COLOR = (0,202,128)
LIGHT_BLUE = (173, 216, 230)
LIGHT_RED = (255, 182, 193)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 224)
LIGHT_PURPLE = (216, 191, 216)
LIGHT_ORANGE = (255, 228, 181)
CORNER_COLOR = LIGHT_BLUE
SIDE_COLORS = [LIGHT_RED, LIGHT_GREEN, LIGHT_YELLOW, LIGHT_ORANGE]
COLORS = [RED, BLUE, GREEN, YELLOW]
COLOR_NAMES = ["Red", "Blue", "Green", "Yellow"]


for i in range((grid_size-4)*4):
    color=SIDE_COLORS[i//6]
    thisGrid = boardattr(GridToInfo[i], NamesToPrice[GridToInfo[i]][0], NamesToPrice[GridToInfo[i]][1], -1, color)
    GridInfo.append(thisGrid)
color=CHANCE_COLOR
element1 = random.randint(0, 5)
thisGrid = boardattr("機會", 0, 0, -1, color)
GridInfo.insert(element1,thisGrid)
element2 = random.randint(7, 12)
thisGrid = boardattr("機會", 0, 0, -1, color)
GridInfo.insert(element2,thisGrid)
element3 = random.randint(14, 19)
thisGrid = boardattr("機會", 0, 0, -1, color)
GridInfo.insert(element3,thisGrid)
element4 = random.randint(21, 26)
thisGrid = boardattr("機會", 0, 0, -1, color)
GridInfo.insert(element4,thisGrid)
color=OPPORTUNITY_COLOR
element1 = random.randint(0, 6)
thisGrid = boardattr("命運", 0, 0, -1, color)
GridInfo.insert(element1,thisGrid)
element2 = random.randint(8, 14)
thisGrid = boardattr("命運", 0, 0, -1, color)
GridInfo.insert(element2,thisGrid)
element3 = random.randint(16, 22)
thisGrid = boardattr("命運", 0, 0, -1, color)
GridInfo.insert(element3,thisGrid)
element4 = random.randint(24, 30)
thisGrid = boardattr("命運", 0, 0, -1, color)
GridInfo.insert(element4,thisGrid)
color =CORNER_COLOR
thisGrid = boardattr("Start", 0, 0, -1, color)
GridInfo.insert(0,thisGrid)
thisGrid = boardattr("YouBike站 1 ", 0, 0, -1, color)
GridInfo.insert(9,thisGrid)
thisGrid = boardattr("監獄", 0, 0, -1, color)
GridInfo.insert(18,thisGrid)
thisGrid = boardattr("YouBike站 2 ", 0, 0, -1, color)
GridInfo.insert(27,thisGrid)


# 设置时钟
clock = pygame.time.Clock()

# 開始畫面
while True:
    screen.fill((255, 222, 173))
    font = pygame.font.SysFont('arialunicode', 40)
    message = "請選擇玩家人數"
    text_surface = font.render(message, True, BLACK)
    message_bg_rect = pygame.Rect(200, 100, 400, 70)
    pygame.draw.rect(screen, (255, 250, 205), message_bg_rect.inflate(20, 10))
    text_rect = text_surface.get_rect(midtop=message_bg_rect.midtop)
    screen.blit(text_surface, text_rect)

    rules = [
        "遊戲規則：",
        "1. 每位玩家輪流擲骰子，玩家移動對應的步數。",
        "2. 每次通過起點（繞一圈），將獲得500元。",
        "3. 如果玩家停在特殊格子，則執行特殊操作。",
        "4. 只要有人破產，就結算剩下的人誰錢最多，為贏家。",
        "5. 每位玩家起始資產2000元，請謹慎使用。",
        "6. 每場遊戲的格子位置皆為隨機"
    ]
    rules_font = pygame.font.SysFont('arialunicode', 20)
    rules_bg_rect = pygame.Rect(150, 200, 500, 250)
    pygame.draw.rect(screen, (255, 250, 205), rules_bg_rect.inflate(20, 10))
    for i, line in enumerate(rules):
        rule_surface = rules_font.render(line, True, BLACK)
        rule_rect = rule_surface.get_rect(topleft=(rules_bg_rect.left + 10, rules_bg_rect.top + 0 + i * 30))
        screen.blit(rule_surface, rule_rect)

    two_player = Button("2 Players", (340, 500), (255, 182, 193), (219, 112, 147), (120, 50))
    three_player = Button("3 Players", (340, 600), (135, 206, 235), (70, 130, 180), (120, 50))
    four_player = Button("4 Players", (340, 700), (60, 179, 113), (46, 139, 87), (120, 50))
    two_player.draw(screen)
    three_player.draw(screen)
    four_player.draw(screen)
    pygame.display.flip()
    confirm = False
    while not confirm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if two_player.is_clicked(event):
                confirm = True
                num_players = 2
            elif three_player.is_clicked(event):
                confirm = True
                num_players = 3
            elif four_player.is_clicked(event):
                confirm = True
                num_players = 4
        two_player.check_hover()
        three_player.check_hover()
        four_player.check_hover()
        clock.tick(30)
        pygame.display.flip()
    break


# 绘制游戏板


def draw_board():
    count = 0
    # 绘制上边
    font = pygame.font.SysFont('arialunicode', 15)
    font1 = pygame.font.SysFont('arialunicode', 10)
    for i in range(grid_size-1):
        GridInfo[count].x = i * cell_size
        GridInfo[count].y = 0
        rect = pygame.Rect(GridInfo[count].x, GridInfo[count].y, cell_size, cell_size)
        pygame.draw.rect(screen, GridInfo[count].color, rect)
        k = 2
        if i == 0:
            k = 1
        if GridInfo[count].who!=-1:
            house =pygame.Rect(GridInfo[count].x+cell_size-cell_size/5, GridInfo[count].y+cell_size-cell_size/5, cell_size/5, cell_size/5)
            message = f"過路費:{GridInfo[count].fine}"
            text_surface = font1.render(message, True, BLACK)
            showfine = text_surface.get_rect(center=(GridInfo[count].x + cell_size* 2/5 , GridInfo[count].y + cell_size* 9/ 10))
            pygame.draw.rect(screen, COLORS[GridInfo[count].who], house)
            screen.blit(text_surface, showfine)

        pygame.draw.rect(screen, BLACK, rect, k)
        text = font.render(GridInfo[count].name, True, BLACK)
        text_rect = text.get_rect(midtop=rect.midtop)
        screen.blit(text, text_rect)
        count += 1
    # 绘制右边
    for i in range(grid_size-1):
        GridInfo[count].x = (grid_size - 1) * cell_size
        GridInfo[count].y = i * cell_size
        rect = pygame.Rect(GridInfo[count].x, GridInfo[count].y, cell_size, cell_size)
        pygame.draw.rect(screen, GridInfo[count].color, rect)
        k = 2
        if i == 0:
            k = 1
        if GridInfo[count].who!=-1:
            house =pygame.Rect(GridInfo[count].x+cell_size-cell_size/5, GridInfo[count].y+cell_size-cell_size/5, cell_size/5, cell_size/5)
            message = f"過路費:{GridInfo[count].fine}"
            text_surface = font1.render(message, True, BLACK)
            showfine = text_surface.get_rect(center=(GridInfo[count].x + cell_size* 2/5 , GridInfo[count].y + cell_size* 9/ 10))
            pygame.draw.rect(screen, COLORS[GridInfo[count].who], house)
            screen.blit(text_surface, showfine)
        pygame.draw.rect(screen, BLACK, rect, k)
        text = font.render(GridInfo[count].name, True, BLACK)
        text_rect = text.get_rect(midtop=rect.midtop)
        screen.blit(text, text_rect)
        count += 1

    # 绘制下边
    for i in range(grid_size-1):
        GridInfo[count].x = (grid_size - 1 - i) * cell_size
        GridInfo[count].y = (grid_size - 1) * cell_size
        rect = pygame.Rect(GridInfo[count].x, GridInfo[count].y, cell_size, cell_size)
        pygame.draw.rect(screen, GridInfo[count].color, rect)
        k = 2
        if i == 0:
            k = 1
        if GridInfo[count].who!=-1:
            house =pygame.Rect(GridInfo[count].x+cell_size-cell_size/5, GridInfo[count].y+cell_size-cell_size/5, cell_size/5, cell_size/5)
            message = f"過路費:{GridInfo[count].fine}"
            text_surface = font1.render(message, True, BLACK)
            showfine = text_surface.get_rect(center=(GridInfo[count].x + cell_size* 2/5 , GridInfo[count].y + cell_size* 9/ 10))
            pygame.draw.rect(screen, COLORS[GridInfo[count].who], house)
            screen.blit(text_surface, showfine)
        pygame.draw.rect(screen, BLACK, rect, k)
        text = font.render(GridInfo[count].name, True, BLACK)
        text_rect = text.get_rect(midtop=rect.midtop)
        screen.blit(text, text_rect)
        count += 1

    # 绘制左边
    for i in range(grid_size-1):
        GridInfo[count].x = 0
        GridInfo[count].y = (grid_size - 1 - i) * cell_size
        rect = pygame.Rect(GridInfo[count].x, GridInfo[count].y, cell_size, cell_size)
        pygame.draw.rect(screen, GridInfo[count].color, rect)
        k = 2
        if i == 0:
            k = 1
        if GridInfo[count].who!=-1:
            house =pygame.Rect(GridInfo[count].x+cell_size-cell_size/5, GridInfo[count].y+cell_size-cell_size/5, cell_size/5, cell_size/5)
            message = f"過路費:{GridInfo[count].fine}"
            text_surface = font1.render(message, True, BLACK)
            showfine = text_surface.get_rect(center=(GridInfo[count].x + cell_size* 2/5 , GridInfo[count].y + cell_size* 9/ 10))
            pygame.draw.rect(screen, COLORS[GridInfo[count].who], house)
            screen.blit(text_surface, showfine)
        pygame.draw.rect(screen, BLACK, rect, k)
        text = font.render(GridInfo[count].name, True, BLACK)
        text_rect = text.get_rect(midtop=rect.midtop)
        screen.blit(text, text_rect)
        count += 1

# 绘制玩家


def draw_players(positions, colors):
    player_positions = {}
    for idx, position in enumerate(positions):
        if position not in player_positions:
            player_positions[position] = []
        player_positions[position].append(colors[idx])

    for position, player_colors in player_positions.items():
        x = GridInfo[position].x+cell_size/2
        y = GridInfo[position].y+cell_size/2
        offset = 0
        for player_color in player_colors:
            pygame.draw.circle(screen, player_color,(x, y + offset), (cell_size-40) // 2 - 5)
            offset += 10


# 绘制当前玩家信息


def draw_current_player_message(current_player, color):
    font = pygame.font.Font(None, 36)
    message = f"{COLOR_NAMES[current_player]} Player's Turn"
    text_surface = font.render(message, True, BLACK)
    message_bg_rect = text_surface.get_rect(
        center=(width // 2, height - cell_size - 50))
    pygame.draw.rect(screen, color, message_bg_rect.inflate(20, 10))
    screen.blit(text_surface, message_bg_rect)


# 绘制玩家金钱信息


def draw_player_money(player_money):
    font = pygame.font.Font(None, 24)
    for idx, money in enumerate(player_money):
        message = f"{COLOR_NAMES[idx]}: ${money}"
        text_surface = font.render(message, True, BLACK)
        screen.blit(text_surface, (width // 2-40,6*cell_size + 30 * (idx + 1)))



player_positions = [0] * num_players
player_colors = COLORS[:num_players]
player_money = [2000] * num_players
current_player = 0
dice_result = -1
diceturn = 0
dice_image = None
rolling = Button("Roll Dice", (340, 100), (255, 215, 0), (218, 165, 32), (120, 50)) 

players_in_jail = {"0": 0,"1": 0,"2": 0,"3": 0}
while True: # 開始進行遊戲
    screen.fill(WHITE)
    draw_board()
    draw_players(player_positions, player_colors)
    draw_current_player_message(current_player, player_colors[current_player])
    rolling.draw(screen)
    
    if dice_result != -1:
        dice_image_rect = dice[dice_result].get_rect(center=dice_rect.center)
        screen.blit(dice[dice_result], dice_image_rect)
    draw_player_money(player_money)
    pygame.display.flip()
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if rolling.is_clicked(event):
            diceturn = random.randint(2, 6)
            while diceturn > 0:
                dice_result = random.randint(0, 5)
                dice_image_rect = dice[dice_result].get_rect(center=dice_rect.center)
                screen.blit(dice[dice_result], dice_image_rect)
                pygame.display.flip()
                clock.tick(10)
                diceturn -= 1
            
            if players_in_jail[str(current_player)] == 1:
                new_position = 18
                players_in_jail[str(current_player)] = 2
                
            else:
                new_position = (player_positions[current_player] + dice_result + 1) % ((grid_size-1) * 4)
                players_in_jail[str(current_player)] = 0
            
            if new_position < player_positions[current_player]:
                player_money[current_player] += 500
            player_positions[current_player] = new_position
            
            screen.fill(WHITE)
            draw_board()
            rolling.draw(screen)
            pygame.display.flip()
            draw_players(player_positions, player_colors)
            pygame.display.flip()
            
            dice_image_rect = dice[dice_result].get_rect(center=dice_rect.center)
            screen.blit(dice[dice_result], dice_image_rect)
            font = pygame.font.SysFont('arialunicode', 20)
            
            if GridInfo[new_position].who == -1 and GridInfo[new_position].name not in ["Start", "機會", "命運", "監獄","YouBike站 1 ",'YouBike站 2 '] and player_money[current_player] >= GridInfo[new_position].price:

                message1 = f"你要買{GridInfo[new_position].name}嗎？"
                text_surface1 = font.render(message1, True, BLACK)
                message2 = f"售價：${GridInfo[new_position].price},過路費：${GridInfo[new_position].fine}"
                text_surface2 = font.render(message2, True, BLACK)
                
                message_bg_rect = pygame.Rect(cell_size*2.75, cell_size*4, 4.5*cell_size, cell_size*1.8)
                inflated_bg_rect = message_bg_rect.inflate(20, 10)
                pygame.draw.rect(screen, GridInfo[new_position].color, message_bg_rect.inflate(20, 10))
                
                text_rect1 = text_surface1.get_rect(center=(inflated_bg_rect.centerx, inflated_bg_rect.centery - 12))
                text_rect1.y -= 35
                text_rect2 = text_surface2.get_rect(center=(inflated_bg_rect.centerx, inflated_bg_rect.centery + 12))
                text_rect2.y -= 28
                screen.blit(text_surface1, text_rect1)
                screen.blit(text_surface2, text_rect2)
                confirm_button = Button("確認", (300, 200), (155, 236, 173), (128, 189, 142))
                reject_button = Button("拒絕", (450, 200), (215, 122, 128), (188, 75, 75))
                confirm_button.rect.topleft = (message_bg_rect.left + 50, message_bg_rect.bottom - 60)
                confirm_button.text_rect = confirm_button.text_surf.get_rect(center = confirm_button.rect.center)
                reject_button.rect.topleft = (message_bg_rect.right - 150, message_bg_rect.bottom - 60)
                reject_button.text_rect = reject_button.text_surf.get_rect(center = reject_button.rect.center)
                confirm_button.draw(screen)
                reject_button.draw(screen)
                pygame.display.flip()
                confirm = False
                
                while not confirm:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if confirm_button.is_clicked(event):
                            confirm = True
                            GridInfo[new_position].who = current_player
                            player_money[current_player] -= GridInfo[new_position].price
                        elif reject_button.is_clicked(event):
                            confirm = True
                    confirm_button.check_hover()
                    reject_button.check_hover()
                    clock.tick(30)
                    draw_player_money(player_money)
                    draw_current_player_message(current_player, player_colors[current_player])
                    pygame.display.flip()
                    
            elif GridInfo[new_position].who != -1 and GridInfo[new_position].who!= current_player and GridInfo[new_position].name not in ["Start", "機會", "命運", "監獄","YouBike站"]:
                font = pygame.font.Font(None, 24)
                message1 = f"+${GridInfo[new_position].fine}"
                text_surface1 = font.render(message1, True, RED)
                screen.blit(text_surface1, (width // 2+67, 6*cell_size + 30 * (GridInfo[new_position].who+1)))
                message2 = f"-${GridInfo[new_position].fine}"
                text_surface2 = font.render(message2, True, GREEN)
                screen.blit(text_surface2, (width // 2+67, 6*cell_size + 30 * (current_player+1)))
                draw_player_money(player_money)
                draw_current_player_message(current_player, color)
                pygame.display.flip()
                pygame.time.wait(2000)
                player_money[current_player] -= GridInfo[new_position].fine
                player_money[GridInfo[new_position].who] += GridInfo[new_position].fine
            
            
            
            if GridInfo[new_position].name in ["機會", "命運"]:
                random.shuffle(Chance_cards)
                selected_Chance_cards = Chance_cards[0]
            
                message_bg_rect = pygame.Rect(cell_size*2.75, cell_size*4, 4.5*cell_size, cell_size*1.8).inflate(20, 10)
                pygame.draw.rect(screen, GridInfo[new_position].color, message_bg_rect)
                font = pygame.font.SysFont('arialunicode', 20)
                draw_text(screen, selected_Chance_cards, message_bg_rect, font, pygame.Color('black'), 10)

                confirm_button = Button("確認", (300, 200), (155, 236, 173), (128, 189, 142))
                confirm_button.rect.topleft = (message_bg_rect.right - 120, message_bg_rect.bottom - 60)
                confirm_button.text_rect = confirm_button.text_surf.get_rect(center = confirm_button.rect.center)

                confirm_button.draw(screen)
                pygame.display.flip()
                confirm = False
                while not confirm:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if confirm_button.is_clicked(event):
                            confirm = True
                            Chance_cards
                            player_money[current_player] += chance_cards[selected_Chance_cards]
                            
                        
                    
                    confirm_button.check_hover()
                    clock.tick(30)
                    draw_player_money(player_money)
                    draw_current_player_message(current_player, player_colors[current_player])
                    pygame.display.flip()
                    
            elif  GridInfo[new_position].name in ["監獄"] and players_in_jail[str(current_player)] == 0 :
                players_in_jail[str(current_player)] = 1
                message1 = '玩家停止行動一回合並扣除200點'
                text_surface1 = font.render(message1, True, BLACK)
                player_money[current_player] -= 200  # Assuming a fine of 200
                # Skip the player's next turn
                player_positions[current_player] = new_position
                
                message_bg_rect = pygame.Rect(cell_size*2.75, cell_size*4, 4.5*cell_size, cell_size*1.8).inflate(20, 10)
                pygame.draw.rect(screen, GridInfo[new_position].color, message_bg_rect)
            
                text_rect1 = text_surface1.get_rect(center=(inflated_bg_rect.centerx, inflated_bg_rect.centery - 12))
                text_rect1.y -= 35
                screen.blit(text_surface1, text_rect1)

                confirm_button = Button("確認", (300, 200), (155, 236, 173), (128, 189, 142))
                confirm_button.rect.topleft = (message_bg_rect.right - 120, message_bg_rect.bottom - 60)
                confirm_button.text_rect = confirm_button.text_surf.get_rect(center = confirm_button.rect.center)

                confirm_button.draw(screen)
                pygame.display.flip()
                confirm = False
                while not confirm:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if confirm_button.is_clicked(event):
                            confirm = True
                            player_money[current_player] -= 200 
                            player_positions[current_player] = new_position
                            
                    confirm_button.check_hover()
                    clock.tick(30)
                    draw_player_money(player_money)
                    draw_current_player_message(current_player, player_colors[current_player])
                    pygame.display.flip()
                
            
            elif  GridInfo[new_position].name in ["YouBike站 1 ","YouBike站 2 "]:

                # Update the player's position
                if GridInfo[new_position].name in ["YouBike站 1 "]:
                    message_move ='玩家從YouBike站 1移到 YouBike站 2.'
                    text_surface1 = font.render(message_move, True, BLACK)
                    new_position = 27
                    
                elif GridInfo[new_position].name in ["YouBike站 2 "]:
                    message_move ='玩家從YouBike站 2移到 YouBike站 1.'
                    text_surface1 = font.render(message_move, True, BLACK)
                    new_position = 9
 
                message_bg_rect = pygame.Rect(cell_size*2.75, cell_size*4, 4.5*cell_size, cell_size*1.8).inflate(20, 10)
                pygame.draw.rect(screen, GridInfo[new_position].color, message_bg_rect)
                
                text_rect1 = text_surface1.get_rect(center=(inflated_bg_rect.centerx, inflated_bg_rect.centery - 12))
                text_rect1.y -= 35
                screen.blit(text_surface1, text_rect1)

                confirm_button = Button("確認", (300, 200), (155, 236, 173), (128, 189, 142))
                confirm_button.rect.topleft = (message_bg_rect.right - 120, message_bg_rect.bottom - 60)
                confirm_button.text_rect = confirm_button.text_surf.get_rect(center = confirm_button.rect.center)

                confirm_button.draw(screen)
                pygame.display.flip()
                confirm = False
                while not confirm:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if confirm_button.is_clicked(event):
                            confirm = True
                            player_positions[current_player] = new_position
                            
                            draw_players(player_positions, player_colors)
                            draw_current_player_message(current_player, player_colors[current_player])
                
                    
                    confirm_button.check_hover()
                    clock.tick(30)
                    draw_player_money(player_money)
                    draw_current_player_message(current_player, player_colors[current_player])
                    pygame.display.flip()


            if player_money[current_player] < 0:
                break
            current_player = (current_player + 1) % num_players
    if player_money[current_player] < 0:
                break
    

wealth = max(player_money)
winner = COLOR_NAMES[player_money.index(wealth)]
while True:
    screen.fill((255, 222, 173))
    font = pygame.font.SysFont('arialunicode', 35)
    message10 = f"Winner: {winner}"
    text_surface10 = font.render(message10, True, BLACK)
    message11 = f"wealth: ${wealth}"
    text_surface11 = font.render(message11, True, BLACK)
    message_bg_rect = pygame.Rect(200, 100, 400, 70)
    pygame.draw.rect(screen, (255, 250, 205), message_bg_rect.inflate(20, 10))
    text_rect10 = text_surface10.get_rect(midtop=message_bg_rect.midtop)
    text_rect11 = text_surface11.get_rect(midtop=message_bg_rect.midtop)
    text_rect10.y -= 16
    text_rect11.y += 30
    screen.blit(text_surface10, text_rect10)
    screen.blit(text_surface11, text_rect11)
    quitbutton = Button("Quit", (340, 500), (255, 182, 193), (219, 112, 147), (120, 50))
    quitbutton.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if quitbutton.is_clicked(event):
            pygame.quit()
            sys.exit()
