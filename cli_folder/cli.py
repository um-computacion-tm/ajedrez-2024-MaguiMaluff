from game.chess import Chess

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)


def play(chess):
    try:
        chess.print_all()
        row = int(input("From Row: "))
        column = str(input("From Column: "))
        column = chess.get_column(column)
        new_row = int(input("To Row: "))
        new_col = str(input("To Column: "))
        new_col = chess.get_column(new_col)
        chess.move_piece_board(chess.get_piece(row, column), [new_row, new_col])
        end = str(input("End Game? y/n"))
        chess.end_game(end)
        chess.next_turn()

    except Exception as e:
        print('Error', e)



if __name__ == '__main__':
    main()