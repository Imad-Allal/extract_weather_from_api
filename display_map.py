import folium
import pandas as pd


def get_data_set():
    dataSet = pd.read_csv('./transformed_data.csv')
    position = dataSet[[ "city", "latitude","longitude", "temperature"]]
    return position


def display_map(position):
    map = folium.Map(location=[position.latitude.mean(), position.longitude.mean()], zoom_start=5)

    for index, location_info in position.iterrows():
        folium.Marker([location_info["latitude"], location_info["longitude"]], popup=location_info["temperature"]).add_to(map)

    return map

def main():
    position = get_data_set()
    map = display_map(position)
    map
