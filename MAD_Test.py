import sys
import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from ToolKit import MAD
# import Nothing

###############################################################################
### Model info section

model = LinearRegression(normalize=True)

Notes = """These are my different extra important notes.
These have a carriage return in them too!!!"""

MAD(model, extra_notes=Notes) #, locals=locals())
