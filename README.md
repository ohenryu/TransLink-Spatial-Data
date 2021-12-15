# TransLink Spatial Data

<b>What:</b>   
TransLink is the statutory public transit authority for the Metro Vancouver region. This GitHub repository is a collection of free, public, and ready-for-analysis TransLink datasets that I have created.

<b>Why:</b>  
While the individual municipalities within Metro Vancouver have public transit related datasets in their open data portals, there is no comprehensive data available that covers the entire region and is up to date. TransLink provides [General Transit Feed Specification (GTFS) data](https://developer.translink.ca/servicesgtfs/gtfsdata) on a regular basis but the data format is not the most user-friendly, especially for GIS analysis where data formats like .shp and .geojson are preferred. As a result, I created this data repository to provide updated region-wide TransLink datasets for use in mapping, analysis, data visualization, and more.

<b>How:</b>  
I have converted the TransLink-provided GTFS data to feature classes and shapefiles using the Public Transit Tools toolbox in ArcGIS Pro. In addition, table join and dissolve operations were performed to preserve data integrity and enhance ease of use. I will provide the Python script tools below for download.
___________________________________________________________________________
<p align="center">
<img src="images/Transit_Routes.png" width=800" height="470">
</p>  

______________________________________________________________________________
*Datasets are currently based on GTFS data released on Dec.13, 2021*

### Available Datasets:  
* Transit Routes (all)  
* SkyTrain Routes   
* Bus Routes  
* NightBus Routes  
* Rapid Transit Routes


### In Progress:
* Transit Stations (all)  
* Bus Exchanges  
* SkyTrain Stations   
* Bus Stations  
* Transit Frequency  

### Script Tools:

* [GTFS_Shape_to_FC.py](script_tools/GTFS_Shape_to_FC.py)

### Other
* [Hex color codes for major routes](other/route_colors.txt)
