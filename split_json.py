from __future__ import unicode_literals
import json
import youtube_dl
import multiprocessing
import io
from operator import itemgetter
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

sent_file = io.open('vs_testis1_file','w',encoding='utf8')
def download((videoname, url)):
	ydl_opts = {"outtmpl": r"{}.%(ext)s".format(videoname),
				'ignoreerrors': True}
	print 'url: ',url
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])

with open('test.story-in-sequence.json', 'r') as file1:
	data = json.load(file1)

a = data['annotations']
#b = data['sentences']
#b = sorted(b, key=lambda x: natural_keys(x['video_id']))
#video_url = list()
video_id = list()
#video_start_time = list()
video_duration = list()
category = list()
sentence = list()
video_id_sent = list()
vocabulary = list()
sent = dict()
caption = list()
for i in range(len(a)):
	if a[i][0]['text'][-2] == ' ' and a[i][0]['text'][-1] == '.':
		sent = a[i][0]['text'][:-2]
		sent_file.write(sent)
		sent_file.write('\n')
	else:
		sent_file.write(a[i][0]['text'])
		sent_file.write('\n')
	#video_url.append(a[i]['url'])
	#video_id.append(a[i]['id'])
	#category.append(a[i]['category'])
	#video_start_time.append(a[i]['start time'])
	#video_duration.append(float(a[i]['end time'])-float(a[i]['start time']))
	#category.append(a[i]['category'])

#for j in range(len(b)):
#	sentence.append(b[j]['caption'])
#	video_id_sent.append(b[j]['video_id'])
#	sent_file.write(b[j]['video_id'])
#	sent_file.write('\t')
#	sent_file.write(b[j]['caption'])
#	sent_file.write('\n')
sent_file.close()
#p = multiprocessing.Pool(5)
#p.map(download,zip(video_id,video_url))
