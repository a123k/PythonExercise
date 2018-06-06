import collections
from sys import stdout


def find_most_common_words(file, n):
    """
    This function returns the most common words in the text file
    :param file: location of the text file
    :param n: number decides how many top occurrence needs to be returned
    :return: return top n frequently used word in the text file
    """
    words = collections.Counter()
    if isfile_text(file):

        with open(file, 'r', encoding='utf-8') as text_file:

            for line in text_file:
                # Word Definition
                # 1. Words are case Sensitive  in this Program i.e. cat , CAT , cAT are three different words
                # 2. Any item in a line which is separated by whitespace character
                # is considered as Word, by default split function splits by whitespace characters
                words.update(line.split())

        all_words = dict(words)
        all_words_list = []
        for key, value in all_words.items():
            temp = [key, value]
            all_words_list.append(temp)
        # Returning top n words from the sorted list
        return sorted(all_words_list, key=lambda x: (-x[1], x[0]))[:n]


def output_to_console(input_string):

    """
    This function prints input string to console
    :param input_string:
    :return:
    """
    print('Word - Occurrences')
    for x in input_string:
        print(*x, sep=' - ', file=stdout)

    stdout.flush()


def isfile_text(file_name):
    """
    This function check the file passed is text file or not
    :param file_name: Name of the file
    :return: True if the file is text file
    """
    is_text_file = True
    try:

        with open(file_name, "r", encoding='utf-8') as file:
                file_data = file.read(512)
    except UnicodeDecodeError:
        print('File is not a Text File')
        is_text_file = False

    return is_text_file


def run_application(file, top_n):
    """
    This main function calls common word count and stdout functions
    :param file:location of the text file
    :param top_n : top n frequently used word in the text file
    :return:
    """
    top_n_freq_word = find_most_common_words(file, top_n)
    if top_n_freq_word:
        output_to_console(top_n_freq_word)
        return top_n_freq_word
    else:
        return
