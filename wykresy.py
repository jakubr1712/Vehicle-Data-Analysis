import pandas as pd
import plotly.express as px


def map_state_vehicles(states_geo, vehicle_counts):
    df_states = states_geo.merge(vehicle_counts, on='State_Code', how='left')
    df_states['Vehicle_Count'] = df_states['Vehicle_Count'].fillna(0)

    # Create a map
    fig = px.scatter_geo(df_states,
                         lat='Lat',
                         lon='Lon',
                         hover_name='State_Name',
                         hover_data={'Vehicle_Count': True},
                         size_max=50,
                         title='Vehicle Counts by State')

    fig.update_traces(marker=dict(size=10))
    fig.update_layout(geo=dict(scope='usa'))
    fig.show()


def average_vehicle_range_chart(grouped_data):
    # Create a bar chart
    fig = px.bar(grouped_data, x='Make', y='Electric Range',
                 color='Electric Vehicle Type',
                 barmode='group',
                 height=600,
                 title='Average Electric Vehicle Range by Make and Type')

    fig.update_layout(xaxis={'categoryorder': 'total descending'},
                      xaxis_tickangle=-45)
    fig.update_xaxes(title='Make and Type')
    fig.update_yaxes(title='Average Range')
    fig.show()


def brand_share_chart(make_data):
    # Create a bar chart
    fig = px.bar(make_data, x='Make', y='Share', color='Make',
                 labels={'Make': 'Make', 'Share': 'Share'},
                 title='Vehicle Brand Share Comparison')

    fig.show()


def range_vs_price_chart(data_json):
    df = pd.DataFrame(data_json)

    # Create a scatter plot
    fig = px.scatter(df, x='Electric Range', y='Base MSRP', color='Make',
                     labels={'Electric Range': 'Electric Range',
                             'Base MSRP': 'Base MSRP'},
                     title='Relationship Between Electric Range and Base MSRP of Vehicles')

    fig.show()
