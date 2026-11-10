import math
import numpy as np
from fractal import sierpinski

def dichte_punkte(polys, delta):
    seg = np.concatenate([np.stack([np.array(p)[:-1], np.array(p)[1:]], 1)
                          for p in polys])
    a, b = seg[:, 0], seg[:, 1]
    m = int(np.ceil(np.linalg.norm(b - a, axis=1).max() / delta)) + 1
    t = np.linspace(0, 1, m)[None, :, None]
    return (a[:, None, :] * (1 - t) + b[:, None, :] * t).reshape(-1, 2)

def boxcount(pts, eps):
    idx = np.floor(pts / eps).astype(np.int64)
    return len(np.unique(idx[:, 0] * 1_000_003 + idx[:, 1]))

if __name__ == "__main__":
    h = math.sqrt(3) / 2
    polys = sierpinski((0.5, 0), (1, h), (0, h), n=4, k=3)

    eps = 2.0 ** -np.arange(1, 13)
    pts = dichte_punkte(polys, delta=eps.min() / 2)
    N = np.array([boxcount(pts, e) for e in eps])

    lokal = -np.diff(np.log(N)) / np.diff(np.log(eps))
    for e, d in zip(eps[1:], lokal):
        print(f"eps = {e:.5f}   local slope = {d:.2f}")