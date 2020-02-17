import time
import tkinter as tk

# Time
minutes = 30
seconds = 0
enableTimer = True

def DisplayCountdown():
    global minutes
    global seconds
    global enableTimer
    
    if enableTimer == False:
        enableTimer = True
        return
    
    start_button['state'] = 'disabled'
        
    if minutes == 0 and seconds == 0:
        countdown_display.configure(text='Stand up!')
        return
    elif seconds == 0:
        seconds=60
        minutes-=1
        countdown_display.after(1000, DisplayCountdown)
    else:        
        seconds-=1
        if seconds < 10:
            str_seconds = '0' + str(seconds)
            str_minutes = str(minutes)
            countdown_display.configure(text= str_minutes + ':' + str_seconds)
            countdown_display.after(1000, DisplayCountdown)
        else:
            countdown_display.configure(text='%s:%s' % (minutes,seconds))
            countdown_display.after(1000, DisplayCountdown)

def ResetTimer():
    start_button['state'] = 'normal'
    global minutes
    global seconds
    global enableTimer
    enableTimer = False
    minutes = 30
    seconds = 0
    str_seconds = '0' + str(seconds)
    countdown_display.configure(text='%s:' % (minutes) + str_seconds)
                   
# Window
window = tk.Tk()
window.title('Stand Up Timer')
window.configure(bg = 'black')

# Information label
start_label = tk.Label(window,font = 'ariel 20',bg = 'black',fg = 'green',text = 'Click the start button to begin the timer.')
start_label.grid(row = 0, column = 0)

# Display Count Down
countdown_display = tk.Label(window,font = 'ariel 40',bg = 'black',fg = 'green',text = 'Countdown displayed here!')
countdown_display.grid(row = 1, column = 0)

# Start button
start_button = tk.Button(window,text='Start',command=DisplayCountdown)
start_button.grid(row = 2, column = 0)

# Restart button
reset_button = tk.Button(window,text='Reset',command=ResetTimer)
reset_button.grid(row = 3, column = 0)

# Window main loop
window.mainloop()

