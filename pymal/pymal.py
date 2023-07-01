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
        offset: int = 0, \
        fields: list[Fields] or list[str] = None\
            ) -> list:

        res = self.__getData(['anime'], {
            "q": query,
            "limit": limit,
            "offset": offset,
            "fields": self.__formatFields(fields)
        })

        return res
    
    def getAnimeDetails(
        self, animeId: int, \
        fields: list[str] or list[Fields] = None \
            ) -> dict:

        res = self.__getData(['anime', str(animeId)], {
            "fields": self.__formatFields(fields)
        })

        return res
    
    def getAnimeRanking(
        self, 
        rankingType: Ranking or str, 
        limit: int = 100, 
        offset: int = 0,
        fields: list[str] or list[Fields] = None
            ) -> list[dict]:

        res = self.__getData(['anime', 'ranking'], {
            "ranking_type": rankingType.value,
            "limit": limit,
            "offset": offset,
            "fields": self.__formatFields(fields)
        })

        return res

    def getSeasonalAnime(
        self,
        year: int,
        season: Season or str,

        sort: str = "anime_score",
        limit: int = 100,
        offset: int = 0,
        fields: list[str] or list[Fields] = None
            ) -> list[dict]:

        res = self.__getData(['anime', 'season', str(year), season], {
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "fields": self.__formatFields(fields)
        })

        return res
