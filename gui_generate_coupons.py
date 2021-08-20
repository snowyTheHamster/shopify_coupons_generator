import traceback
import PySimpleGUI as sg
import generate_coupons

layout = [
    [sg.Text('Exported Coupons CSV File:'), sg.Input(key='_EXPORTED_CSV_'), sg.FileBrowse()],
    [sg.Text('No. of Coupon Codes:'), sg.InputText('50', key='_COUPON_NO_', size=(15, 1))],
    [sg.Text('Length of Coupon Code:'), sg.InputText('5', key='_CODE_LENGTH_', size=(15, 1))],
    [sg.Text('Characters to Use:'), sg.InputText('ABDEFGHJMNPQRTVYZ2345678', key='_LETTERS_', size=(60, 1))],
    [sg.Text('')],
    [sg.Button("RUN", size=(10, 1), bind_return_key=True, key='_RUN_')],
    [sg.Output(size=(60, 10))],
]

window: object = sg.Window('Bulk Generate Coupon Codes', layout, element_justification='left')

try:
    while True:
        event, values = window.read()
        if event is None:
            break

        if event == '_RUN_':

            if values['_EXPORTED_CSV_'] == '' or values['_COUPON_NO_'] == '' or values['_CODE_LENGTH_'] == '' or values['_LETTERS_'] == '':
                print('None of the fields can be empty')

            else:
                exported_csv = values['_EXPORTED_CSV_']
                coupon_no = int(values['_COUPON_NO_'])
                code_length = int(values['_CODE_LENGTH_'])
                letters = str(values['_LETTERS_'])

                generate_coupons.generate_coupons(exported_csv, coupon_no, code_length, letters)

except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened. Here is the info:', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)