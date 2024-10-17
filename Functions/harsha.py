harsha_moves = []
def algo(opponent_moves):
    '''
    Use the opponent moves to decide your next move
    Return True if you want to nuke the opponent, False otherwise
    '''
    if not opponent_moves:
        # Cooperate on the first move
        move = False
    elif opponent_moves[-1] == True:
        # If the opponent nuked last
        return True
    else:
        return False
    