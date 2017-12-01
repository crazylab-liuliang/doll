# 配置开机启动
sudo vim /etc/rc.local

在 exit 0 上面添加启动命令

/usr/bin/python2.7 /home/doll/machine/main.py