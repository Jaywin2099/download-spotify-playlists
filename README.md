# download-spotify-playlists
get ur user id from spotify then run the python to download all your accessible playlists audios


usage
    py download_playlists.py {user id}

format is mp3 by default. u can change this constant to Format.WAV too if u wanna

all this does is use the spotify api along with a library someone else created to download spotify playlists.
there's a better way of doing this for sure, like using spotipy or something but idgaf. this works.

all the playlists u wanna download have to be added to ur spotify profile by right clicking them and hitting 'add to profile'.
no private playlists are collected by the app.

if u wanna downlaod an album, add the whole album to a new playlist named that album. 

requirements:
    -ffmpeg
    -youtube-dl
        old versions usually throw an error so be careful. if that happens, install using:
pip install --upgrade --force-reinstall git+https://github.com/ytdl-org/youtube-dl.git"
    -ffmpy
    -spotipy
    -tldextract
    -validators
    -click
    -requests
