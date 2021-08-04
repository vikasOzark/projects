from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk
from PIL import ImageDraw,ImageFont

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
		self.load_img = Image.open('/home/vikas/Pyhton file/bg.jpg')
		resized = self.load_img.resize((1920, 1300),Image.ANTIALIAS)
		self.bg = ImageTk.PhotoImage(resized)
		self.root.config(bg='#34ebba')
		self.color = '#1d1e1f'
		
		

#	1st frame creation--------		-alpha, -topmost, -zoomed, -fullscreen, or -type
		fram1 = Frame(self.root,bg = 'white')
		fram1.place(x=250,y=0,relwidth=1,relheight=1)

#	Title and its labes for entry--------------x=40,y=10
		title = Label(fram1,text='Registration Window',font=('times new row',20,'bold'),fg='green',bg=self.color,image=self.bg).place(relwidth=1,relheight=1)
		
		first_name = Label(fram1,text = "First Name *",font=('times new row',14,'bold',),fg='white',bg=self.color).place(x = 40,y = 60)
		self.first_name = Entry(fram1,width = 30,insertbackground='#a4e0c9')
		self.first_name.place(x = 40,y = 90)

		last_name = Label(fram1,text = "Last Name ",font=('times new row',14,'bold'),fg='white',bg=self.color).place(x = 300,y = 60)
		self.last_name = Entry(fram1,width = 30)
		self.last_name.place(x = 300,y = 90)

		Mobile_num = Label(fram1,text = "Mobile Number *",font=('times new row',14,'bold'),fg='white',bg=self.color).place(x = 40,y = 120)
		self.Mobile_num = Entry(fram1,width = 30)
		self.Mobile_num.place(x = 40,y = 150)

		Age = Label(fram1,text = "Age *",font=('times new row',14,'bold'),fg='white',bg=self.color).place(x = 300,y = 120)
		self.Age = Entry(fram1,width = 30)
		self.Age.place(x = 300,y = 150)

		email = Label(fram1,text = "Email *",font=('times new row',14,'bold'),fg='white',bg=self.color).place(x = 40,y = 180)
		self.email = Entry(fram1,width = 30)
		self.email.place(x = 40,y = 210)

		passwd = Label(fram1,text = "Password *",font=('times new row',14,'bold'),fg='white',bg=self.color).place(x = 300,y = 180)
		self.passwd = Entry(fram1,width = 30,show='*')
		self.passwd.place(x = 300,y = 210)


		re_passwd = Label(fram1,text = "Re-Enter Password *",font=('times new row',14,'bold'),fg='white',bg=self.color).place(x = 200,y = 240)
		self.re_passwd = Entry(fram1,width = 30,show='*')
		self.re_passwd.place(x =180,y = 280)


#	Fetching data -----------------------
		def fetch_data(self):

			fetch = Frame(self.root,bg='white')
			fetch.place(x=250,y=0,relwidth=1,relheight=1)

			self.Output = Text(fetch, x = 300, y = 90,height = 30 , width = 85, bg = "light cyan",wrap = WORD).pack()
			
			name = Label(fetch,text = "Name",font=('times new row',14,'bold'),bg='white').place(x = 60,y = 60)
			self.name = Entry(fetch,width = 30)
			self.name.place(x = 60,y = 90)

			DOB = Label(fetch,text = "Date Of Birth",font=('times new row',14,'bold'),bg='white').place(x = 310,y = 60)
			self.DOB = Entry(fetch,width = 30)
			self.DOB.place(x = 310,y = 90)

			ok_btn = Button(fetch,text='See Data',command=lambda:show_data(self)).place(x=135 , y = 150)
			Exit = Button(fetch,text = "Exit",command=self.root.destroy).place(x = 220,y = 150)
				
# 	log in frame creation-----------------
		def log_in_frame(self):
			log_frame = Frame(self.root,bg='white')
			log_frame.place(x=250,y=0,relwidth=1,relheight=1)

			log_in_username = Label(log_frame,text = "USERNAME",font=('times new row',14,'bold'),bg='white').place(x = 60,y = 60)
			self.log_in_username = Entry(log_frame,width = 40)
			self.log_in_username.place(x = 60,y = 90)

			log_in_passwd = Label(log_frame,text = "Password",font=('times new row',14,'bold'),bg='white').place(x = 400,y = 60)
			self.log_in_passwd = Entry(log_frame,width = 40)
			self.log_in_passwd.place(x = 400,y = 90)

			log_in_ = Button(log_frame,text = "Log in",command=lambda:log_check(self)).place(x = 140,y = 400)
			Exit = Button(log_frame,text = "Exit",command=self.root.destroy).place(x = 255,y = 400)

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
					see_data_frame(self)

#	database fetch data ------------
		def show_data(self):
			name = self.name.get()
			try:
				cur.execute('SELECT * FROM Credentials WHERE first_name=%s',(name,))
				out_cur = cur.fetchone()
				print(out_cur)
				#self.Output.insert(root,0.0,test)
				
			except Exception as es:
				messagebox.showinfo('Something Wrong',f'{es}')

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
			stg_number = str(Mobile_num)

			if first_name == '' or Mobile_num == '' or  Age == '' or email == '' or passwd == '' :
				messagebox.showwarning("Warning",'Fill All Required Parameters',parent=self.root)

			#elif stg_number != len(10):
				#messagebox.showinfo('Phone Number','Invalid NUmber')

			elif passwd != len(8):
				messagebox.showinfo('Password Format','Atleast 8 Charater, Should be having ( @ , $ , & , ^ )')

			elif passwd != re_passwd:
				messagebox.showwarning('Warning','Password not matched' , parent=self.root)
			
			elif cur == None:
				cur.execute("INSERT INTO Credentials(first_name,last_name,mobile_number,age,email,passwd) VALUES(%s,%s,%s,%s,%s,%s)",(first_name,last_name,Mobile_num,Age,email,passwd))
				conn.commit()
				fetch_data(self)

			else:
				messagebox.showinfo("Email Matched","Email Already Exist")
				
# 	2nd frame--------------------------m
		def see_data_frame(self):
			regstr_frame = Frame(self.root,bg='white')
			regstr_frame.place(x=250,y=0,relwidth=1,relheight=1)

			see_data = Button(regstr_frame,text='See Data',command=lambda:fetch_data(self)).place(x=40 , y = 400)
			log_out = Button(regstr_frame,text='Log Out',command= lambda:log_in_frame(self)).place(x=160,y=400)
			exit = Button(regstr_frame,text='Exit',command=self.root.destroy).place(x = 260, y = 400)

#	buttons for resg ,Exit and login------------------
		submit_button = Button(fram1,text = "Register",command =lambda: Check_reg(self),relief=RIDGE,activebackground='#46dbd9').place(x = 40,y = 400)

		log_in = Button(fram1,text = "Log in",command=lambda:log_in_frame(self),relief=RIDGE,activebackground='#46dbd9').place(x = 140,y = 400)

		Exit = Button(fram1,text = "Exit",command=self.root.destroy,relief=RIDGE,activebackground='#46dbd9').place(x = 225,y = 400)

		log_test = Button(fram1,text = "Log test",command=lambda:fetch_data(self),relief=RIDGE,activebackground='#46dbd9').place(x = 300,y = 400)


#--------------------------------------------------------------------
def Main():
	obj = Registration(root)

Main()
root.mainloop()
