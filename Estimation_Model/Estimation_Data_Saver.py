"""
Saving the output of the Estimation Filter in Saved Data/Estimation_Data/[dir_name]/filename(s)
"""
#general
import os
import json
import numpy as np
from pathlib import Path
#own



this_path = Path(__file__)
parent_path = this_path.parent.parent
print(parent_path)