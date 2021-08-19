import csv
import random

# Uses "discounts_export_1.csv" file exported from shopify

existing_coupons = [] # populate this list with existing codes from exported csv file
new_coupons = [] # populate this with new coupon codes for later


# adds existing coupons to a list
with open('discounts_export_1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        thecode = row['Name']        
        existing_coupons.append(thecode) # add coupons to existing_coupons list


# length of coupon code + no. of coupons
def get_random_string(length, repeat_no):
    i = 0
    while i < repeat_no:
        letters = 'ABDEFGHJMNPQRTVYZ2345678' # choose characters here
        new_code = ''.join(random.choice(letters) for i in range(length))

        if new_code not in(existing_coupons):
            new_coupons.append(new_code)
            i += 1
        else:
            # if new coupon already exists, skip and don't increment i
            pass


    # save new coupons to new csv file
    f = open('new_codes.csv', 'w', newline='')
    writer = csv.writer(f)
    for thecode in new_coupons:
        writer.writerow([thecode])        
    f.close()


# run script, choose length of coupon and no. of coupons to generate
get_random_string(6, 50)