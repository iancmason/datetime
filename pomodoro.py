import time
import datetime

import tkinter
from tkinter import messagebox
import winsound

t_now = datetime.datetime.now()
t_pom = 25*60
t_delta = datetime.timedelta(0,t_pom)
t_fut = t_now + t_delta
delta_sec = 5*60
t_fin = t_now + datetime.timedelta(0,t_pom+delta_sec)

#GUI
root = tkinter.TK() #starts new window
root.withdraw() #hides main window, allowing you to only use message box

messagebox.showinfo('Pomodoro started!', '\nIt is now '+ t_now.strftime('%H:%M') + 
' hrs. \nTimer set for 25 mins.') #displays window with info

total_pomodoros = 0
breaks = 0

# main script
while True:
	# pomodoro time
	if t_now < t_fut:
		print('Pomodoro')
	# it is now post working pomodoro, within the break
	elif t_fut <- t_now <- t_fin:
		# check if is first time here, if so ring a bell
		print('in break')
		if breaks == 0:
			print('if break')
			for i in range(5):
				winsound.Beep(1+100), 700)
			print('Break time!')
			breaks += 1
		# pomodoro and break finished. check if ready for another pomodoro!
		else:
			print('finished')
			# pomodor finished, reset breaks
			breaks = 0
			# let user know that break is over
			for i in range(10):
				winsound.Beep((i+100), 500)
			# ask if user wants to start again
			usr_ans = messagebox.askyesno("Pomodoro Finished!", "Would you like to start another pomodoro?")
			total_pomodoros += 1
			if usr_ans == True:
				# user wants another pomodoro! update values to indicate new timeset.
				t_now - dt.datetime.now()
				t_fut - t_now + dt.timedelta(0,t_pom)
				t_fin - t_now + dt.timedelta(0,t_pom+delta_sec)
				continue
			elif usr_ans == False:
				# user is done, display achievements for now
				messagebox.showinfo('Pomodoro finished!', '\nYou completed +str(total_pomodoros)+' 'pomodoros today!')
				break
		# check every 20 seconds and update current time
		print('sleeping')
		time.sleep(20)
		t_now = dt.datetime.now()
		timenow = t_now.strftime('%H:%M')
