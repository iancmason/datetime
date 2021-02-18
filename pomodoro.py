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

