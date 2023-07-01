import requests
from .enums import AnimeFields

class Pymal:
    clientID = None

    def __init__(self, clientID):
        self.clientID = clientID

        r = requests.get("https://api.myanimelist.net/v2", headers={
            "X-MAL-CLIENT-ID": self.clientID
        })

        if r.json()['message'] == 'Invalid client id':
            raise Exception("Invalid client ID")
    
    def getAnimeList(self, query, limit=4):
        r = requests.get("https://api.myanimelist.net/v2/anime?q=" + query + "&limit=" + str(limit), headers={
            "X-MAL-CLIENT-ID": self.clientID
        })

        return r.json()['data']
    
    def getAnimeDetails(self, animeId, fields=AnimeFields.ALL):
        r = requests.get("https://api.myanimelist.net/v2/anime/" + str(animeId) + "?fields=" + fields.value, headers={
            "X-MAL-CLIENT-ID": self.clientID
        })

        return r.json()