from plots import (
    average_vehicle_range_chart,
    brand_share_chart,
    map_state_vehicles,
    range_vs_price_chart,
)

from functions import (
    average_vehicle_range_by_make,
    cafv_filter,
    check_vin_with_digit,
    count_vehicles_in_county,
    filter_by_electric_type,
    get_data_for_legislative_district,
    group_by_make,
    prepare_geo_state_data,
    sort_by_model_year,
    total_vehicle_count_by_category,
    vehicle_price_analysis,
)
from load_data import fetch_state_data, fetch_vehicle_data, load_data

states_api_url = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-united-states-of-america-state-millesime/records?limit=60&refine=ste_type%3A%22state%22&refine=year%3A%222022%22'

# Loading data
vehicle_data = load_data(
    fetch_vehicle_data(
        'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD')
)

us_states_data = load_data(fetch_state_data(states_api_url))

# Generating plots and maps
average_vehicle_range_chart(
    average_vehicle_range_by_make(vehicle_data)
)

brand_share_chart(
    total_vehicle_count_by_category(
        vehicle_data, 'Make', 'Make', 'Share')
)

map_state_vehicles(
    total_vehicle_count_by_category(
        vehicle_data, 'State', 'State_Code', 'Vehicle_Count'),
    prepare_geo_state_data(us_states_data)
)

range_vs_price_chart(vehicle_data)

# Analytical functions
vin_check_results = check_vin_with_digit(vehicle_data, "2C4RC1N7")
electric_vehicles = filter_by_electric_type(vehicle_data)
vehicles_sorted = sort_by_model_year(vehicle_data)
brand_groups = group_by_make(vehicle_data, "KIA")
count_in_county = count_vehicles_in_county(vehicle_data, 'Seattle')
price_analysis = vehicle_price_analysis(vehicle_data)
cafv_vehicles = cafv_filter(vehicle_data)
data_for_district = get_data_for_legislative_district(
    vehicle_data, 10.0)

analytical_function_results = [
    ("First two vehicles in vehicle data", vehicle_data[:2]),
    ("KIA brand vehicles", brand_groups['KIA']),
    ("Number of VIN check results", len(vin_check_results)),
    ("Number of electric vehicles", len(electric_vehicles)),
    ("First two vehicles sorted by model year",
     vehicles_sorted[:2]),
    ("First two KIA brand vehicles", brand_groups['KIA'][:2]),
    ("Number of vehicles in a county", count_in_county),
    ("Vehicle price analysis", price_analysis),
    ("First two CAFV-eligible vehicles", cafv_vehicles[:2]),
    ("First two vehicles for a specific legislative district",
     data_for_district[:2]),
]

for description, data in analytical_function_results:
    print(description + ":\n")
    print(data)
    print("\n" + "="*50 + "\n")
