import requests
import pprint

# Uncomment two lines below if you get status code 429 (rate limit exceeded)
# import requests_cache
# requests_cache.install_cache('cmput174_cache')

BASE_URL = "https://api.tvmaze.com"

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    dicta = requests.get(BASE_URL + "/search/shows?q=" + query)
    dictionarties = dicta.json()
    
    return dictionarties


def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    show = show['show']
    show_name = show.get('name', "?")
    
    premier = show.get('premiered', "?")
    if premier == None:
        premier = "?"
    else:
        premier = premier[0:4]
        
    ended = show.get('ended', "?")
    if type(ended) == type(None):
        ended = "?"
    elif ended != "?":
        ended = ended[0:4]
        
    genre = show.get('genres', ["?"])
        
    final = show_name + " (" + premier + "-" + ended + " "
    
    x = 0
    for i in genre[0:-1]:
        final = final + i + ", "
        x += 1
        
    if x == len(genre)-1:
        final = final + genre[-1]
        
    final = final + " )"
        
    return final



def get_seasons(show_id: int) -> list[dict]:
    """
    Get the seasons for a given show_id
    """
    dat = requests.get(BASE_URL + "/shows/" + str(show_id) + "/seasons")
    dictionaries = dat.json()
    return dictionaries



def format_season_name(season: dict) -> str:
    """
    Format the season name
    """
    number = "season " + str(season.get('number', '?'))
    start = season.get('premiereDate')[0:4]
    
    end = season.get('endDate', '?')
    if end == "?":
        end = "?"
    else:
        end = str(end[0:4])
        
    episodes = str(season.get('episodeOrder'))
    if episodes == "None":
        episodes = "?"
    
    final = number + " (" + str(start) + " - " + end + "), " + episodes + " episodes"
    
    return final

def get_episodes_of_season(season_id: int) -> list[dict]:
    """
    Get the episodes of a given season of a show
    season_id is the id (not the number!) of the season
    """
    dat = requests.get(BASE_URL + "/seasons/" + str(season_id) + "/episodes")
    dictionaries = dat.json()
    return dictionaries    
    # TODO: Implement the function

def format_episode_name(episode: dict) -> str:
    """
    Format the episode name
    """
    name = " " + episode.get('name', '?') + " "
    
    season_number = "S" + str(episode.get('season', '?'))
    
    episode_number = "E" + str(episode.get('number', '?'))
    if episode_number == "ENone":
        season_number = ""
        episode_number = " *Special*"
    
    rating = "(rating: " + str(episode.get('rating').get('average', '?')) + ")"
    if episode.get('rating').get('average') == None:
        rating = "(No Rating)"
    
    final = season_number + episode_number + name + rating
    return final


def main():
    """
    Main function 
    """ 
    
    query = input("Search for a show: ")
    results = get_shows(query)
    
    if not results:
        print("No results found")
    else:
        n = 1
        print("Here are the results:")
        
        for i in range(len(results)):
            print( str(n) + ". " + format_show_name(results[i]))
            n += 1
            
            
    print(" ")
    # SEASON           
    show_id = int(input("Select a show: "))
    
    if show_id not in range(len(results)):
        show_id = input("Incorrect input")
    else:
        show_id = results[show_id-1]['show']['id'] #-1 so its in range
        
    results = get_seasons(show_id)
    
    if not results:
        print("No results found")
    else:
        n = 1
        print("Seasons of", query + ":")
        
        for i in range(len(results)):
            print( str(n) + ". " + format_season_name(results[i]))
            n += 1
            
    # SEASON - EPISODE
    print(" ")
    season_id = int(input("Select a season: "))
    dummy_id = str(season_id)
    
    if season_id not in range(1,len(results)): # start at 1 so its in human
        season_id = input("Incorrect input")
    else:
        season_id = results[season_id-1]['id'] # -1 so its in range  
    
    results = get_episodes_of_season(season_id)
    
    if not results:
        print("No results found")
    else:
        n = 1
        print("Episodes of", query, "S" + dummy_id + ":")
        
        for i in range(len(results)):
            print( str(n) + ". " + format_episode_name(results[i]))
            n += 1

                
if __name__ == '__main__':
    main()