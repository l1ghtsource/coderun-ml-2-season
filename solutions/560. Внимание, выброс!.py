import numpy as np
from sklearn.neighbors import LocalOutlierFactor

file_path = '/kaggle/input/coderun-anomaly/attention_to_emission_input.txt'
with open(file_path, 'r') as file:
    n, m = map(int, file.readline().split())

    data = []
    for _ in range(n):
        data.append(list(map(float, file.readline().split())))

data = np.array(data)[:50000]

lof = LocalOutlierFactor()
y_pred = lof.fit_predict(data)
anomalies = np.where(y_pred == -1)[0] + 1

output_file = 'output.txt'
with open(output_file, 'w') as out_file:
    out_file.write(f'{len(anomalies)}\n')
    for anomaly in anomalies:
        out_file.write(f'{anomaly}\n')
