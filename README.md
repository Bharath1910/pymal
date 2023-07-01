# Pymal

Pymal is a simple python wrapper for the [Mal API](https://myanimelist.net/apiconfig/references/api/v2). It is currently under development, use at your own risk. 

The project is not affiliated with MyAnimeList in any way. If you have any questions, feel free to open an issue.

# Usage

1. Get your client id from [MAL](https://myanimelist.net/apiconfig)
2. Create a `Pymal` object with your client id and use the object to make requests

```python

from pymal import Pymal

pymal = Pymal(clientID="your_client_id")

```
## Anime

1. Get anime list

```python
res = pymal.getAnimeList(query="Anime name")

print(res)
```

2. Get anime details

```python
res = pymal.getAnimeDetails(animeID=1735)

print(res)
```

3. Get anime ranking

```python
res = pymal.getAnimeRanking(rankingType="all", limit=10)

print(res)
```

4. Get seasonal anime

```python
res = pymal.getSeasonalAnime(year=2021, season="summer")

print(res)
```

---

Please consider donating to support the project.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/bharath1910)