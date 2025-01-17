from pygame import *
import time as tm
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_x, player_speed_y, move_keys):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.move_keys = move_keys
        self.alive = True
        self.downtiming = tm.time()
        self.movetiming = tm.time()
        self.time_rect_y = None

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def move(self):
        global fast_down
        keys = key.get_pressed()
        if keys[self.move_keys[0]] and self.rect.x > 0 and self.alive == True:
            if tm.time() - self.movetiming > 0.3:
                self.movetiming = tm.time()
                self.rect.x -= self.speed_x

        if keys[self.move_keys[1]] and self.rect.x < 225 and self.alive == True:
            if tm.time() - self.movetiming > 0.3:
                self.movetiming = tm.time()
                self.rect.x += self.speed_x

        if keys[self.move_keys[2]] and self.rect.y != height_limit and self.alive == True:
            fast_down = True
            if tm.time() - self.movetiming > 0.1:
                self.movetiming = tm.time()
                self.rect.y += self.speed_y
        else:
            fast_down = False

        if tm.time() - self.downtiming > game_speed and self.alive == True and fast_down == False:
            self.downtiming = tm.time()
            self.time_rect_y = self.rect.y
            self.rect.y += self.speed_y

    def dead(self):
        if self.rect.y == height_limit:
            self.alive = False

        for a in alive_blocks:
            if a.alive == False:
                self.alive = False
                alive_blocks.empty()

        for b in blocks:
            if self.rect.y == b.rect.y - 25 and self.rect.x == b.rect.x and not b in alive_blocks:
                self.alive = False

def clear():
    global count, timee, i
    for b in blocks:
        if b.rect.y == count: #475
            if not b in clear_list:
                clear_list.append(b)
                if len(clear_list) == 10:
                    for c in clear_list:
                        c.kill()
                        cleared_list.append(c)
                        

                        if tm.time() - timee > 0.5:
                            timee = tm.time()
                            for b in blocks:
                                if b.rect.y <= count:
                                    b.rect.y += 25

                if len(cleared_list) == 10:
                    for c in cleared_list:
                        if c in clear_list:
                            clear_list.remove(c)

    clear_list.clear()                        
    count = count - 25
    if count == 200:
        count = 475
    


def set_block():
    global block1, block2, block3, block4, alive_blocks, block_form
    block_color = choice(colors)
    block_form = choice(forms)
    if block_form == 1: #лінія
        block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
        block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
        block3 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
        block4 = Player(block_color, 100, 100, 25, 25, 25, 25, movekeys)
    elif block_form == 2: #квадрат
        block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
        block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
        block3 = Player(block_color, 125, 25, 25, 25, 25, 25, movekeys)
        block4 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
    elif block_form == 3: #зигзаг1
        block1 = Player(block_color, 125, 25, 25, 25, 25, 25, movekeys)
        block2 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
        block3 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
        block4 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
    elif block_form == 4: #зигзаг2
        block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
        block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
        block3 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
        block4 = Player(block_color, 125, 75, 25, 25, 25, 25, movekeys)
    elif block_form == 5: #трикутник
        block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
        block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
        block3 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
        block4 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
    elif block_form == 6: #кут 90 градусів1
        block1 = Player(block_color, 100, 25, 25, 25, 25, 25, movekeys)
        block2 = Player(block_color, 100, 50, 25, 25, 25, 25, movekeys)
        block3 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
        block4 = Player(block_color, 125, 75, 25, 25, 25, 25, movekeys)
    elif block_form == 7: #кут 90 градусів2
        block1 = Player(block_color, 125, 25, 25, 25, 25, 25, movekeys)
        block2 = Player(block_color, 125, 50, 25, 25, 25, 25, movekeys)
        block3 = Player(block_color, 125, 75, 25, 25, 25, 25, movekeys)
        block4 = Player(block_color, 100, 75, 25, 25, 25, 25, movekeys)
    alive_blocks.add(block1, block2, block3, block4)
    blocks.add(block1, block2, block3, block4)

img_redblock = 'redblock.png'
img_blueblock = 'blueblock.png'
img_greenblock = 'greenblock.png'
movekeys = [K_a, K_d, K_s] 

timee = tm.time()
forms = [1,2,3,4,5,6,7]
colors = [img_redblock, img_blueblock, img_greenblock]

height_limit = 475
win_width = 250
win_height = 500
display.set_caption("Pin-pong")
window = display.set_mode((win_width, win_height))

clock = time.Clock()
fps = 60
game_speed = 0.3
fast_down = False

alive_blocks = sprite.Group()
blocks = sprite.Group()

count = 475
clear_list = []
cleared_list = []

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    if not finish:
        dt = clock.tick(fps)
        
        draw.rect(window, (200,255,255), Rect(0, 0, win_width, win_height))

        if len(blocks) == 0:
            set_block()

        if len(alive_blocks) == 0:
            set_block()

        clear()

        for b in alive_blocks:
            b.move()
            b.dead()
            b.reset()

        blocks.draw(window)

        display.update()
