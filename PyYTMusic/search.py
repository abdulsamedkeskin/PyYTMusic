import requests
from typing import List, Dict
from .constants import *
from youtube_dl import YoutubeDL

ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


class Search:
    def search(self, query: str, filter: List = None, limit: int = None) -> List[Dict]:
        filters = ['songs', "albums", "artists", "playlists",
                   "videos", "community playlists"]
        if filter is not None:
            for i in filter:
                if i and i not in filters:
                    raise Exception("Invalid filter")
        UNAUTHORIZED_PAYLOAD.update({"query": query})
        req = requests.post(
            API_URL, json=UNAUTHORIZED_PAYLOAD)
        res = req.json()
        results = eval(SEARCH_RESULTS)
        search_results = []
        for i in range(len(results)):
            try:
                filter_query = (eval(FILTER)).lower()
                for _ in range(len(eval(CONTENTS))):
                    if limit == _:
                        break
                    if filter_query == "videos" or filter_query == "songs" or filter_query == "top result":
                        video_id = eval(VIDEO_ID)
                        with YoutubeDL(ydl_opts) as ydl:
                            player_url = ydl.extract_info(
                                f"https://music.youtube.com/watch?v={video_id}", download=False)
                    data = {
                        "type": filter_query,
                        "name": eval(MUSIC_NAME),
                        "thumbnails": eval(THUMBNAIL),
                    }
                    if filter is None:
                        top_result_data = {
                            "author": eval(AUTHOR),
                            "videoId": video_id,
                            "playerUrl": eval(MUSIC_URL),
                            "duration": eval(DURATION),
                        }
                        data = {**data, **top_result_data}
                        search_results.append(data)
                        raise StopIteration
                    if filter_query in filter:
                        if filter_query == "top result":
                            top_result_data = {
                                "author": eval(AUTHOR),
                                "videoId": video_id,
                                "playerUrl": eval(MUSIC_URL),
                                "duration": eval(DURATION),
                            }
                            data = {**data, **top_result_data}
                        if filter_query == "songs":
                            songs_data = {
                                "author": eval(AUTHOR),
                                "videoId": video_id,
                                "playerUrl": eval(MUSIC_URL),
                                "duration": eval(DURATION),
                                "browseId": eval(BROWSE_ID).split("_")[-1],
                            }
                            data = {**data, **songs_data}
                        if filter_query == "videos":
                            video_data = {
                                "author": eval(AUTHOR),
                                "videoId": video_id,
                                "playerUrl": eval(VIDEO_URL),
                                "videoViews": eval(VIDEO_VIEWS),
                                "duration": eval(DURATION),
                            }
                            data = {**data, **video_data}
                        if filter_query == "albums":
                            album_data = {
                                "name": eval(ALBUM_NAME),
                                "album_type": eval(ALBUM_TYPE),
                                "artist": eval(ALBUM_ARTIST),
                            }
                            data = {**data, **album_data}
                        if filter_query == "artists":
                            artists_data = {
                                "name": eval(ARTIST_NAME),
                                "subscriber": eval(ARTIST_SUBSCRIBER),
                            }
                            data = {**data, **artists_data}
                        if filter_query == "community playlists":
                            playlist_data = {
                                "name": eval(PLAYLIST_NAME),
                                "creator": eval(PLAYLIST_CREATOR),
                                "song_count": eval(PLAYLIST_SONG_COUNT),
                            }
                            data = {**data, **playlist_data}
                        search_results.append(data)
            except KeyError:
                pass
            except StopIteration:
                return {"results": search_results}
        return {
            "results": search_results,
        }
