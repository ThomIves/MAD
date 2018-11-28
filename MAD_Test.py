import sys
import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from ToolKit import MAD
# import Nothing

###############################################################################
### Model info section

model = LinearRegression(normalize=True,copy_X=False)

Notes = """In this run, I decided to not log the:
    python version, 
    the pip requirements, and
    the imports"""

MAD(model, extra_notes=Notes) #, py_version=False, pip_requirements=False, imports=False, capture_notes=False)
