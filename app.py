from flask import Flask
import requests as r

app = Flask('jokeapi')

@app.route('/')
def jokeresponse():
    response = r.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        print(joke['setup'])
        print(joke['punchline'])
        return(f"{joke['setup']} : {joke['punchline']}")
    else:
        
        return("Failed to fetch joke")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)