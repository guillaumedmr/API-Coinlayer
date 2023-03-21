import requests
from pandas.io.json import json_normalize
import json

def prix_crypto(devise):

    try :
        cle_api = "c5ebce0697d27a150d2bf41a5fb320be" # Clé API Coinlayer (gratuite sur le site officiel)
        url = "http://api.coinlayer.com/api/live?access_key=" + cle_api
        reponse = requests.get(url)
        
        contenu_txt = reponse.text
        contenu_json = json.loads(contenu_txt)
        
        for i in contenu_json['rates']:
            if i == devise:
                print(contenu_json['rates'][i])
    except :
        print("Erreur")
            
    
prix_crypto("BTC")