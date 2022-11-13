# with open('index.html','r') as webpage:
#     with open('output.txt','a') as wf:
#         for line in webpage.readlines():
#             if '<a href=' in line:
#                 pos = line.find('<a href=')
#                 first_quate = line.find('\"',pos)
#                 second_quate = line.find('\"',first_quate+1)
#                 url = line[first_quate+1:second_quate]
#                 wf.write(url + '\n')


with open('index.html','r') as webpage:
    with open('output2.txt','a') as wf:
        page = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_quate = page.find('\"',pos)
                second_quate =page.find('\"',first_quate +1)
                url = page[first_quate+1:second_quate]
                wf.write(url + '\n')
                page = page[second_quate:]
