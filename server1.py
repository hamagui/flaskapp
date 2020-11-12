from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return(render_template('root.html'))

@app.route('/firstrequest', methods=['GET'])
def firstRequest():
    return(render_template('index.html'))

@app.route('/secondrequest', methods=['GET'])
def secondRequest():
    userAgent = str(request.headers['User-Agent'])
    return(render_template('start.html', userAgent = userAgent))

@app.route('/fourthrequest', methods=['GET'])
def fourthRequest():
    API_KEY = '2ef86e0676f4fa8c5c0e938a152916c7'
    city = request.args.get('q')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    #data = response.content
    #temperature = response.content('main')
    temper = response.json()
    #weather = temperature['weather'][0]['description']
    return temper
    #return weather
    #return('You just posted.... ' )

'''@app.route('/thirdrequest', methods=['GET', 'POST'])
def thirdRequest():
    myobj={1: 'hello world'}
    x= requesd.post (http://127.0.0.1.5000/thirdrequest',data = myobj)
    return x
    #reqData = request.form
    #return('You just posted.... ' + str(reqData))'''

@app.route('/form-example', methods=['GET', 'POST']) 
def form_example():
    if request.method == 'POST':
          #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']
        
        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                Language: <input type="text" name="language"><br>
                Framework: <input type="text" name="framework"><br>
                <input type="submit" value="Submit"><br>
            </form>'''


if __name__ == '__main__':
    app.run(debug=True)
