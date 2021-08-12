#Step 1: Importing necessary libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
import seaborn as sns
from IPython.display import display_html
from itertools import chain,cycle
import warnings
warnings.filterwarnings('ignore')

#Step 2: Reading and understanding our data
pokemon = pd.read_csv('Pokemon.csv')
pokemon.shape
{
    "tags": [
        "hide-input",
    ]
}
pokemon.info
pokemon.isna().sum()
pokemon.describe().round(1)

#Step 3: Data Cleaning (to make our data more readable)

#3.1: Fields of the dataset
pokemon = pokemon.rename(columns = {'#':'Pokedex #'})
pokemon['Type 2'] = pokemon['Type 2'].fillna(value = 'None')
pokemon['Dual Type'] = np.where(pokemon['Type 2'].isna(), False, True)

#3.2: Changing datatype of categorical variables and continuous variables 
pokemon.columns
pokemon.columns[1:]

categorical = ['Pokedex #','Type 1', 'Type 2', 'Generation', 'Legendary', 'Dual Type']
continuous = []
for field in pokemon.columns[2:]:
    if field not in categorical:
        continuous.append(field)
for i in categorical: 
    pokemon[i] = pokemon[i].astype('category')
for j in continuous:
    pokemon[j] = pokemon[j].astype('int')
   
#3.3: Data Transformation of Pokemon Name

def mega_pokemon(string):
    return 'Mega' in string

def primal_pokemon(string):
    return 'Primal' in string

def incarnate_forme(string):
    return 'Incarnate' in string 

def therian_forme(string):
    return 'Therian' in string

pokemon['Name'] = pokemon['Name'].apply(lambda x: 'Mega ' + x.split("Mega")[0] if mega_pokemon(x) else x)
pokemon['Name'] = pokemon['Name'].apply(lambda x: 'Primal ' + x.split("Primal")[0] if primal_pokemon(x) else x)
pokemon['Name'] = pokemon['Name'].apply(lambda x: x.split("Incarnate Forme")[0] + " (Incarnate Forme)" if incarnate_forme(x) else x)
pokemon['Name'] = pokemon['Name'].apply(lambda x: x.split("Therian Forme")[0] + " (Therian Forme)" if therian_forme(x) else x)

for i in [7,163]:
    pokemon['Name'][i] += ' X'
    
for j in [8,164]:
    pokemon['Name'][j] += ' Y'
    
deoxys_formes = [' (Normal Forme)', ' (Attack Forme)', ' (Defense Forme)', ' (Speed Forme)']
for i in range(428,432):
    pokemon['Name'][i] = 'Deoxys' + deoxys_formes[i-428]
    
wormadam_formes = [' (Plant Cloak)', ' (Sandy Cloak)', ' (Trash Cloak)']
for i in range(458,461):
    pokemon['Name'][i] = 'Wormadam' + wormadam_formes[i - 458]

rotom_formes = ['Heat', 'Wash', 'Frost', 'Fan', 'Mow']
for i in range(532,537):
    pokemon['Name'][i] = rotom_formes[i-532] + ' Rotom'

pokemon['Name'][544] = "Giratina " + pokemon['Name'][544].split("Giratina")[1]
pokemon['Name'][545] = "Giratina " + pokemon['Name'][545].split("Giratina")[1]

pokemon['Name'][550] = "Shaymin " + pokemon['Name'][550].split("Shaymin")[1]
pokemon['Name'][551] = "Shaymin " + pokemon['Name'][551].split("Shaymin")[1]

pokemon['Name'][615] = "Darmanitan " + pokemon['Name'][615].split("Darmanitan")[1]
pokemon['Name'][616] = "Darmanitan " + pokemon['Name'][616].split("Darmanitan")[1]

pokemon['Name'][711] = pokemon['Name'][711].split('Kyurem')[1] + 'Kyurem'
pokemon['Name'][712] = pokemon['Name'][712].split('Kyurem')[1] + 'Kyurem' 

formes = ['Ordinary Forme', 'Resolute Forme', 'Aria Forme', 'Pirouette Forme']
for i in range(713, 717):
    pokemon['Name'][i] = pokemon['Name'][i].split(formes[i-713])[0] + " (" + formes[i-713] + ")"
    
pokemon['Name'][746] = 'Meowstic (Male)'
pokemon['Name'][747] = 'Meowstic (Female)'

pokemon['Name'][750] = pokemon['Name'][750].split('Blade Forme')[0] + ' (Blade Forme)'
pokemon['Name'][751] = pokemon['Name'][751].split('Shield Forme')[0] + ' (Shield Forme)'

def small_size(string):
    return 'Small Size' in string

def average_size(string):
    return 'Average Size' in string 

def large_size(string):
    return 'Large Size' in string

def super_size(string):
    return 'Super Size' in string 

pokemon['Name'] = pokemon['Name'].apply(lambda x: x.split('Small Size')[0] + ' (Small Size)' if small_size(x) else x)
pokemon['Name'] = pokemon['Name'].apply(lambda x: x.split('Average Size')[0] + ' (Average Size)' if average_size(x) else x)
pokemon['Name'] = pokemon['Name'].apply(lambda x: x.split('Large Size')[0] + ' (Large Size)' if large_size(x) else x)
pokemon['Name'] = pokemon['Name'].apply(lambda x: x.split('Super Size')[0] + ' (Super Size)' if super_size(x) else x)

pokemon['Name'][794] = 'Zygarde (50% Forme)'

for i in [797,798]:
    pokemon['Name'][i] = 'Hoopa' + pokemon['Name'][i].split('HoopaHoopa')[1]

    



