# Koch–Sierpiński

A Sierpiński triangle whose smallest triangles are replaced by Koch
snowflakes: one fractal nested inside the algorithm of another.

![Result](sierpinski_koch.png)

## Idea

The classic Sierpiński triangle is built by repeatedly splitting a
triangle into three smaller copies and leaving the middle one empty.
Normally the recursion ends in a plain triangle. Here it ends in a
Koch snowflake, which is itself generated recursively.

There are two independent recursion depths:

- $n$: depth of the Sierpiński recursion
- $k$: depth of the Koch recursion

## Why it fits together

A Koch bump on a triangle of side $L$ has height $\frac{\sqrt{3}}{6}L$,
which is exactly the inradius of the triangular hole next to it. The tips
of the three neighbouring snowflakes therefore meet in the centre of each
hole, and nothing overlaps.

## Some numbers

For a start triangle of side $L$:

- Number of snowflakes: $3^n$
- Segments per snowflake: $3 \cdot 4^k$
- Total boundary length:

$$
\ell = 3L \left(\tfrac{3}{2}\right)^{n} \left(\tfrac{4}{3}\right)^{k}
$$

- Area of one snowflake as $k \to \infty$: $\tfrac{8}{5}$ of its start triangle

## Usage

```bash
pip install matplotlib numpy
python plot.py          # draws the fractal
python dimensions.py    # estimates the dimension
```

Change `n` and `k` at the bottom of each script. Large values such as
`n=5, k=4` produce several hundred thousand segments and take a moment.

## Implementation

- `fractal.py`
  - `koch(a, b, s, tiefe)` builds a Koch curve between two points as a list
    of points. `s = ±1` chooses the side the bump points to.
  - `schneeflocke(A, B, C, k)` joins three Koch curves into a snowflake and
    makes the bumps point outward.
  - `sierpinski(A, B, C, n, k)` splits the triangle recursively and returns
    the snowflake polygons.
- `plot.py` draws the polygons with matplotlib.
- `dimensions.py` estimates the box-counting dimension.

## Dimension

### Hausdorff dimension

Cover a set $F$ with sets $U_i$ of diameter at most $\delta$, add up
$(\mathrm{diam}\, U_i)^s$, take the cheapest covering and let
$\delta \to 0$:
$$
\mathcal{H}^s(F) = \lim_{\delta \to 0} \, \inf \sum_i (\mathrm{diam}\, U_i)^s
$$

For small $s$ this is $\infty$, for large $s$ it is $0$. The Hausdorff
dimension $\dim_H F$ is the value of $s$ where it jumps.

**Koch curve.** At level $m$ the curve is covered by $4^m$ pieces of
diameter $3^{-m}$, which costs

$$
4^m \left(3^{-m}\right)^s = \left(\frac{4}{3^s}\right)^m .
$$

This tends to $0$ for $3^s > 4$, so $\dim_H \le \ln 4 / \ln 3$. Putting
mass $4^{-m}$ on every level-$m$ piece and applying the mass distribution
principle gives the same lower bound. Hence

$$
\dim_H(\text{Koch}) = \frac{\ln 4}{\ln 3} \approx 1.262 .
$$

**Sierpiński triangle.** The same argument with $3^m$ pieces of diameter
$2^{-m}$ gives

$$
\dim_H(\text{Sierpiński}) = \frac{\ln 3}{\ln 2} \approx 1.585 .
$$

Both values also solve the Moran equation $\sum_i r_i^D = 1$ for
self-similar sets: $4 \left(\tfrac13\right)^D = 1$ and
$3 \left(\tfrac12\right)^D = 1$.

### Box-counting dimension

Box counting allows only grid squares of one size $\varepsilon$. With
$N(\varepsilon)$ the number of squares that touch $F$,

$$
\dim_B F = \lim_{\varepsilon \to 0} \frac{\ln N(\varepsilon)}{\ln (1/\varepsilon)} .
$$

Hausdorff coverings may mix sizes, so they are never more expensive, and
$\dim_H F \le \dim_B F$ always holds.

### Dimension of this fractal

The answer depends on the limit. Hausdorff dimension is countably stable:
a countable union has the supremum of the individual dimensions.

| Set | Hausdorff | Box counting |
|---|---|---|
| Finite $n$ and $k$ (a polyline) | $1$ | $1$ |
| $n$ fixed, $k \to \infty$ ($3^n$ Koch curves) | $1.262$ | $1.262$ |
| Limit $n \to \infty$ (Sierpiński triangle) | $1.585$ | $1.585$ |
| All snowflakes of all levels together | $1.262$ | $1.585$ |

The last row shows the difference between the two. The set is a countable
union of Koch curves, so its Hausdorff dimension is $\ln 4 / \ln 3$. At box
size $\varepsilon = 2^{-m}$, the $3^m$ snowflakes of level $m$ alone need
about $3^m = \varepsilon^{-\ln 3 / \ln 2}$ boxes, so its box-counting
dimension is $\ln 3 / \ln 2$. Box counting sees how the snowflakes
accumulate along the Sierpiński triangle, and Hausdorff does not.

### Numerical estimate

`dimensions.py` places points densely along the outline, counts occupied
grid squares for $\varepsilon = 2^{-1}, \dots, 2^{-12}$ and prints the
local slope of $\ln N$ against $\ln(1/\varepsilon)$. A finite picture has
dimension $1$, but the slope shows three scale ranges. With leaf side
$s = 2^{-n}$:

- $\varepsilon \gg s$: slope $\approx 1.585$ (Sierpiński structure)
- $s \, 3^{-k} \ll \varepsilon \ll s$: slope $\approx 1.262$ (Koch structure)
- $\varepsilon \ll s \, 3^{-k}$: slope $\approx 1$ (straight segments)

For $n = 4$, $k = 3$ the crossovers lie near $\varepsilon \approx 0.0625$
and $\varepsilon \approx 0.0023$. Box counting on a grid is accurate to
about $\pm 0.05$, so these are estimates that confirm the exact values.

## License

MIT
