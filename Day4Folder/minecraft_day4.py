# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def HouseWall (length, height):
    slot1 = 2
    for i in range (4):
        agent.set_slot (1)
        for j in range (height):
            agent.place (FORWARD)
            agent.move (UP, 1)
        
        agent.move (DOWN, 1)
        agent.move (RIGHT, 1)
        agent.set_slot (slot1)
        for j in range (length - 2):
            for k in range (height):
                if agent.get_item_count(slot1) == 0:
                    slot1 += 1
                    agent.set_slot (slot1)

                agent.place (FORWARD)
                if j % 2 == 0:
                    agent.move (DOWN, 1)
                else:
                    agent.move (UP, 1)

            if j % 2 == 1:
                agent.move (DOWN, 1)
            
            agent.move (RIGHT, 1)
        agent.move (RIGHT, 1)
        agent.move (FORWARD, 1)
        agent.turn (LEFT)
        if (length - 2) % 2 == 1:
            agent.move (DOWN, height - 1)

    if length % 2 == 1:
        agent.move (RIGHT, (length - 1) / 2)
    else:
        agent.move (RIGHT, length / 2)
    agent.destroy (FORWARD)
    agent.move (UP, 1)
    agent.destroy (FORWARD)
    agent.move (DOWN, 1)
    agent.set_slot (27)
    agent.place (FORWARD)

def maze():
    while agent.detect (AgentDetection.BLOCK, DOWN):
        if not agent.detect (AgentDetection.BLOCK, LEFT):
            agent.turn (LEFT)
        else:
            if agent.detect (AgentDetection.BLOCK, FORWARD):
                agent.turn (RIGHT)
        
        agent.move (FORWARD, 1)

def dig():
    while agent.detect (AgentDetection.BLOCK, DOWN):
        agent.destroy (DOWN)
        agent.move (DOWN, 1)
        
################## On Chat Commands Section #####################