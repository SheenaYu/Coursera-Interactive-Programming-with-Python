# "Stopwatch: The Game"
# Author: Sheena Yu
# http://www.codeskulptor.org/#user43_DK29ngapdL_3.py

# global status
WIDTH = 300
HEIGHT = 200
t = 0
# Counter variables that count the successful stops and total attemps
success = 0
attempt = 0
# boolean global variable that is only set to True when "start" button is pressed
running = False


# Import modules
import simplegui

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    # the final format is 𝙰:𝙱𝙲.𝙳
    mins = t // 600
    secs = (t - mins * 600) // 10
    if secs < 10:
            secs = "0" + str(secs)
    else:
        secs = str(secs)
    tenth_secs = str(t % 10)
    return str(mins) + ":" + secs + "." + tenth_secs 

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True

def stop():
    global running, success, attempt
    # avoid changing these successes and attempts when the timer is already stopped
    if running:
        timer.stop()
        running = False
        attempt += 1
        if t % 10 == 0:
            success += 1
    
def reset():
    global t, running, success, attempt
    timer.stop()
    t = success = attempt = 0
    running = False

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1
    return t
        
# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [WIDTH/2 - 30, HEIGHT/2], 24, 
                     "white", "sans-serif")
    canvas.draw_text(str(success) + "/" + str(attempt), 
                     [WIDTH - 50, 30], 20, "green", "sans-serif")
    
# create frame
frame = simplegui.create_frame("Stopwatch", WIDTH, HEIGHT)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 150)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset, 150)

# start frame
frame.start()

# Please remember to review the grading rubric
