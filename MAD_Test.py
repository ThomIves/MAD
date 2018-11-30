from sklearn.linear_model import LinearRegression
from ToolKit import MAD

###############################################################################
### Model info section

model = LinearRegression(normalize=True,copy_X=False)

Notes = """Logging the model with TWO non-default parameter and logging all aspects.
Removed the py_version, pip_requirements and imports logging this time."""

MAD(model, extra_notes=Notes) #, py_version=False, pip_requirements=False, imports=False) 
#, capture_notes=False)
