# quilt_colors
Randomize quilt block colors without letting adjacent blocks be the same color.

# Example
```python
from quilt_colors import Quilt

# each color in the color pallet reprisents a diferent color
# width and heigh are the number of quilt blocks
quilt = Quilt(width=15, height=21, color_pallet='rgbyp')
quilt.choose_colors()
print(quilt)
```
