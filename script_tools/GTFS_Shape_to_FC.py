# Name: GTFS_Shape_to_FC.py
# Description: Converts GTFS shapes.txt data into polylines with route names and route type attached to each polyline.
# Date: December 14, 2021
# ====================================================================================================

# Import modules
import arcpy
import os

# Get tool parameters
gtfs_shapes = arcpy.GetParameterAsText(0)   # GTFS shapes.txt file
output_FC = arcpy.GetParameterAsText(1)     # output feature class file path
projection = arcpy.GetParameterAsText(2)    # defined projection for output

# Define variables
path, name = os.path.split(output_FC)
temp_FC_0 = path + "/temp_FC_0"
temp_FC_1 = path + "/temp_FC_1"

# Convert GTFS to feature class
arcpy.conversion.GTFSShapesToFeatures(gtfs_shapes, temp_FC_0)

# Dissolve the created transit lines
arcpy.management.Dissolve(temp_FC_0, temp_FC_1, "route_id")

# Perform table join to add route name and number to each transit line
arcpy.management.JoinField(temp_FC_1, "route_id", temp_FC_0, "route_id", ["route_short_name", "route_long_name", "route_type_text"])

# Update rows with null values in the "route_short_name" field
with arcpy.da.UpdateCursor (temp_FC_1, ["route_short_name", "route_long_name"]) as cursor:
    # Loop through rows and fill in values if null
    for row in cursor:
        if row[0] == None:
            row[0] = row[1]

        # Update cursor with new row values
        cursor.updateRow(row)

# Project dataset using the specified projection
arcpy.management.Project(temp_FC_1, output_FC, projection)

# Delete temporary feature classes from geodatabase
arcpy.management.Delete(temp_FC_0)
arcpy.management.Delete(temp_FC_1)








