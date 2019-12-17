from pygame.locals import *
import pygame
import maze_setup as m

def main():

    # Here is where you will insert your character and block art images
    player = "Images/Santa-1.png.png"
    block = "Images/Box-1.png.png"
    prize = "Images/Cookies-1.png.png"

    # This is how to initialize our Maze Game
    Maze = m.Maze_Game(player, block, prize)

    # Let's change the speed of our player

    if Maze.on_init() == False:
        Maze._running = False

    while (Maze._running):
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        # Here is where you will control your character in the maze
        # This is an example of moving the player right using the right arrow key
        if (keys[K_RIGHT]):
            Maze.player.moveRight()

        # Try to move the player left, up, and down using the example above
        # Hint: You will need 3 'if' statements !
        #if ('''insert code'''):







        if (keys[K_ESCAPE]):
            Maze._running = False

        Maze.on_loop()
        Maze.on_render()
    Maze.on_cleanup()


if __name__ == "__main__":
    main()