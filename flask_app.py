import os
import requests, json
from flask import Flask,redirect,url_for,render_template,request
from steam_api import get_csgo3, get_csgo4

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    output1 = ""
    output2 = ""

    id = "76561198800721901"

    try:
        output1 = get_csgo3(id)
    except Exception as E:
        print(E)
        output1 = "E" + str(E)

    try:
        output2 = get_csgo4(id)
    except Exception as E:
        print(E)
        output2 = "E" + str(E)


    if request.method=='POST':
        id = request.form['player_id']
        
        try:
            output1 = get_csgo3(id)
        except Exception as E:
            print(E)
            output1 = "E" + str(E)

        try:
            output2 = get_csgo4(id)
        except Exception as E:
            print(E)
            output2 = "E" + str(E)

        return render_template('index.html', output1=output1, output2=output2)
    return render_template('index.html', output1=output1, output2=output2)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)