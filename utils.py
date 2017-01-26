import glob
import os


def find_all_path_in_folder_recur(path, extension='.*'):
    files = []
    for filepath in glob.iglob('{}/**/*{}'.format(path, extension), recursive=True):
        if not os.path.isdir(filepath):
            files.append(filepath)
    return files


def get_only_filename(path):
    return path.split('/')[-1]


def filter_list_only_filename(original_list):
    return [get_only_filename(i) for i in original_list]


def filter_list_lowercase(original_list):
    return [i.lower() for i in original_list]
