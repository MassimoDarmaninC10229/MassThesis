import csv, os
from pathlib import Path

#init variables
p = ('')#base path
k = 0 #

## Details about Folder
full_name = []
sat = []
sensor = []
date_format = []
time_format = []

##########################################

#Go through given directory
def traverse_root_directory(p):
    #path = Path(p)
    
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(p):
        path = root.split(os.sep) #array
        #print(path) #path3 = end of subfolders

        pathln = len(os.path.basename(root)) #len 99: end of subfolders, 94: +1, 3/5: month
        #print(pathln)
    
        if pathln == 99:
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
            #print(date_format)

            #rename_folders(p, date_format, time_format, sensor, sat) 
            
            #write_to_csv(sat, date_format, sensor, time_format)

#Rename folder           
def rename_folders(p, date_format, time_format, sensor, sat):
    dir = p
    os.chdir(dir)
    month_folders = os.listdir(dir)
    #print(month_folders)

    for i in range (len(month_folders)):
        pre_folders = os.listdir(dir + '/' + month_folders[i])
        #print(pre_folders)

        #for x in pre_folders:
            #print(x)

        for x in range(len(pre_folders)):
            old_path = p + '/'+ month_folders[i] + '/' + pre_folders[x]
            new_path = date_format + '_T' + time_format + '__' + sensor + '__' + sat
            #print(new_path.encode('unicode-escape').decode().replace('\\\\', '\\'))
            #os.rename(old_path , new_path)

#CSV
def write_to_csv( sat, date_format, sensor, time_format, full_name):
    #print(sat, date_format, sensor, time_format)
    with open('data_downloaded.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Satellite", "Sensor", "Time", "File Name"])

        for i in range(len(sat)):
            writer.writerow([date_format[i], sat[i], sensor[i], time_format[i], full_name[i]]) 

##########################################

#base covid for-loop
for i in range(5):
    #2017
    if i == 0:
        p = ('D:/Thesis Sentinel Data/2017/covid')
        traverse_root_directory(p)
        #print(p)
    
    #2018
    if i == 1:
        p = ('D:/Thesis Sentinel Data/2018/covid')
        traverse_root_directory(p)
        #print(p)

    #2019
    if i == 2:
        p = ('D:/Thesis Sentinel Data/2019/covid')
        traverse_root_directory(p)
        #print(p)

    #2020
    if i == 3:
        p = ('D:/Thesis Sentinel Data/2020/covid')
        traverse_root_directory(p)
        #print(p)

    #2021
    if i == 4:
        p = ('D:/Thesis Sentinel Data/2021/covid')
        traverse_root_directory(p)
        #print(p)

'''print('Sat:\n'+str(sat))
print('Sensor:\n'+str(sensor))
print('Date:\n'+str(date_format))
print('Time:\n'+str(time_format))'''

write_to_csv(sat, date_format, sensor, time_format, full_name)