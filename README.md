# DEM-o-matic

Creates synthetic digital elevation models (DEMs) from point data.

Prerequisites:

- [GDAL](https://www.gdal.org/) (I installed mine through installing [QGIS](https://www.qgis.org/en/site/forusers/download), which might be easier)

- Python 3

Usage:

1. Add points to `dem_orig.csv`. Contour interpolation will be done between consecutive points of the same elevation, in order.

2. Open a terminal in the folder with `interp.py` and run  `python3 interp.py dem_orig.csv <interpolation interval>` where `<interpolation interval>` is the distance between points in Easting/Northing units, e.g. 10. Too fine values may cause sharp contours, while too sparse values may result in rough contours.

3. Run `gdal_grid` with the appropriate settings. Example outputs are produced with `gdal_grid -a invdist:power=3.0:smoothing=5.0:maxpoints=6 -outsize 1200 1200 -of GTiff -l dem dem.vrt dem.tiff`. See [gdal_grid documentation](https://www.gdal.org/gdal_grid.html) for details on interpolation algorithms.

4. The resulting `dem.tiff` should be readable by QGIS/ArcGIS. Some programs may take a .png instead; this can be done using [gdal_translate](https://www.gdal.org/gdal_translate.html) with something like (`gdal_translate -of PNG -scale -outsize 120 120 dem.tiff dem.png` )

Further steps:

- To 3D print, run a .png through [heightmap2stl](https://sourceforge.net/projects/heightmap2stl/) (using grayfix.py may also be needed to fix grayscale log values, e.g. `python grayfix.py dem.png dem_fix.png`)

- Import a voxel version to [MagicaVoxel](https://ephtracy.github.io/) with [FileToVox](https://github.com/Zarbuz/FileToVox)

- Import to Sketchup with the [BitmapToMesh](https://sketchucation.com/forums/viewtopic.php?f=323&t=31339) plugin (may not work, try other plugins or maybe convert to STL and use [Sketchup-STL](https://extensions.sketchup.com/en/content/sketchup-stl))
