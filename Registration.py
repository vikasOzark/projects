from tkinter import *
from tkinter import messagebox
from tkinter import StringVar
import tksheet
import mysql.connector
from PIL import Image,ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import requests
from bs4 import BeautifulSoup
from alpha_vantage.timeseries import TimeSeries
import json
import pandas
from tkcalendar import Calendar

#----------------------------------- 

conn = mysql.connector.connect(
			host= 'localhost',
			user='root',
			passwd='Vikas@123',
			database='GYM',
			auth_plugin='mysql_native_password')
cur = conn.cursor(buffered=True)
root = Tk()

#-----------------------------

class Registration:
	def __init__(self,root):
		self.root = root
		self.root.title('DASH WINDOW')
		self.root.geometry('1350x700+0+0')
		self.root.attributes( '-zoomed',True)  
		self.root.config(bg='#34ebba')

		self.color = 'white'
		self.txt_color = 'green'
		self.x_cordnts_enty = 900
		self.x_2ndRow = 1200	
		self.button_c = "light cyan"
		self.api_key = '2S3HAXUPTY554T7C'	

#	1st Canvas creation--------		-alpha, -topmost, -zoomed, -fullscreen, or -type
		fram1 = Canvas(self.root,bg = 'white')
		fram1.place(x=250,y=0,relwidth=1,relheight=1)

		#fram1 = LabelFrame(fram_main,text = ' Home Register',height=800,width=600,bg='white')
		#fram1.place(x=800,y=100)

#	Title and its labes for entry--------------x=40,y=10
		
		first_name = Label(fram1,
			text = "First Name *",
			font=('times new row',14,'bold',),
			fg=self.txt_color,
			bg=self.color).place(
								x = self.x_cordnts_enty,
								y = 60)
		
		self.first_name = Entry(fram1,
			width = 30,
			borderwidth=5,
			relief=RIDGE)
		self.first_name.place(
							x = self.x_cordnts_enty, 
							y = 90)

		last_name = Label(fram1,
			text = "Last Name ",
			font=('times new row',14,'bold'),
			fg=self.txt_color,
			bg=self.color).place(
								x =self.x_2ndRow, 
								y = 60)

		self.last_name = Entry(fram1,
			width = 30,
			borderwidth=5,
			relief=RIDGE)
		self.last_name.place(
							x = self.x_2ndRow,
							y = 90)

		Mobile_num = Label(fram1,
			text = "Mobile Number *",
			font=('times new row',14,'bold'),
			fg=self.txt_color,
			bg=self.color).place(
								x = self.x_cordnts_enty,
								y = 125)

		self.Mobile_num = Entry(fram1,
			width = 30,
			borderwidth=5,
			relief=RIDGE)
		self.Mobile_num.place(
							x = self.x_cordnts_enty,
							y = 150)

		Age = Label(fram1,
			text = "Age *",
			font=('times new row',14,'bold'),
			fg=self.txt_color,
			bg=self.color).place(
								x = self.x_2ndRow,
								y = 125)

		self.Age = Entry(fram1,
			width = 30,
			borderwidth=5,
			relief=RIDGE)
		self.Age.place(
					x = self.x_2ndRow,
					y = 150)

		email = Label(fram1,
			text = "Email *",
			font=('times new row',14,'bold'),
			fg=self.txt_color,
			bg=self.color).place(
								x = self.x_cordnts_enty,
								y = 185)

		self.email = Entry(fram1,
			width = 30,
			borderwidth=5,
			relief=RIDGE)
		self.email.place(
						x = self.x_cordnts_enty,
						y = 210)

		passwd = Label(fram1,
			text = "Password *",
			font=('times new row',14,'bold'),
			fg=self.txt_color,
			bg=self.color).place(
								x = self.x_2ndRow,
								y = 185)

		self.passwd = Entry(fram1,
			width = 30,
			show='*',
			borderwidth=5,
			relief=RIDGE)
		self.passwd.place(
						x = self.x_2ndRow,
						y = 210)

		re_passwd = Label(fram1,
			text = "Re-Enter Password *",
			font=('times new row',14,'bold'),
			fg=self.txt_color,
			bg=self.color).place(
								x = 1050,
								y = 245)

		self.re_passwd = Entry(fram1,
			width = 30,
			show='*',
			borderwidth=5,
			relief=RIDGE)
		self.re_passwd.place(
							x =1050,
							y = 280)

#	buttons for resg ,Exit and login------------------

		submit_button = Button(fram1,text = "Register",
									command = lambda: Check_reg(self),
									relief = RAISED,
									activebackground=self.button_c).place(x = 900,y = 350)

		log_in = Button(fram1,text = "Log in",
									command = lambda:log_in_Canvas(self),
									relief=RAISED,
									activebackground=self.button_c).place(x = 1010,y = 350)

		Exit = Button(fram1,text = "Exit",
									command = self.root.destroy,
									relief=RAISED,
									activebackground='red').place(x = 1110,y = 350)

		log_test = Button(fram1,text = "Log test",
									command = lambda:fetch_data(self),
									relief=RAISED,
									activebackground=self.button_c).place(x = 1200,y = 350)

