#from tabula import read_pdf

#pdf = "chem_gt/chemistry-9701-june-2025.pdf"

#tabula_data = read_pdf(pdf, pages = "all", lattice = "true")
#print(tabula_data[1])

#import os
#from tabula import read_pdf

#filenames = os.listdir("chem_gt")
#print(filenames)
# output = ['chemistry-9701-june-2022.pdf', 'chemistry-9701-june-2023.pdf', 'chemistry-9701-june-2024.pdf', 'chemistry-9701-june-2025.pdf', 'chemistry-9701-march-2022.pdf', 'chemistry-9701-march-2023.pdf', 'chemistry-9701-march-2024.pdf', 'chemistry-9701-march-2025.pdf', 'chemistry-9701-march-2026.pdf', 'chemistry-9701-november-2022.pdf', 'chemistry-9701-november-2023.pdf', 'chemistry-9701-november-2024.pdf', 'chemistry-9701-november-2025.pdf']
#it prints out the file name, not the path, and tabula's read_pdf() cannot find its path and so raises an error
# so os.listdir() won't work.


#for file in filenames:
#    tabula_data = read_pdf(file, pages = "all", lattice ="true")
#    print(tabula_data)

#import glob
#from tabula import read_pdf

#path = "chem_gt"

#filenames = glob.glob(path + '/*.pdf')

# output = ['chem_gt\\chemistry-9701-june-2022.pdf', 'chem_gt\\chemistry-9701-june-2023.pdf', 'chem_gt\\chemistry-9701-june-2024.pdf', 'chem_gt\\chemistry-9701-june-2025.pdf', 'chem_gt\\chemistry-9701-march-2022.pdf', 'chem_gt\\chemistry-9701-march-2023.pdf', 'chem_gt\\chemistry-9701-march-2024.pdf', 'chem_gt\\chemistry-9701-march-2025.pdf', 'chem_gt\\chemistry-9701-march-2026.pdf', 'chem_gt\\chemistry-9701-november-2022.pdf', 'chem_gt\\chemistry-9701-november-2023.pdf', 'chem_gt\\chemistry-9701-november-2024.pdf', 'chem_gt\\chemistry-9701-november-2025.pdf']
# gives relative file path but hey, can't have everything
# hope it works for tabula

#list_of_information = []

#for file in filenames:
#    tabular_data = read_pdf(file, pages = "all", lattice ="true" )
#    list_of_information.append(tabular_data)
#    print(list_of_information[0])
# output is some weird thing, far far far from wanted results

#trying another way

from tabula import read_pdf
import glob

# set search path and glob for files
path = "chem_gt"
filenames = glob.glob(path + '/*.pdf')
# output = ['chem_gt\\chemistry-9701-june-2022.pdf', 'chem_gt\\chemistry-9701-june-2023.pdf', 'chem_gt\\chemistry-9701-june-2024.pdf', 'chem_gt\\chemistry-9701-june-2025.pdf', 'chem_gt\\chemistry-9701-march-2022.pdf', 'chem_gt\\chemistry-9701-march-2023.pdf', 'chem_gt\\chemistry-9701-march-2024.pdf', 'chem_gt\\chemistry-9701-march-2025.pdf', 'chem_gt\\chemistry-9701-march-2026.pdf', 'chem_gt\\chemistry-9701-november-2022.pdf', 'chem_gt\\chemistry-9701-november-2023.pdf', 'chem_gt\\chemistry-9701-november-2024.pdf', 'chem_gt\\chemistry-9701-november-2025.pdf']

# create empty list to store dataframes

list = []

# loop through list of files and read each one into a dataframe and append to list
for file in filenames:
    # read in pdf
    wanted_info = read_pdf(file, stream = "true", guess = "false")
    # append df to list
    list.append(wanted_info[0])
print(list)

# concatenate our list of dataframes into one!
#df = pd.concat(li, axis=0)
#print(df.shape)
#df.head()