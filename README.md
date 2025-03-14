# Kuehne+Nagel Take Home Assignment - Querying https://endoflife.date

## Description
This small scripts queries a product from [endoflife.date](https://endoflife.date) API and saves the response to output-<PRODUCT_NAME>.csv file.
The default product is set to 'Windows', but a product can also be chosen manually by supplying a command line argument when running the script.

Python version used - 3.13.2
Dependencies are listed in requirements.txt

## Installation
### Creating a Python virtual environment
1. Clone this repository to the desired location and move there 
```
git clone https://github.com/kemplar285/endoflife.date_v.trelin
```

2. Open the folder

```
cd .\endoflife.date_v.trelin\
```

3. Create a virtual environment in the current folder

```
python -m venv .
```

4. Activate the environment

```
.\Scripts\activate
```

5. Install all the dependencies from requirements.txt file

```
pip install -r requirements.txt
```

Now you're good to go!

## Running the script

You can now run the script. An argument can be supplied to query a product other than Windows, but it is optional.
This script will create a separate output file for each product.
IMPORTANT: New queries will overwrite the existing file.

```
python .\query.py <OPTIONAL_PRODUCT_ARGUMENT>
```