# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def wall (height, length):
    slot = 1
    agent.set_slot(slot)
    for i in range (2):
        agent.turn (RIGHT)
    
    agent.move (BACK, 1)
    for i in range (length - 1):
        for j in range (height):
            if agent.get_item_count(slot) == 0:
                slot += 1
                agent.set_slot(slot)
            agent.place (FORWARD)
            if i % 2 == 0:
                agent.move (UP, 1)
            else:
                agent.move (DOWN, 1)
        
        if i % 2 == 0:
            agent.move (DOWN, 1)
        
        agent.move (BACK, 1)
    if i % 2 == 1:
        agent.move (DOWN, height)

    for k in range (height):
        agent.move (UP, 1)
        if agent.get_item_count(slot) == 0:
            slot += 1
            agent.set_slot(slot)
        agent.place (DOWN)

################## On Chat Commands Section #####################
player.on_chat ("wall", wall)