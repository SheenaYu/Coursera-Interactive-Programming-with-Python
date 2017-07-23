## Class Code:

[Keyboard Input](http://www.codeskulptor.org/#examples-keyboard_echo.py)

[Position Control](http://www.codeskulptor.org/#examples-position_control.py)

[Motion Explicit](http://www.codeskulptor.org/#examples-motion_explicit.py)

[Implicit Timer](http://www.codeskulptor.org/#examples-motion_implicit.py)

[Collisions and Reflections](http://www.codeskulptor.org/#examples-collisions_and_reflections.py)

[Position Control](http://www.codeskulptor.org/#examples-position_control.py)

[Velocity Control](http://www.codeskulptor.org/#examples-velocity_control.py)

[Lists Mutation](http://www.codeskulptor.org/viz/#examples_lists_mutation.py)

[Examples Tip 4](http://www.codeskulptor.org/#examples-tips4.py)

* * *

## Practice Exercise

###### 1. Create a list that contains first 6 prime numbers in ascending order. (This list should be created manually.) Print out the 2nd, 4th, and 6th numbers in this list.

[Prime List](http://www.codeskulptor.org/#exercises_lists_primes_solution.py)


###### 2. Given the list 𝚊 in the template, make a new reference 𝚋 to 𝚊. Update the first entry in 𝚋 to be zero. What happened to the first entry in 𝚊? Explain your answer (in a comment).

[List Reference](http://www.codeskulptor.org/#exercises_lists_reference_solution.py)

###### 3. Given the list 𝚊 in the template, make a new copy 𝚋 of the list 𝚊 using the function 𝚕𝚒𝚜𝚝. Update the first entry in 𝚋 to be zero. What happened to the first entry in 𝚊? Explain your answer (in a comment).

[List Copy](http://www.codeskulptor.org/#exercises_lists_copy_solution.py)

###### 4. Write a function 𝚊𝚍𝚍_𝚟𝚎𝚌𝚝𝚘𝚛(𝚟, 𝚠) that takes two 2D vectors 𝚟 and 𝚠 (represented as lists) and returns a new 2D vector (represented as a list) that is the sum of the two vectors. Remember that vector addition is performed independently on each corresponding element of the lists. Hint: returning 𝚟 + 𝚠 does not work. 

[Lists Add](http://www.codeskulptor.org/#exercises_lists_add_solution.py)

###### 5. Challenge: The program template below is a program designed to run two independent timers with their own start and stop buttons. In particular, each timer should be controlled by its own buttons independent of the other timer's buttons. The current version has an error that causes both timers to work in unison. Find and fix this error. 

[Lists Debug](http://www.codeskulptor.org/#exercises_lists_debug_solution.py)

###### 6. The program template contains a program designed to echo the message "𝙿𝚛𝚎𝚜𝚜𝚎𝚍 𝚞𝚙 𝚊𝚛𝚛𝚘𝚠" or "𝙿𝚛𝚎𝚜𝚜𝚎𝚍 𝚍𝚘𝚠𝚗 𝚊𝚛𝚛𝚘𝚠" whenever the appropriate key is pressed. Debug the program template and fix the program.

[Keyboard Debugging](http://www.codeskulptor.org/#exercises_keyboard_debug_solution.py)

###### 7. Complete the program template below so that each press of the up arrow increases the radius of the white ball centered in the middle of the canvas by a small fixed amount and each press of the down arrow key decreases the radius of the ball by the same amount. Your added code should be placed in the keydown handler. (Note that 𝚍𝚛𝚊𝚠_𝚌𝚒𝚛𝚌𝚕𝚎 will throw an error if the radius of the circle is decreased to zero or less.) 

[Keyboard Ball1](http://www.codeskulptor.org/#exercises_keyboard_ball1_solution.py)

###### 8. Complete the program template so that the program displays "𝚂𝚙𝚊𝚌𝚎 𝚋𝚊𝚛 𝚍𝚘𝚠𝚗" on the canvas while the space bar is held down and "𝚂𝚙𝚊𝚌𝚎 𝚋𝚊𝚛 𝚞𝚙" while the space bar is up. You will need to add code to both the keydown and keyup handlers. 

[Space Bar](http://www.codeskulptor.org/#exercises_keyboard_spacebar_solution.py)

###### 9. Challenge: Complete the program template below so that holding down the up arrow key increases the radius of the white ball centered in the middle of the canvas by a small fixed amount each frame. Releasing the up arrow key causes that growth to cease. You will need to add code to the keydown and keyup handlers as well as the draw handler. 

[Keyboard Ball2](http://www.codeskulptor.org/#exercises_keyboard_ball2_solution.py)



* * *


## Quiz 4a

##### Q1: 

One of the tasks that you will engage in when learning a new programming language is locating the name of a built-in function that performs a common, simple operation. While you might be tempted to write your own code that performs this operation, locating a built-in function is usually preferable since the built-in version is automatically correct and others that read your code will immediately recognize what your code is doing.

Python has a built-in function that adds up the numbers in a list. For example, given the list [𝟷, 𝟸, 𝟻, 𝟺], this function returns 𝟷 + 𝟸 + 𝟻 + 𝟺 = 𝟷𝟸. Use your search skills to find the name of this built-in function. Enter the name of the built-in function below, without any parentheses or arguments.

(Note that we could just tell you the name of this function. However, the point of this problem is for you to start learning how to locate useful language features on your own.)

`Answer: sum`

##### Q2: 

Let 𝚖𝚢_𝚕𝚒𝚜𝚝 be the list ["𝚃𝚑𝚒𝚜", "𝚌𝚘𝚞𝚛𝚜𝚎", "𝚒𝚜", "𝚐𝚛𝚎𝚊𝚝"].

What is 𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)?
What non-negative number is the index of "𝚐𝚛𝚎𝚊𝚝"? I.e., how would you replace the question marks in 𝚖𝚢_𝚕𝚒𝚜𝚝[???] so that the resulting value is "𝚐𝚛𝚎𝚊𝚝"?
Submit two numbers, one for each of these two questions, separated by spaces.

`Answer: 4 3`

##### Q3: 

Let 𝚖𝚢_𝚕𝚒𝚜𝚝 be the list ["𝚃𝚑𝚒𝚜", "𝚌𝚘𝚞𝚛𝚜𝚎", "𝚒𝚜", "𝚐𝚛𝚎𝚊𝚝"].

We can use Python's slice notation to get part of this list. What non-negative numbers can be used to get the slice ["𝚌𝚘𝚞𝚛𝚜𝚎", "𝚒𝚜"]? I.e., what two non-negative numbers should we put in 𝚖𝚢_𝚕𝚒𝚜𝚝[??? : ???] to get that result?

Submit the two numbers in order, separated only by spaces.

`Answer: 1 3`

##### Q4: 

If we want to split a list 𝚖𝚢_𝚕𝚒𝚜𝚝 into two halves, which of the following uses slices to do so correctly?

More precisely, if the length of 𝚖𝚢_𝚕𝚒𝚜𝚝 is 2n, i.e., even, then the two parts should each have length n. If its length is 2n+1, i.e., odd, then the two parts should have lengths n and n+1.

`Answer: `

𝚖𝚢_𝚕𝚒𝚜𝚝[: 𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝) // 𝟸] and 𝚖𝚢_𝚕𝚒𝚜𝚝[𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝) // 𝟸 :]
Correct 

𝚖𝚢_𝚕𝚒𝚜𝚝[: 𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝) // 𝟸 - 𝟷] and 𝚖𝚢_𝚕𝚒𝚜𝚝[𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝) // 𝟸 :]
Un-selected is correct 

𝚖𝚢_𝚕𝚒𝚜𝚝[𝟶 : 𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝) // 𝟸] and 𝚖𝚢_𝚕𝚒𝚜𝚝[𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝) // 𝟸 : 𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)]
Correct 

𝚖𝚢_𝚕𝚒𝚜𝚝[𝟶 : 𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝) // 𝟸] and 𝚖𝚢_𝚕𝚒𝚜𝚝[𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝) // 𝟸 + 𝟷 : 𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)]
Un-selected is correct 

##### Q5: 

What is the distance between point [𝟺, 𝟽] and the nearest point on the circle centered at [𝟸, 𝟿] with radius 2? Provide at least 4 digits of accuracy.

Hint: The distance between a point and a circle is the distance between the point and the center of the circle minus the radius of the circle. You can use the point-to-point distance code described in this week's videos.

`Answer: 0.8284`

```python
import math
distance = math.sqrt(4+4) - 2
print distance
```

##### Q6: 

A ball with velocity [𝟺, 𝟸] reflects off a vertical wall. What is its new velocity?

`Answer: `

[-𝟺, -𝟸]

[𝟺, -𝟸]

[-𝟺, 𝟸]
Correct 

[𝟺, 𝟸]

##### Q7: 

Which of the following illustrate how to properly structure a keydown or keyup event handler? (For more advanced Python programmers, assume that you have just imported simplegui and haven't used 𝚏𝚛𝚘𝚖.)


```python
def keydown_handler(key):
    if key == "left":
        …
```
Un-selected is correct 


```python
def keydown_handler(key):
    if key == simplegui.KEY_MAP["left"]:
        …
```
Correct 


```python
def keydown_handler(key):
    if "left" == simplegui.KEY_MAP[key]:
        …
```
Un-selected is correct 


```python
def keydown_handler(key):
    if key == KEY_MAP["left"]:
        …
```
Un-selected is correct 

##### Q8: 

Assume you have a program with a keydown handler. You run it, and press a single key and hold it down continuously. How many times does the keydown handler get called?

Experiment in CodeSkulptor to find out.

`Answer: `

1
Correct 

Unlimited — i.e., repeatedly until you finally release the key

2 — once at the beginning and once when you release the key

##### Q9: 

Several keys on the keyboard, such as Shift, CapsLock, and Ctrl, typically act to modify what happens when you press other keys, rather than doing anything on their own. When using the SimpleGUI keydown handler, how are such keys treated?

Experiment in CodeSkulptor to find out.

`Answer: `

Independent key press events — e.g., pressing Shift by itself creates an event
Correct 
Yes, for example Shift gives the value 16.

No effect — e.g., pressing the Shift key does not create or modify the behavior of any event.

Modify other key presses — e.g., pressing the 'a' key creates an event with a different value than pressing Shift and 'a' together.

* * * 

## Quiz 4b

##### Q1: 

In Python, [𝟷, 𝟸, 𝟹] is of type list. What is the name of the type of (𝟷, 𝟸, 𝟹)?

`Answer: `
Triple

Set

Pair

Array

Tuple
Correct 

##### Q2: 

Which of the following types of data are immutable in Python?

`Answer: `

Lists
Un-selected is correct 

Booleans
Correct 

Tuples
Correct 

Numbers
This should be selected 

Strings
Correct 

##### Q3: 

Which of the following functions must include a 𝚐𝚕𝚘𝚋𝚊𝚕 𝚙𝚘𝚒𝚗𝚝 declaration in order to change the global variable 𝚙𝚘𝚒𝚗𝚝?

```python
point = [0, 0]
def function1():
    point[0] += 1
    point[1] += 2
def function2():
    point = [50, 50]
```

`Answer: `

𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗𝟷
Un-selected is correct 

𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗𝟸
Correct 

##### Q4: 

Consider the following program.


```python
a = [49, 27, 101, -10]
b = a
c = list(a)
d = c
a[3] = 68
c[2] = a[1]
b = a[1 : 3]
b[1] = c[2]
```

What are the elements of the list in variable 𝚋? Just enter the numbers, separated by spaces.

First try to figure it out in your head, but go ahead and run it in CodeSkulptor before you submit your answers.

`Answer: `

27 27
Correct Response 

##### Q5: 

In our program, the variable 𝚙𝚘𝚜𝚒𝚝𝚒𝚘𝚗 represents a 2D position on the canvas. We want to be able to change the position by some amount in variable 𝚍𝚎𝚕𝚝𝚊. Why is the following code snippet incorrect?


```python
position = [50, 50]
delta = [1, -2]
…
position = position + delta
```

Note that the ellipses represent that we might have code in between what is shown, but such code is irrelevant and omitted.

`Answer: `

Lists do not support the + operator.

One of the elements of 𝚍𝚎𝚕𝚝𝚊 is negative.

The numbers in 𝚙𝚘𝚜𝚒𝚝𝚒𝚘𝚗 cannot be changed.

The + operator on lists does not mean addition of the numbers in a list.
Correct 

##### Q6: 

Consider the following program.


```python
a = ["green", "blue", "white", "black"]
b = a
c = list(a)
d = c
a[3] = "red"
c[2] = a[1]
b = a[1 : 3]
b[1] = c[2]
```

At the end of this code, to how many list objects do the variables refer?

If you run the code and print the variables' values, you can begin to answer this question. After all, if two variables print differently, they certainly can't refer to the same object. However, if two variables print the same, you still need to determine whether they refer to the same object. One way is to step through the code while drawing reference diagrams. Another is to mutate one and see if others also mutate.


`Answer: `

[codeInCodeSkulptor](http://www.codeskulptor.org/#user43_OXvpSCLBn9_1.py)

3

4 — The four variables each refer to different lists.
This should not be selected 

1 — The four variables each refer to the same list.

2


##### Q7: 

Convert the following specification into code. Do the point and rectangle ever overlap?

A point starts at [𝟷𝟶, 𝟸𝟶]. It repeatedly changes position by [𝟹, 𝟶.𝟽] — e.g., under button or timer control. Meanwhile, a rectangle stays in place. Its corners are at [𝟻𝟶, 𝟻𝟶] (upper left), [𝟷𝟾𝟶, 𝟻𝟶] (upper right), [𝟷𝟾𝟶, 𝟷𝟺𝟶] (lower right), and [𝟻𝟶, 𝟷𝟺𝟶] (lower left).

To check for overlap, i.e., collision, just run your code and check visually. You do not need to implement a point-rectangle collision test. However, we encourage you to think about how you would implement such a test.

`Answer: `
Yes
Correct 

No

##### Q8: 

Assume we are using acceleration control for a spaceship in a game. That is, we regularly have the following updates:

The position is incremented by the time interval multiplied by the velocity. This happens on each draw event.
The velocity is incremented by the time interval multiplied by the acceleration. This happens on each draw event.
The acceleration is periodically incremented by some fixed vector (the same vector for each step). This could happen on keyboard or timer events.
Assume that, initially, the ship is stationary and subject to no acceleration. What sort of trajectory will the spaceship fly in?

Either figure this out mathematically, or implement it in CodeSkulptor and see what happens.

`Answer: `

Unpredictable

A non-linear, smooth curve

A straight line
Correct 
Since the change to acceleration is a fixed vector, both the acceleration and velocity will always be a multiple of this fixed vector. Therefore, the trajectory of the ship will follow a straight line in the direction of the fixed vector.

Spiral

##### Q9: 

Write a Python program that initializes a global variable to 5. The keydown event handler updates this global variable by doubling it, while the keyup event handler updates it by decrementing it by 3.

What is the value of the global variable after 12 separate key presses, i.e., pressing and releasing one key at a time, and repeating this 12 times in total?

To test your code, the global variable's value should be 35 after 4 key presses.

`Answer: `

```python
import simplegui
x = 5

def keydown(key):
    global x
    if key == simplegui.KEY_MAP["space"]:
        x = 2*x
        
def keyup(key):
    global x
    if key == simplegui.KEY_MAP["space"]:
        x -= 3
        
def draw(canvas):
    canvas.draw_text(str(x), (50, 50), 12, "Red")
                     
                     
frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw)

frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)

frame.start()
```

[codeInCodeSkulptor](http://www.codeskulptor.org/#user43_OXvpSCLBn9_0.py)

8195
Correct Response 