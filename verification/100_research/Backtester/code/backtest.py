import pandas as pd, numpy as np, os
np.random.seed(0)
n = 500
price = 100 + np.cumsum(np.random.normal(0,1,n))
signal = np.sign(np.convolve(np.diff(price, prepend=price[0]), [1,1,1], 'same'))
fee = 0.0002
pos = signal[:-1]
ret = np.diff(price)/price[:-1]
pnl = pos*ret - fee*np.abs(np.diff(pos, prepend=0))
df = pd.DataFrame({'price':price[1:], 'pos':pos, 'ret':ret, 'pnl':pnl})
os.makedirs('results', exist_ok=True)
df.to_csv('results/toy_backtest.csv', index=False)
print('Wrote results/toy_backtest.csv')
