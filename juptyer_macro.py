'''
Macro for jupyter notebooks

Save locally 

    %macro -q import_setup <cell_number>
    %store import_setup
    
Load

    %store -r import_setup
    import_setup
    
'''

import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import re
from sklearn.model_selection import train_test_split
import sklearn
from tqdm import tqdm

%load_ext lab_black

