# quilt_colors
Randomly assign colors to a quilt without letting any colors touch.

# Example
```python
from quilt_colors import color_quilt, new_quilt, print_quilt

colors = {'red', 'green', 'blue', 'yellow', 'mauve'}
quilt = color_quilt(new_quilt(10, 15), colors)
print_quilt(quilt)
```
