from flask import Flask,redirect, request, render_template, session
import os
from iex_query import *
from pca_model import *

app = Flask(__name__)

app.secret_key = (os.urandom(16))


@app.route('/')
def home_page(name=None):
    return render_template('homepage.html', name=name)

@app.route('/walkthrough')
def calcs():
    session['tickers'] = stocks
    data, dataraw = get_and_clean_data(stocks)
    graph1 = plot_stock_rets(data)
    graph2 = plotlypca()
    graph3 = highest_corr()
    return render_template('walkthrough.html', plot1 = graph1, plot2=graph2, plot3=graph3)
