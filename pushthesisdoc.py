#!/usr/local/bin/python3
import os
import glob
import shutil

# get a list of all txt files
rmline = "rm -rf /Users/zijianzhou/Documents/Python/utils/docs/html"
os.system(rmline)
os.system("echo \"finished removing docs\"")
os.system("doxygen /Users/zijianzhou/Documents/Python/utils/docs/Doxyfile")
os.system("echo \"finished generating docs\"")
# not sure about the address
copyline = "sshpass -p \"raspberry\" scp -r /Users/zijianzhou/Documents/Python/utils/docs/html pi@172.22.31.168:/home/pi/usbdrv/docs/monsterfarm"
os.system(copyline)
os.system("echo \"finish copying docs\"")
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname = '172.22.31.168'
username = 'pi'
# 私钥的密码，没有则不需要传递password参数
password = 'raspberry'
ssh.connect(hostname, username = username, password = password)
stdin, stdout, stderr = ssh.exec_command('sudo reboot')

ssh.close()
