"""
This class will be gather the API data for the coin
"""
import requests


class DataSource:
    def __init__(self):
        self.url = " "
        self.headers = {
            "X-RapidAPI-Key": "611f5013famsh1fc2f5d32f20cf8p1a2138jsn53b7569f471e",
            "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
        }
        self.querystring = {}

    def get_data_for_top_coins(self):
        """
        Get JSON data from coinranking api for the top 50 coins
        :return: dict
        """
        self.url = "https://coinranking1.p.rapidapi.com/coins"
        self.querystring = {
            "referenceCurrencyUuid": "yhjMzLPhuIDl", "timePeriod": "24h",
            "tiers[0]": "1", "orderBy": "marketCap", "orderDirection": "desc",
            "limit": "50", "offset": "0"
        }

        response = requests.request("GET", self.url, headers=self.headers,
                                    params=self.querystring)
        return response.json()

    def get_data_for_coin(self, uuid):
        """
        Gets the JSON for the last 24 hrs of a certain coin
        :param uuid: the specific id set by coinranking for a coin
        :return: JSON
        """
        self.url = f"https://coinranking1.p.rapidapi.com/coin/{uuid}/history"

        # we can set other parameters later
        self.querystring = {
            "referenceCurrencyUuid": "yhjMzLPhuIDl", "timePeriod": "24h"
        }
        response = requests.request("GET", self.url, headers=self.headers,
                                    params=self.querystring)
        return response.json()

    def search_for_coin(self, query):
        """
        :param query: the user's query that is entered
        :return:
        """
        query = query.replace(' ', '+')
        self.url = f"https://api.coinranking.com/v2/search-suggestions?query={query} "
        self.querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl"}

        response = requests.request("GET", self.url, headers=self.headers,
                                    params=self.querystring)
        return response.json()
