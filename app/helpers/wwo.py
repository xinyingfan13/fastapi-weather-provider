from fastapi import HTTPException

import requests
import os

WWO_DATETIME_URL = os.getenv("WWO_DATETIME_URL")
WWO_WEATHER_URL = os.getenv("WWO_WEATHER_URL")
WWO_KEY = os.getenv("WWO_KEY")


def get_date_time_from_wwo(cities: [str]):
    """
    get date time information for each city
    :param cities:
    :return:
    """
    timezone_list = {}
    for city in cities:
        params = {
            "q": city,
            "format": "json",
            "key": WWO_KEY,
        }
        response = requests.get(WWO_DATETIME_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            timezone = data["data"]["time_zone"][0]["localtime"]
            timezone_list[city] = timezone
        else:
            timezone_list[city] = None
    return timezone_list


def get_weather_from_wwo(cities: [str]):
    """
    get temporature for each city
    :param cities:
    :return:
    """
    temp_list = {}
    for city in cities:
        params = {
            "q": city,
            "format": "json",
            "key": WWO_KEY,
        }
        response = requests.get(WWO_WEATHER_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            temp = data["data"]["current_condition"][0]["temp_F"]
            date = data["data"]["weather"][0]["date"]
            temp_list[city] = {"date": date, "temperature": [f"{temp}F"]}
        else:
            temp_list[city] = None
    return temp_list
