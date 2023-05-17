from flask import Flask, render_template, request, Response
import openai
import config
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


openai.api_key = config.openai_apikey
openai.organization = "org-UyJwFhjycnAHScHGFcRstI7a"

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

if __name__ == '__main__':
    app.run()
