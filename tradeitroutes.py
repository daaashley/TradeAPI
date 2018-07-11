from flask import Flask, render_template, request
from PyQt5 import QtCore, QtGui, QtWidgets
import requests, webbrowser
import os
import socket
import threading
import settings
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import user
import subprocess
import polytrader
#PolyTrader Routes 5/3/2018 David Ashley
#API Key from TradeIt: "d50a18d412684656a7481a43d3f9f43a"

#__name__ is root path
settings.init()
app = Flask(__name__)


global globalToken 
global globalAccountNumber


#First Route, Index page used to call popup, postmessage sent to calling page
@app.route('/index')
def index(name=None):
    #Payload for initial login pop-up
    payload = {
        "apiKey":"d50a18d412684656a7481a43d3f9f43a",
        "broker":"Dummy"
        }
    #Request for OAuth pop-up page URL
    popUpURLInfo = requests.session()
    popUpURLInfo  = requests.post('https://ems.qa.tradingticket.com/api/v1/user/getOAuthLoginPopupUrlForWebApp', params=payload)
    popUpURLInfoData  = popUpURLInfo.json()
    print(popUpURLInfoData)
    #Returns page used to call pop-up page, passes OAuth URL data to page for calling
    return render_template('index.html', name=name,brokerData=popUpURLInfoData['oAuthURL'])
    

#Route that recieves post request from pop-up calling page
@app.route('/confirm',methods=['POST', 'GET'])
def confirm(name=None):
    #Grabs postmessage oAuthVerifier data from form
    authData = request.form['auth']
    payload = {
            "apiKey":"d50a18d412684656a7481a43d3f9f43a",
            "oAuthVerifier":authData
    }
    #Uses oAuthVerifier to retrieve userToken and userId
    accessTokenData = requests.post('https://ems.qa.tradingticket.com/api/v1/user/getOAuthAccessToken', params=payload)
    accessToken = accessTokenData.json()
    payload2 = {
        'userToken':accessToken['userToken'],
        'userId':accessToken['userId'],
        'apiKey':"d50a18d412684656a7481a43d3f9f43a"
    }
    #Uses userToken and userId to authenticate and retrieve account info
    accountInfo = requests.post('https://ems.qa.tradingticket.com/api/v1/user/authenticate?1455723756890', params=payload2)
    account = accountInfo.json()
    print(account)
    
    globalToken = account['token']
    globalAccountNumber = account['accounts'][0]['accountNumber']
    print(globalToken + "-------" + globalAccountNumber)
    
    payload3 = {
            'token':globalToken,
            'accountNumber':globalAccountNumber
                    }
    accountOverviewData = requests.post('https://ems.qa.tradingticket.com/api/v1/balance/getAccountOverview', params=payload3)
    accountOverview = accountOverviewData.json()
    print(accountOverview)
    settings.userData.append(accountOverview)
    print(settings.userData)
    file = open('config.txt','w')
    file.write(globalToken+'\n')
    file.write(globalAccountNumber)
    cwd = os.getcwd()
    print(cwd)
    os.system('python polytrader3.py '+globalToken + ' ' + globalAccountNumber)
    
    
    return render_template('index.html')



