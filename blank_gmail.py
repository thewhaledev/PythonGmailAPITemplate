from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64 #imports for message sending start here
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apiclient import errors

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["#"] #Enter scope here

#credentials function
def credentials():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

message_text="#" # The text you want to send to the recipient
subject = "#" # The subject line of the email
sender = "#" # The account that is sending the email
to = "#" # The recipient

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text, "html") #You can remove the "html" if sending plain text
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

#---------------------------------------------------------------
service = credentials()
user_id = "#" # The account sending the email
message = create_message(sender, to, subject, message_text) #create message

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError:
        print("An error occured")

send_message(service, user_id, message) #send message

#----------------------------------------------------------------
