import re

from utils import find_all_path_in_folder_recur, read_file


def extract_occurrences_from_one_file(string):
    # extract filename only
    # po to remove jsp and json
    return re.findall('/([^/\s]+\.(?:js|css))[^po]', string)

def extract_occurrences_from_one_file(string):
    # extract filename only
    # po to remove jsp and json
    return re.findall('/([^/\s]+\.(?:js|css))[^po]', string)


def extract_all_occurrences(path):
    all_references = []
    files = find_all_path_in_folder_recur(path)
    for filepath in files:
        # print('Looking for occurrences in the file {}'.format(filepath))
        read_data = read_file(filepath)
        all_references += extract_occurrences_from_one_file(read_data)
    return all_references
