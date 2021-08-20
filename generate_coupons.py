import csv
import random

def generate_coupons(exported_csv, coupon_no, code_length, letters):
    existing_coupons = [] # populate this list with existing codes from exported csv file
    new_coupons = [] # populate this with new coupon codes for later


    # adds existing coupons to a list
    with open(exported_csv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            thecode = row['Name']        
            existing_coupons.append(thecode) # add coupons to existing_coupons list


    i = 0
    while i < coupon_no:
        new_code = ''.join(random.choice(letters) for i in range(code_length))

        if new_code not in(existing_coupons) and new_code not in (new_coupons):
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
    print(f'{coupon_no} coupon codes generated as saved in new_codes.csv')
