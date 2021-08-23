from tkinter import *

import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk
from charts import plot

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

		submit_button = Button(fram1,text = "Register",command =lambda: Check_reg(self),relief = RAISED).place(x = 900,y = 350)

		log_in = Button(fram1,text = "Log in",command=lambda:log_in_Canvas(self),relief=RAISED).place(x = 1010,y = 350)

		Exit = Button(fram1,text = "Exit",command=self.root.destroy,relief=RAISED).place(x = 1110,y = 350)

		log_test = Button(fram1,text = "Log test",command=lambda:fetch_data(self),relief=RAISED).place(x = 1200,y = 350)


#	Fetching data -----------------------
		def fetch_data(self):

			fetch_home = Canvas(self.root,bg='white')
			fetch_home.place(x=250,y=0,relwidth=1,relheight=1)

			fetch = LabelFrame(fetch_home,text='See User Data',bg = 'white',width=600,height=300)
			fetch.place(x=50,y=100)

			self.Output = Text(fetch_home,height = 17 , width = 115, bg = "light cyan",wrap = WORD)
			self.Output.place(x = 700,y = 100)

			name = Label(fetch,text = "Name",font=('times new row',14,'bold'),bg='white').place(x = 60,y = 60)
			self.name = Entry(fetch,width = 30)
			self.name.place(x = 60,y = 90)

			DOB = Label(fetch,text = "Date Of Birth",font=('times new row',14,'bold'),bg='white').place(x = 310,y = 60)
			self.DOB = Entry(fetch,width = 30)
			self.DOB.place(x = 310,y = 90)

			ok_btn = Button(fetch,text='See Data',command=lambda:show_data(self)).place(x=135 , y = 150)
			Exit = Button(fetch,text = "Exit",command=self.root.destroy).place(x = 250,y = 150)
			back_btn = Button(fetch,text='Back',command=lambda:see_data_Canvas(self)).place(x=320,y = 150)
				


#	database fetch data ------------
		def show_data(self):
			name = self.name.get()
			
			try:
				cur.execute('SELECT * FROM Credentials WHERE first_name=%s',(name,))
				self.out_cur=cur.fetchone()
				text = self.Output.insert(0.0,self.out_cur)
				
			except Exception as es:
				messagebox.showinfo('Something Wrong',f'{es}')


# 	log in Canvas creation-----------------
		def log_in_Canvas(self):
			_Canvas = Canvas(self.root,bg='white')
			_Canvas.place(x=250,y=0,relwidth=1,relheight=1)

			log_Canvas = LabelFrame(_Canvas, text="LOG IN",bg='white',height=300,width=800)  
			log_Canvas.place(x=100,y=100)  

			log_in_username = Label(log_Canvas,text = "USERNAME",font=('times new row',14,'bold'),bg='white',).place(x = 60,y = 60)
			self.log_in_username = Entry(log_Canvas,width = 40,relief=RIDGE,borderwidth=5)
			self.log_in_username.place(x = 60,y = 90)

			log_in_passwd = Label(log_Canvas,text = "Password",font=('times new row',14,'bold'),bg='white').place(x = 400,y = 60)
			self.log_in_passwd = Entry(log_Canvas,width = 40,show='*',borderwidth=5,relief=RIDGE)
			self.log_in_passwd.place(x = 400,y = 90)

			log_in_ = Button(log_Canvas,text = "Log in",command=lambda:log_check(self),relief=RAISED).place(x = 60,y = 150)
			Exit = Button(log_Canvas,text = "Exit",command=self.root.destroy,relief=RAISED).place(x = 150,y = 150)


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
			
			if first_name == '' or Mobile_num == '' or  Age == '' or email == '' or passwd == '' :
				messagebox.showwarning("Warning",'Fill All Required Parameters',parent=self.root)

			elif len(Mobile_num) != 10:
				messagebox.showinfo('Phone Number','Invalid NUmber')


			elif passwd != re_passwd:
				messagebox.showwarning('Warning','Password not matched' , parent=self.root)
			

			elif len(passwd) <= 7:
				messagebox.showinfo('Password Format','Atleast 8 Charater, Should be having ( @ , $ , & , ^ )')

			elif cur == None:
				cur.execute("INSERT INTO Credentials(first_name,last_name,mobile_number,age,email,passwd) VALUES(%s,%s,%s,%s,%s,%s)",
																					(first_name,last_name,Mobile_num,Age,email,passwd))
																						
				conn.commit()
				fetch_data(self)

			else:
				messagebox.showinfo("Email Matched","Email Already Exist")
				

# 	2nd Canvas--------------------------m

		def see_data_Canvas(self):
			regstr_frame = Canvas(self.root,bg='white')
			regstr_frame.place(x=250,y=0,relwidth=1,relheight=1)

			labelframe1 = LabelFrame(regstr_frame, text="Options",width=500,height=200,bg='white')  
			labelframe1.place(x=100,y=100)  

			see_data = Button(labelframe1,text='See Data',command=lambda:fetch_data(self)).place(x=10 , y = 20)
			log_out = Button(labelframe1,text='Log Out',command= lambda:log_in_Canvas(self)).place(x=120,y=20)
			exit = Button(labelframe1,text='Exit',command=self.root.destroy).place(x = 220, y = 20)

			stocks_view_DB = Button(labelframe1,text='See Stocks',command=lambda:stocks_view(self)).place(x = 10 , y = 60)


# 	stock data canvas ------------------

		def stocks_view(self):
			from tkinter import StringVar

			browse_canvas = Canvas(self.root,bg = 'white')
			browse_canvas.place(x=250,y=0,relwidth=1,relheight=1)

			lable_frame_br = LabelFrame(browse_canvas,
				text = 'Browse Options',
				bg='white',width=600,
				height=400)
			lable_frame_br.place(x = 50 , y = 50)
#-----------------------------------------------------
			options = ('Daily','Weekly','Monthly')
			StringVr = StringVar()
			StringVr.set(options[0])
			option_menu = OptionMenu(lable_frame_br,StringVr,*options)
			option_menu.place(x = 10 , y = 50)

			string_val  = StringVr.get()
#----------------------------------------------

			chart_render = Frame(browse_canvas,
				bg = 'light cyan',
				height=395,width=900)
			chart_render.place(x= 700, y = 55)

#-------------------------------------------------

			chart_lableFrame = Text(browse_canvas,
				height = 27 , 
				width = 195, bg = "light cyan",
				wrap = WORD)
			chart_lableFrame.place(x = 50,y = 500)

#------------------------------------------------

			btn = Button(lable_frame_br,
				text= 'tes',
				command=lambda:plot(
									chart_render,
									chart_lableFrame,string_val
									))
									

			btn.place(x = 10 ,y = 10)


def Main():
	obj = Registration(root)

Main()
root.mainloop()
