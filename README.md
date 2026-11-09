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

For a start triangle of side L:

- Number of snowflakes: 3^n
- Total boundary length: 3L · (3/2)^n · (4/3)^k
- Area of one snowflake as k → ∞: 8/5 of its start triangle
- Fractal dimensions: Sierpiński triangle log 3 / log 2 ≈ 1.585,
  Koch curve log 4 / log 3 ≈ 1.262

For n → ∞ at fixed k the snowflakes shrink and the set approaches
the Sierpiński triangle. For k → ∞ at fixed n every boundary becomes
a Koch curve with infinite length but finite area.

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
