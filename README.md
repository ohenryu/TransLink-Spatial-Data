# TransLink Spatial Data

<b>What:</b>   
TransLink is the statutory public transit authority for the Metro Vancouver region. This GitHub repository is a collection of free, public, and ready-for-analysis TransLink datasets that I have created.

<b>Why:</b>  
While individual municipalities within Metro Vancouver have public transit related datasets in their open data portals, there is no comprehensive data publicly available that covers the entire region and is up to date. TransLink provides [General Transit Feed Specification (GTFS) data](https://developer.translink.ca/servicesgtfs/gtfsdata) on a regular basis but the data format is not very user-friendly, especially for GIS analysis where data formats like .shp and .geojson are preferred. As a result, I created this data repository to provide updated regional TransLink datasets for use in mapping, analysis, data visualization, and more.

<b>How:</b>  
I converted the TransLink-provided GTFS data to feature classes and shapefiles using the [Public Transit Tools toolbox](https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/an-overview-of-the-transit-feed-gtfs-toolset.htm) in ArcGIS Pro. In addition, table join and dissolve operations were performed to preserve data integrity and enhance ease of use. I will provide the Python script tools below for download.
___________________________________________________________________________
<p align="center">
<img src="images/Transit_Routes.png" width="766" height="450">
</p>  

______________________________________________________________________________
*Datasets are currently based on GTFS data released on Dec.13, 2021*

### Available Datasets:
__*(scroll down for download instructions)*__ 
* [Transit Routes (all)](/datasets/Transit_Routes_(ALL))   
* [SkyTrain Routes](datasets/SkyTrain_Routes)   
* [Bus Routes](datasets/Bus_Routes)
* [NightBus Routes](datasets/NightBus_Routes)  
* [Rapid Transit Routes](datasets/Rapid_Transit_Routes)


### In Progress:
* Transit Stations (all)  
* Bus Exchanges  
* SkyTrain Stations   
* Bus Stations  
* Transit Frequency  
* Datasets in geojson format  

### Script Tools:

* [GTFS_Shape_to_FC.py](script_tools/GTFS_Shape_to_FC.py)

### Other
* [Hex color codes for major routes](other/route_colors.txt)
______________________________________________________________________________
### How to Download Datasets  
* **If you want the whole repository:**  
Scroll to the top of this page, click the green button that says 'Code', and then click 'Download ZIP'.
                                                            
* **If you want a specific dataset:**  
Scroll up to the available datasets, click on your desired dataset, choose a data format, and copy the URL in your web browser. Open [downgit.github.io](https://downgit.github.io) or [download-directory.github.io](https://download-directory.github.io) and paste the URL.
