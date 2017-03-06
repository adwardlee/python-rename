import argparse
import os
import sys
import glob
import random

sys.path.append('.')


parser = argparse.ArgumentParser()
parser.add_argument('frame_path', type=str, help="root directory holding the frames")
parser.add_argument('--out_list_path', type=str, default='data/')
parser.add_argument('--shuffle', action='store_true', default=False)
parser.add_argument('--dataset',type=str, default='action40')

args = parser.parse_args()
frame_path = args.frame_path
out_path = args.out_list_path
shuffle = args.shuffle
dataset = args.dataset

if not os.path.isdir(out_path):
	os.mkdir(out_path)


def parse_directory(path):

   ## Parse directories holding extracted frames from standard benchmarks

    print 'parse frames under folder {}'.format(path)
    frame_folders = sorted(glob.glob(os.path.join(path, '*')))

    def count_files(directory):
        lst = os.listdir(directory)
        cnt_list = len(lst)
        return cnt_list

    # check RGB
    counts = 0
    dir_dict = list()
    for i,f in enumerate(frame_folders):
        all_cnt = count_files(f)
        counts += all_cnt
        dir_dict.append(f)

        if i % 10 == 0:
            print '{} classes parsed'.format(i)

    print '{} images analysis done'.format(counts)
    return dir_dict


def build_split_list(folders_info, shuffle=False):
    allfiles = list()
    for num, folder in enumerate(folders_info):
	files = glob.glob(os.path.join(folder,'*'))
	for x in files:		
		allfiles.append('{} {}\n'.format(x, num))
    if shuffle:
	random.shuffle(allfiles)
    return allfiles

folders_info = parse_directory(frame_path)
names = build_split_list(folders_info, shuffle)
open(os.path.join(out_path, '{}_image_train_test_split.txt'.format(dataset)), 'w').writelines(names)
