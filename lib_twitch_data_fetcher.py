from requests import post as r_post, get as r_get
from json import load as j_load



##————————————————————————————————————————————————————————————————————————————##

class FileExtensionError(Exception):
    pass

class StreamNotLiveError(Exception):
    pass



##————————————————————————————————————————————————————————————————————————————##

def get_api_access_token(config_file:str) -> str:
    if (not config_file.endswith(".json")):
        raise FileExtensionError("The file must have a .json extension.")

    with open(config_file) as file:
        credentials = j_load(file)

    client_id = credentials["client_id"]
    client_secret = credentials["client_secret"]

    # Get OAuth token
    token_url = "https://id.twitch.tv/oauth2/token"
    my_params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }

    response = r_post(token_url, params=my_params)
    response.raise_for_status()

    access_token = response.json().get("access_token")
    if (not access_token):
        raise Exception("Failed to retrieve access token.")

    return access_token



##————————————————————————————————————————————————————————————————————————————##

def get_stream_name_and_game(config_file:str, token:str,
                    stream_username:str, output_format:str):

    if (not config_file.endswith(".json")):
        raise FileExtensionError("The file must have a .json extension.")

    with open(config_file) as file:
        credentials = j_load(file)

    client_id = credentials["client_id"]

    my_headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {token}"
    }

    url = f"https://api.twitch.tv/helix/streams?user_login={stream_username}"
    stream_response = r_get(url , headers=my_headers)
    stream_response.raise_for_status()

    if (not stream_response.json()["data"]):
        raise StreamNotLiveError("The stream is not live.")

    stream_data = stream_response.json()["data"][0]
    stream_title = stream_data["title"]
    game_id = stream_data["game_id"]

    game_url = f"https://api.twitch.tv/helix/games?id={game_id}"
    game_response = r_get(game_url, headers=my_headers)
    game_response.raise_for_status()
    game_name = game_response.json()["data"][0]["name"]

    if (output_format == "json"):
        raise Exception("JSON format not supported yet")
    elif (output_format != "dict"):
        raise Exception("Supported formats are 'dict' and 'json'.")
    else:
        dict_name_and_game = {
            "stream_title": stream_title,
            "game_name": game_name,
        }

        return dict_name_and_game



##————————————————————————————————————————————————————————————————————————————##

def get_dict_from_stream(username:str, config_file:str):
    token = get_api_access_token(config_file)
    my_dict = get_stream_name_and_game(config_file, token, username, 'dict')
    return my_dict



##————————————————————————————————————————————————————————————————————————————##

if (__name__ == "__main__"):
    config_file = "_config_twitch_api.json"
    example_stream_username = "couriway"

    print(get_dict_from_stream(example_stream_username, config_file))


