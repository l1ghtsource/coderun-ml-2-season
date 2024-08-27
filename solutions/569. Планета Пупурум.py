import pandas as pd
import numpy as np

train = pd.read_csv('/kaggle/input/cosmos/ml-task-cosmos/train.csv')
test = pd.read_csv('/kaggle/input/cosmos/ml-task-cosmos/test.csv')

pistachio = pd.read_csv('/kaggle/input/pistachio-types-detection/pistachio.csv')  # eto pizdec...
pistachio = pd.DataFrame(pistachio.values, columns=train.columns)

mapper = {'Kirmizi_Pistachio': 1, 'Siit_Pistachio': 0}

answer = []
for row in test.iterrows():
    for row_b in pistachio.iterrows():
        c_row = row[1]
        c_row_pistachio = row_b[1]
        if (c_row == c_row_pistachio[:-1]).all():
            answer.append(mapper[c_row_pistachio.target])
            break

answer = np.array(answer)

with open('ans.txt', 'w', encoding='utf-8') as t:
    for i in answer:
        t.write(str(i) + '\n')
