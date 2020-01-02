#!python3
import ezsheets
import pickle
import os.path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials-docs.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
ss = ezsheets.Spreadsheet('12vKZ3hVANpvvI-8eDzTg80YoCR85jIFXl8m6CGV44wU')
sheet = ss[0]

contentTitle = sheet['E12']
contentOutline = sheet['F12']

title = contentTitle
body = {
    'title': title
}
drive_response = drive_service.files().copy(
    fileId=document_id, body=body).execute()
document_copy_id = drive_response.get('1Hrq6qITXuJXxofVrmV2HoD00uyBYkDXjaKAh9yAuKpg')
service = build('docs', 'v1', credentials=creds)
doc = service.documents() \
    .create(body=body).execute()
print('Created document with title: {0}'.format(
    doc.get('title')))
docId = doc.get('documentId')

requests = [
        {
        'insertText': {
            'location': {
                'index': 1
            },
            'text': contentOutline
        }
    }#,
    #{
    #    'updateTextStyle': {
    #        'range': {
    #            'startIndex': 1,
    #            'endIndex': 66
    #        },
    #        'textStyle': {
    #            'bold': True
    #        },
    #        'fields': 'bold'
    #    }
    #}
]

result = service.documents().batchUpdate(
    documentId=docId, body={'requests': requests}).execute()


