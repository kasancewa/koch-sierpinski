import math
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from fractal import sierpinski

if __name__ == "__main__":
    h = math.sqrt(3) / 2
    polys = sierpinski((0.5, 0), (1, h), (0, h), n=4, k=2)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.add_collection(PolyCollection(polys, facecolor="#7F77DD55",
                                     edgecolor="#534AB7", linewidth=0.4))
    ax.autoscale_view()
    ax.set_aspect("equal")
    ax.invert_yaxis()
    ax.axis("off")
    plt.savefig("sierpinski_koch.png", dpi=300, bbox_inches="tight")
    plt.show()