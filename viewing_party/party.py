
from typing import ItemsView

#wave 1
def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        new_movie = {"title": title, "genre": genre, "rating": rating,}
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data

# wave 2
def get_watched_avg_rating(user_data):
    average_rating = 0.0
    movies_watched = len(user_data["watched"])
    rating_numerator = 0
    
    for movie in user_data["watched"]:
        rating_numerator += movie["rating"]

    if len(user_data["watched"]) == 0:
        return average_rating
    else:
        average_rating = (rating_numerator / movies_watched)
        return average_rating

def get_most_watched_genre(user_data):
    genre_list = []
    genre_dict = {}
    most_frequent = ""
    frequency = 0
    
    if len(user_data["watched"]) == 0:
        return None
    
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    
    for genre in genre_list:
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1
    
    for key, value in genre_dict.items():
        if value > frequency:
            frequency = value
            most_frequent = key
    
    return most_frequent

# wave 3
def get_unique_watched(user_data):
    friend_movie_list = []
    user_movie_list = []
    unique_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movie_list.append(movie["title"])

    for movie in user_data["watched"]:
        user_movie_list.append(movie["title"])

    unique_watched = set(user_movie_list) - set(friend_movie_list)
    
    for movie in unique_watched:
        unique_list.append({"title": movie})
    
    return unique_list

def get_friends_unique_watched(user_data):
    friend_movie_list = []
    user_movie_list = []
    unique_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movie_list.append(movie["title"])
    
    for movie in user_data["watched"]:
        user_movie_list.append(movie["title"])

    unique_watched = set(friend_movie_list) - set(user_movie_list)
    
    for movie in unique_watched:
        unique_list.append({"title": movie})
    
    return unique_list

# wave 4
def get_available_recs(user_data):
    possible_recommendations = []
    host_list = []
    user_movie_list = []
    final_list = []
    friend_host_list = []

    for movie in user_data["watched"]:
        user_movie_list.append(movie["title"])

    for host in user_data["subscriptions"]:
        host_list.append(host)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in host_list:
                possible_recommendations.append(movie["title"])
                friend_host_list.append(movie["host"])

    recommendations = set(possible_recommendations) - set(user_movie_list)

    if recommendations == False:
        return None

    for item in recommendations:
        i = possible_recommendations.index(item)
        final_list.append({"title": possible_recommendations[i], "host": friend_host_list[i]})
    
    return final_list

# wave 5
def get_new_rec_by_genre(user_data):
    if user_data["watched"] == False:
        return None

    most_watched_genre = get_most_watched_genre(user_data)
    possible_recommendations = []
    user_movie_list = []
    final_list = []

    for movie in user_data["watched"]:
        user_movie_list.append(movie["title"])
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == most_watched_genre:
                possible_recommendations.append(movie["title"])

    recommendations = set(possible_recommendations) - set(user_movie_list)
    
    if recommendations == False:
        return None
    
    for item in recommendations:
        i = possible_recommendations.index(item)
        final_list.append({"title": possible_recommendations[i], "genre": most_watched_genre})
    
    return final_list
    
def get_rec_from_favorites(user_data):
    possible_recommendations = []
    user_movie_list = []
    final_list = []

    if user_data["favorites"] == False:
        recommendations = []
        return recommendations
        
    for movie in user_data["favorites"]:
        user_movie_list.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            possible_recommendations.append(movie["title"])

    recommendations = set(user_movie_list) - set(possible_recommendations)
    
    for title in recommendations:
        final_list.append({"title": title})
    
    return final_list