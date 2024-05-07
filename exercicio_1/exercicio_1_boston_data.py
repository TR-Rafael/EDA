"""
Exercicio boston data
- pode ser feito por até 3 alunos e não mais que isso

- Atividades que devem ser feitas:

    - Analisar se existem missing values e tratar de acordo com o bom senso.
    - Analisar se existem outlier e tratar.
    - Verificar a necessidade de fazer normalização ou padronização dos dados.
    - Realizar a EDA completa desta base de dados.
"""

import pandas as pd
from sklearn import datasets
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]