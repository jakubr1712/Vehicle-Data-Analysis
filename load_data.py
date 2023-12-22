import json

import pandas as pd
import requests


def fetch_vehicle_data(url):
    # Load data
    df = pd.read_csv(url)
    print(df.dtypes)

    # Remove unnecessary columns
    columns_to_remove = ['Electric Utility', '2020 Census Tract']
    df.drop(columns=columns_to_remove, inplace=True)

    # Remove rows where 'City' and 'Vehicle Location' are null
    df = df[df['City'].notnull() & df['Vehicle Location'].notnull()]

    # Save data
    df.to_json('vehicles_data.json', orient='records',
               force_ascii=False, indent=4)

    return 'vehicles_data.json'


def fetch_state_data(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        json_file_path = 'US_states.json'

        with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)

        print(f"Data has been successfully saved to {json_file_path}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    return json_file_path


def load_data(file_path):
    with open(f"./{file_path}", "r") as json_file:
        data = json.load(json_file)
        return data
