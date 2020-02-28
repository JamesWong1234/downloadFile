
import json
import os
import shutil

from rarfile import RarFile




with open("./config/config.json",'r') as load_f:
    load_dict = json.load(load_f)    


download_folder = load_dict['mac_path']
VR_rootdir = download_folder + '/VR'
stream_rootdir = download_folder + '/stream'


'''
#move file
for file in os.listdir(download_folder):
    if file.endswith('.rar'):
        if file.find('vr') != -1:
            shutil.move(os.path.join(download_folder, file),os.path.join(VR_rootdir, file))
        else:
            shutil.move(os.path.join(download_folder, file),os.path.join(stream_rootdir, file))
'''

#unrar
folders = [VR_rootdir,stream_rootdir]
for folder in folders:
    list = os.listdir(folder)
    for file_name in list:
        print(file_name)
        path = os.path.join(folder, file_name)
        if os.path.isfile(path) & path.endswith('.rar'):
            #un_rar(path)
            
            with RarFile(path) as rf:
                rf.extractall(path=folder)
            