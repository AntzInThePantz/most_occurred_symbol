# most_occured_symbol
**prerequisite:**  
python3  
python3 Module virtualenv

**how to install with console script:**  
```
~ git clone https://github.com/AntzInThePantz/most_occurred_symbol.git  
~ cd most_occurred_symbol  
~ python3 -m venv .  
~ . bin/activate  
~ python3 setup.py develop  
```

**how to install without console script:**  
```
~ git clone https://github.com/AntzInThePantz/most_occurred_symbol.git  
~ cd most_occurred_symbol  
~ python3 -m venv .  
~ . bin/activate  
~ chmod +x most_occurred_symbol/__init__.py
```

**how to execute with console script:**  
```
~ find-most-occurred-letter
```

**how to execute without console script:**  
```
~ ./most_occurred_symbol/__init__.py
```

**how to run tests:**  
```
~ pip install nose
~ python setup.py test --with-coverage
```
