
from flask import Flask, request, render_template
import requests as HTTP
from bs4 import BeautifulSoup as SOUP 

#Initialising the flask application
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        
        emotion=request.form['emotion']
        print(emotion) 
	# movie based on emotion Sad
        if(emotion == "Sad"):
            urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc' 
	# movie based on emotion Anticipation
        elif(emotion == "Anticipation"):
            urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    # movie based on emotion Fear
        elif(emotion == "Fear"):
            urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc' 
	# movie based on emotion Enjoyment
        elif(emotion == "Enjoyment"):
            urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
	# movie based on emotion Trust
        elif(emotion == "Trust"):
            urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

	
	#Getting the Data from the Website using HTTp
        response = HTTP.get(urlhere)
        data = response.text 
        soup = SOUP(data, "lxml") 
        supa = soup.find_all('h3', attrs={'class' : 'lister-item-header'})
        print(len(supa))
        
        list = []
        
        for header in supa:
            name = "";
            aElement_soup = header.find_all('a')
            spanElement_soup = header.find_all('span')
            spanElement = spanElement_soup[0]
            name = name + spanElement.text
            aElement = aElement_soup[0]
            name = name +" "+ aElement.text
            if len(spanElement_soup)>1:
                spanElement = spanElement_soup[1]
                name = name +" "+  spanElement.text
            
            list.append(name)

        return render_template('home.html',prediction_text="{}".format(emotion),data=list)





if __name__ == "__main__":
    app.run(debug=False)
