# coding: utf_8

import psutil
import requests
import time
import subprocess

token_txt = open('token.txt', 'r', encoding='utf_8')
token = token_txt.read()
token_txt.close()

headers = {'Content-Type': 'application/json', 'authorization': token}

while True:
    cpu_per = int(psutil.cpu_percent())

    gpu_per_o = subprocess.check_output("nvidia-smi --query-gpu=utilization.gpu --format=csv,nounits",shell = True)
    gpu_per = gpu_per_o.decode('utf-8').splitlines()

    custom_status_json = {"custom_status": {'text': 'CPU: ' + str(cpu_per) + '% GPU: ' + str(gpu_per[1]) + '%'}}
    cs_patch = requests.patch('https://canary.discord.com/api/v8/users/@me/settings', json = custom_status_json, headers = headers)

    #print('CPU: ' + str(cpu_per) + '% GPU: ' + str(gpu_per[1]) + '%')
    time.sleep(1)
