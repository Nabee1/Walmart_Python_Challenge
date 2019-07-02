import pandas as pd
import numpy as np

def checkNullValues(df : pd.DataFrame) -> bool:
	return df.isnull().values.any()

def countNullValues(df : pd.DataFrame):
	return df.isnull().sum()

