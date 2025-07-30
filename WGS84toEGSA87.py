###################
# To run this script, give:
#
# -> As first argument the directory of the geojson files that
#    need to be parsed
# -> As second argument the destination directory that the .txt files that'll
#    be created from the data of the geojson files (from the first arg)
#
# ---> Note
# The directories should already exist, otherwise this program won't work
#
###################

import json
import pyproj
import os
import sys

directory = sys.argv[1]
directory_dest = "results"

# Define the source and target coordinate systems
src_proj = pyproj.Proj("EPSG:4326")  # WGS84
tgt_proj = pyproj.Proj("EPSG:2100")  # EGSA87

os.makedirs(directory_dest, exist_ok=True)

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f, "r") as ff:
            x, y = 0, 0
            json_data = ff.read()
            data = json.loads(json_data)
            coordinates = data["features"][0]["geometry"]["coordinates"][0]

            filename = filename.replace(".geojson", "")


            # Convert the coordinates from WGS84 to EGSA87
            counter = 0
            for lat, lon in coordinates:
                x, y = pyproj.transform(src_proj, tgt_proj, lon, lat)

                # Reset the coordinates inside the file, if file already exists
                # ELSE create an empty file
                if counter == 0:
                    with open(
                        directory_dest + "/" + filename + "EGSA87.txt", "w"
                    ) as file_txt:
                        file_txt.write("")
                    counter += 1

                with open(
                    directory_dest + "/" + filename + "EGSA87.txt", "a"
                ) as file_txt:
                    file_txt.write(f"{x},{y}\n")
