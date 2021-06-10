---
layout: default
title: Cell
nav_order: 2
description: ""
permalink: /cell
---

# Cell
The cells are alive!

### Sofware (for developers)

[Get the last version of this software here](https://github.com/PythonForChange/Cell/blob/main/cell.py.

### Installation
#### Option 1: Use pip (recommended, last stable version)
1. Install pyforchange
```
pip install pyforchange
```
2. Import cell in your python file
```python
import pyforchange.cell
```
3. Enjoy!

#### Option 2: Download the source (unstable pre-realise version)
1. Download [cell](https://github.com/PythonForChange/Cell/blob/main/cell.py) into your proyect folder
2. Import cell in your python file
```python
import cell
```
3. Enjoy!

### Usage
Create main.py
```python
from pyforchange.cell import *

adress= "main"
n=20

main=Cell(adress,adress,0,n)
main.reproduction()
execute(main.newname)
```

Execute it.
