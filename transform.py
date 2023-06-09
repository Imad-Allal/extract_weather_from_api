import glob
import json

import pandas as pd

import folium


def get_all_filenames():
    # this function should return a list of filenames
    files = glob.glob("raw_data_*")
    return files

def transform_one_file(filename):
    file = open(filename)
    data = json.load(file)

    listCities = []
    

    for key, value in data.items():
        cityInfos = dict()
        cityInfos["city"] = key
        cityInfos["latitude"] = value["latitude"]
        cityInfos["longitude"] = value["longitude"]
        cityInfos["temperature"] = value["current_weather"]["temperature"]
        cityInfos["time"] = value["current_weather"]["time"]
        listCities.append(cityInfos)
    return listCities

def merge_all_files_in_pandas_df(files):
    output = []
    for fname in files:
        output_one_file = transform_one_file(fname)
        output.extend(output_one_file)
    df = pd.DataFrame(output)
    return df

def drop_duplicates(df_):
    # dropping duplicated rows using a function of pandas.DataFrame
    return df_.drop_duplicates()



def main():
    files = get_all_filenames()
    print(files)

    data = transform_one_file(files[0])
    print(data)
    df = merge_all_files_in_pandas_df(files)
    df = drop_duplicates(df)
    print(df)
    df.to_csv("transformed_data.csv", index=False)


main()
