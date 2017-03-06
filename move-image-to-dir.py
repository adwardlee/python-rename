import os
import sys
import argparse
import shutil

sys.path.append('.')

parser = argparse.ArgumentParser()
parser.add_argument('--srcDir', type=str, default='/media/llj/storage/action-images/JPEGImages',help="root directory holding the frames")
parser.add_argument('--actiontxt', type = str, default='/media/llj/storage/action-images/ImageSplits/actions.txt')

args = parser.parse_args()

srcDir = args.srcDir
actiontxt = args.actiontxt

targetDir = srcDir

def read_file(file_name):
   f = open(file_name)
   content = [x.split()[0] for x in f.readlines()]
   return content[1:]

actions = read_file(actiontxt)
for fname in os.listdir(srcDir):
    if not os.path.isdir(os.path.join(srcDir, fname)):
        for prefix in actions:
            if fname.startswith(prefix):
                if not os.path.isdir(os.path.join(targetDir, prefix)):
                    os.mkdir(os.path.join(targetDir, prefix))
                shutil.move(os.path.join(srcDir, fname), os.path.join(targetDir, prefix))



