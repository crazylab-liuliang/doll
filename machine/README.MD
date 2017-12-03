# 配置开机启动
sudo vim /etc/rc.local

在 exit 0 上面添加启动命令

/usr/bin/python2.7 /home/doll/machine/main.py

## 更改键盘布局   
树莓派Raspbian默认键盘布局为UK，需修改为布局US  
1. 打开配置界面   
```bash
sudo dpkg-reconfigure keyboard-configuration
```  

2. 进入后，选择 Generic 101-key PC  
   按tab键，选中 OK 按钮，再按Enter确认。

3. 选择 English (US)

4. 选择 English (US, alternative international)

5. 重启
```bash
sudo reboot
```

[参考文档](http://blog.csdn.net/c80486/article/details/8460271)   
