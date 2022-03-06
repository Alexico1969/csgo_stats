import os
import requests, json
from flask import Flask,redirect,url_for,render_template,request
from steam_api import get_csgo3, get_csgo4, get_csgo5
from helper import fill_till

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    output1 = ""
    output2 = ""
    output3 = "TEST"

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

    try:    
        output3 = get_csgo5()
    except Exception as E:
        print(E)
        output3 = "E" + str(E)


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

        try:
            output3 = get_csgo5()
        except Exception as E:
            print(E)
            output3 = "E" + str(E)

        return render_template('index.html', output1=output1, output2=output2, output3=output3)
    return render_template('index.html', output1=output1, output2=output2, output3=output3)


@app.route('/last',methods=['GET','POST'])
def last():
    output1 = get_csgo5()
    print(">>> output1", output1)
    #output1['last_match_wins'] = "99999"
    return render_template('last.html', output1=output1)


@app.route('/api',methods=['GET','POST'])
def api():
    data = get_csgo5()
    print(">>> output1", data)
    output = "```"
    output += "-------------------------------------------- \n"
    output += "| Player    | Kills | Deaths | Damage done | \n"
    output += "-------------------------------------------- \n"
    output +=  "| " + fill_till("Kristiaan", 9) 
    output += " | " + fill_till(data['kristiaan_last_match_kills'], 5) 
    output += " | " + fill_till(data['kristiaan_last_match_deaths'], 6)
    output += " | " + fill_till(data['kristiaan_last_match_damage'], 6)
    output += " |\n" 
    '''
        <tr>
            <td class="al_left">Kristiaan|
            |{{data['kristiaan_last_match_kills']}}|
            |{{data['kristiaan_last_match_deaths']}}|
            |{{data['kristiaan_last_match_damage']}}|
        </tr>
        <tr>
            <td class="al_left">Muffin|
            |{{data['muffin_last_match_kills']}}|
            |{{data['muffin_last_match_deaths']}}|
            |{{data['muffin_last_match_damage']}}|
        </tr>
        <tr>
            <td class="al_left">Devlin|
            |{{data['devlin_last_match_kills']}}|
            |{{data['devlin_last_match_deaths']}}|
            |{{data['devlin_last_match_damage']}}|
        </tr>
        <tr>
            <td class="al_left">Alex|
            |{{out['alex_last_match_kills']}}|
            |{{out['alex_last_match_deaths']}}|
            |{{out['alex_last_match_damage']}}|
        </tr>
    '''
    output += "```" 
    return output


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)