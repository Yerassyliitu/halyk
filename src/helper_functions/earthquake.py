import urllib.request
import json
import datetime


def haversine(lat1, lon1, lat2, lon2):
    """
    Вычисляет расстояние между двумя географическими координатами в километрах, используя формулу Хаверсина.

    :param lat1: Широта первой точки в градусах
    :param lon1: Долгота первой точки в градусах
    :param lat2: Широта второй точки в градусах
    :param lon2: Долгота второй точки в градусах
    :return: Расстояние между двумя точками в километрах
    """
    from math import radians, sin, cos, sqrt, atan2

    R = 6371  # Радиус Земли в километрах

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


async def fetch_earthquakes(user_latitude, user_longitude, minutes, radius):
    """
    Получает данные о землетрясениях в заданном радиусе и временном интервале от USGS API.

    :param user_latitude: Широта пользователя
    :param user_longitude: Долгота пользователя
    :param minutes: Временной интервал в минутах
    :param radius: Радиус в километрах для поиска землетрясений
    :return: Список сообщений о землетрясениях
    """
    response = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson")
    jsonResponse = json.load(response)

    current_time = datetime.datetime.now()

    all_messages = []  # Список для хранения всех сообщений о землетрясениях

    # Извлекаем данные, которые не изменяются в цикле
    features = jsonResponse["features"]
    fromtimestamp = datetime.datetime.fromtimestamp

    for index in range(len(features)):
        location = features[index]["properties"]["place"]
        magnitude = features[index]["properties"]["mag"]
        coordinates = features[index]["geometry"]["coordinates"]
        quake_latitude, quake_longitude = coordinates[1], coordinates[0]

        distance_km = haversine(user_latitude, user_longitude, quake_latitude, quake_longitude)

        # Если землетрясение в пределах заданного радиуса и произошло в течение последних N минут, добавляем сообщение
        if distance_km <= radius and (current_time - fromtimestamp(
                features[index]["properties"]["time"] / 1000.)).total_seconds() <= minutes * 60:
            time = features[index]["properties"]["time"]
            readableTime = fromtimestamp(float(time) / 1000.).strftime('%Y-%m-%d %H:%M:%S')

            message = {
                "magnitude": magnitude,
                "location": location,
                "readableTime": readableTime,
                "distance_km": distance_km
            }
            all_messages.append(message)
            print(
                f"Recent Earthquake of M {magnitude} near {location} at {readableTime}. Distance: {distance_km:.2f} km.")

    return all_messages


# Пример использования функции
# user_latitude = 43.222015
# user_longitude = 76.851250
# user_messages = get_earthquakes(user_latitude, user_longitude, minutes=5, radius=500)
# print("All Messages:", user_messages)
