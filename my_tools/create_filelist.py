import random
from os import path, listdir, rename, rmdir, mkdir
import datetime


def get_filelist(file_dataset, perc):
    sample_size = round(len(file_dataset) * (perc/100))
    print(f'len : {len(file_dataset)}, size: {sample_size}')
    return [ file_dataset[i] for i in random.sample(range(len(file_dataset)), sample_size) ]


def get_files_from_dir(dir_abs_path):
    files = [f for f in listdir(dir_abs_path) if path.isfile(path.join(dir_abs_path, f))]
    return files


def create_subset(inp_abs_path, out_abs_path, perc):
    inp_files = get_files_from_dir(inp_abs_path)
    subset_files = get_filelist(inp_files, perc)

    
    if not path.isdir(out_abs_path):
        mkdir(out_abs_path)

    for file in subset_files:
        rename(f'{inp_abs_path}/{file}', f'{out_abs_path}/{file}') 
