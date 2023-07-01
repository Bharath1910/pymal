import requests

MAL_API_ENDPOINT = "https://api.myanimelist.net/v2"

class Pymal:
    clientID: str = None

    def __init__(self, clientID: str) -> None:
        self.clientID = clientID

        r = requests.get(MAL_API_ENDPOINT, headers={
            "X-MAL-CLIENT-ID": self.clientID
        })

        if r.json()['message'] == 'Invalid client id':
            raise Exception("Invalid client ID")
    
    def getAnimeList(self, query: str, limit: int = 4) -> list:
        r = requests.get(f"{MAL_API_ENDPOINT}/anime", headers={
            "X-MAL-CLIENT-ID": self.clientID
        }, params={
            "q": query,
            "limit": limit
        })

        return r.json()['data']
    
    def getAnimeDetails(self, animeId: int, fields: list = None) -> dict:
        if fields is not None:
            fields = [field.value for field in fields]
            fields = ",".join(fields)
        
        r = requests.get(f"{MAL_API_ENDPOINT}/anime/{animeId}", headers={
            "X-MAL-CLIENT-ID": self.clientID
        }, params={
            "fields": fields
        })

        return r.json()