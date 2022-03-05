import os
import requests, json

def get_csgo3(id="76561198800721901"):

    response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8CF76EF68B96295C7A2EB84E9C8904FB&steamids=" + id)
    result = json.loads(response.text)
    return result["response"]

def get_csgo4(id="76561198800721901"):
    response = requests.get("http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=8CF76EF68B96295C7A2EB84E9C8904FB&steamid=" + id)
    result = json.loads(response.text)
    return result["playerstats"]

def get_data(player, id):
    data_dict = {}
    try:
        response = requests.get("http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=8CF76EF68B96295C7A2EB84E9C8904FB&steamid=" + id)
        result = json.loads(response.text)
        data = result["playerstats"]["stats"]
        for d in data:
            name = d['name']
            if name[:4] == "last":
                value = d['value']
                data_dict[player + "_" + name] = value
    except Exception:
        print("** ERROR ** Player probably set their account to private")
        data_dict['error'] = "** ERROR ** " + player + " probably set their account to private"


    return data_dict

def get_csgo5():

    data_dict = {}

    id_alex = "76561198800721901"
    id_devlin = "76561198176394198"
    id_muffin = "76561198356224120"
    id_kristiaan = "76561198049071062"

    data_alex = get_data("alex", id_alex)
    data_devlin = get_data("devlin", id_devlin)
    data_muffin = get_data("muffin", id_muffin)
    data_kristiaan = get_data("kristiaan", id_kristiaan)

    data_dict.update(data_alex)
    data_dict.update(data_devlin)
    data_dict.update(data_muffin)
    data_dict.update(data_kristiaan)

    return data_dict


