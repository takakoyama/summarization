from flask import Flask, render_template, request, Response
import openai
import config
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os


openai.api_key = os.getenv("openai_api")
openai.organization =os.getenv("openai_organization")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['text']
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[ 
            {"role": "user", "content": f"日本語で要約してください: {prompt}"},
            ],
        )      
            
        summarized_text= response["choices"][0]["message"]["content"]

        return summarized_text
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
