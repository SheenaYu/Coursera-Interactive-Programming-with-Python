## Class Code:

[String Processing](http://www.codeskulptor.org/#examples-strings.py)

[Money example2](http://www.codeskulptor.org/#examples-money-1.py)

[Interactive Drawing](http://www.codeskulptor.org/#examples-interactive_drawing.py)

[Move a ball](http://www.codeskulptor.org/#exercises_drawing_ball_solution.py)

[Timers](http://www.codeskulptor.org/#examples-timers.py)

[Visualizing Drawing and Timers](http://www.codeskulptor.org/viz/#examples-timers.py)

[Programming Tips - 3 (1)](http://www.codeskulptor.org/#examples-tips3-events.py)

[Programming Tips - 3 (2)](http://www.codeskulptor.org/#examples-tips3.py)

## Practice Exercise

###### 1. Given the solution from the following problem, we again want a counter printed to the console. Add three buttons that start, stop and reset the counter, respectively.

[Counter buttons](http://www.codeskulptor.org/#exercises_timers_buttons_solution.py)


###### 2. Use a timer to toggle the canvas background back and forth between red and blue every 3 seconds. Use the CodeSkulptor Docs to locate the appropriate call to change the background color of the canvas.

[Toggle background](http://www.codeskulptor.org/#exercises_timers_toggle_solution.py)

###### 3. Create a circle in the center of the canvas. Use a timer to increase its radius one pixel every tenth of a second. 

[Expanding circle](http://www.codeskulptor.org/#exercises_timers_circle_solution.py)

###### 4. Challenge: Use a timer to measure how fast you can press a button twice. Create a button that starts a timer that ticks every hundredth of a second. The first button press starts the measurement. The second button press ends the measurement. Print to the console the time elapsed between button presses. The next two button presses should repeat this process, making a new measurement. Hint: We suggest that you keep track of whether the program is on the first or second button press using a global Boolean variable. 

[Reflex Test](http://www.codeskulptor.org/#exercises_timers_reflex_solution.py)




* * *


## Quiz 3a

##### Q1:


What Python operator takes two strings (e.g., "𝚜𝚞𝚗" and "𝚛𝚒𝚜𝚎") and forms the combination of these two strings, one followed by the other (e.g., "𝚜𝚞𝚗𝚛𝚒𝚜𝚎")?

Ans: +

##### Q2:

What does the draw handler parameter represent?

Ans: The canvas

##### Q3:

What happens if you draw text outside the canvas coordinates?
   
Ans: Some or none of the text is shown. Conceptually, the text is drawn at whatever coordinates are given, but only whatever text fits within the canvas coordinates is shown.

##### Q4:

Assume we have a canvas that is 200 pixels wide and 300 pixels high. We want to draw a green line between the upper left corner of the canvas and the lower right corner of the canvas. Which of the following calls will accomplish this?

Ans: `canvas.draw_line((0, 0), (200, 300), 10, "Green”)`


##### Q5:

Consider the following function definition.

```python
def date(month, day):
    """Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day."""
    return month + "/" + day

print date(2, 12)
```

This definition leads to an error. To fix it, what Python expression should replace the question marks below?

```python
def date(month, day):
    """Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day."""
    return ???

print date(2, 12)
```

Ans: `𝚜𝚝𝚛(𝚖𝚘𝚗𝚝𝚑) + "/" + 𝚜𝚝𝚛(𝚍𝚊𝚢)`

##### Q6:

Assume we have a variable 𝚠𝚘𝚛𝚍 that contains a string, such as "𝙼𝚒𝚜𝚜𝚒𝚜𝚜𝚒𝚙𝚙𝚒" or "𝚒𝚗𝚍𝚒𝚟𝚒𝚜𝚒𝚋𝚕𝚎". We would like to determine how many "𝚒"'s are in the string 𝚠𝚘𝚛𝚍. What code should replace the question marks in the following function definition?

```python
def number_of_i(word):
    """Returns the number of lower-case i's in the word."""
    return ???
```

There is a built-in function or method that will do this. Look in the CodeSkulptor documentation for the appropriate one.

Ans: 𝚠𝚘𝚛𝚍.𝚌𝚘𝚞𝚗𝚝("𝚒")


##### Q7:

Where should your 𝚍𝚛𝚊𝚠_𝚝𝚎𝚡𝚝, 𝚍𝚛𝚊𝚠_𝚕𝚒𝚗𝚎, and similar drawing calls be?

Ans: In a draw handler, or a helper function called from it


##### Q8:

Which of the following function calls are valid, i.e., don't lead to an error?

Ans:

* `int(“5”)`

* `float(“5.4”)`

##### Q9:

Turn the following description into a CodeSkulptor program, and run it.

1.Create a 300-by-300 canvas.
2.Draw two circles with radius 20 and white lines of width 10. One is centered at (90,200) and one at (210,200).
3.Draw a red line of width 40 from (50,180) to (250,180).
4.Draw two red lines of width 5 from (55,170) to (90,120) and from (90,120) to (130,120).
5.Draw a red line of width 140 from (180,108) to (180,160).

The resulting picture is a simple diagram of what?

Ans: An automobile

##### Q10:

The following is a diagram of an archery target.

![archery target](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/C74TXbr4EeW43wpBjgOOlw_44888b7c09e4e4368feba741f0245e02_target.png?expiry=1498780800000&hmac=U6AnmHb6CZZoryk3hADJj6MjVcKtscDnie29InMmjEI)

To draw this in CodeSkulptor, we can put a small yellow circle with a black border on top of a slightly bigger yellow circle with a black border, … on top of a big white circle with a black border. In what order should your code draw these circles?

Ans: Largest first



* * * 

## Quiz 3b

##### Q1:

When the following code is executed, how many times is 𝚝𝚒𝚖𝚎𝚛_𝚑𝚊𝚗𝚍𝚕𝚎𝚛 called?

```python
import simplegui

def timer_handler():
    …

timer = simplegui.create_timer(10, timer_handler)
timer.start()
```

The body of 𝚝𝚒𝚖𝚎𝚛_𝚑𝚊𝚗𝚍𝚕𝚎𝚛 isn't given, as it is irrelevant for this question. You may want to finish the code and run it before submitting your answer.

Ans: Unlimited — It is called repeatedly until you stop the program.

##### Q2:

You want a timer to create exactly 1000 events. Which of the following solutions are possible?

Ans: Have a global counter for the number of timer calls. In the timer handler, increment the counter. In the timer handler, check the count and possibly stop the timer.

##### Q3:

How do you change the frequency of a running timer, either increasing or decreasing the frequency? E.g., in the code below, we want code at the question marks that changes the timer.

```python
…
timer = simplegui.create_timer(1000, timer_handler)
timer.start()
…
???
```


Ans: You can't. But, you can stop this timer, and start a new one with a different frequency and same handler.

```python
timer.stop()
timer = simplegui.create_timer(300, timer_handler)
timer.start()
```


##### Q4:

How many timers can you have running at once?

Ans: Unlimited

##### Q5:

The function 𝚝𝚒𝚖𝚎.𝚝𝚒𝚖𝚎() is used in Python to keep track of time. What unit of time is associated with the value returned by 𝚝𝚒𝚖𝚎.𝚝𝚒𝚖𝚎()? Hint: Look in the [documentation](http://www.codeskulptor.org/docs.html).

Ans: Second

##### Q6:

In Python, the 𝚝𝚒𝚖𝚎 module can be used to determine the current time. This module includes the method 𝚝𝚒𝚖𝚎 which returns the current system time in seconds since a date referred as the Epoch. The Epoch is fixed common date shared by all Python installations. Using the date of the Epoch and the current system time, an application such as a clock or calendar can compute the current time/date using basic arithmetic.

Write a CodeSkulptor program that experiments with the method 𝚝𝚒𝚖𝚎.𝚝𝚒𝚖𝚎() and determines what date and time corresponds to the Epoch. Enter the year of the Epoch as a four digit number. (Remember to 𝚒𝚖𝚙𝚘𝚛𝚝 𝚝𝚒𝚖𝚎.)

Ans: 1970

##### Q7:

The Python code below uses a timer to execute the function 𝚞𝚙𝚍𝚊𝚝𝚎() 10 times, computing a good approximation to a common mathematical function. Examine the code, and run it while varying the input value 𝚗.

What is the common name for what this computes?

```python
# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state

result = 1
iteration = 0
max_iterations = 10

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n

def get_next(current):
    """??? Part of mystery computation."""
    return 0.5 * (current + n / current)

# timer callback

def update():
    """??? Part of mystery computation."""
    global iteration, result
    iteration += 1
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", result
    else:
        result = get_next(result)

# register event handlers

timer = simplegui.create_timer(1, update)

# start program

init(13)
timer.start()

```

Ans: Square root of n

Explanation: Such a computation is more typically written using loops, which we haven't introduced yet in this course. However, this example illustrates timers and handler/callback functions and one possible use for them.


##### Q8:

Given any initial natural number, consider the sequence of numbers generated by repeatedly following the rule:

divide by two if the number is even or
multiply by 3 and add 1 if the number is odd.
The Collatz conjecture states that this sequence always terminates at 1. For example, the sequence generated by 23 is:

23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1

Write a Python program that takes a global variable 𝚗 and uses a timer callback to repeatedly apply the rule above to 𝚗. Use the code from the previous question as a template. I suggest that your code prints out the sequence of numbers generated by this rule. Run this program for 𝚗 = 217. What is the largest number in the sequence generated by this starting value?

To test your code, starting at 𝚗 = 23 generates a sequence with a maximum value of 160.

Ans: 736

```python
import simplegui

n = 23

# timer callback

def update():
    global n
    if n == 1:
        timer.stop()
    elif n % 2 == 0:
        n = n/2
        print n
    else:
        n = n*3 + 1
        print n

# register event handlers

timer = simplegui.create_timer(100, update)

# start program

timer.start()
```

##### Q9:

CodeSkulptor runs your Python code by converting it into Javascript when you click the "Run" button and then executing this Javascript in your web browser. Open this [example](http://www.codeskulptor.org/#examples-explosion_animation.py) and run the provided code. If the SimpleGUI frame is spawned as a separate window, you should see an animation of an explosion in the canvas for this frame. If the SimpleGUI frame is spawned as a separate tab on top of the existing window containing the code (as happens in some browser configurations), the animation will "freeze" and a single static image is displayed. (If the SimpleGUI frame spawns as a separate window, you can also cause the animation to freeze by opening a new tab on top of the code window.)

As explained in the FAQ (check the Resources tab on the left), what is the explanation for this behavior?

Ans: To save resources, modern browsers only execute the Javascript associated with the topmost tab of a window. The animation freezes since the code tab and its associated Javascript is no longer the topmost tab.







