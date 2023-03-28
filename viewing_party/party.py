# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        return {"title": title, "genre": genre, "rating": rating}
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):

    average_rating = 0.0


    if not user_data["watched"]:
        return average_rating
    
    for movie in user_data["watched"]:
        average_rating += movie["rating"]
    average_rating = average_rating / len(user_data["watched"])
    return average_rating


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

