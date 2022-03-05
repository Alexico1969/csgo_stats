import os
import requests, json

def get_csgo3(id="76561198800721901"):

    response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8CF76EF68B96295C7A2EB84E9C8904FB&steamids=" + id)
    result = json.loads(response.text)
    return result["response"]

def get_csgo4(id=76561198800721901):
    response = requests.get("http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=8CF76EF68B96295C7A2EB84E9C8904FB&steamid=" + id)
    result = json.loads(response.text)
    return result["playerstats"]


