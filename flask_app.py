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
    error = ""
    print(">>> output1", data)
    output = "```"   

    output += "-------------------------------------------- \n"
    output += "| LAST ROUND STATS |   Rounds won: " + fill_till(str(data['alex_last_match_wins']), 7) + " | \n"
    output += "-------------------------------------------- \n"   
    output += "\n"
    output += "-------------------------------------------- \n"
    output += "| Player    | Kills | Deaths | Damage done | \n"
    output += "-------------------------------------------- \n"
    if 'kristiaan_last_match_kills' in data:
        output +=  "| " + fill_till("Kristiaan", 9) 
        output += " | " + fill_till("  " + str(data['kristiaan_last_match_kills']), 5) 
        output += " | " + fill_till("  " + str(data['kristiaan_last_match_deaths']), 6)
        output += " | " + fill_till("   " + str(data['kristiaan_last_match_damage']), 11)
        output += " |\n" 
    else:
        error +=  "Kristiaan's Steam profile is set to private\n"

    if 'muffin_last_match_kills' in data:
        output +=  "| " + fill_till("Muffin", 9) 
        output += " | " + fill_till("  " + str(data['muffin_last_match_kills']), 5) 
        output += " | " + fill_till("  " + str(data['muffin_last_match_deaths']), 6)
        output += " | " + fill_till("   " + str(data['muffin_last_match_damage']), 11)
        output += " |\n"
    else:
        error +=  "Muffin's Steam profile is set to private\n"

    if 'devlin_last_match_kills' in data:
        output +=  "| " + fill_till("Devlin", 9) 
        output += " | " + fill_till("  " + str(data['devlin_last_match_kills']), 5) 
        output += " | " + fill_till("  " + str(data['devlin_last_match_deaths']), 6)
        output += " | " + fill_till("   " + str(data['devlin_last_match_damage']), 11)
        output += " |\n" 
    else:
        error +=  "Devlin's Steam profile is set to private\n"


    if 'alex_last_match_kills' in data:
        output +=  "| " + fill_till("Alex", 9) 
        output += " | " + fill_till("  " + str(data['alex_last_match_kills']), 5) 
        output += " | " + fill_till("  " + str(data['alex_last_match_deaths']), 6)
        output += " | " + fill_till("   " + str(data['alex_last_match_damage']), 11)
        output += " |\n"  
    else:
        error +=  "Alex' Steam profile is set to private\n"

    output += "-------------------------------------------- \n"
    output += "\n"
    output += error
    output += "\n"
    output += "```"
    output += "\n"
    return output


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)