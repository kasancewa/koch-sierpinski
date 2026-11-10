# Koch–Sierpiński

A Sierpiński triangle whose smallest triangles are replaced by Koch
snowflakes: one fractal nested inside the algorithm of another.

![Result](sierpinski_koch.png)

## Idea

The classic Sierpiński triangle is built by repeatedly splitting a
triangle into three smaller copies and leaving the middle one empty.
Normally the recursion ends in a plain triangle. Here it ends in a
Koch snowflake instead, which is itself generated recursively.

So there are two independent recursion depths:

- `n`: depth of the Sierpiński recursion (3^n snowflakes)
- `k`: depth of the Koch recursion (3·4^k segments per snowflake)

## Why it fits together

A Koch bump on a triangle of side L has height L·√3/6, which is
exactly the inradius of the triangular hole next to it. The tips of
the three neighbouring snowflakes therefore meet precisely in the
centre of each hole. Nothing overlaps, and the Sierpiński structure
stays clearly visible.

## Some numbers

For a start triangle of side $L$:

- Number of snowflakes: $3^n$
- Segments per snowflake: $3 \cdot 4^k$
- Total boundary length:

$$
\ell = 3L \left(\tfrac{3}{2}\right)^{n} \left(\tfrac{4}{3}\right)^{k}
$$

- Area of one snowflake as $k \to \infty$: $\tfrac{8}{5}$ of its start triangle
- Fractal dimensions:

$$
D_\text{Sierpiński} = \frac{\ln 3}{\ln 2} \approx 1.585, \qquad
D_\text{Koch} = \frac{\ln 4}{\ln 3} \approx 1.262
$$

The Koch bump on a triangle of side $L$ has height $\frac{\sqrt{3}}{6}L$, which equals the inradius of the neighbouring hole.
## Dimension

### Definition

The box-counting dimension of a set $F \subset \mathbb{R}^2$ is

$$
D = \lim_{\varepsilon \to 0} \frac{\ln N(\varepsilon)}{\ln (1/\varepsilon)},
$$

where $N(\varepsilon)$ is the number of grid squares of side $\varepsilon$ that
touch $F$. If $N(\varepsilon) \approx c\,\varepsilon^{-D}$, then
$\ln N = D \ln(1/\varepsilon) + \ln c$, so $D$ is the slope of a straight
line in a log-log plot.

For self-similar sets that satisfy the open set condition, the Hausdorff
dimension equals the box-counting dimension and solves the Moran equation

$$
\sum_{i=1}^{m} r_i^{\,D} = 1 .
$$

- Sierpiński triangle: $m = 3$, $r = \tfrac12$, so $3 \left(\tfrac12\right)^D = 1$ and
  $D = \dfrac{\ln 3}{\ln 2} \approx 1.585$.
- Koch curve: $m = 4$, $r = \tfrac13$, so $4 \left(\tfrac13\right)^D = 1$ and
  $D = \dfrac{\ln 4}{\ln 3} \approx 1.262$.

### Three scaling regimes

At finite depths $n$ and $k$ the picture is only a polyline, so its true
dimension is 1. Over a range of scales it still behaves like a fractal.
Let $L = 1$. A leaf triangle has side $s = 2^{-n}$ and the finest Koch segment
has length $s \cdot 3^{-k}$.

**1. Large boxes, $\varepsilon \gg s$.** At scale $\varepsilon = 2^{-m}$ the
structure consists of $3^m$ triangles, so

$$
N(\varepsilon) \approx 3^m = \varepsilon^{-\ln 3 / \ln 2}
\quad\Rightarrow\quad D \approx 1.585 .
$$

**2. Medium boxes, $s\,3^{-k} \ll \varepsilon \ll s$.** One snowflake outline
consists of $4^j$ pieces of length $s\,3^{-j}$. With $\varepsilon = s\,3^{-j}$
one snowflake needs $(s/\varepsilon)^{\ln 4 / \ln 3}$ boxes, and there are
$3^n$ snowflakes:

$$
N(\varepsilon) \approx 3^n \left(\frac{s}{\varepsilon}\right)^{\ln 4 / \ln 3}
\quad\Rightarrow\quad D \approx 1.262 .
$$

**3. Small boxes, $\varepsilon \ll s\,3^{-k}$.** The outline is a smooth
polyline of total length

$$
\ell = 3^n \cdot 3s \left(\tfrac43\right)^k ,
$$

so $N(\varepsilon) \approx \ell / \varepsilon$ and $D = 1$.

The crossovers lie at $\varepsilon \approx 2^{-n}$ and
$\varepsilon \approx 2^{-n} 3^{-k}$. For $n = 4$, $k = 3$ that is
$\varepsilon \approx 0.0625$ and $\varepsilon \approx 0.0023$.

### Limits

- $n \to \infty$ (any $k$): the snowflakes shrink to points and the set
  becomes the Sierpiński triangle, $D = \ln 3 / \ln 2$.
- $k \to \infty$ ($n$ fixed): the outline is a union of $3^n$ Koch curves,
  $D = \ln 4 / \ln 3$ (the filled region has $D = 2$).

### Numerical estimate

`dimensions.py` places many points along the outline, counts the occupied
grid squares for $\varepsilon = 2^{-1}, 2^{-2}, \dots, 2^{-12}$ and prints
the local slope

$$
D_\text{loc} = -\frac{\ln N(\varepsilon_{i+1}) - \ln N(\varepsilon_i)}
                      {\ln \varepsilon_{i+1} - \ln \varepsilon_i} .
$$

The three plateaus in $D_\text{loc}$ match the regimes above. Box counting is
accurate to about $\pm 0.05$, so the values are estimates, not exact results.
## Implementation

- `koch(a, b, s, depth)` builds a Koch curve between two points as a
  list of points. `s = ±1` chooses which side the bump points to.
- `schneeflocke(A, B, C, k)` joins three Koch curves into a snowflake
  and makes sure the bumps point outward.
- `sierpinski(A, B, C, n, k)` splits the triangle recursively and
  returns the snowflake polygons.
- `plot.py` draws them with matplotlib.

## Usage

    pip install matplotlib
    python plot.py

Change `n` and `k` at the bottom of `plot.py`. Large values such as
`n=5, k=4` produce several hundred thousand segments and take a moment.

## Tests

    pytest

Checks the number of snowflakes (3^n) and the number of points per
snowflake (3·4^k + 1).

## Possible extensions

- Use Koch curves as the edges of the Sierpiński triangle too
- Swap the base shape (Koch snowflake, Minkowski island, …)
- Interactive version in the browser (HTML/JavaScript)

## License

MIT
