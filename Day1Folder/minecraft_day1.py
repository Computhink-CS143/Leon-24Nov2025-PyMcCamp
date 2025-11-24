# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def teleport():
    agent.teleport_to_player()

def MoveF(steps):
    agent.move (FORWARD, steps)

def MoveB(steps):
    agent.move (BACK, steps)

def MoveU(steps):
    agent.move (UP, steps)

def MoveD(steps):
    agent.move (DOWN, steps)

def MoveL(steps):
    agent.move (LEFT, steps)

def MoveR(steps):
    agent.move (RIGHT, steps)

def TurnL():
    agent.turn (LEFT)

def TurnR():
    agent.turn (RIGHT)

def obby1 ():
    agent.move (FORWARD, 4)
    agent.move (LEFT, 4)
    agent.move (FORWARD, 3)
    for i in range (3):
        agent.move (UP, 1)
        agent.move (FORWARD, 1)
    agent.move (FORWARD, 1)
    for i in range (3):
        agent.move (FORWARD, 1)
        agent.move (DOWN, 1)

def move(fb, ud, lr, blks):
    if fb == 2:
        agent.move (FORWARD, blks)
    elif fb == 1:
        agent.move (BACK, blks)
    
    if ud == 2:
        agent.move (UP, blks)
    elif ud == 1:
        agent.move (DOWN, blks)
    
    if lr == 2:
        agent.move (LEFT, blks)
    elif lr == 1:
        agent.move (RIGHT, blks)

def turn (lr, times):
    if lr == 1:
        for i in range (times):
            agent.turn (LEFT)
    elif lr == 0:
        for i in range (times):
            agent.turn (RIGHT)

################## On Chat Commands Section #####################
player.on_chat ("come", teleport)
player.on_chat ("mf", MoveF)
player.on_chat ("mb", MoveB)
player.on_chat ("mu", MoveU)
player.on_chat ("md", MoveD)
player.on_chat ("ml", MoveL)
player.on_chat ("mr", MoveR)
player.on_chat ("tl", TurnL)
player.on_chat ("tr", TurnR)
player.on_chat ("obby1", obby1)
player.on_chat ("m", move)
player.on_chat ("t", turn)