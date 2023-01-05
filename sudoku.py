FULL_BOARD = [[1,6,8, 5, 7, 2, 9,3,4], [4,5,7,3,9,1,6,2,8], [9,3,2,4,6,8,5,1,7], [6,2,9,6,5,1,7,4,3], [7,4,3,2,8,9,5,1,6],[1,5,6,3,7,4,2,8,9],[3,9,5,4,1,7,2,8,6], [8,7,2,9,6,5,1,3,4], [6,4,1,8,2,3,7,9,5]]
BOARD = [[], [], [], [], [],[],[], [], []]
IS_GAME_ENDED = False


def is_all_board_valid(full_board):
    '''
    A full board must repeat every number exactly 9 times. 
    The function count every number and append it into a list of counts
    If the list is full of 9, the function return true
    '''
    if IS_GAME_ENDED:
        counts = []
        for i in range(1, 10):
            all_numbers_in_board = [item for sublist in full_board for item in sublist]
            counts.append(all_numbers_in_board.count(i))

        if counts.count(9) == 9:
            return True

    
    return False



def main():
    return 0


def select_position(SELECTED_POSITION,draw_selector=False):
    if draw_selector and pos == SELECTED_POSITION:
        return '1'



def draw_board(full_board, draw_selector):

    for i in range(9):
        print(f' {select_position(0,draw_selector)} | {select_position(1,draw_selector)} | {select_position(2,draw_selector)} ')
        print('___|___|___')
        print(f' {select_position(3,draw_selector)} | {select_position(4,draw_selector)} | {select_position(5,draw_selector)} ')
        print('___|___|___')
        print(f' {select_position(6,draw_selector)} | {select_position(7,draw_selector)} | {select_position(8,draw_selector)} ')
        print('   |   |   ')
        return full_board

  
draw_board(FULL_BOARD)