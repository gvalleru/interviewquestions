from hashlib import md5
import os
from collections import defaultdict


def get_hash(file_path):
    with open(file_path, 'rb') as f:
        return md5(f.read()).hexdigest()


def find_duplicate_files(parent_dir):
    my_dict = defaultdict(list)
    for p_dir, c_dir, files in os.walk(parent_dir):
        for file_ in files:
            f_path = p_dir+"/"+file_
            my_dict[get_hash(f_path)].append(f_path)

    files_list = [x for x in my_dict.values() if len(x) > 1]
    for line in files_list:
        print line


def main():
    my_dir = "/users/gopivalleru/test"
    find_duplicate_files(my_dir)


if __name__ == '__main__':
    main()
