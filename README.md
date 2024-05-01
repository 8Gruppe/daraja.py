# Daraja - Easy to use wrapper around M-Pesa Daraja API

[![PyPI version](https://badge.fury.io/py/daraja.svg)](https://badge.fury.io/py/daraja)


This module provides functions around the Mpesa Daraja API to simplify the whole integration process(problem).

This is what you need to do to get things running:

1. Fill out the `config.json` file with your credentials from Daraja dashboard.

2. Install daraja with `pip install daraja`

3. Import the `mpesa` module from `daraja` like so:
```python
from daraja import Mpesa
```

4. Instantiate a Mpesa object with only two parameters, the config.json file and your environment(either "dev" or "prod"); dev being a development environment and prod being a production environment. This value is used to determine the API endpoints that will be used.
```python
...

mpesa = Mpesa(config_file="config.json", env="prod")
```

5. Use the Mpesa object to do stuff, like so:
```python
...
response = mpesa.stk(receiver="254791500264", amount=50)
print(response)
```

I am working on extending this to cover all the remaining features the Daraja API has to offer. If you can help with it, [contact](https://read.gitahi.me/contact) me.
