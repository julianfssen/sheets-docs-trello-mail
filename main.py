#!python3
import ezsheets
import pickle
import os.path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

ss = ezsheets.Spreadsheet('12vKZ3hVANpvvI-8eDzTg80YoCR85jIFXl8m6CGV44wU')
sheet = ss[0]

createTitle = sheet['E12']
createBody = sheet['F12']

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

title = createTitle
body = {
    'title': title
    "body": {
    "content": [
      {
        "endIndex": 1,
        "sectionBreak": {
          "sectionStyle": {
            "columnSeparatorStyle": "NONE",
            "contentDirection": "LEFT_TO_RIGHT",
            "sectionType": "CONTINUOUS"
          }
        }
      },
      {
        "startIndex": 1,
        "endIndex": 71,
        "paragraph": {
          "elements": [
            {
              "startIndex": 1,
              "endIndex": 71,
              "textRun": {
                "content": "Greenbird’s Role In Achieving the Sustainable Development Goals (SDG)\n",
                "textStyle": {}
              }
            }
          ],
          "paragraphStyle": {
            "headingId": "h.o4qxnc456sgw",
            "namedStyleType": "HEADING_1",
            "alignment": "CENTER",
            "direction": "LEFT_TO_RIGHT"
          }
        }
      }

service = build('docs', 'v1', credentials=creds)
doc = service.documents() \
    .create(body=body).execute()
print('Created document with title: {0}'.format(
    doc.get('title')))
docId = doc.get('documentId')
