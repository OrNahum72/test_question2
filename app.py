from flask import Flask
import requests as r

app = Flask('jokeapi')

@app.route('/')
def jokeresponse():
    joke = {
    "type": "general",
    "setup": "Why did the Clydesdale give the pony a glass of water?",
    "punchline": "Because he was a little horse!",
    "id": 324}
    print(joke['setup'])
    print(joke['punchline'])
    return(f"{joke['setup']} : {joke['punchline']}")
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)