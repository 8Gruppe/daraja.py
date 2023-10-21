# Daraja - Easy to use functions around M-Pesa Daraja API

[![PyPI version](https://badge.fury.io/py/daraja.svg)](https://badge.fury.io/py/daraja)


This module provides functions around the daraja api to simplify the whole integration process.

This is what you need to do:

1. Fill out the `config.json` file with your credentials from Daraja dashboard.

2. Install daraja with `pip install daraja`

3. Import the `mpesa` module from `daraja` like so:
```python
from daraja import mpesa
```

4. Instantiate a Mpesa object with only two parameters, the config.json file and your environment(either dev or prod)
```python
...

mpesa = mpesa.Mpesa(config_file="config.json", env="prod")
```

5. Use the Mpesa object to do stuff, like so:
```python
...
response = mpesa.stk(receiver="254791500264, amount=50)
print(response)
```

I am working on implementing the remaining endpoints and even right now this does not work functionally well and i am working to solve the issue.


