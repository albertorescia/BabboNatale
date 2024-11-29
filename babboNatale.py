#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue November 22 18:32:09 2022

@author: albertorescia
"""
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from getpass import getpass
from email.utils import formatdate


def permuta(n):

    l = list(n)
    random.shuffle(l)
    n2 = l

    return n2

def controlla(n, n2):

    for prima, dopo in zip(n, n2):
        #print ("Prima ", prima, " e dopo ", dopo)
        if prima == dopo:
            return True
        else:
            continue

    return False

def send_email(email, pwd, donatore, indirizzo, ricevente):

    smtp = smtplib.SMTP('smtp.unige.it', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, pwd)

    msg = MIMEMultipart()
    msg['Subject'] = "Farai il regalo a "+ricevente.upper()+"!"
    msg['From'] = "email.address@host.com" #Mettere indirizzo mail da cui si invia per avere header corretto.
    msg['Date'] = formatdate(localtime=True)
    msg['To'] = ricevente
    
    text = ''
  
    msg.attach(MIMEText(text))

    smtp.sendmail(from_addr=email, to_addrs=indirizzo, msg=msg.as_string())
    smtp.quit()

if __name__ == "__main__":

#Aggiungere qui nomi ed inidirizzi
    nomi_dict =	{
    "Pippo" : "pippo@gmail.com",
    "Franco" : "franco@gmail.com",
    "Luigi Di Maio" : "giggino.di.maio@esteri.it"
    }
    
    nomi = []
    for key in nomi_dict:
        nomi.append(key)
    nomi2 = permuta(nomi)

    check = controlla(nomi, nomi2)

    while check is True:
        nomi2 = permuta(nomi2)
        #print("Nomi 2 ", nomi2)
        check = controlla(nomi, nomi2)
    
    #entrare in gmail
    email = input('Da quale indirizzo vuoi inviare la mail?\n')
    pwd = getpass()

    for key, ricevente in zip(nomi_dict, nomi2):
        #print(key, "fa il regalo a ", ricevente)
        send_email(email, pwd, key, nomi_dict[key], ricevente)
    
    print("Done")
    