#	Fetching data -----------------------
		def fetch_data(self):

			fetch_home = Canvas(self.root,bg='white')
			fetch_home.place(x=250,y=0,relwidth=1,relheight=1)

			fetch = LabelFrame(fetch_home,text='See User Data',bg = 'white',width=600,height=300)
			fetch.place(x=50,y=100)

			header = ['Id','Name','Last Name','Mobile Number','Age','Email','Password']
			self.sheet = tksheet.Sheet(fetch_home,show_table = True,
													headers = header ,
													header_align = "center",
													height=300,width=800,)
			self.sheet.place(x = 700,y = 100)


			name_l = Label(fetch,text = "Name",font=('times new row',14,'bold'),bg='white').place(x = 60,y = 60)
			self.name = Entry(fetch,width = 30)
			self.name.place(x = 60,y = 90)

			Age = Label(fetch,text = "Age",font=('times new row',14,'bold'),bg='white').place(x = 310,y = 60)
			self.Age = Entry(fetch,width = 30)
			self.Age.place(x = 310,y = 90)

			ok_btn = Button(fetch,text='See Data',
									command=lambda:show_data(self),
									activebackground=self.button_c).place(x=135 , y = 150)

			Exit = Button(fetch,text = "Exit",
									command=self.root.destroy,
									activebackground='red').place(x = 250,y = 150)

			back_btn = Button(fetch,text='Back',
									command=lambda:see_data_Canvas(self),
									activebackground=self.button_c).place(x=320,y = 150)
				


#	database fetch data ------------
		def show_data(self):
			names = self.name.get()
			Age = self.Age.get()
			try:
				cur.execute('SELECT * FROM Credentials WHERE first_name=%s',(names,))
				self.out_cur=list(cur.fetchone())

				cur.execute('SELECT * FROM Credentials WHERE Age=%s',(Age,))
				self.out_age=list(cur.fetchone())

				if self.out_cur and self.out_age != None:
					self.sheet.set_sheet_data([[f'{values}' for values in self.out_cur]])

			except:
				messagebox.showinfo('Something Wrong','Please Provide Correct Details')


# 	log in Canvas creation----------------------
		def log_in_Canvas(self):
			_Canvas = Canvas(self.root,bg='white')
			_Canvas.place(x = 250,y = 0,relwidth = 1,relheight = 1)

			log_Canvas = LabelFrame(_Canvas, text="LOG IN",bg ='white',height=300,width=800)  
			log_Canvas.place(x=100,y=100)  

			log_in_username = Label(log_Canvas,text = "USERNAME",
												font=('times new row',14,'bold'),
												bg='white',).place(x = 60,y = 60)

			self.log_in_username = Entry(log_Canvas,width = 40,relief=RIDGE,borderwidth=5)
			self.log_in_username.place(x = 60,y = 90)

			log_in_passwd = Label(log_Canvas,text = "Password",
												font=('times new row',14,'bold'),
												bg='white').place(x = 400,y = 60)

			self.log_in_passwd = Entry(log_Canvas,width = 40,show='*',borderwidth=5,relief=RIDGE)
			self.log_in_passwd.place(x = 400,y = 90)

			log_in_ = Button(log_Canvas,text = "Log in",
										command=lambda:log_check(self),
										relief=RAISED,
										activebackground=self.button_c).place(x = 60,y = 150)

			Exit = Button(log_Canvas,text = "Exit",
										command=self.root.destroy,
										relief=RAISED,
										activebackground='red').place(x = 150,y = 150)


# 	log in credencials with check if empty cell are left---------------
		def log_check(self):
			# DABASES user name and passwd check---------------
			user = self.log_in_username.get()
			passwd = self.log_in_passwd.get()

			if user == '' or passwd == '' :
				messagebox.showwarning('Warning','Credentials Needed',parent= self.root)

			else:
				user = cur.execute("SELECT * FROM Credentials WHERE email= %s",(user,))
				user = cur.fetchone()

				pas = cur.execute("SELECT * FROM Credentials WHERE passwd = %s",(passwd,))
				pas = cur.fetchone()

				if user == None:
					messagebox.showinfo('Wrong Credentials','Invalid Email !')
				elif pas == None :
					messagebox.showinfo('Wrong Credentials','Invalid Password !')
				else:
					see_data_Canvas(self)

