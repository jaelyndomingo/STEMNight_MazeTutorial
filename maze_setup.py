from pygame.locals import *
import pygame

''' DO NOT modify this file pls '''

class Player:
    x = 44
    y = 44
    speed = 20

    def change_speed(self, new_speed):
        self.speed = new_speed

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed


class Maze:
    def __init__(self):
        self.M = 10
        self.N = 10
        self.maze = [[1,1,1,1,1,1,1,1,1,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,1,1,0,1,1,1,1,0,1],
                     [1,1,1,0,0,0,0,0,0,1],
                     [1,0,1,1,1,0,1,1,0,1],
                     [1,0,1,0,0,0,1,1,1,1],
                     [1,0,0,0,1,0,0,1,1,1],
                     [1,1,1,1,1,1,0,1,2,1],
                     [1,1,1,0,0,0,0,0,0,1],
                     [1,1,1,1,1,1,1,1,1,1]]

    def draw(self,display,maze_block,prize):
        for by in range(self.M):
            for bx in range(self.N):
                if self.maze[by][bx] == 1:
                    display.blit(maze_block, ( bx * 44 , by * 44 ) )

                elif self.maze[by][bx] == 2:
                    display.blit(prize, ( bx * 44 , by * 44 ) )



class Maze_Game:
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

    '''
    if (keys[K_LEFT]):
        Maze.player.moveLeft()

    if (keys[K_UP]):
        Maze.player.moveUp()

    if (keys[K_DOWN]):
        Maze.player.moveDown()
    '''