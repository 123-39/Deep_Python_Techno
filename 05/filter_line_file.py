"""
filter_file function
"""


def filter_file(filename, word_list):
    """
    Search list of words in file
    """
    try:
        with open(filename, "r", encoding='utf-8') as file:
            right_line = []
            lower_word_list = " ".join(word_list).lower().split()
            while True:
                file_line = file.readline().replace("\n", "")
                if file_line:
                    lower_file_line = file_line.lower().split()
                    if set(lower_word_list) & set(lower_file_line):
                        right_line.append(file_line)
                else:
                    break

            file.close()
            return right_line
    except FileNotFoundError:
        return f"There is no file '{filename}'"
