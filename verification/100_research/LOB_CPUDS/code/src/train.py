import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib, os

os.makedirs('ckpts', exist_ok=True)
df = pd.read_csv('data/synth_lob.csv')
X = df[['midprice','imbalance']].values
y = df['y'].values

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
clf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
probs = clf.predict_proba(Xte)[:,1]
auc = roc_auc_score(yte, probs)
print('AUC', round(auc,4))
joblib.dump({'model': clf}, 'ckpts/baseline.pkl')
with open('results_auc.txt','w') as f: f.write(str(auc))
