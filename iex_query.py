import pandas_datareader as web
from datetime import datetime
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import psycopg2
import cvxopt as opt
from cvxopt import blas, solvers
import numpy as np
import matplotlib.dates as mdates
import pygal
import plotly
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.tools as tls
import json
import mpld3

def get_data(ticker):

    start = datetime(2016, 1, 1)
    end   = datetime(2019, 3, 1)

    f = web.DataReader(ticker, 'iex', start, end)
    df = f["close"]
    df.index.name = 'date'
    return df
