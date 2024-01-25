def check_path_coordinates(path, board):
    """checks if a path is valid, if its rows and columns distance is at most
    1 and that there is no double coordinate in the path"""
    board_length = len(board)
    if not path:
        return None
    for i in range(len(path) - 1):
        path_i_1 = path[i][1]
        path_i_0 = path[i][0]
        if path_i_0 < 0 or path_i_1 < 0 or path_i_0 >= board_length or \
                path_i_1 >= board_length:
            return False
        if path.count(path[i]) != 1:
            return False
        if abs(path_i_0 - path[i + 1][0]) > 1:
            return False
        if abs(path_i_1 - path[i + 1][1]) > 1:
            return False
    return bool(
        path.count((path[-1])) == 1 and 0 <= path[-1][0] < board_length and
        0 <= path[-1][1] < board_length)


def path_to_word(path, board):
    """returns the word that comes out of the path coordinates that are on the
    board"""
    word = ''
    for tup in path:
        x, y = tup
        word += board[x][y]
    return word


def is_valid_path(board, path, words):
    """checks if the path is legal and if the word that its creates is
    valid- in the collection of words"""
    if type(words) != list:
        words = list(words)
    words.sort()
    if not check_path_coordinates(path, board):
        return None
    word = path_to_word(path, board)
    if not word_in_lst(word, words, 0, len(words)):
        return None
    return word


def get_board_cells(board):
    """returns cells of board"""
    return [(row, col) for col in range(len(board[0])) for row in range(
        len(board))]


def get_border_of_cell(board_height, board_length, cell):
    """function returns the cells that are the border of given cell"""
    border_cells = []
    row, col = cell
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= (row + i) < board_height and 0 <= (col + j) < board_length:
                border_cells.append((row + i, col + j))
    return border_cells


def get_words_with_starting_string(words, start):
    """returns a list of all the valid words in the words' collection that
    start with a specific start string"""
    lst = []
    word_length = len(start)
    for word in words:
        word_start = word[0: word_length]
        if word_start == start:
            lst.append(word)
        else:
            if word_start > start:
                break
    return lst


def word_in_lst(word, lst, low, high):
    """function returns true if word is in lst and False otherwise"""
    if high <= low:
        return False
    mid = (high + low) // 2
    if lst[mid] == word:
        return True
    if lst[mid] > word:
        return word_in_lst(word, lst, low, mid)
    return word_in_lst(word, lst, mid + 1, high)


def find_length_helper(n, board, words, counter, check_word, check_path,
                       last_cell, all_paths, path_count=True):
    """this is a helper function for find length n paths and n words"""
    if counter >= n:
        if word_in_lst(check_word, words, 0, len(words)):
            if path_count:  # if counting length of path, append path
                all_paths.append(check_path[:])
            else:  # if counting length of word, check if word is len n,
                # and if so append path
                if len(check_word) == n:
                    all_paths.append((check_path[:]))
        check_path.clear()
    else:
        for (r, c) in get_border_of_cell(len(board), len(board[0]), last_cell):
            # continues path with border of cell
            if (r, c) in check_path:  # if cell is in current path, go to next
                # cell
                continue
            board_r_c = board[r][c]
            current_word = check_word + board_r_c
            new_words = get_words_with_starting_string(words, current_word)
            # returns list of words that start with current word
            if len(new_words) > 0:
                if path_count is True:
                    add_count = 1  # counts path len
                else:
                    add_count = len(board_r_c)  # counts word len
                find_length_helper(n, board, new_words, counter + add_count,
                                   current_word, check_path[:] + [(r, c)],
                                   (r, c), all_paths, path_count)


def find_length_n_paths(n, board, words):
    """function returns all paths in len of n, that lead to words in words"""
    if type(words) != list:
        words = list(words)
    words.sort()
    all_paths = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            check_word = board[y][x]  # starts checking string that is in
            # board[y][x]
            new_words = get_words_with_starting_string(words, check_word)
            # returns a list of words that start with check_word
            if len(new_words) > 0:
                find_length_helper(n, board, new_words, 1, check_word,
                                   [(y, x)],
                                   (y, x), all_paths)  # continues finding path
                # around (y,x) cell
    return all_paths


def find_length_n_words(n, board, words):
    """function returns all paths to words in len n that are in words list"""
    if type(words) != list:
        words = list(words)
    words.sort()
    all_paths = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            check_word = board[y][x]  # starts checking string that is in
            # board[y][x]
            new_words = get_words_with_starting_string(words, check_word)
            # returns a list of words that start with check_word
            if len(new_words) > 0:
                find_length_helper(n, board, new_words, len(board[y][x]),
                                   check_word, [(y, x)],
                                   (y, x), all_paths, False)
                # continues finding path around (y,x) cell
    return all_paths


def longer_list_path(list_path):
    """function returns the longest path in list path"""
    return max(list_path, key=len)


def max_score_paths(board, words):
    """returns list of paths to every word in words, that gives the highest
    score"""
    list_max_scores = []
    for word in words:
        paths = find_length_n_words(len(word), board, [word])
        if len(paths) > 0:
            list_max_scores.append(longer_list_path(paths))
    return list_max_scores
