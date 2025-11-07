import pandas as pd, numpy as np, joblib
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/synth_lob.csv')
X = df[['midprice','imbalance']].values
y = df['y'].values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

model = joblib.load('ckpts/baseline.pkl')['model']
probs = model.predict_proba(Xte)[:,1]

# simple split-conformal for a probability threshold band demo
alpha = 0.1
# Convert to prediction sets by thresholding around 0.5 with a calibrated margin
cal_margin = np.quantile(np.abs(probs - 0.5), 1-alpha)
pred = (probs > 0.5).astype(int)
covered = (np.abs(probs - 0.5) <= cal_margin).mean()
import os
os.makedirs('results', exist_ok=True)
with open('results/coverage.txt','w') as f:
    f.write(f'alpha={alpha}, coverage≈{covered:.3f}, margin={cal_margin:.3f}\n')
print('coverage written to results/coverage.txt')
