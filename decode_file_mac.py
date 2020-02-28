import os
import shutil
import json
from rarfile import RarFile

def print_stream(folder):
    pathss=[]
    for root, dirs, files in os.walk(folder):
        path = [os.path.join(root, name) for name in files]
        pathss.extend(path) 

    for path in pathss:   
        if os.path.isfile(path) & path.endswith('.txt'):
            #print(path)
            fp = open(path, "r", encoding="utf8")
            for line in fp.readlines():
                if '.wmv' in line or '.mp4' in line:
                    print(line)
            fp.close()

def print_VR(folder):

    pathss=[]
    for root, dirs, files in os.walk(folder):
        path = [os.path.join(root, name) for name in files]
        pathss.extend(path)   

    for path in pathss:                
        if os.path.isfile(path) & path.endswith('.txt'):
            fp = open(path, "r", encoding="utf8")
            for line in fp.readlines():
                if line.endswith('rar\n'):
                    print(line)
            fp.close()

if __name__ == '__main__':
    with open("./config/config.json",'r') as load_f:
        load_dict = json.load(load_f) 
    #mac
    #if load_dict['system'] == 'mac':
    download_folder = load_dict['mac_path']
    VR_rootdir = download_folder + '/VR'
    stream_rootdir = download_folder + '/stream'

    #move file
    for file in os.listdir(download_folder):
        if file.endswith('.rar'):
            if file.find('vr') != -1:
                shutil.move(os.path.join(download_folder, file),os.path.join(VR_rootdir, file))
            else:
                shutil.move(os.path.join(download_folder, file),os.path.join(stream_rootdir, file))
    #unrar
    folders = [VR_rootdir,stream_rootdir]
    for folder in folders:
        list = os.listdir(folder)
        for file_name in list:
            path = os.path.join(folder, file_name)
            if os.path.isfile(path) & path.endswith('.rar'):
                with RarFile(path) as rf:
                    rf.extractall(path=folder)

    #get_address
    print_VR(VR_rootdir)
    print_stream(stream_rootdir)


