from flask import Flask, render_template
from flask import request
from trends import global_trends
from region_trend import trending_searches
from kw_trend import getkw_trends
from sentiment_keyword import sentiment

app = Flask(__name__)

@app.route("/")
@app.route("/home",methods=['GET', 'POST'])
def hello_world():
    #global_trends()
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/glb")
def glb():
    data = global_trends()
    return render_template('global_trends.html', data=data)

@app.route("/exp", methods=['GET', 'POST'])
def exp():
    return render_template('exp.html')

@app.route("/region", methods=['GET', 'POST'])
def region():
    select = request.form.get('country')
    data = trending_searches(str(select))
    return render_template('regiontrend.html', data=data)

@app.route("/search", methods=['GET', 'POST'])
def search():
    select = request.form.get('search_kw')
    #return str(select)
    data = getkw_trends(str(select))
    data2 = sentiment(str(select))
    return render_template('searchtrend.html', data=data, data2=data2)

@app.route("/sentiment", methods=['GET', 'POST'])
def sent():
    select = request.form.get('search_kw')
    #return str(select)
    data = getkw_trends(str(select))
    data2 = sentiment(str(select))
    return render_template('trendsenti.html', data=data, data2=data2)