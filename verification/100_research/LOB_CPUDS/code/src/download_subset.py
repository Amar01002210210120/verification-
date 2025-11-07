import pandas as pd
import numpy as np, os

os.makedirs('data', exist_ok=True)
# Generate a tiny synthetic 'LOB-like' sample to avoid licensing issues.
rng = np.random.default_rng(0)
n = 2000
df = pd.DataFrame({
    'midprice': rng.normal(0,1, n).cumsum()+100.0,
    'imbalance': rng.uniform(-1,1, n),
})
df['y'] = (df['midprice'].shift(-5) > df['midprice']).astype(int)
df = df.dropna().reset_index(drop=True)
df.to_csv('data/synth_lob.csv', index=False)
print('Wrote data/synth_lob.csv', len(df))
