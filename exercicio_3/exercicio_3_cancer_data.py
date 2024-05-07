"""
Exercicio cancer_data.csv
- pode ser feito por até 3 alunos e não mais que isso

- Atividades que devem ser feitas:

    - Analisar se existem missing values e tratar de acordo com o bom senso.
    - Analisar se existem outlier e tratar.
    - Verificar a necessidade de fazer normalização ou padronização dos dados.
    - Realizar a EDA completa desta base de dados.
"""

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import model_selection
import numpy as np
import pandas as pd

#carregar arquivo para uma variável
dataframe = pd.read_csv('cancer_data.csv')
print(dataframe.head())
print('oi')

