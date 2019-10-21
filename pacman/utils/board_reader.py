def read(file_path):
    board = []
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            board.append(line.replace('\n', ''))
            line = file.readline()

        return tuple(board)
