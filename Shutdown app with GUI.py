import tkinter
import os

def restart():
  return os.system("shutdown /r /t 1")    #/r for restart and /t for time delay and number for seconds
def restart_with_time():
  return os.system("shutdown /r /t 20")
def log_out():
  return os.system("shutdown -l")   #-l = log out command
def shutdown():
  return os.system("shutdown /s /t 1")    #/s = shut down



st = tkinter.Tk()      #GUI window  #st =shut
st.title("Shutdown Python app with GUI")    #Window title
st.geometry("500x250")    #Window size width and height
st.config(bg="silver")    #Background color

restart_button = tkinter.Button(st, text="Restart", font=("Times New Roman",10,"bold"),relief=tkinter.RAISED, cursor = "plus", command = restart)  #tkinter.RAISED
restart_button.place(x=62.5,y=60,height=40,width=100)

restart_with_time_button = tkinter.Button(st, text="Restart\nwith Timer", font=("Times New Roman",10,"bold"),relief=tkinter.RAISED, cursor = "plus", command = restart_with_time)  #tkinter.RAISED
restart_with_time_button.place(x=62.5,y=140,height=40,width=100)

log_out_button = tkinter.Button(st, text="Log Out", font=("Times New Roman",10,"bold"),relief=tkinter.RAISED, cursor = "plus", command = log_out)  #tkinter.RAISED
log_out_button.place(x=337.5,y=140,height=40,width=100)

shut_down_button = tkinter.Button(st, text="Shut Down", font=("Times New Roman",10,"bold"),relief=tkinter.RAISED, cursor = "plus", command = shutdown)  #tkinter.RAISED
shut_down_button.place(x=337.5,y=60,height=40,width=100)

st.mainloop()
