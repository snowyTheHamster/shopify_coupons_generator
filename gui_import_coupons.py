import traceback
import PySimpleGUI as sg
import import_coupons

layout = [
    [sg.Radio('1. Enter URL/ALogin/Password', "_RADIO_MODE1_", default=True, key='Radio_1', enable_events=True), sg.Radio('2. Login with shopify_login.txt', "_RADIO_MODE1_", key='Radio_2', enable_events=True)],
    [sg.Text('2. Create shopify_login.txt in same location as this App. 1st line: username, 2nd line: password, 3rd line: shopurl')],
    [sg.Text('Shopify URL:'), sg.InputText('', key='_SITE_URL_', size=(30,1))],
    [sg.Text('Shopify Username:'), sg.InputText('', key='_USERNAME_', size=(30,1))],
    [sg.Text('Password:'), sg.InputText('', key='_PASSWORD_', password_char='*', size=(30,1))],
    [sg.Text('csv file with coupon codes:'), sg.Input(key='_COUPON_CSV_'), sg.FileBrowse()],
    [sg.Text('Discount Percent:'), sg.InputText('15', key='_DISCOUNT_AMT_', size=(15, 1))],
    [sg.Text('Minimum Spending:'), sg.InputText('500', key='_MINIMUM_SPENDING_', size=(15, 1))],
    [sg.Text('Date Start:'), sg.InputText('2021-09-01', key='_DATE_START_', size=(15, 1))],
    [sg.Text('Time Start:'), sg.InputText('12:00 am', key='_TIME_START_', size=(15, 1))],
    [sg.Text('Date End:'), sg.InputText('2022-09-30', key='_DATE_END_', size=(15, 1))],
    [sg.Text('Time End:'), sg.InputText('11:59 pm', key='_TIME_END_', size=(15, 1))],
    [sg.Text('')],
    [sg.Button("RUN", size=(10, 1), bind_return_key=True, key='_RUN_')],
    [sg.Output(size=(60, 10))],
]

window: object = sg.Window('Shopify Bulk Coupon Generator', layout, element_justification='left')

try:
    while True:
        event, values = window.read()
        if event is None:
            break

        if values['Radio_2'] == True:
            window.find_element('_USERNAME_').Update(disabled = True)
            window.find_element('_PASSWORD_').Update(disabled = True)
            window.find_element('_SITE_URL_').Update(disabled = True)
        if values['Radio_1'] == True:
            window.find_element('_USERNAME_').Update(disabled = False)
            window.find_element('_PASSWORD_').Update(disabled = False)
            window.find_element('_SITE_URL_').Update(disabled = False)

        if event == '_RUN_':

            if values['_COUPON_CSV_'] == '' \
	    		or values['_DISCOUNT_AMT_'] == '' or values['_MINIMUM_SPENDING_'] == '' \
	    		or values['_DATE_START_'] == '' or values['_TIME_START_'] == '' \
	    		or values['_DATE_END_'] == '' or values['_TIME_END_'] == '':
                		print('None of the fields can be empty')

            else:
                coupon_csv = values['_COUPON_CSV_']
                discount_amt= int(values['_DISCOUNT_AMT_'])
                minimum_spending = int(values['_MINIMUM_SPENDING_'])
                date_start = str(values['_DATE_START_'])
                time_start = str(values['_TIME_START_'])
                date_end = str(values['_DATE_END_'])
                time_end = str(values['_TIME_END_'])
                if values['Radio_1'] == True:
                    username = str(values['_USERNAME_'])
                    password = str(values['_PASSWORD_'])
                    site_url = str(values['_SITE_URL_'])
                elif values['Radio_2'] == True:
                    f = open("./shopify_login.txt", "r")
                    username = f.readline().strip()
                    password = f.readline().strip()
                    site_url = f.readline().strip()

                import_coupons.import_coupons(discount_amt, minimum_spending, date_start, time_start, date_end, time_end, coupon_csv, site_url, username, password)

except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened. Here is the info:', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)