








##you can create a MySQL database in the local system using MySQL workbench and connect it using root user name and password 


# from flask import Flask
# import mysql.connector
# from twilio.rest import Client
# from urllib.parse import urlparse, parse_qsl

# app = Flask(__name__)

# # Function to fetch phone number and destination account
# def get_phone_number(target_license_plate):
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="enter_your_password",
#         database="enter_db_name"
#     )
#     cursor = db.cursor()
    
#     query = "SELECT phno, Amount FROM tollgate_dataset WHERE `LicensePlate` = %s"
#     cursor.execute(query, (target_license_plate,))
#     result = cursor.fetchone()
    
#     cursor.close()
#     db.close()
    
#     if result:
#         return result[0], result[1]
#     return None, None


# # Function to generate UPI payment link
# def generate_upi_payment_link(license_plate, Amount):
#     upi_link = f"https://linkpayment.netlify.app/index?pa=enter_your_upi_id&pn=enter_name_here&cu=INR&am={amount}&lp={license_plate}"
#     return upi_link


# def update_payment_status(upi_link):
#     # Extract the license plate from the UPI payment link
#     license_plate = parse_query(upi_link)
    
#     # Update the payment status in the database
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="akdadmin@146",
#         database="tollgate_db"
#     )
#     cursor = db.cursor()
    
#     query = "UPDATE tollgate_dataset SET TransactionStatus = 'success' WHERE `LicensePlate` = %s"
#     cursor.execute(query, (license_plate,))
    
#     db.commit()
#     cursor.close()
#     db.close()

# def parse_query(url):
#     """Parse the query string of a URL and return a dictionary of the parameters."""
#     query_string = urlparse(url).query
#     query_dict = dict(parse_qsl(query_string))
#     if 'lp' in query_dict:
#             return query_dict['lp']
#     else:
#         return None
#     #return query_dict



# # Function to send UPI payment link via Twilio SMS
# def send_upi_payment_link(phone_number, upi_link):
    # account_sid = "enter-the-account_sid-from-twilio-account"
    # auth_token = "enter-the-auth_token-from-twilio-account"
#     # twilio_phone_number = "your_twilio_phone_number"
    
#     client = Client(account_sid, auth_token)
    
#     try:
#         message = client.messages.create(
#             body=upi_link,
#             from_="enter-number-got-from-twilio",
#             to=phone_number
#         )
#         print(f"UPI Payment link sent successfully to {phone_number}. SID: {message.sid}")
#         update_payment_status(upi_link)
#     except Exception as e:
#         print(f"Failed to send UPI Payment : {str(e)}")

# @app.route('/send_payment_link/<license_plate>', methods=['GET'])
# def send_payment_link(license_plate):
#     phone_number, Amount = get_phone_number(license_plate)
#     if phone_number:
#         upi_link = generate_upi_payment_link(license_plate, Amount)
#         send_upi_payment_link(phone_number, upi_link)
#         # Update the payment status in the database
#         update_payment_status(license_plate)
#         return f'UPI Payment link sent successfully to {phone_number}. Amount: {Amount}.'
#     else:
#         return 'License plate not found.'

# if __name__ == '__main__':
#     app.run()






## or you can export that database into a .csv file and connect to that 





from flask import Flask
import pandas as pd
from twilio.rest import Client
from urllib.parse import urlparse, parse_qsl

app = Flask(__name__)

# Path to the CSV file
CSV_FILE_PATH = 'TollGate_dataset.csv'

# Function to fetch phone number and destination account from CSV
def get_phone_number(target_license_plate):
    df = pd.read_csv(CSV_FILE_PATH)
    row = df[df['LicensePlate'] == target_license_plate]
    
    if not row.empty:
        phone_number = str(row.iloc[0]['phno'])
        amount = row.iloc[0]['Amount']

# Ensure the phone number has the country code
        if not phone_number.startswith("+91"):
            phone_number = "+91" + str(phone_number)
        return phone_number, amount
    return None, None

# Function to generate UPI payment link
def generate_upi_payment_link(license_plate, amount):
    #i deployed it in netlify 
    upi_link = f"https://linkpayment.netlify.app/index?pa=enter_your_upi_id&pn=enter_name_here&cu=INR&am={amount}&lp={license_plate}"
    return upi_link

def update_payment_status(upi_link):
    # Extract the license plate from the UPI payment link
    license_plate = parse_query(upi_link)
    
    # Load CSV data
    df = pd.read_csv(CSV_FILE_PATH)
    
    # Update the payment status in the DataFrame
    df.loc[df['LicensePlate'] == license_plate, 'TransactionStatus'] = 'success'
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv(CSV_FILE_PATH, index=False)

def parse_query(url):
    """Parse the query string of a URL and return the license plate."""
    query_string = urlparse(url).query
    query_dict = dict(parse_qsl(query_string))
    return query_dict.get('lp', None)

# Function to send UPI payment link via Twilio SMS
def send_upi_payment_link(phone_number, upi_link):
    account_sid = "enter-the-account_sid-from-twilio-account"
    auth_token = "enter-the-auth_token-from-twilio-account"
    
    client = Client(account_sid, auth_token)
    
    try:
        message = client.messages.create(
            body=upi_link,
            from_="enter-number-got-from-twilio",
            to=phone_number
        )
        print(f"UPI Payment link sent successfully to {phone_number}. SID: {message.sid}")
        update_payment_status(upi_link)
    except Exception as e:
        print(f"Failed to send UPI Payment link: {str(e)}")

@app.route('/send_payment_link/<license_plate>', methods=['GET'])
def send_payment_link(license_plate):
    phone_number, amount = get_phone_number(license_plate)
    if phone_number:
        upi_link = generate_upi_payment_link(license_plate, amount)
        send_upi_payment_link(phone_number, upi_link)
        return f'UPI Payment link sent successfully to {phone_number}. Amount: {amount}.'
    else:
        return 'License plate not found.'

if __name__ == '__main__':
    app.run()
