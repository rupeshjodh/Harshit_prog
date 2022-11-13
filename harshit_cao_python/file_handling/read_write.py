with open('f2.txt','r') as rf:
    with open('f1.txt','w') as wf:
        wf.write(rf.read())