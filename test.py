import shutil
from unrar import rarfile
#import rarfile  
import os  
def un_rar(file_name):  
    """unrar zip file"""  
    rar = rarfile.RarFile(file_name)  
    if os.path.isdir(file_name + "_files"):  
        pass  
    else:  
        os.mkdir(file_name + "_files")  
    os.chdir(file_name + "_files")  
    rar.extractall()


if __name__ == '__main__':
    download_folder = 'D:\Downloads'
    VR_rootdir = 'D:\Downloads\VR'
    stream_rootdir = 'D:\Downloads\stream'
    for file in os.listdir(download_folder):
        if file.endswith('.rar'):
            if file.find('vr') != -1:
                shutil.move(os.path.join(download_folder, file),os.path.join(VR_rootdir, file))
            else:
                shutil.move(os.path.join(download_folder, file),os.path.join(stream_rootdir, file))


