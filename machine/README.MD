## 系统配置   
1. [安装Raspbian-lite系统](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md)
2. [更换键盘布局](http://blog.csdn.net/c80486/article/details/8460271)   
```bash
sudo dpkg-reconfigure keyboard-configuration   
```

- 选择 ***Generic 101-key PC***  按tab键，选中 OK 按钮，再按Enter确认。   

- 选择 ***English (US)*** 按tab键，选中 OK 按钮，再按Enter确认。   

- 选择 ***English (US, alternative international)***   按tab键，选中 OK 按钮，再按Enter确认。   

- 重启机器后键盘布局修改才能生效  
```bash
sudo reboot
```
3. 安装 git ffmpeg pip, flask requests pyserial

```bash
sudo apt-get install git   
sudo apt-get install ffmpeg   
sudo apt-get install python-pip   
sudo pip install flask   
sudo pip install requests   
sudo pip install pyserial   
```

## 启动服务

1. 启动树莓派   
2. 在桌面打开终端   
3. 通过cd 命令进入当前文件夹   
```bash	
cd /home/Ledo_CatchDollOL/RaspberryPi/machine
```

4. 运行python 脚本   
```bash
sudo python main.py
```

## 配置开机启动
1. 安装vim(文本编辑器)
```bash
sudo apt-get install vim
```

2. 编辑rc.local
```bash
sudo vim /etc/rc.local
```

3. 在 exit 0 上面添加启动命令
```bash
sudo /usr/bin/python2.7 /home/Ledo_CatchDollOL/RaspberryPi/machine/main.py &
```

## 关闭服务
```
sudo killall python2.7
```

