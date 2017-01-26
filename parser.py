import re

from utils import find_all_path_in_folder_recur


def extract_occurrences_from_one_file(filepath):
    # print('Looking for occurrences in the file {}'.format(filepath))
    with open(filepath, 'r', errors='ignore') as f:
        read_data = f.read()
    # extract filename only
    # po to remove jsp and json
    return re.findall('/([^/\s]+\.js)[^p]', read_data)


def extract_all_occurrences(path):
    all_references = []
    # TODO: fix to increase referencle from any file to any file
    files = find_all_path_in_folder_recur(path)
    for a_file in files:
        all_references += extract_occurrences_from_one_file(a_file)
    return all_references
