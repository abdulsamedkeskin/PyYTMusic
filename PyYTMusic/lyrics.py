import requests
from .constants import *


class Lyrics:
    def lyrics(self, name: str, browse_id: str) -> str:
        UNAUTHORIZED_PAYLOAD.update({"browseId": f"MPREb_{browse_id}"})
        req = requests.post(LYRICS_URL, json=UNAUTHORIZED_PAYLOAD)
        res = req.json()
        try:
            results = eval(LYRICS_RESULTS)
        except:
            raise Exception("Invalid browse ID")
        for i in range(len(results)):
            if name == eval(LYRICS_NAME):
                UNAUTHORIZED_PAYLOAD['browseId'] = f"MPLYt_{browse_id}-{i+1}"
                lyrics = requests.post(LYRICS_URL, json=UNAUTHORIZED_PAYLOAD)
                result = lyrics.json()
        return {"result": eval(LYRICS)}
