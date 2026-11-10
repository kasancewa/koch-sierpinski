import math
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

def koch(a, b, s, tiefe):
    """Punkte von a (ohne) bis b (mit) auf einer Koch-Kurve.
    s = +1/-1 bestimmt, auf welche Seite die Spitze zeigt."""
    if tiefe == 0:
        return [b]
    dx, dy = (b[0] - a[0]) / 3, (b[1] - a[1]) / 3
    p1 = (a[0] + dx, a[1] + dy)
    p3 = (b[0] - dx, b[1] - dy)
    w = s * math.sqrt(3) / 2          # sin(+-60 Grad)
    spitze = (p1[0] + dx / 2 - dy * w, p1[1] + dx * w + dy / 2)
    return (koch(a, p1, s, tiefe - 1) + koch(p1, spitze, s, tiefe - 1)
            + koch(spitze, p3, s, tiefe - 1) + koch(p3, b, s, tiefe - 1))

def schneeflocke(A, B, C, k):
    """Koch-Schneeflocke mit dem Dreieck ABC als Startform."""
    cx, cy = (A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3
    punkte = [A]
    for a, b in ((A, B), (B, C), (C, A)):
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        dx, dy = (b[0] - a[0]) / 3, (b[1] - a[1]) / 3
        # Testspitze mit s=+1: zeigt sie vom Schwerpunkt weg?
        tx = dx / 2 - dy * math.sqrt(3) / 2
        ty = dx * math.sqrt(3) / 2 + dy / 2
        s = 1 if tx * (mx - cx) + ty * (my - cy) > 0 else -1
        punkte += koch(a, b, s, k)
    return punkte

def sierpinski(A, B, C, n, k):
    """Liste von Polygonen: bei Tiefe 0 eine Koch-Schneeflocke."""
    if n == 0:
        return [schneeflocke(A, B, C, k)]
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    AB, BC, CA = mid(A, B), mid(B, C), mid(C, A)
    return (sierpinski(A, AB, CA, n - 1, k)
            + sierpinski(AB, B, BC, n - 1, k)
            + sierpinski(CA, BC, C, n - 1, k))

if __name__ == "__main__":
    h = math.sqrt(3) / 2
    polys = sierpinski((0.5, 0), (1, h), (0, h), n=4, k=2)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.add_collection(PolyCollection(polys, facecolor="#7F77DD55",
                                     edgecolor="#534AB7", linewidth=0.4))
    ax.autoscale_view()
    ax.set_aspect("equal")
    ax.invert_yaxis()     # y zeigt nach unten wie im Browser
    ax.axis("off")
    plt.savefig("sierpinski_koch.png", dpi=300, bbox_inches="tight")
    plt.show()