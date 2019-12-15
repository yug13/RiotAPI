import requests
import json
import riot_consts as Consts

class RiotAPI(object):

    def __init__(self, api_key, region = Consts.REGIONS['na']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params = {}):
        args = {'api_key' : self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                region=self.region,
                url= api_url
                ),
            params=args
            )
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by-name'].format(
            version=Consts.API_VERS['summoner'],
            summonerName=name
            )
        return self._request(api_url)

    def champion(self):
        api_url = Consts.URL['static_champion'].format(
            version=Consts.API_VERS['datadragon']
            )
        return self._request(api_url)

    def rotations(self):
        api_url = Consts.URL['rotations'].format(
            version=Consts.API_VERS['rotations']
            )
        return self._request(api_url)
