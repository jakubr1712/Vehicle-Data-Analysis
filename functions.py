import pandas as pd


def prepare_geo_state_data(states_data):
    states_info = []
    for state in states_data['results']:
        state_code = state['ste_stusps_code']
        state_name = state['ste_name'][0]
        centroid = state['geo_point_2d']
        states_info.append({
            'State_Code': state_code,
            'State_Name': state_name,
            'Lat': centroid['lat'],
            'Lon': centroid['lon']
        })
    df_states = pd.DataFrame(states_info)
    return df_states


def average_vehicle_range_by_make(data):
    df = pd.DataFrame(data)
    grouped = df.groupby(['Electric Vehicle Type', 'Make'])[
        'Electric Range'].mean().reset_index()
    return grouped


def total_vehicle_count_by_category(data_json, category, col1, col2):
    df = pd.DataFrame(data_json)
    factor_counts = df[category].value_counts().reset_index()
    factor_counts.columns = [col1, col2]
    return factor_counts


def check_vin_with_digit(vehicle_data, digit):
    return [vehicle for vehicle in vehicle_data if digit in vehicle.get('VIN (1-10)', '')]


def vehicle_price_analysis(vehicle_data):
    prices = [float(vehicle.get('Base MSRP', 0))
              for vehicle in vehicle_data if vehicle.get('Base MSRP', '')]
    return {
        "average_price": round(sum(prices) / len(prices), 2) if prices else 0,
        "median_price": sorted(prices)[len(prices) // 2] if prices else 0,
        "max_price": max(prices) if prices else 0,
        "min_price": min(prices) if prices else 0
    }


def sort_by_model_year(vehicle_data):
    return sorted(vehicle_data, key=lambda x: x.get('Model Year', 0))


def get_data_for_legislative_district(vehicle_data, district):
    return [vehicle for vehicle in vehicle_data if vehicle.get('Legislative District', None) == district]


def count_vehicles_in_county(vehicle_data, county):
    return sum(1 for vehicle in vehicle_data if vehicle.get('county', '') == county)


def filter_by_electric_type(vehicle_data):
    return [vehicle for vehicle in vehicle_data if "Electric Vehicle (PHEV)" in vehicle.get('Electric Vehicle Type', '')]


def group_by_make(vehicle_data, make):
    groups = {}
    for vehicle in vehicle_data:
        make = vehicle.get('make', make)
        if make in groups:
            groups[make].append(vehicle)
        else:
            groups[make] = [vehicle]
    return groups


def cafv_filter(vehicle_data):
    return [vehicle for vehicle in vehicle_data if vehicle.get('Clean Alternative Fuel Vehicle (CAFV) Eligibility', '') == 'Clean Alternative Fuel Vehicle Eligible']
