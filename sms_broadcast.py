import pandas as pd
import sys, getopt
from twilio.rest import Client


def main(argv):
    file, nameColumn, phoneColumn, template, sendReal, twilioSid, twilioToken, twilioFrom = parseArgs(argv)

    rows = pd.read_csv(file)
    rows = rows[[nameColumn, phoneColumn]]

    client = Client(twilioSid, twilioToken)

    for index, row in rows.iterrows():
        text = template.replace('<name>', row[nameColumn])
        phone = '+{}'.format(row[phoneColumn])
        sendSms(phone, text, sendReal, client, twilioFrom)


def sendSms(phone, text, sendReal, client, twilioFrom):
    print('Sending SMS to {}. text: {}'.format(phone, text))

    if sendReal:
        message = client.messages.create(
            to=phone,
            from_=twilioFrom,
            body=text)

        print(message.sid)


def parseArgs(argv):
    try:
        opts, args = getopt.getopt(argv, "hsf:t:n:p:i:o:r:",
                                   ["send_real", "file=", "template=", "name_column=", "phone_column=", "twilio_sid", "twilio_token", "twilio_from"])
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    file = ''
    template = ''
    nameColumn = 'Name'
    phoneColumn = 'Phone number'
    sendReal = False
    twilioSid = ''
    twilioToken = ''
    twilioFrom = ''
    for opt, arg in opts:
        if opt == '-h':
            printHelp()
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
        elif opt in ("-i", "--twilio_sid"):
            twilioSid = arg
        elif opt in ("-o", "--twilio_token"):
            twilioToken = arg
        elif opt in ("-r", "--twilio_from"):
            twilioFrom = arg
    return file, nameColumn, phoneColumn, template, sendReal, twilioSid, twilioToken, twilioFrom


def printHelp():
    print(
        'sms_broadcast.py -s -f <csv_file> -t <text_template> -n <name_column_name> ' +
        '-p <phone_number_column_name> -i <twilio_sid> -o <twilio_token> -r <twilio_from>')


if __name__ == "__main__":
    main(sys.argv[1:])
