import random
from os import path, listdir, rename, rmdir, mkdir
import datetime
import argparse
import sys


def get_filelist(file_dataset, perc):
    sample_size = round(len(file_dataset) * (perc/100))
    print(f'len : {len(file_dataset)}, size: {sample_size}')
    return [ file_dataset[i] for i in random.sample(range(len(file_dataset)), sample_size) ]


def get_files_from_dir(dir_abs_path):
    exclude_files = ['Thumbs.db']
    files = [f for f in listdir(dir_abs_path) if path.isfile(path.join(dir_abs_path, f)) and f not in exclude_files]
    return files


def create_subset(inp_abs_path, out_abs_path, perc):
    inp_files = get_files_from_dir(inp_abs_path)
    subset_files = get_filelist(inp_files, perc)
    
    if not path.isdir(out_abs_path):
        mkdir(out_abs_path)

    for file in subset_files:
        rename(f'{inp_abs_path}/{file}', f'{out_abs_path}/{file}') 


def main(argv):
    parser = argparse.ArgumentParser(description="Create a subset of files using 'n' percent of files from the source directory. These randomly selected files will be moved to the destination directory")

    parser.add_argument("source_dir", type=str, help="Absolute directory path with trailing / of the source files")
    parser.add_argument("destination_dir", type=str, help="Absolute directory path with trailing / of the destination wherein the subset is created")
    parser.add_argument("percentage", type=int, help="Percentage of the source files to be used to create subset")

    args = parser.parse_args(argv)

    create_subset(args.source_dir, args.destination_dir, args.percentage)

if __name__ == "__main__":
    main(sys.argv[1:])