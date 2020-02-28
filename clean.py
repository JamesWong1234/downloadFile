import os
import shutil
import json


if __name__ == '__main__':

    with open("./config/config.json",'r') as load_f:
        load_dict = json.load(load_f) 
    #mac
    if load_dict['system'] == 'mac':
        download_folder = load_dict['mac_path']
        VR_rootdir = download_folder + '/VR'
        stream_rootdir = download_folder + '/stream'
    else:
        VR_rootdir = 'D:\Downloads\VR'
        stream_rootdir = 'D:\Downloads\stream'

    folders = [VR_rootdir,stream_rootdir]
    for folder in folders:
        shutil.rmtree(folder) # 能删除该文件夹和文件夹下所有文件
        os.mkdir(folder)
