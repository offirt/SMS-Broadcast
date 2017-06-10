import pandas as pd
import sys, getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:t:n:p:", ["file=", "template=", "name_column=", "phone_column="])
    except getopt.GetoptError:
        print('sms_broadcast.py -f <csv_file> -t <text_template> -n <name_column_name> -p <phone_number_column_name>')
        sys.exit(2)

    file = ''
    template = ''
    nameColumn = 'Name'
    phoneColumn = 'Phone number'
    for opt, arg in opts:
        if opt == '-h':
            print('sms_broadcast.py -f <csv_file> -t <text_template> -n <name_column_name> -p <phone_number_column_name>')
            sys.exit()
        elif opt in ("-f", "--file"):
            file = arg
        elif opt in ("-t", "--template"):
            template = arg
        elif opt in ("-n", "--name_column"):
            nameColumn = arg
        elif opt in ("-p", "--phone_column"):
            phoneColumn = arg

    sendSms(file, template, nameColumn, phoneColumn)


def sendSms(file, template, nameColumn, phoneColumn):
    rows = pd.read_csv(file)
    rows = rows[[nameColumn, phoneColumn]]

    print(rows)


if __name__ == "__main__":
    main(sys.argv[1:])
