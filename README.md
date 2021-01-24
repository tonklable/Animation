# Mr.Dinosaur Interactive Animation

## Natprawee Pattayawij

## 1 Introduction

This interactive animation is inspired by Google Chrome’s ”Dinosaur Game.”
This game lets the player be a dinosaur dodging obstacles including cacti and
pterodactyls by hitting the space bar and down button. On the contrary, this
interactive animation lets the user decide whether a cactus or a pterodactyl
will be released, and Mr.Dinosaur, a smart dinosaur, will dodge the obstacles
smartly until the user decides to let he take a rest.

## 2 Template

## 2.1 Description

First of all, before the idea of Mr.Dinosaur came out, a template of animation
had been coded so that the animation can be set more easily. In this template,
rectangular objects can be added to 27*10 frame by a list containing coordinates
of their bottom-left and top-right edges. To illustrate, consider the following
list,

```
objects=[[[2,3],[6,8]],[[7,6],[26,10]]].
```
<img src="https://github.com/tonklable/Dinosaur-Animation/blob/main/Picture/example.png" width="300"  />

```
Figure 1: Example output of the objects from template
```
The list ”objects” add two rectangular objects as in Figure 1. The first rectangle has bottom-left and top-right coordinates at (2,3) and (6,8) respectively
according to Cartesian coordinate with (0,0) at the bottom left of the frame as
well as the second rectangle that has bottom-left and top-right coordinates at
(7,6) and (26,10) respectively. These four coordinates are listed in the ”objects”
list, and coordinates of the same rectangle are assigned in the same sub-list (the
list inside). More rectangles can be added by adding more sub-list with the
coordinates of the bottom-left and top-right edges of the rectangle.

### 2.2 How it works

Since each rectangle has two coordinates (for bottom-left and top-right edges)
so-called ”object variable”, value x and y of the coordinates are changed to list’s
coordinates (yturns to list’s index called y′and x turns to a digit of the number
in each index called x′). Then, x′ is used to calculate in the following function
by for-loop.


f(x′) = 1 + 10<sup>2</sup> + 10<sup>3</sup> +...+ 10<sup>x</sup>

Then,f(x) of the first coordinate minuses that of the second coordinate, and the
result is taken to plus number in each index of the ”chosen” list (the proposed
list) between y′ of the first and second coordinates by using for-loop. Finally,
for-loop is again used to run this mechanism for each rectangle’s coordinates
given, and the ”result” list is assigned.

### 2.3 Suggestions

According to the functionf(x′), it would be easier if the ** operator (the power
operator) in Python can be used, for the assignment allows only 4 arithmetic
operations. Therefore, the for-loop of multiplication is used instead. Moreover,
Python’s classes can be used to facilitate this mechanism.

## 3 Process

All objects are animated on 31 frames or so-called 1 set (using for-loop) in each
input. There are unlimited sets until the input is to stop. Speed to change
frames is fixed by time.sleep(0.05). Here is the process of each frame in set:

1. Receive an int input from the user to decide whether to release cactus,
    pterodactyl or to stop; put 1 for cactus; put 2 for pterodactyl; put 3 to
    stop the animation. (User put it before the set starts.)
2. Receive the ”chosen” list containing the picture of Mr.Dinosaur to be used
    in this frame from the frame before; for the first frame, use the proposed
    ”chosen” list (the list containing Mr.Dinosaur running on the ground).
3. Assign an obstacle object variable in the template (by using if-else branching). (See Section 4.1 for cactus, and see Section 4.2 for pterodactyl.)
4. Print each line of the ”result” list from the template (by using for-loop).
    (See Section 2)
5. Assign the ”chosen” list containing the picture of running, jumping or
    stooping Mr.Dinosaur, and send it to the next frame. (See Section 4.3)

## 4 Objects

### 4.1 Cactus
<img src="https://github.com/tonklable/Dinosaur-Animation/blob/main/Picture/cactus.png" width="300"  />

