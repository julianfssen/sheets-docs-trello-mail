import __init__
ss = __init__.Spreadsheet('12vKZ3hVANpvvI-8eDzTg80YoCR85jIFXl8m6CGV44wU')
sheet = ss[0]

contentTitle = sheet['E12']
contentOutline = sheet['F12']
print(contentTitle)
title = contentTitle
uu = __init__.updateDoc('1oxwp7Y19OUvbQx1H4xO04yVA43kS6dZMgpIlIcz_89U', contentTitle, contentOutline)
print("Updated")
#dd = __init__.createDoc(title)
#cc = __init__.copyDoc('1Hrq6qITXuJXxofVrmV2HoD00uyBYkDXjaKAh9yAuKpg')
#body =
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

