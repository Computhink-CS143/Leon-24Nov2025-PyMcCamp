# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def chop():
    while True:
        agent.destroy (FORWARD)
        agent.move (FORWARD, 1)
        height = 1
        while agent.detect(AgentDetection.BLOCK, UP):
            agent.destroy (FORWARD)    
            agent.destroy (LEFT)
            agent.destroy (UP)
            agent.move (UP, 1)
            height += 1
        agent.move (DOWN, 1)
        agent.move (LEFT, 1)
        for i in range (height):
            agent.destroy (FORWARD)
            agent.move (DOWN, 1)
            agent.collect(LOG_JUNGLE)
        agent.move (FORWARD, 1)
        agent.move (RIGHT, 1)
        agent.collect(LOG_JUNGLE)
        while not agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.move (FORWARD, 1)

def mine(length):
    while True:
        for i in range (2):
            agent.destroy (DOWN)
            agent.move (DOWN, 1)
        for i in range (length):
            agent.destroy (FORWARD)
            agent.destroy (UP)
            agent.destroy (DOWN)
            agent.destroy (LEFT)
            agent.destroy (RIGHT)
            agent.move (DOWN, 1)
            agent.collect_all()
            agent.move (UP, 1)
            agent.move (FORWARD, 1)
        agent.destroy (LEFT)
        agent.destroy (RIGHT)
        agent.destroy (UP)
        agent.destroy (DOWN)
        agent.move (DOWN, 1)
        agent.collect_all()
        agent.move (UP, 1)
        agent.move (LEFT, 1)
        for i in range (2):
            for j in range (2):
               agent.turn (LEFT)
            for k in range (length):
                agent.destroy (UP)
                agent.destroy (DOWN)
                agent.move (DOWN, 1)
                agent.collect_all()
                agent.move (UP, 1)
                agent.move (FORWARD, 1)
                agent.destroy (UP)
                agent.destroy (DOWN)
                agent.move (DOWN, 1)
                agent.collect_all()
                agent.move (UP, 1)
            agent.move (LEFT, 2)

################## On Chat Commands Section #####################
player.on_chat ("chop", chop)
player.on_chat ("mine", mine)