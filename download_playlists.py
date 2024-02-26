
'''

USAGE:

py download_playlists.py {user id}

format is mp3 by default. u can change this constant to Format.WAV too if u wanna
'''
from savify.types import Format, Quality
FORMAT = Format.MP3
'''
readme:

all this does is use the spotify api along with a library someone else created to download spotify playlists.
there's a better way of doing this for sure, like using spotipy or something but idgaf

all the playlists u wanna download have to be added to ur spotify profile by right clicking them and hitting 'add to profile' (if of course the playlist is private).
no private playlists are collected by the app.

if u wanna downlaod an album, add the whole album to a new playlist named that album. 

requirements:
    -ffmpeg
    -youtube-dl
        old versions usually throw an error so be careful. if that happens, install using:
        "pip install --upgrade --force-reinstall git+https://github.com/ytdl-org/youtube-dl.git"
    -ffmpy
    -spotipy
    -tldextract
    -validators
    -click
    -requests

50 lines of code added by jacob winter and not chatgpt
updated 4/28/23

'''

from requests import get
from sys import argv, exit
from json import loads
from savify import Savify
from savify.utils import PathHolder
from savify.logger import Logger
from subprocess import check_output


# this is my spotify api id and secret. don't steal pls
i='c50761c5580b418f840105280812de04'
se='7ef6d550f41841eca6bfae54708a7645'


# ------------- gets user id -------------
try:
    user = argv[1]

    if user.lower() == 'jacob':
        user = 'yx3kmxaxozsixms2a38fcnei7'

    print('getting user: ' + user)
except:
    print('need to pass user id as command line argument')
    exit()


# ------------- gets api token -------------
token = check_output('curl --silent -X POST "https://accounts.spotify.com/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id='+i+'&client_secret='+se+'"', shell=True)

token = loads(token)['access_token']


# ------------- fetches playlists ------------- 
response = get(f"https://api.spotify.com/v1/users/{user}/playlists", headers={"Authorization": f"Bearer {token}"})

playlists = response.json()

# savify downloader instance
s = Savify(api_credentials=(i,se),quality=Quality.BEST, download_format=Format.WAV,path_holder=PathHolder(downloads_path=f'{user}/'),logger=Logger('.logs/'), skip_cover_art=True)

# parses the json for playlist name and id 
for item in playlists['items']:
    n, id = item['name'], item['id']
    print('downloading', n)
    
    t = 'playlist'
    if item['href'].split('/')[4] == 'album':
        t = 'album'
    
    # updates path as playlist name for clarity
    s.path_holder = PathHolder(downloads_path=f'{user}/{n}')

    # downloads playlist into the path
    s.download(f'https://open.spotify.com/playlist/{id}')