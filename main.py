from othello import Othello


def input_move():
    x, y = input("choose a cell [separate with space]: ").split()
    move = (int(x), int(y))

    return move


if __name__ == '__main__':
    board = Othello()

    while not board.game_finished():
        board.print(options=True, turn=True, scores=True)

        move = input_move()
        board.play(move)
