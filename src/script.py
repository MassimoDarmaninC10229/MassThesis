import os
from pathlib import Path
from netCDF4 import Dataset
import pandas as pd
import numpy as np
import snappy
from snappy import HashMap
import gc   
from snappy import GPF
jpy = snappy.jpy
from snappy import ProductIO, File
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cartopy.crs as ccrs
import numpy as np
import rasterio
from rasterio.windows import Window
from rasterio.plot import show
from rasterio.enums import Resampling
import cartopy.crs as ccrs

##init variables
pc_base_directory = ('C:/Sentinel 3 Data/') 
laptop_base_directory = ('C:/Users/Massimo/Documents/SchoolFolder/ThirdYear/Thesis/SentinelData/2021/extra')

base_directory = laptop_base_directory
k=0
path = Path(base_directory)

## Details about Folder
full_name = []
sat = []
sensor = []
date_format = []
time_format = []

for root, dirs, files in os.walk(base_directory):
    path = root.split(os.sep)

    pathln = len(os.path.basename(root)) #len 99: end of subfolders, 94: +1, 3/5: month
    #print(pathln)

    ###pathln == 99 is how I will differentiate sentinel 3 products
    if pathln == 99:    
        ###Gathering Product details such as date & time and storing them    
        current_path = base_directory + '/'  + os.path.basename(root)
        print(current_path)

        #string[ start_index_pos: end_index_pos: step_size]
        full_name.append(os.path.basename(root))
        #print(full_name)
        
        path_name_30chars = os.path.basename(root)[ :30] #30chars include: (0-2)Sat, (4-8)Sensor, (13-31)Type, Year, Month, Date, Time
        #print(path_name_30chars)

        sat.append(path_name_30chars[:3])
        sensor.append(path_name_30chars[4:12])

        date = path_name_30chars[16:24]
        date_format.append(date[:4] + '/' + date[4:6] + '/' + date[6:])

        time = path_name_30chars[25:29]
        time_format.append(time[:2] + ':' + time[2:])

        ###Reading product 1 at a time        
        File = jpy.get_type('java.io.File') #file type        
        archi=File(current_path) #product to be read
        product = ProductIO.readProduct(archi)
        reader = snappy.ProductIO.getProductReader('SEN3')
        print('All Bands for product ' + path_name_30chars)
        print(str(list(product.getBandNames())))
'''
print(full_name)  
print(sat)
print(date_format)
print(time_format)'''