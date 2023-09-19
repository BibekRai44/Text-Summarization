import requests
import flask
from flask import render_template ,url_for

app=flask.Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

#min_length=int(input("Enter a minimum length :"))
#max_length=int(input("Enter a maximum length :"))
	
data= "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

#print("Your string is being summarized....")
#output=query({"inputs":data,"parameters":{"min_length":min_length,"max_length":max_length},})


#print(output)

if __name__ == '__main__':
	app.run(debug=True)