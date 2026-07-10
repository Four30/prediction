import glob
import camelot
import pandas as pd

dict = {"9701":"chem_gt\\gt", "9700":"bio_gt\\gt", "9702":"phy_gt\\gt", "9709": "math_gt\\gt"}
#Getting the old (pre-2026) tables first
path_input = str(input("What subject are you taking?"))
path = dict[path_input]
print(path)
path =path + "\\new_layout_2026"
print(path)