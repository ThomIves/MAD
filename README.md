![MaShell Logo](https://github.com/ThomIves/MAD/blob/master/MAD_logo.png)

# MAD
> "Model and Dependencies" - capture machine learning settings and dependencies

I love doing machine learning competitions, but I get "MAD" at myself when I let my model settings and results mixed up. I try hard to avoid this, but it still happens, because I can be an idiot. This python module is a way to avoid these (my) issues. Another script is forthcoming that can prepend competition results to the log file names created by this script. 

## Installing / Getting started

Clone or download this to a directory of your choosing. Play with it from what I have provided and make it your own from there. 

To run everything as written, you will need (as one of the log files states):
  1) python version:
     3.5.2 (default, Nov 23 2017, 16:37:01) 
     *I am sure you can change things to make it work for other python version if it's even necessary.*
  2) pip requirements:
     numpy==1.15.2
     pandas==0.23.4
     sklearn==0.0
  3) Necessary Imports:
     import sys
     import sklearn
     from sklearn.linear_model import LinearRegression
     import numpy as np
     import pandas as pd
     from ToolKit import MAD

You will find for your logging pleasure (until you butcher it and make it your own ... which I would do too):
  1) ToolKit.py - houses the MAD class and it's methods and is painfully documented and pep8'd to death!
  2) MAD_Test.py - a simple machine learning file that literaly does nothing but instantiate a model from an sklearn machine learning class and then creates the magic log of everything you (in the future) or someone else wants to replicate your modeling. 
  3) model_logs - a directory holding two complete log files as examples. 

## Deploying / Publishing

I would appreciate it, as you share your work leveraged from this set of scripts, if you would please keep a referral back to my github repo. Thanks! I'd do the same for you. :-)

## Contributing

I am open to share the development and improvements of this with others, but it has been solo up until now. Let me know if you'd like to contribute. 

## Links

This work came from https://github.com/ThomIves/MAD originally. 

## Licensing

"The code in this project is licensed under MIT license."


