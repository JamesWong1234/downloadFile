import os
import shutil


if __name__ == '__main__':
    folders = ['D:\Downloads\VR','D:\Downloads\stream']
    for folder in folders:
        shutil.rmtree(folder) # 能删除该文件夹和文件夹下所有文件
        os.mkdir(folder)