# 	check for registration----------

		def Check_reg(self):
			first_name = self.first_name.get()
			last_name = self.last_name.get()
			Mobile_num = self.Mobile_num.get()
			Age = self.Age.get()
			email = self.email.get()
			passwd = self.passwd.get()
			re_passwd = self.re_passwd.get()

			cur.execute('SELECT email FROM Credentials  WHERE email= %s',(email,))
			check = cur.fetchone()
			
			if first_name == '' or Mobile_num == '' or  Age == '' or email == '' or passwd == '' :
				messagebox.showwarning("Warning",'Fill All Required Parameters',parent=self.root)

			elif len(Mobile_num) != 10:
				messagebox.showinfo('Phone Number','Invalid NUmber')


			elif passwd != re_passwd:
				messagebox.showwarning('Warning','Password not matched' , parent=self.root)
			

			elif len(passwd) <= 7:
				messagebox.showinfo('Password Format','Atleast 8 Charater, Should be having ( @ , $ , & , ^ )')

			elif check == None:
				cur.execute("INSERT INTO Credentials(first_name,last_name,mobile_number,age,email,passwd) VALUES(%s,%s,%s,%s,%s,%s)",
																					(first_name,last_name,Mobile_num,Age,email,passwd))
																						
				conn.commit()
				messagebox.showinfo('Success','Succesfully Sighed Up')
				see_data_Canvas(self)
				

			else:
				messagebox.showinfo("Email Matched","Email Already Exist")

#------adding new stock into the db ----------------------------------------------------------
		def DB_stock_add(self):
			try:
				comp_name = self.comp_add_widget.get()
				comp_symbol = self.comp_add_symbol.get()
				
				cur.execute('INSERT INTO Stock_data(Stock_name,Stock_symbol) VALUES(%s,%s)',(comp_name,comp_symbol))
				conn.commit()
				messagebox.showinfo('Adding','Done')
				
			except:
				messagebox.showinfo('Try again','Check Again')
		


# 	2nd Canvas--------------------------m

		def see_data_Canvas(self):
			regstr_frame = Canvas(self.root,bg='white')
			regstr_frame.place(x=250,y=0,relwidth=1,relheight=1)
#----------------------------------------------------------------
			labelframe1 = LabelFrame(regstr_frame, text="Options",width=500,height=300,bg='white')  
			labelframe1.place(x=100,y=100)  
#--------------------------------------------------------------------
			lable_frame_add = LabelFrame(regstr_frame,
										text = 'New Stock Add',
										bg='white',width=500,
										height=300)
			lable_frame_add.place(x = 700 , y = 100)
#--------------------------------------------------------------------
			add_company = Button(lable_frame_add,text='Exceute',
										command=lambda:DB_stock_add(self),
										activebackground=self.button_c).place(x=390 , y = 240)
										
			add_company = Button(lable_frame_add,text='Clear',
											command=lambda:Clear_entry(self),
											activebackground=self.button_c).place(x=330 , y = 240)
#--------------------------------------------------------------------
			comp_add_l = Label(lable_frame_add,
						text = "Company Name :",
						font=('times new row',12,'bold'),
						fg=self.txt_color,
						bg=self.color).place(
											x = 10,
											y = 20)

			self.comp_add_widget = Entry(lable_frame_add,
										width = 30,
										borderwidth=5,
										relief=RIDGE)
			self.comp_add_widget.place(
							x =190,
							y = 20)
#--------------------------------------------------------------------
			comp_add_l = Label(lable_frame_add,
						text = "Company Symbol :",
						font=('times new row',12,'bold'),
						fg=self.txt_color,
						bg=self.color).place(
											x = 10,
											y = 80)
 
			self.comp_add_symbol = Entry(lable_frame_add,
										width = 30,
										borderwidth=5,
										relief=RIDGE)
			self.comp_add_symbol.place(
							x =190,
							y = 76)

#--------------------------------------------------------------------

			see_data = Button(labelframe1,text='See Data',
										command=lambda:fetch_data(self),
										activebackground=self.button_c).place(x=10 , y = 20)

			log_out = Button(labelframe1,text='Log Out',
										command= lambda:log_in_Canvas(self),
										activebackground=self.button_c).place(x=120,y=20)

			exit = Button(labelframe1,text='Exit',
										activebackground='red',
										command=self.root.destroy).place(x = 220, y = 20)

			stocks_view_DB = Button(labelframe1,text='See Stocks',
										command=lambda:stocks_view(self),
									activebackground=self.button_c).place(x = 10 , y = 60)
		def Clear_entry(self):
			self.comp_add_widget.delete(0,END)
			self.comp_add_symbol.delete(0,END)


