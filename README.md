# shopify_coupons_generator

A python script that generates shopify coupon codes in bulk using selenium.

- install python and set up selenium (download/save chromedriver and specify path in import_shopify_coupons.py)
- set up virtual environment and install the pip modules using the requirements.txt file
- export existing coupons from shopify using the export function. (filename should be discounts_export_1.csv)
- edit & run 'python generate_coupons.py' to generate unique coupons
- edit & run 'python import_shopify_coupons.py' to import generated coupons into your shopify site

```
python -m venv .venv
. .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python generate_coupons.py

python import_shopify_coupons.py
```
