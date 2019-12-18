from pygame.locals import *
import pygame
import maze_setup

def main():

    # Here is where you will insert your character and block art images
    player : str = "Images/Santa-1.png.png"
    block : str = "Images/Box-1.png.png"
    prize : str = "Images/Cookies-1.png.png"


    # This is how to initialize our Maze Game
    Maze : maze_setup = maze_setup.MazeGame(player, block, prize)


    # Let's change the speed of our player
    #Maze.player.change_speed(20)



    if Maze.on_init() == False:
        Maze._running = False

    while (Maze._running):
        pygame.event.pump()
        keys = pygame.key.get_pressed()



        # Here is where you will control your character in the maze
        # This is an example of moving the player right using the right arrow key
        if (keys[K_RIGHT]):
            Maze.player.move_right()

        # Try to move the player left, up, and down using the example above
        # Hint: You will need 3 'if' statements !
        #if ('''insert code'''):

        if (keys[K_LEFT]):
            Maze.player.move_left()

        if (keys[K_UP]):
            Maze.player.move_up()

        if (keys[K_DOWN]):
            Maze.player.move_down()




        if (keys[K_ESCAPE]):
            Maze._running = False


        #Maze.prize_collected()
        Maze.on_loop()
        Maze.on_render()
    Maze.on_cleanup()


if __name__ == "__main__":
    main()