# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def teleport():
    agent.teleport_to_player()

def obby ():
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

def move(fblr, ud, blks):
    if fblr == 2:
        agent.move (FORWARD, blks)
    elif fblr == 1:
        agent.move (BACK, blks)
    
    if ud == 2:
        agent.move (UP, blks)
    elif ud == 1:
        agent.move (DOWN, blks)
    
    if fblr == 4:
        agent.move (LEFT, blks)
    elif fblr == 3:
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
player.on_chat ("obby", obby)
player.on_chat ("m", move)
player.on_chat ("t", turn)