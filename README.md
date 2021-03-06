# market-auction-value
Technical Assessment - Full Stack Engineer (Python) - Prediktive


### Examples:

- Calculate based on data in the JSON file:
```
py market-auction.py 87390 2020
{'Market': 54133.382013999995, 'Auction': 37818.936615}
```

- Examples with no data in the JSON but using default ratios
```
py market-auction.py 87390 2021
{'Market': 57381.384934839996, 'Auction': 40088.072811900005}
py market-auction.py 87390 2022
{'Market': 60824.2680309304, 'Auction': 42493.35718061401}
py market-auction.py 87390 2023
{'Market': 64473.72411278622, 'Auction': 45042.95861145085}
```

- No data in JSON but older years
```
py market-auction.py 87390 2015
{'Market': 28207.298411919997, 'Auction': 19200.71426568}
py market-auction.py 87390 2014
{'Market': 26514.860507204794, 'Auction': 18048.6714097392}
py market-auction.py 87390 2013
{'Market': 24923.968876772506, 'Auction': 16965.751125154846}
```