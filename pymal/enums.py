from enum import Enum

class AnimeFields(Enum):
    ALL = """id,title,main_picture,alternative_titles,
             start_date,end_date,synopsis,mean,rank,
             popularity,num_list_users,num_scoring_users,
             nsfw,created_at,updated_at,media_type,
             status,genres,my_list_status,num_episodes,
             start_season,broadcast,source,
             average_episode_duration,rating,pictures,
             background,related_anime,related_manga,
             recommendations,studios,statistics"""
    ID = "id"
    TITLE = "title"
    MAIN_PICTURE = "main_picture"
    ALTERNATIVE_TITLES = "alternative_titles"
    START_DATE = "start_date"
    END_DATE = "end_date"
    SYNOPSIS = "synopsis"
    MEAN = "mean"
    RANK = "rank"
    POPULARITY = "popularity"
    NUM_LIST_USERS = "num_list_users"
    NUM_SCORING_USERS = "num_scoring_users"
    NSFW = "nsfw"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    MEDIA_TYPE = "media_type"
    STATUS = "status"
    GENRES = "genres"
    MY_LIST_STATUS = "my_list_status"
    NUM_EPISODES = "num_episodes"
    START_SEASON = "start_season"
    BROADCAST = "broadcast"
    SOURCE = "source"
    AVERAGE_EPISODE_DURATION = "average_episode_duration"
    RATING = "rating"
    PICTURES = "pictures"
    BACKGROUND = "background"
    RELATED_ANIME = "related_anime"
    RELATED_MANGA = "related_manga"
    RECOMMENDATIONS = "recommendations"
    STUDIOS = "studios"
    STATISTICS = "statistics"

