def ema(prev, cur, alpha):
    return alpha * cur + (1 - alpha) * prev
