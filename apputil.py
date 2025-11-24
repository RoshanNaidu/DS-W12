import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt

current_board=np.array([
    1,1,1,
    1,1,1,
    1,1,1,
], dtype=int)

def update_board(current_board):
    board=current_board.reshape((3,3))
    board_pad=np.pad(board, pad_width=1, mode='constant', constant_values=0)
    neighbor_count=(board_pad[0:-2, 0:-2] + board_pad[0:-2, 1:-1] + board_pad[0:-2, 2:  ] +  # above
                    board_pad[1:-1, 0:-2]                         + board_pad[1:-1, 2:  ] +  # sides
                    board_pad[2:  , 0:-2] + board_pad[2:  , 1:-1] + board_pad[2:  , 2:  ] )  # below
    #rules
    alive=(board==1)
    survive=alive & ((neighbor_count==2)|(neighbor_count==3))
    born=(~alive) & (neighbor_count==3)
    updated_board = (survive|born).astype(int)
    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)