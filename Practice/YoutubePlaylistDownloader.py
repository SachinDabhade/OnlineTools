# Importing libraries
import bs4 as bs
import sys
import urllib.request
import pytube

links = []


def exact_link(link):
	vid_id = link.split('=')
	# print(vid_id)
	str = ""
	for i in vid_id[0:2]:
		str += i + "="

	str_new = str[0:len(str) - 1]
	index = str_new.find("&")

	new_link = "https://www.youtube.com" + str_new[0:index]
	return new_link


url = "https://www.youtube.com/watch?v=lcJzw0JGfeE&list=PLqM7alHXFySENpNgw27MzGxLzNJuC_Kdj"
# Scraping and extracting the video
# links from the given playlist url
page = Page(url)
count = 0

soup = bs.BeautifulSoup(page.html, 'html.parser')
for link in soup.find_all('a', id='thumbnail'):

	# not using first link because it is
	# playlist link not particular video link
	if count == 0:
		count += 1
		continue
	else:
		try:
			# Prevents error for links with no href.
			vid_src = link['href']
			# print(vid_src)
			# keeping the format of link to be
			# given to pytube otherwise in some cases
			new_link = exact_link(vid_src)

			# error might occur due to this
			# print(new_link)

			# appending the link to the links array
			links.append(new_link)
		except Exception as exp:
			pass # No function necessary for invalid <a> tags.

# print(links)

# downloading each video from
# the link in the links array
for link in links:
	yt = pytube.YouTube(link)

	# Downloaded video will be the best quality video
	stream = yt.streams.filter(progressive=True,
							file_extension='mp4').order_by(
		'resolution').desc().first()
	try:
		stream.download()
		# printing the links downloaded
		print("Downloaded: ", link)
	except:
		print('Some error in downloading: ', link)


# Code 1
import pytube
link = input('Please enter a url link\n')
yt = pytube.YouTube(link)
stream = yt.streams.first()
finished = stream.download(quiet=False)
print('Download is complete')

# Code 2
from pytube import Playlist
from pytube import Channel
p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
C = Channel('https://www.youtube.com/c/ProgrammingKnowledge')
print('======')
for video in C.videos:
    print('Downloading')
    video.streams.first().download()
    print('Sachin')
    exit()
for video in p.videos:
    print(video.streams)
    # video.streams.first().download(quiet=False)
for url in p.video_urls:
    print(url)

# Code 3
import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = 'D:\\Users\\Jean-Pierre\\Downloads'

playlist = Playlist('https://www.youtube.com/playlist?list=PLzwWSJNcZTMSW-v1x6MhHFKkwrGaEgQ-L')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(quite=False, output_path=DOWNLOAD_DIR)

# Code 4
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PL6gx4Cwl9DGCkg2uj3PxUWhMDuTw3VKjM')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
playlist.download_all()

# Code 5
from pytube import Playlist

playlist = Playlist('URL')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
    urls.append(video_url)
    for url in urls:
        my_video = YouTube(url)

        print("*****************DOWNLOAD VID*************")
        print(my_video.title)

        my_video = my_video.streams.get_highest_resolution()
        path = "PATH"
        my_video.download(path)
        print("VIDEO DOWNLOAD DONNNNE")

# Code 6
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    try:
        print(video.streams.filter(file_extension='mp4'))
        stream = video.streams.get_by_itag(137) # 137 = 1080P30
        stream.download()
    except AttributeError:
        stream = video.streams.get_by_itag(22) # 22, 136 = 720P30; if 22 still don't work, try 136
        stream.download()
    except:
        print("Something went wrong.")

# Code 7
import re
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=Pd5k1hvD2apA0DwI3XMiSDqp')   
DOWNLOAD_DIR = 'D:\Video'
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    
print(len(playlist.video_urls))    
for url in playlist.video_urls:
    print(url)    
for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(DOWNLOAD_DIR)

# Code 8
# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')

#to set the name of the file
yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
