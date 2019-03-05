##The sutomate project
##for college wifi self login
##when you assert upon a condition,
##the reply will give if the assertion is true or false. 

from selenium import webdriver
import subprocess
from Tkinter import * 

results = subprocess.check_output(['netsh' , 'wlan', 'show', 'interface'])
string1 = 'Students'
string2 = 'Hostel'

rain = results.find(string1, 0, len(results))   ### discrepancy in find as it finds even a single letter
november = results.find(string2, 0, len(results)) ### ok for my purpose though
a = ['Login failed. Invalid user name/password. Please contact the administrator.', 'Login failed. You have reached the maximum login limit.']

def func():
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
    driver.get('http://theURL')

    username = driver.find_element_by_name('username')
    username.send_keys('YOURID')

    password = driver.find_element_by_name('password')
    password.send_keys('YOURPASSWORD')
    
    blick = driver.find_element_by_id('loginbutton')
    blick.click()

    
if rain != -1 or november != -1:
    func()
    
else:
    root = Tk()
    root.title('Not connected')
    label_1= Label(root, text="Not Connected to wifi")
    label_1.grid(row=1,column =1, pady=10, padx=5, sticky=W)
    label_1= Label(root, text="SSID: Students or Hostel.")
    label_1.grid(row=1,column =2, pady=10, padx=5, sticky=E)


    button_file= Button(root, text="QUIT")
    button_file.bind("<Button-1>", lambda event : root.destroy())
    button_file.grid(row = 2, column =2, padx=10, pady=10)
    
    button_ref= Button(root, text="TRY AGAIN")
    button_ref.bind("<Button-1>", lambda event : func())
    button_ref.grid(row = 2, column =1, pady=10)

    root.mainloop()




'''
Add thia if you want to. i think its not uaeful for me.

elem = driver.find_element_by_id('loginfailed')
    print elem.text

    if elem.text in a:
        root = Tk()
        root.title('Login Failed')
        button_file= Button(root, text="QUIT")
        button_file.bind("<Button-1>", lambda event : root.destroy())
        button_file.grid(row = 1, column =2, padx=10, pady=10)
        
        button_ref= Button(root, text="TRY AGAIN")
        button_ref.bind("<Button-1>", lambda event : func())
        button_ref.grid(row = 1, column =1, padx=10, pady=10)

        root.mainloop()
'''
            
    
