from constants import my_path
from parser import extract_all_occurrences
from utils import find_all_path_in_folder_recur, filter_list_only_filename, filter_list_lowercase


STATIC_FILES_EXTENSIONS = ['js', 'css']

static_files_in_filesystem = []
for extension in STATIC_FILES_EXTENSIONS:
    static_files_in_filesystem += find_all_path_in_folder_recur(my_path, extension)

static_files_in_filesystem_filename = filter_list_only_filename(static_files_in_filesystem)
static_files_in_filesystem_filename_lower = filter_list_lowercase(static_files_in_filesystem_filename)

references_path = extract_all_occurrences(my_path)
references_files = filter_list_only_filename(references_path)

print('Suspects list:')
for i in references_files:
    if i not in static_files_in_filesystem_filename and i.lower() in static_files_in_filesystem_filename_lower:
        print(i)
        # res = subprocess.check_output('find . -name "*{}*"'.format(i), stderr=subprocess.STDOUT)