
## Land Registry

This is a simple solution to translate the geo-data from the [Fields Area Measure Free](https://play.google.com/store/apps/details?id=lt.noframe.fieldsareameasure&pli=1)
application to the ones required for .gov land registry in Greece.

## Running the script

To run the script simply run: `python3 WGS84toEGSA87.py files_directory/` and provide the files directory which you want to convert from
WGS84 to EGSA87 encoding. The directory should contain all the `.geojson` files provided from the application. The script will return a "results"
directory with the converted coordinates in `.txt` files.
