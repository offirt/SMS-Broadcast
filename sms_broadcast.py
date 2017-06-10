import pandas as pd
import sys, getopt


def main(argv):
    file, nameColumn, phoneColumn, template, sendReal = parseArgs(argv)

    rows = pd.read_csv(file)
    rows = rows[[nameColumn, phoneColumn]]

    for index, row in rows.iterrows():
        text = template.replace('<name>', row[nameColumn])
        sendSms(row[phoneColumn], text, sendReal)


def sendSms(phone, text, sendReal):
    print('Sending SMS to {}. text: {}'.format(phone, text))

    # if sendReal == True:
        # Send SMS.

def parseArgs(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:t:n:p:s", ["file=", "template=", "name_column=", "phone_column=", "send_real"])
    except getopt.GetoptError:
        print('sms_broadcast.py -s -f <csv_file> -t <text_template> -n <name_column_name> -p <phone_number_column_name>')
        sys.exit(2)
    file = ''
    template = ''
    nameColumn = 'Name'
    phoneColumn = 'Phone number'
    sendReal = False
    for opt, arg in opts:
        if opt == '-h':
            print('sms_broadcast.py -s -f <csv_file> -t <text_template> -n <name_column_name> -p <phone_number_column_name>')
            sys.exit()
        elif opt in ("-s", "--send_real"):
            sendReal = True
        elif opt in ("-f", "--file"):
            file = arg
        elif opt in ("-t", "--template"):
            template = arg
        elif opt in ("-n", "--name_column"):
            nameColumn = arg
        elif opt in ("-p", "--phone_column"):
            phoneColumn = arg
    return file, nameColumn, phoneColumn, template, sendReal


if __name__ == "__main__":
    main(sys.argv[1:])
