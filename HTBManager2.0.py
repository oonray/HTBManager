#!/usr/bin/python3
"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: htbmanage.py
:date: 11.08.2019

This progam is made to manage the different aspects of Hack The Box Automatically.
It is designed to make a structured setup for your machines.
"""
import variables, argparse, json, sys, os, requests, colorama
from errors import *

init()

argparser = argparse.ArgumentParser(description="Manages Hack The Box Machines and Hacking Session")


base_url = "https://www.hackthebox.eu/api"
headers = {"User-Agent":"curl/7.65.1"}
"""
+######
| MisC
+######
"""
def add_token(url,token):
    ret =  "{}{}?api_token={}".format(base_url,url,token)
    print(ret)
    return ret

def get_api_token():
    with open(os.path.join(variables.CONF_FOLDER,"htb.conf")) as f:
        key = json.loads(f.read())["key"]
        if(key=="<your api key here>"):
            print("You must add a api key to {}/htb.conf".format(variables.CONF_FOLDER))
            exit()
        return key


def get(url):
    request = requests.get(url,headers=headers)
    check_response(request)
    return request

def check_response(response):
    if response.status_code != 200:
        fetch_error()

argparser.add_argument("action",help="The action you want to take eg. START, LIST, DOWNLOAD")

"""
+#######
| Start
+#######
"""
start_group = argparser.add_argument_group("START")

"""
Start Session
"""
start_group.add_argument("-s",help="Session, Machine To start session with")
def start_session():
    pass

"""
Start VPN
"""
start_group.add_argument("-v",help="Start VPN conneciton",action="store_true")
def start_vpn():
   pass


"""
Start Last session
"""
start_group.add_argument("-l",help="Continue the last session", action="store_true")
def start_last():
    pass

"""
Start STD Scans
Start Lease
"""

"""
+######
| LIST
+######
"""
list_group = argparser.add_argument_group("LIST")

"""
List Machines
"""
list_group.add_argument("-m",help="Lists active machines")


def get_all_machines():
   url = "/machines/get/all"
   return get(add_token(url,get_api_token()))

def parse_all_machines(request):
    parsed_data = json.dumps(request.data)
    return parsed_data

def print_all_machines(machines):
    print(machines)

"""
List Active
List Retired
List OSCP
"""

"""
Download ALL
"""
def download_all():
    pass


"""
Download Active
Download Retired
Download OSCP
"""

"""
Stop VPN
Stop Lease
"""

"""
Add Host to /etc/hosts
"""

"""
Remove Host form /etc/hosts
"""

if __name__ == "__main__":
    get(add_token("/lol",get_api_token()))
