import requests
import json
import urllib
import Champion


#response = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/40653807?api_key=RGAPI-606fc1f2-a61f-4ee4-abaa-06ad9fa8bd48")
#data = response.json()
#print(response)
#for i in range(10):
#    print (data[i])


static_url = "https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"
request = requests.get(static_url)
myKeys = (request.json()['data']['Aatrox'].keys())
print(myKeys)
Aatrox = request.json()['data']['Aatrox']
#print(Aatrox)


#result = dictfilter(Aatrox, wanted_keys)
#print (result, "\n")

#print(Aatrox['stats'], "\n")

#for i in range(len(request.json()['data'])):


wanted_keys = ['id','key','stats','title','info']
dictfilter = lambda x,y: dict([ (i,x[i]) for i in x if i in set(y)])
champion_names = list(request.json()['data'].keys())
champion_dict = {}
for champion in champion_names:
    current_champ = request.json()['data'][champion]
    temp_data = dictfilter(current_champ, wanted_keys)
    myChampion = Champion.Champion(temp_data)
    champion_dict[champion] = myChampion.create_entry()
