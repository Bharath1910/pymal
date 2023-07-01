import requests
from .enums import Ranking

MAL_API_ENDPOINT = "https://api.myanimelist.net/v2"

class Pymal:
    clientID: str = None

    def __getData(self, pathParams: list[str] = [], queryParams: dict = None) -> dict:
        if queryParams is None:
            queryParams = {}
        
        r = requests.get(f"{MAL_API_ENDPOINT}/{'/'.join(pathParams)}", headers={
            "X-MAL-CLIENT-ID": self.clientID
        }, params=queryParams)

        return r.json()

    def __init__(self, clientID: str) -> None:
        self.clientID = clientID
        res = self.__getData()

        if res['message'] == 'Invalid client id':
            raise Exception("Invalid client ID")
    
    def getAnimeList(self, query: str, limit: int = 4) -> list:
        res = self.__getData(['anime'], {
            "q": query,
            "limit": limit
        })

        return res['data']
    
    def getAnimeDetails(self, animeId: int, fields: list = None) -> dict:
        if fields is not None:
            fields = [field.value for field in fields]
            fields = ",".join(fields)

        res = self.__getData(['anime', str(animeId)], {
            "fields": fields
        })

        return res
    
    def getAnimeRanking(self, rankingType: Ranking, limit: int = 100):
        res = self.__getData(['anime', 'ranking'], {
            "ranking_type": rankingType.value,
            "limit": limit
        })

        return res['data']