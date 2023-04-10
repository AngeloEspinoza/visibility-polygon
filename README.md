# Visibility Polygon
<p align="center">
  <img src="https://user-images.githubusercontent.com/40195016/230996739-a48dafe9-1aaf-48f6-b67e-6a1fe8c875b8.gif" alt="animated" />
</p>

## Description
A 2D simulation in the framework Pygame for computing the visibility polygon regarding a robot that is considered to be a point $p$ on a plane with the 
presence of obstacles. The environment is a kind of corridor where the robot moves along. In order to make the robot explore the environment and generate the multiple
visibility polygons that get generated through the exploration, the keyboard arrows can be used.

## Usage
```
usage: visibility_polygon.py [-h] [-st  [...]] [-sr | --show_rays | --no-show_rays]

Implements the visibility polygon algorithm for a point.

options:
  -h, --help            show this help message and exit
  -st  [ ...], --start  [ ...]
                        Initial position of the robot in X and Y, respectively
  -sr, --show_rays, --no-show_rays
                        Show only the casted rays on screen
```

## Examples
Display the robot only showing the cast of the rays and not the polygon

```python3 visibility_polygon.py --show_rays```

Set the initial position of the robot at $p = (20, 20)$

```python3 visibility_polygon.py --start 20, 20```


## License 
MIT License

Copyright (c) [2023] [Angelo Espinoza]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
