import os
import requests, json

def get_csgo3():
    response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8CF76EF68B96295C7A2EB84E9C8904FB&steamids=76561198800721901")
    result = json.loads(response.text)
    return result

def get_csgo4():
    response = requests.get("http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=440&key=8CF76EF68B96295C7A2EB84E9C8904FB&steamid=76561198800721901")
    result = json.loads(response.text)
    return result

def get_csgo():

  output = ""
  

  # Kristiaan #

  response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198049071062?TRN-Api-Key=a3915614-eac4-4c2d-be77-6a7efa91ee81")

  json_data =json.loads(response.text)

  try:
    kills = json_data['data']['segments'][0]['stats']['kills']['value']
    win_loss = json_data['data']['segments'][0]['stats']['wlPercentage']['value']
    output += f"Kristiaan has made {kills} kills, and has a win/loss ration of {win_loss} \n"
  except:
    print("------ ERROR ------")
    print()
    print("json_data: ", json_data)

  # muffin #
  
  response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198356224120?TRN-Api-Key=a3915614-eac4-4c2d-be77-6a7efa91ee81")

  json_data =json.loads(response.text)

  try:
    kills = json_data['data']['segments'][0]['stats']['kills']['value']
    win_loss = json_data['data']['segments'][0]['stats']['wlPercentage']['value']
    output += f"Muffin has made {kills} kills, and has a win/loss ration of {win_loss} \n"
  except:
    print("------ ERROR ------ MUFFIN ------")
    print()
    print("json_data: ", json_data)

  # Devlin #

  response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198176394198?TRN-Api-Key=a3915614-eac4-4c2d-be77-6a7efa91ee81")

  json_data =json.loads(response.text)


  kills = json_data['data']['segments'][0]['stats']['kills']['value']
  win_loss = json_data['data']['segments'][0]['stats']['wlPercentage']['value']
  output += f"Devlin has made {kills} kills, and has a win/loss ration of {win_loss} \n"

  # Alex #

  response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198800721901?TRN-Api-Key=a3915614-eac4-4c2d-be77-6a7efa91ee81")

  json_data =json.loads(response.text)


  kills = json_data['data']['segments'][0]['stats']['kills']['value']
  win_loss = json_data['data']['segments'][0]['stats']['wlPercentage']['value']
  output += f"Alex has made {kills} kills, and has a win/loss ration of {win_loss} \n"
  
  return output

def get_csgo2():
  output = '```'
  output += "--------------------------------\n"
  output += "--------------------------------\n"
  output += "| Name      | Kills | Win/loss |\n"
  output += "|-----------|-------|----------|\n"
  
  # Kristiaan #

  response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198049071062?TRN-Api-Key=a3915614-eac4-4c2d-be77-6a7efa91ee81")

  json_data =json.loads(response.text)

  try:
    kills = json_data['data']['segments'][0]['stats']['kills']['value']
    win_loss = json_data['data']['segments'][0]['stats']['wlPercentage']['value']
    output+= f"| Kristiaan | {kills} |   {win_loss}   |\n"
  except:
    print("------ ERROR ------")
    print()
    print("json_data: ", json_data)

  # Muffin #

  response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198356224120?TRN-Api-Key=a3915614-eac4-4c2d-be77-6a7efa91ee81")

  json_data =json.loads(response.text)

  try:
    kills = json_data['data']['segments'][0]['stats']['kills']['value']
    win_loss = json_data['data']['segments'][0]['stats']['wlPercentage']['value']
    output+= f"| Muffin    | {kills} |   {win_loss}   |\n"
  except:
    print("------ ERROR ------")
    print()
    print("json_data: ", json_data)

  # Devlin #

  response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198176394198?TRN-Api-Key=a3915614-eac4-4c2d-be77-6a7efa91ee81")

  json_data =json.loads(response.text)

  try:
    kills = json_data['data']['segments'][0]['stats']['kills']['value']
    win_loss = json_data['data']['segments'][0]['stats']['wlPercentage']['value']
    output+= f"| Devlin    |  {kills} |   {win_loss}   |\n"
  except:
    print("------ ERROR ------")
    print()
    print("json_data: ", json_data)

  # Alex #

  response = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198800721901?TRN-Api-Key=a3915614-eac4-4c2d-be77-6a7efa91ee81")

  json_data =json.loads(response.text)

  try:
    kills = json_data['data']['segments'][0]['stats']['kills']['value']
    win_loss = json_data['data']['segments'][0]['stats']['wlPercentage']['value']
    output+= f"| Alex      | {kills} |   {win_loss}   |\n"
  except:
    print("------ ERROR ------")
    print()
    print("json_data: ", json_data)





  
  output += "--------------------------------\n"
  output += '```'
  
  return output


print(get_csgo3())
print()
#print("-------------------")
#print()
#print(get_csgo4())