from flask import Flask,jsonify
import requests
from googletrans import Translator

url ="https://newsapi.org/v2/top-headlines?language=en&apiKey=306c8e6520a741458b66dc32555e5eb8"

app= Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
l = []
b={}
translator = Translator()

@app.route("/")
def api():
    new = requests.get(url).json()
    for i in new['articles']:
        if new['articles'].index(i)>9:
            break
        else:
            a={}
            t=translator.translate(i['title'],dest='fr')
            d=translator.translate(i['description'], dest='fr')
            
            a['title_en']= i['title']
            a['desc_en']=i['description']
        
            a['title_fr']=t.text
            a['desc_fr']=d.text
        
            a['timestamp']=i['publishedAt']
            a['image_url']=i['urlToImage']
        
            l.append(a)
        
    b['news']=l
    return jsonify(b)
    
    
if __name__ == "__main__":
    app.run(debug=True)