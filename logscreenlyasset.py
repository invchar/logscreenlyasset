#!/usr/bin/env python3
import json
import datetime
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Create play log for asset from dump of playlists from Screenly API')
parser.add_argument('--screenlymanagementpath')
parser.add_argument('--dumppath')
parser.add_argument('--assettitle')
args = parser.parse_args()

screenlymanagementpath = vars(args)['screenlymanagementpath']
dumppath = vars(args)['dumppath']
assettitle = vars(args)['assettitle']


subprocess.call("{}screenlymanagement.py --action dumpPlaylists --filepath {}".format(screenlymanagementpath, dumppath), shell=True)

with open("{}data.json".format(dumppath)) as f:
	json = json.load(f)

playlists = json['playlists']

print('Playlist log')
print('Generated ' + str(datetime.datetime.now()))

for playlist in playlists:
	if any(a['title'] == assettitle for a in playlist['assets']):
		total_time = 0.0
		for asset in playlist['assets']:
			total_time += asset['duration']
		print(playlist['title'])
		print('-- Army04.png plays every ' + '{0:02.0f}:{1:02.0f}'.format(*divmod(total_time , 60)))

