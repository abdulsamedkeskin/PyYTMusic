API_URL = "https://music.youtube.com/youtubei/v1/search"
LYRICS_URL = "https://music.youtube.com/youtubei/v1/browse"
SEARCH_RESULTS = "res['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']"
LYRICS_RESULTS = "res['contents']['singleColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['musicShelfRenderer']['contents']"
CONTENTS = "results[i]['musicShelfRenderer']['contents']"
LYRICS = "result['contents']['sectionListRenderer']['contents'][0]['musicDescriptionShelfRenderer']['description']['runs'][0]['text']"
LYRICS_NAME = "results[i]['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']"
MUSIC_NAME = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']"
VIDEO_ID = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['navigationEndpoint']['watchEndpoint']['videoId']"
THUMBNAIL = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['thumbnail']['musicThumbnailRenderer']['thumbnail']['thumbnails']"
DURATION = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][-1]['text']"
MUSIC_URL = "player_url['formats'][0]['url']"
VIDEO_URL = "player_url['formats'][-1]['url']"
FILTER = "results[i]['musicShelfRenderer']['title']['runs'][0]['text']"
AUTHOR = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][2]['text']"
ALBUM_NAME = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']"
ALBUM_TYPE = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']"
ALBUM_ARTIST = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][2]['text']"
ARTIST_NAME = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']"
ARTIST_SUBSCRIBER = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][2]['text']"
PLAYLIST_NAME = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']"
PLAYLIST_CREATOR = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][2]['text']"
PLAYLIST_SONG_COUNT = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][4]['text']"
VIDEO_VIEWS = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][4]['text']"
BROWSE_ID = "results[i]['musicShelfRenderer']['contents'][_]['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][-3]['navigationEndpoint']['browseEndpoint']['browseId']"
UNAUTHORIZED_PAYLOAD = {
    "context": {
        "client": {
            "clientName": "WEB_REMIX",
            "clientVersion": "1.20220808.01.00",
        },
        "request": {
            "useSsl": True,
        },
    }
}
