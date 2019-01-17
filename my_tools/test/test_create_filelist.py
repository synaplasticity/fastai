from os import listdir, getcwd

from my_tools.create_filelist import get_filelist, get_files_from_dir, create_subset


def test_random_file_list_20_perc():
    file_dataset = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']

    assert len(get_filelist(file_dataset, 20)) == 1


def test_random_file_list_20_perc_of_10():
    file_dataset = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt',
                    'file66.txt', 'file7.txt', 'file8.txt', 'file9.txt', 'file10.txt']

    assert len(get_filelist(file_dataset, 20)) == 2


def test_random_file_list_20_perc_of_6():
    file_dataset = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt',
                    'file66.txt']

    assert len(get_filelist(file_dataset, 20)) == 1


def test_get_files_from_dir():
    assert get_files_from_dir('.')


def test_create_sub_sample_20_perc():
    inp_ds = '/home/vinod/programming/DL/fastai/my_tools/test/tmp'
    out_ds = '/home/vinod/programming/DL/fastai/my_tools/test/tmp/out'
    create_subset(inp_ds, out_ds, 20)
    assert len(listdir(out_ds)) is 1