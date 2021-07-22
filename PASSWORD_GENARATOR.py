import random
import string
def Get_pwd():
    while True:
        try:
            Len_passwd = int(input('Please enter Your desire lenth of the PASSWORD:: '))
            Add_name = input('Please enter the any desire keyword:: ').capitalize()
            ran_chatr = ['@@','$$','&_','%~','@&']
            ran_digit = [1,2,3,4,5,6,7,8,9,0]
            #Main = []
            if Len_passwd >= 6:
                pwd = Add_name + random.choice(ran_chatr) + str(random.randint(0,10))+'\n'
                #Main.append(pwd)
                with open('Password.txt','a') as file:
                    file.write(pwd)
                inp = input('Want to print new password or Quit(P),(Q),(r):: ').lower()
                if inp == 'p':
                    print(pwd)
                elif inp == 'r':
                    with open('Password.txt','a') as file:
                        print(file.read())
                else:
                    quit()
        except:
            print('kuch to gadbad hai')
Get_pwd()