# 	PLOTING CHART

		def plot(self):
			ts = TimeSeries(key=self.api_key,output_format='json')
			date = self.date_widget.get()
			frequently = self.StringVr.get()

			comp_str_get = self.String_Comp.get()
			cur.execute('SELECT * FROM Stock_data  where Stock_name = %s',(comp_str_get,))
			db_symbol = cur.fetchone()[2]

			if len(date) >= 11:
				messagebox.showinfo('Alert','Date Not Correct')

			elif len(date) <= 9:
				messagebox.showinfo('Alert','Date Not Correct')

			elif frequently == 'Daily':
				data = ts.get_daily(db_symbol)

			elif frequently == 'Weekly':
				data = ts.get_weekly(db_symbol)

			elif frequently == 'Monthly':
				data = ts.get_monthly(db_symbol)

			stock_data= data[0][date]
			stock_value = list(stock_data.values())

			self.sheet.set_sheet_data([[f'{values}' for values in stock_value]])

			
			# the figure that will contain the plot
			fig = Figure(figsize = (5, 5),
							dpi = 80)
			# adding the subplot
			plot1 = fig.add_subplot(111)

			# plotting the graph
			plot1.plot(stock_value[:4])

			# creating the Tkinter canvas
			# containing the Matplotlib figure
			canvas = FigureCanvasTkAgg(fig,master = self.chart_render)
			canvas.draw()

			# placing the canvas on the Tkinter window
			canvas.get_tk_widget().pack()

			# creating the Matplotlib toolbar
			toolbar = NavigationToolbar2Tk(canvas,self.chart_render)  
			toolbar.update()

			# placing the toolbar on the Tkinter window
			canvas.get_tk_widget().pack()
			print(Option_val(self))

# 	stock data canvas ------------------

		def stocks_view(self):
			browse_canvas = Canvas(self.root,bg = 'white')
			browse_canvas.place(x=250,y=0,relwidth=1,relheight=1)

			lable_frame_br = LabelFrame(browse_canvas,
				text = 'Browse Options',
				bg='white',width=600,
				height=400)
			lable_frame_br.place(x = 50 , y = 50)


#-----------------------------------------------------			
			company_name = Label(lable_frame_br,
						text = "Company name :",
						font=('times new row',12,'bold'),
						fg=self.txt_color,
						bg=self.color).place(
											x = 10,
											y = 15)

			cur.execute('SELECT * FROM Stock_data')
			com_val = cur.fetchall()

			options=[]
			for i in com_val:
				value = i[1]
				options.append(value)

			self.String_Comp = StringVar()
			self.String_Comp.set(' Select ')
			option_menu = OptionMenu(lable_frame_br,self.String_Comp,*options)
			option_menu.place(x = 170 , y = 10)

#-----------------------------------------------------

			frequently_choose = Label(lable_frame_br,
						text = "Frequently :",
						font=('times new row',12,'bold'),
						fg=self.txt_color,
						bg=self.color).place(
											x = 10,
											y = 55)

			options = ('Daily','Weekly','Monthly')
			self.StringVr = StringVar()
			self.StringVr.set(' Choose ')
			option_menu = OptionMenu(lable_frame_br,self.StringVr,*options)
			option_menu.place(x = 170 , y = 50)
#	-----------------------------------------------------
			date_choose = Label(lable_frame_br,
						text = "Date :",
						font=('times new row',12,'bold'),
						fg=self.txt_color,
						bg=self.color).place(
											x = 10,
											y = 95)
			date_fromat  = Label(lable_frame_br,fg='grey',
											text='(YYYY-MM-DD)',
											bg = 'white')
			date_fromat.place(x=70,y=95)

			self.date_widget = Entry(lable_frame_br,
									width = 30,
									borderwidth=5,
									relief=RIDGE)
			self.date_widget.place(
							x =170,
							y = 90)

#----------------------------------------------------------
			btn = Button(lable_frame_br,
				text= 'Submit',
				activebackground=self.button_c,
				command=lambda:plot(self))
			btn.place(x = 470 ,y = 335)

			exit = Button(lable_frame_br,activebackground='red',
										text='Close',
										command=self.root.destroy).place(x = 330, y = 335)

			back_to_data = Button(lable_frame_br,text='Back',
										activebackground=self.button_c,
										command=lambda:see_data_Canvas(self)).place(x = 400, y = 335)

#----------------------------------------------
			self.chart_render = Frame(browse_canvas,
									bg = 'light cyan',
									height=395,width=900)
									#(x= 700, y = 55)
			self.chart_render.place(x= 800, y = 55)
			
#------------------------------------------------
			header = ['open','High','Low','Close','Volume']
			self.sheet = tksheet.Sheet(browse_canvas,
											show_table = True,
											headers = header ,
											header_align = "center",
											height=400,width=1200,)

			self.sheet.place(x = 50,y = 600)
			
#----geting values from option widget -------------------

		def Option_val(self):
			val = self.StringVr.get()
			company = self.String_Comp.get()
			date_widget = self.date_widget.get()
			return val,company,date_widget
		
def Main():
	obj = Registration(root)

Main()
root.mainloop()