```
Figure 2: Output of Mr.Dinosaur jumping over a cactus
```
Cacti(as shown in Figure 2 illustrated by a set of number 1) are obstacles that
Mr.Dinosaur jumps over. In a set in which the input from the user is 1, a cactus
appears on the right and moves to the left in each frame, and then it disappears
on the left.
Cactus’s shape is set by the coordinates in the template. Cactus’s position
is indicated by the number of the frame set in the template. As the number
of frame increase, the x values of each coordinate of the cactus’s template is
assigned lower than the frame before by 1 so that it moves to left. Additionally,
if-else branching is used to make a condition that if the number of the frame
exceeds 25, the coordinates are empty so that the cactus disappear. In each
frame, the result list is added to the ”chosen” list of that frame.

### 4.2 Pterodactyl

<img src="https://github.com/tonklable/Dinosaur-Animation/blob/main/Picture/bird.png" width="300"  />

```
Figure 3: Output of Mr.Dinosaur stooping under a pterodactyl
```
In the same way as cacti, pterodactyls (as shown in Figure 3 illustrated by a set
of number 1) are obstacles that Mr.Dinosaur stoop under. If the input is 2, a
pterodactyl appears from the right side and fly to the left. Then, it disappears
on the left.
Similar to cactus, pterodactyl’s shape and position are set by the coordinates
in the template and the number of the frame respectively. The x values of
coordinates are assigned to decline by 1 when the number of frame increase by
1 so that the pterodactyl moves to the left. When the number of the frame
is between 24 and 30, the x coordinate is set to 1 so that the pterodactyl
slightly disappear. And when it exceeds 30, the coordinates are empty, as it
fully disappears. In each frame, the result list is added to the ”chosen” list of
that frame


### 4.3 Mr.Dinosaur

Mr.Dinosaur can jump and stoop. What he is going to do depends on the
obstacle he meets. He jumps when a cactus is released, as he stoops when a
pterodactyl is released.
Mr.Dinosaur is illustrated by a set of number 5. The appearance of Mr.Dinosaur in each frame is assigned to the ”chosen” list indicating by the number of
the frame and input. If the input is 1, Mr.Dinosaur needs to jump over the
cactus. The cactus reaches Mr.Dinosaur in frame 15 and leaves in frame 22, so
the chosen list is set to shift up after frame 14 and shift down after frame 22.
Shifting up is coded by using for-loop in each index of the list; the value from
the next index is assigned to the index before, and shifting down is an inverse
of shifting up. Therefore, the chosen list is assigned for each frame.
Moreover, if the input is 2, Mr.Dinosaur needs to stoop under the pterodactyl. The pterodactyl reaches Mr.Dinosaur between frames 14 and 25, so the
chosen list is changed to the stooping list in this interval. Hence, the chosen list
is set to be used in the next frame.

## 5 Overview

The animation starts with Mr.Dinosaur running on the ground. When the user
chooses 1, a cactus is released as shown in Figure 2. After Mr.Dinosaur jumps
over the cactus, the input is asked again as shown in Figure 5. When the user
chooses 2. a pterodactyl is released as shown in Figure 3, and Mr.Dinosaur could
stoop it easily. Then, more input is asked again; if the user chooses 0, the animation is stopped. Mr.Dinosaur then takes a rest as shown in Figure 6. Therefore,
this is an interactive animation that the user can control the animation easily
by filling input.


<img src="https://github.com/tonklable/Dinosaur-Animation/blob/main/Picture/Start.png" width="500"  />

```
Figure 4: Output of the starting point
```


<img src="https://github.com/tonklable/Dinosaur-Animation/blob/main/Picture/continue.png" width="500"  />

```
Figure 5: Output when asking for more input
```



<img src="https://github.com/tonklable/Dinosaur-Animation/blob/main/Picture/rest.png" width="300"  />

```
Figure 6: Output of Mr.Dinosaur taking a rest
```

