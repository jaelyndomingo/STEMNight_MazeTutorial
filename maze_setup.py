from pygame.locals import *
import pygame

''' DO NOT modify this file pls '''

class Player:
    x = 40
    y = 40

    def __init__(self):
        self.speed = 1

    def change_speed(self, new_speed):
        self.speed = new_speed

    def move_right(self):
        if 800 - 80 > self.x:
            self.x = self.x + self.speed

    def move_left(self):
        if 40 < self.x:
            self.x = self.x - self.speed

    def move_up(self):
        if 40 < self.y:
            self.y = self.y - self.speed

    def move_down(self):
        if 600 - 80 > self.y:
            self.y = self.y + self.speed


class Maze:
    def __init__(self):
        self.M = 20
        self.N = 15
        self.maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                     [1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1],
                     [1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                     [1,2,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1],
                     [1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,1],
                     [1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1],
                     [1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1],
                     [1,1,2,1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1],
                     [1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1],
                     [1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1],
                     [1,2,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                     [1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,2,1,1],
                     [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    def draw(self,display,maze_block,prize):
        for by in range(self.N):
            for bx in range(self.M):
                if self.maze[by][bx] == 1:
                    display.blit(maze_block, ( bx * 40 , by * 40 ) )

                elif self.maze[by][bx] == 2:
                    display.blit(prize, ( bx * 40 , by * 40 ) )



class MazeGame:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self, player, block, prize):
        self._running = True
        self._display = None
        self._image_surf = player
        self._block_surf = block
        self._prize_surf = prize
        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Maze game STEM Night tutorial')
        self._running = True
        self._player = pygame.image.load(self._image_surf).convert()
        self._maze_block = pygame.image.load(self._block_surf).convert()
        self._prize = pygame.image.load(self._prize_surf).convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display.fill((0, 0, 0))
        self._display.blit(self._player, (self.player.x, self.player.y))
        self.maze.draw(self._display, self._maze_block, self._prize)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def prize_collected(self):
        if self.player.x in [40, 80, 680]:
            if self.player.y in [200,180,480,500]:
                pygame.draw.rect(self._display,(0,0,0), Rect(self.player.x,self.player.y,40,40),width=0)

    '''
    if (keys[K_LEFT]):
    Maze.player.move_left()

    if (keys[K_UP]):
        Maze.player.move_up()

    if (keys[K_DOWN]):
        Maze.player.move_down()
    '''