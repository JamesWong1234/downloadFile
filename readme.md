windows

0.提取HD1080下载地址：
提取路径：
python D:\project\PycharmProjects\decodedowloadfile\decode_file.py
清理：
python D:\project\PycharmProjects\decodedowloadfile\clean.py
解压VR：

mac:

提取路径：
cd "/Volumes/nvme data/project/PycharmProjects/decodedowloadfile"
/anaconda3/envs/python37/bin/python decode_file_mac.py

清理：
/anaconda3/envs/python37/bin/python clean.py

# 安装解压缩插件的系统准备

Win：

1. 先到RARLab官方下载库文件，http://www.rarlab.com/rar/UnRARDLL.exe ，然后安装；

2. 安装最好选择默认路径，一般在 C:\Program Files (x86)\UnrarDLL\ 目录下；

3. 然后重要的一步，就是添加环境变量，此电脑（我的电脑）右键，属性，找到 高级系统设置，高级 选项卡下点击 环境变量，在系统变量（注意不是用户变量）中 新建，变量名输入 UNRAR_LIB_PATH ，必须一模一样，变量值要特别注意！如果你是64位系统，就输入 C:\Program Files (x86)\UnrarDLL\x64\UnRAR64.dll，如果是32位系统就输入 C:\Program Files (x86)\UnrarDLL\UnRAR.dll ，这个从unrar安装目录的内容也能看出来它是区分64和32位的。

4. 确定保存环境变量后，重启你的PyCharm，代码不变，再运行就不会出错了。这个时候依赖库已经添加到系统环境中。

Linux需要自己手动编译生成so文件，稍微麻烦一点：

1. 同样的，先去下载源文件，不过这就不像Win那样给你封装好了，你需要下载的是源代码：http://www.rarlab.com/rar/unrarsrc-5.4.5.tar.gz ，也就是RARLab官网下载列表中的 UnRAR Source，可以下载到最新版本；

2. 下载完后解压，得到unrar目录，cd unrar 后，使用 make lib 命令将会自动编译库文件，哗啦啦编译完成后，再使用 make install-lib 命令产生 libunrar.so 文件（一般在 /usr/lib 目录下面）；

3. 最后，你仍然需要设置Linux系统的环境变量，找到 /etc 目录下的 profile 文件，当然你可以直接使用 vim /etc/profile 命令来编辑（有WinSCP这种远程访问目录的工具更方便），在 profile 文件末尾加上 export UNRAR_LIB_PATH=/usr/lib/libunrar.so ，别把我这句话的逗号加进去了。成功保存后再使用 source /etc/profile 命令使变量生效。

4. 这样一来，再运行py文件，就不会出错了，至少不会提示找不到unrar库了。

友情提示：如果有同学 make 命令用不了的，请自行安装g++编译器，命令：sudo apt-get install g++
