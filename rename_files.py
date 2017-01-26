import os
import re
import sys
from os import rename
for root, subfolders, files in os.walk('/media/llj/DATA Storage/llj_test/twostreamfusion-master/data/ucf101/tvl1_flow/u'):
        for filenames in files:
            if "frame" in filenames:
                filenames = os.path.join(root,filenames)
                os.rename(filenames,filenames.replace('frame','flow_x_'))
        # for filenames in subfolders:
         # if 'ApplyEye' in filenames:
            #     filenames = os.path.join(root,filenames)
            #     os.rename(filenames,filenames.replace('ApplyEye','Applyeye'))