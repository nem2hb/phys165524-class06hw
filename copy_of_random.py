# -*- coding: utf-8 -*-
"""Copy of Random.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TcQdezwo-byA3MvvF16tJBhrzQQUnmZB

# Random Numbers

Random numbers are useful for many things in computing.  

And, guess what, they are easy to use in Python!  We just need to include the random module like this:
"""

import random

"""Let's see what is in the random module.  (Can you find the documentation using Google "python random module"?).  We can use the dir command to list what is included in the module (as we did with the math module last week)..."""

dir(random)

"""You almost certainly won't need all of those.  But, guess what?  You can look at the random module documentation to figure out what they do!  

You would find that you can generate a random integer number like this.
"""

my_random=random.randint(1,1000)  #get a random number between 1 and 1000
print(my_random)

"""If we run it again, we will get a differnt number.  Run the section above a few times and see.

Now, let's do it 5 times in a for loop.
"""

for i in range(0,5):  #loop with i values from 0 to 4
    print(i,") ",random.randint(1,1000))

"""<span style="color:red">**Exercise 1**:</span>  Print 10 random integers between 0 and 10"""

#Put your code here.
import random

for i in range(10):
    print(random.randint(0, 10))

"""As we discussed in class, random numbers are not truly random, they are based on an algorithm.  And the algorithm needs to be 'seeded' to start it.  We can access the Python random number seed with the "seed" function.

Random number generators are just a program.  An algorithm to select numbers randomly written in code.  The algorithms need a starting point.  We call that the seed.
"""

random.seed(0)  #Set the random number seed to 0  (any int will do)

"""Once we have set a random number seed we have defined how the algorithm will start.  Let's print some random numbers..."""

random.seed(0)
for i in range(0,10):
    print(random.randint(1,1000))

"""Note:  Now if we set the seed again to exactly the same integer, we should get the same results.  """

random.seed(0)
for i in range(0,10):
    print(random.randint(1,1000))

"""Once we set the seed to a specific integer, the sequence of number generated is completely determined.  It is just an algorithm, and it is semi-random.  If you set the seed to the same integer, you will get the same sequence of numbers.  So, for example if you run a program with some random nature, it is repeatable if you use the same starting random number seed.    

If we don't set the seed, our results will be "random":
"""

for i in range(0,10):
    print(random.randint(1,1000))

"""Run the code in the above block a few times - you should see different numbers each time.  

<span style="color:red">**Exercise 2**</span>:  Modify the above code to print a random float between -1 and 1.  Hint:  look at documentation for  "random.uniform"
"""

#Put your code here
import random

for i in range(10):
    print(random.uniform(-1, 1))

"""
Note what happens if we set the seed inside the loop:"""

for i in range(0,5):
    random.seed(0)
    print(random.randint(1,1000))

"""

What happened?  We reset the seed to 0 each time, so we got exactly the same number!  This is almost certainly not what you wanted! Once we set the seed, the algorithm is set to produce a series of 'pseudo-random' numbers.  If you set the seed to the same value again, you will get exactly the same series!

"""

random.seed(0)
for i in range(0,5):
    print(random.randint(1,1000))

"""Much better!

<span style="color:red">**Exercise 3**</span>:  Write code that makes 10 pairs of floats, with random values between between -1 and 1.  That is generate and print two numbers each time through the loop.
"""

#Put your code here
import random

for i in range(10):
    print(random.uniform(-1, 1), random.uniform(-1, 1))

"""**Very Important** : Imagine that you wanted to run a simulation, and that it will take a long time to run. so, you decide to run it on three computers at the same time so it will finish 3 times faster. If you wanted to combine these results to obtain higher statistics would you want to start each simulation with the same seed or diferent seeds?

What if you want to redo the simulation with the same outcome? You would want to know which seed you used.

So, it is good practice to set the seed in the code, and to record it (print it to the screen, or print it to the top of your output file).

If you are submitting many jobs, one strategy is to use the job number as the seed.

If you want your program to get a new seed each time you run it, you may do it based on the time. Here I show you an example using time.

Note: Linux time is often given in the number of seconds since 1970 (or something like that?). If you use seconds, and more than one section start on the same second, you might get duplicate results. So, let's use microseconds (10^-6 seconds).


We will use the time and datetime modules.  

"""

from datetime import datetime
import time

print(datetime.now)

ts= (datetime.now() - datetime(1970,1,1)).total_seconds()
print("Seconds since 1970:",int(ts))
print("Micro Seconds since 1970:",int(ts*100000))
ms=int(ts*1000)

ts2= (datetime.now() - datetime(1970,1,1)).total_seconds()
ms2=int(ts2*1000)
print("microseconds since you ran the last block of code: ",ms2-ms,"10^-6 s")

"""Now that we know how to get time in microseconds, we could use that as our random number seed.  """

ts= (datetime.now() - datetime(1970,1,1)).total_seconds()
random.seed(int(ts))

print("seed= ",int(ts)," --> random: ",random.randint(0,1000))
ts= (datetime.now() - datetime(1970,1,1)).total_seconds()
random.seed(int(ts))
time.sleep(.1)

print("seed= ",int(ts)," --> random: ",random.randint(0,1000))


ts= (datetime.now() - datetime(1970,1,1)).total_seconds()

ms=int(ts*1000)
random.seed(ms)

print("seed= ",int(ms)," --> random: ",random.randint(0,1000))

time.sleep(.1)
ts= (datetime.now() - datetime(1970,1,1)).total_seconds()
ms=int(ts*1000)
random.seed(ms)

print("seed =",int(ms)," --> random: ",random.randint(0,1000))

"""So, you can set your seed based on the time, and record it by printing it to the screen or to your output file.  
NOTE:  normally you only set the seed once at the beginning of the program.  I was just playing with it here to make a point.  

**Major take-home lesson**:  Random numbers are useful, and the seed sets the starting point for the algorith.  It is good practice to **set your random seed**, and to **record it in your program output**.

Now, from your Rivanna command line, you may add, commit, and push your changes to GitHub.
"""

!apt-get install -y git
git clone git@github.com:nem2hb/phys165524-class06hw.git