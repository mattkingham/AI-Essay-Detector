import pandas as pd
import numpy as np
import re
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import contractions
df = pd.read_csv(r"C:\Users\matth\OneDrive\Documents\Machine Learning Projects\AI Essay Detector\Training_Essay_Data.csv")