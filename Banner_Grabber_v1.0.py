# -*- coding: utf-8 -*-
#! /usr/bin/python3


import sys, os, time
import ipaddress
import socket
from queue import Queue
import threading
import pyfiglet
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from clint.textui import colored

qips = Queue()
setipacrack = []
setports = []
setuser = []
setpass = []
settotalcombo =[]
portsyy = []
portsgrab = []

def banniere() :
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
    text="DarkCarders007"
    cprint(figlet_format(text, font="standard"), "green")
    print(colored.blue("DarkTools : Banner_Grabber"))
    print(colored.red("-- Version 1.0 --"))
    print(colored.yellow("Realease: 26/08/2021"))
    print(colored.magenta("Banner_Grabber By DarkCarders007 "))
    print(colored.cyan('https://t.me/DarkCarders007'))
    print(colored.green('https://github.com/DarkCarders007'))
    print(colored.red('https://www.youtube.com/channel/UC7kyGeHDb9YwY-3YjEksEqw'))


def menubase():
   print()
   print(colored.green("1. Grab Sur 1 Seule IP  ")+colored.blue("Basic"))
   print(colored.green("2. Grab Sur Ip's Range ")+colored.yellow("Advanced"))
   print(colored.green("3. Grab Fichier D'Ip's ")+colored.red("Hard"))
   print(colored.green("4. Exit() ")+colored.magenta("Bad"))
   while True:
        try:
            menubaseoption = int(input("On Grab Quoi ? "))
            if menubaseoption == 1:
                crackipsolo()
            elif menubaseoption == 2:
                crackiprange()
            elif menubaseoption == 3:
                crackipfile()
            elif menubaseoption == 4:
                print(colored.magenta("Merci D'Avoir Utilisé Le Tools !"))
                quit()
            else :
                print(colored.red("Invalide Option"))
        except ValueError:
                print(colored.red("Je Ne Vois Cette Option Nulle Part ?!"))


def threadallow():
    print(colored.yellow("\n"+"Grab En Cours...."))
    for x in range(200):
        t = threading.Thread(target=bannergrabber)
        t.daemon = True
        t.start()
        start = time.time()
    qips.join()
    totaltime =  time.time()- start
    print(colored.yellow("Terminé en " + str(totaltime)))
    print(colored.yellow("Grab Ok Enregistrer Dans: Banner_Grabber.txt"))
    menubase()



def bannergrabber():
    while not qips.empty():
        ips = qips.get()
        for port in portsgrab:
            try:
                s = socket.socket()
                s.settimeout(2)
                print(" Ip: "+ips+' Banner Pour Le Port: '+str(port)+"\n")
                s.connect((ips,int(port)))
                answer = s.recv(1024)
                print(answer)
                bannerok = (ips+' Banner Pour Le Port: '+str(port)+"\n"+str(answer)+"\n")
                open('Banner_Grabber.txt', 'a').write(bannerok + "\n")
                s.close()
            except ConnectionRefusedError:
                print(colored.red("Connection Refusé "))
            except TimeoutError :
                print(colored.blue('Timeout ! Pas de Reponse Du Serveur '+ips+"\n"))
                break
            except OSError:
                print("Déco")
                break
        qips.task_done()



def crackipsolo():
    while True:
        server = input("\n"+"Banner Server Adresse: ")
        ports = [21, 22, 25, 80, 8080, 3306]
        for port in ports:
            try:
                s = socket.socket()
                print('Banner Pour Le Port: '+str(port))
                s.settimeout(2)
                s.connect((server, port))
                answer = s.recv(1024)
                print(answer)
                s.close()
            except ConnectionRefusedError:
                print(colored.red("Connection Refusé "))
            except TimeoutError :
                print(colored.blue('Timeout ! Pas de Reponse Du Serveur '+ips+"\n"))
            except OSError:
                print("Déco")
        menubase()


def crackiprange():
     while True :
        portsyy = []
        ipacrackfrom = input("\n"+"From IP: ")
        ipacrackto = input("To IP: ")
        try:
            start_ip = ipaddress.IPv4Address(ipacrackfrom)
            end_ip = ipaddress.IPv4Address(ipacrackto)
            for ip_int in range(int(start_ip), int(end_ip)):
                qips.put(str(ipaddress.IPv4Address(ip_int)))
        except :
            print(input(colored.red("Ce N'Est Pas Une Plage D'Ip's Valide !!")))
            break
        try:
            print(colored.green("0. Port Par Default: 21, 22, 25, 80, 8080, 3306, 3389"))
            print(colored.green("Ou"))
            portsuser = input(colored.green("Entrer Liste De Ports Séparés Par ',':"))
            if portsuser == "0":
                portsdefault = [21, 22, 25, 80, 8080, 3306, 3389]
                for portdef in portsdefault:
                    portdef = str(portdef).strip('\r\n')
                    portsyy.append(portdef)
            else:
                portsuserok = str(portsuser)
                portsuserok = portsuserok.split(',')
                for portsuseroks in portsuserok:
                    portsuseroks = portsuseroks.strip('\r\n')
                    portsyy.append(portsuseroks)
        except ValueError:      ## Si pas un chiffre ou "entree"
                print(colored.red("Je Ne Vois Cette Option Nulle Part ?!"))
        for portsy in portsyy:
            print(portsy)
            portsgrab.append(portsy)
        threadallow()
        break




def crackipfile():
    while True :
        portsyy = []
        iplist = input("Chemin (Path) Vers Le Fichier D'IP's .txt> ")
        try :
            with open(iplist, 'r', encoding='utf-8', errors='ignore') as ipss :
                for ips in ipss:
                    ips = ips.strip('\r\n')
                    qips.put(ips)
        except Exception as exc :
            print('IP_List Error', exc)
        try:
            print(colored.green("0. = Port Par Default: 21, 22, 25, 80, 8080, 3306, 3389"))
            print(colored.green("Ou"))
            portsuser = input(colored.green("Entrer Liste De Ports Séparés Par ',':"))

            if portsuser == "0":
                portsdefault = [21, 22, 25, 80, 8080, 3306, 3389]
                for portdef in portsdefault:
                    portdef = str(portdef).strip('\r\n')
                    portsyy.append(portdef)
            else:
                portsuserok = str(portsuser)
                portsuserok = portsuserok.split(',')
                for portsuseroks in portsuserok:
                    portsuseroks = portsuseroks.strip('\r\n')
                    portsyy.append(portsuseroks)
        except ValueError:      ## Si pas un chiffre ou "entree"
            print(colored.red("Je Ne Vois Cette Option Nulle Part ?!"))
        for portsy in portsyy:
            print(portsy)
            portsgrab.append(portsy)
        threadallow()
        break

banniere()
menubase()
