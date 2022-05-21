import random

width = 8;
height = 8;

world = [[0 for i in range(height)] for j in range(width)];

#gameOver = False;

#while(not gameOver):

appleWasCreated = True;

playerX, playerY = (width//2-1, height//2-1);
playerParts = [[playerX, playerY], [playerX, playerY+1], [playerX, playerY+2]];

appleX = 0;
appleY = 0;

dividedSection = "--|----------------|--";

def setApple(boolean):
    appleWasCreated = boolean;

def createApple():

    place = 1;

    while(place == 1 or place == 2):
        appleX = random.randint(0, width-1);
        appleY = random.randint(0, height-1);
        print(appleX, appleY);
        place = world[appleX][appleY];

    world[appleX][appleY] = 3;
    print(world[appleX][appleY]);

class snake:

    def setInWorld():
        for x in range(len(playerParts)):
            if(x==0):
                pX = playerParts[x][0];
                pY = playerParts[x][1];
                world[pX][pY] = 2;
            else:
                pX = playerParts[x][0];
                pY = playerParts[x][1];
                world[pX][pY] = 1;

    def resetInWorld():
        for x in range(len(playerParts)):
            pX = playerParts[x][0];
            pY = playerParts[x][1];
            world[pX][pY] = 0;

    def updateInWorld():
        print(dividedSection);
        print("-1 : Up");
        print("-2 : Down");
        print("-3 : Right");
        print("-4 : Left");
        print(dividedSection);

        state = True;
        
        while(state):
        
            selection = input("-Select a option : ");
            up = 0;
            right = 0;

            if(selection == "1"):
                up = -1;
            elif(selection == "2"):
                up = 1;
            elif(selection == "3"):
                right = 1;
            elif(selection == "4"):
                right = -1;
            elif(selection == "quit()"):
                exit();

            if(up != 0 or right != 0):
                state = False;
        
        pX = playerParts[0][0]+right;
        pY = playerParts[0][1]+up;
        playerParts.insert(0, [pX, pY]);
        
        if(world[pX][pY] == 3):
            global appleWasCreated;
            appleWasCreated = True;
        else:
            playerParts.pop(-1);

def RenderWorld():

    print(dividedSection);
    print("--|===SNAKE GAME===|--");
    print(dividedSection);
    
    for y in range(width):
        txt = "";
        for x in range(len(world[0])):
            value = world[x][y];
            if(value == 0):
                txt = txt + "#";
            elif(value == 1):
                txt = txt + "O";
            elif(value == 2):
                txt = txt + "U";
            elif(value == 3):
                txt = txt + "@";

        print("     ",txt);

while True:
    
    snake.setInWorld();
    
    if(appleWasCreated):
        createApple();
        appleWasCreated = False;

    RenderWorld();

    snake.resetInWorld();

    snake.updateInWorld();

    for x in range(10):
        print("\n");
