# forex
REQUIREMENTS:
  Docker Version 17.12.0-ce-mac49 (21995) or equivalent for Linux / Windows

HOW TO INSTALL:

`git clone https://github.com/slawek87/forex.git`

HOW TO RUN:

bash```
cd forex_app
docker build -t forex_app:latest .
docker run -p 5000:5000 forex_app
```

HOW TO USE:
open http://0.0.0.0:5000/

Example:
  http://0.0.0.0:5000/?from_currency=EUR&to_currency=USD&quantity=1000
