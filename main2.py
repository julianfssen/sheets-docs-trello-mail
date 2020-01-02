import __init__
ss = __init__.Spreadsheet('12vKZ3hVANpvvI-8eDzTg80YoCR85jIFXl8m6CGV44wU')
sheet = ss[0]

contentTitle = sheet['E12']
contentOutline = sheet['F12']
print(contentTitle)
title = contentTitle
dd = __init__.createDoc(title)
#body = {
#    'title': title
#}
#doc = service.documents() \
#    .create(body=body).execute()
#print('Created document with title: {0}'.format(
#    doc.get('title')))
#
#requests = [
#        {
#        'insertText': {
#            'location': {
#                'index': 1
#            },
#            'text': contentOutline
#        }
#    }#,
#    #{
#    #    'updateTextStyle': {
#    #        'range': {
#    #            'startIndex': 1,
#    #            'endIndex': 66
#    #        },
#    #        'textStyle': {
#    #            'bold': True
#    #        },
#    #        'fields': 'bold'
#    #    }
#    #}
#]
#
#result = __init__.service.documents().batchUpdate(
#    documentId=docId, body={'requests': requests}).execute()
#

