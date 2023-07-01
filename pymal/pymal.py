import requests
from .enums import Ranking, Fields, Season

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
    
    def __formatFields(self, fields: list[str] or list[Fields]) -> str:
        fieldString = ""

        for field in fields:
            if type(field) is str:
                fieldString += field
            
            elif isinstance(field, Fields):
                fieldString += field.value
            
            fieldString += ","
        
        return fieldString[:-1]

    def __init__(self, clientID: str) -> None:
        self.clientID = clientID
        res = self.__getData()

        if res['message'] == 'Invalid client id':
            raise Exception("Invalid client ID")
    
    def getAnimeList(
        self, query: str, limit: int = 4,\
        fields: list[Fields] or list[str] = None\
            ) -> list:

        res = self.__getData(['anime'], {
            "q": query,
            "limit": limit,
            "fields": fields
        })

        return res['data']
    
    def getAnimeDetails(self, animeId: int, fields: list[str] or list[Fields] = None) -> dict:
        if fields is not None:
            fields = [field.value for field in fields]
            fields = ",".join(fields)

        res = self.__getData(['anime', str(animeId)], {
            "fields": fields
        })

        return res
    
    def getAnimeRanking(self, rankingType: Ranking, limit: int = 100) -> list[dict]:
        res = self.__getData(['anime', 'ranking'], {
            "ranking_type": rankingType.value,
            "limit": limit
        })

        return res['data']
    
    def test(self, fields):
        return self.__formatFields(fields)