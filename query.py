import requests
import sys
import pandas

# Allows us to select a product if need arises. Defaults to Windows if no arguments provided.
product = sys.argv[1] if len(sys.argv) >= 2 else "Windows"
print(f"Query for product: {product}")
endoflifeGetAllDetailsURL = f"https://endoflife.date/api/{product}.json"
responseData = requests.get(endoflifeGetAllDetailsURL).json()

# Saves response to csv file.
fileName = f'output-{product}.csv'
pandas.json_normalize(responseData).to_csv(fileName, mode='w', header=True, index=False)


