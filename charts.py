from tkinter import StringVar
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

import requests
from bs4 import BeautifulSoup
from alpha_vantage.timeseries import TimeSeries
import json
import pandas
api_key = '2S3HAXUPTY554T7C'


def data(chart_lableFrame,string_val):
	ts = TimeSeries(key=api_key,output_format='pandas')
	print(string_val)
	if string_val == 'Monthly':
		data = ts.get_monthly('TCS')
		chart_lableFrame.insert(0.0,data[0])
	elif string_val == 'Weekly':
		data = ts.get_monthly('TCS')
		chart_lableFrame.insert(0.0,data[0])
	


def plot(chart_render,chart_lableFrame,string_val):


	# the figure that will contain the plot
	fig = Figure(figsize = (5, 5),
				dpi = 80)

	# list of squares
	y = [5,16,1,5,2,5,2,5,2,2,20]

	# adding the subplot
	plot1 = fig.add_subplot(111)

	# plotting the graph
	plot1.plot(y)

	# creating the Tkinter canvas
	# containing the Matplotlib figure
	canvas = FigureCanvasTkAgg(fig,
							master = chart_render)
	canvas.draw()

	# placing the canvas on the Tkinter window
	canvas.get_tk_widget().pack()

	# creating the Matplotlib toolbar
	toolbar = NavigationToolbar2Tk(canvas,
								chart_render)
	toolbar.update()

	# placing the toolbar on the Tkinter window
	canvas.get_tk_widget().pack()
	data(chart_lableFrame,string_val)
