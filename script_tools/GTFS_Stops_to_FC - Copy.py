# Import modules
import pandas as pd
import numpy as np
import os
#import arcpy

# Read in GTFS text files as Pandas dataframes
routes_df = pd.read_csv(r"D:\GIS Proj\ArcPro\TransLink GTFS\GTFS data\test\routes.txt", header = 0)
stops_df = pd.read_csv(r"D:\GIS Proj\ArcPro\TransLink GTFS\GTFS data\test\stops.txt", header = 0)
stop_times_df = pd.read_csv(r"D:\GIS Proj\ArcPro\TransLink GTFS\GTFS data\test\stop_times.txt", header = 0)
trips_df = pd.read_csv(r"D:\GIS Proj\ArcPro\TransLink GTFS\GTFS data\test\trips.txt", header = 0)

# Fill in missing values in the 'route_short_name' column using values in the 'route_long_name' column
for index in routes_df.index:
    if pd.isnull(routes_df.loc[index, 'route_short_name']):
        routes_df.loc[index, 'route_short_name'] = routes_df.loc[index, 'route_long_name'] 

# Merge trips_df with routes_df on 'route_id' to get route names for each trip
trips_df_merge = trips_df.merge(routes_df, how = 'left', on = 'route_id')

# Convert 'trip_id' column to string for both dataframes
trips_df_merge['trip_id'] = trips_df_merge['trip_id'].astype(str)
stop_times_df['trip_id'] = stop_times_df['trip_id'].astype(str)

# Merge trips_df_merge with stop_times_df on 'trip_id' to get all stop ids for each trip
trips_df_merge_all = trips_df_merge.merge(stop_times_df, how = 'right', on = 'trip_id')

# Create new column 'routes' from 'route_short_name' but converted to string
trips_df_merge_all['routes'] = trips_df_merge_all['route_short_name'].astype(str)

# Create new dataframe from subset of trips_df_merge_all and sort by 'stop_id'
stop_id_sort = trips_df_merge_all[['stop_id', 'routes']].sort_values(by=['stop_id'])

# Concatenate 'routes' strings for each stop_id and remove duplicates
stop_id_sort['routes'] = stop_id_sort.groupby(['stop_id'])['routes'].transform(lambda x: ', '.join(x.unique()))
stop_id_concat = stop_id_sort.drop_duplicates()

# Merge df_final with stop_id_concat on 'stop_id' to get route names for each stop
df_final = stops_df.merge(stop_id_concat, how = 'left', on = 'stop_id')

# Function to 
def fill_route(row):
    
    # Assign column values to variables
    parent = row['parent_station']
    routes = row['routes']
    
    # Check if row has a non-null 'parent_station' value
    if pd.isnull(parent) == False:
        # Find parent row from 'parent_station' value and 
        parent_row = df_final.loc[df_final['stop_id'] == parent]['routes'].index[0]
        # 
        parent_routes = df_final.loc[parent_row, "routes"]
        
        # Check if 
        if pd.isnull(parent_routes) == False:
            # If the route is already in the parent route string, skip to the next row
            if routes in parent_routes:
                next
            # Else, concatenate route to the parent route string
            else:
                df_final.loc[parent_row, "routes"] = parent_routes + ", " + routes
        else:
            df_final.loc[parent_row, "routes"] = routes

def remove_lead_zero(value):
    avalue = list((value).split(", "))

    #avalue = avalue.sort()
    nvalue = ""
    for i in avalue:
        if i.startswith("0"):
            i = int(i)
            #print(i)
        nvalue += (str(i) + ", ")
    return nvalue[:-2]    

df_final.apply(fill_route, axis=1)
df_final["routes"] = df_final["routes"].apply(remove_lead_zero)

df_final.to_csv(r"D:\GIS Proj\ArcPro\TransLink GTFS\GTFS data\test\df_final.csv")