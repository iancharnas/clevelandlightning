#!/usr/bin/env python

#import cProfile
import os
import csv
import json
from geopy import distance
import glob


# Mapbox and geojson works in long, lat format
cleveland = [-81.6944, 41.4993] 
australia = [135.7637, -15.1674]

target_latitude = cleveland[1]
target_longitude = cleveland[0]
target_radius_miles = 100 


### Open all data files, produce a map marker json file for nearby lightning strikes
def main():
    
    strikes = [] # List of strike coordinates in [long, lat] format
    
    # Read all the existing CSV files and save strikes only from the target area
    for path in glob.glob("data" + os.path.sep + "*"):
        with open(path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                [latitude, longitude, strike_time, server, mds, mcg, sta] = row
                # Pay close attention, geopy works in lat, long format
                strike_coords = (latitude, longitude)
                target_coords = (target_latitude, target_longitude)
                #distance.distance is more accurate but great_circle is 20x faster. let's use it.
                if (distance.great_circle(strike_coords, target_coords).miles <= target_radius_miles):
                    strikes.append([longitude, latitude])
                    #print(row)
                    
    # Save those strikes to our geojson file
    geojson = {
        "type": "FeatureCollection",
        "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": coords}} for coords in strikes] 
    }
    json_object = json.dumps(geojson)
    with open("clevelandstrikes.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
    main()
#    cProfile.run('main()')
