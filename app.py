import requests
from flask import Flask, render_template, url_for
from flask import request as req


app = Flask(__name__)
@app.route("/",methods=["GET", "POST"])
def Index():
    return render_template("index.html")

    
@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.method=="POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}


        data=req.form["data"]

        
        maxL=int(req.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length":minL, "max_length":maxL},
        })
        if "summary_text" in output:
            summary_text = output["summary_text"]
            return render_template("index.html", result=summary_text)
        else:
            return "Failed to summarize the text."


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
