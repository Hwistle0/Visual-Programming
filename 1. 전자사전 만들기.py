while True:
    user=input('단어?')
    f=open('dict_test.TXT','r')
    if user=='끝':
        break
    else:
        while True:
            line=f.readline()
            if line =="":
                break
            if line[-1]=='\n':
                line=line[:-1]
            line_sp=line.split(':')
            line_sp_a=line_sp[0].rstrip()
            if user == line_sp_a:
                if line_sp[1]==' ':
                    print('')
                else :
                    print(line_sp[0],line_sp[1])

        
           
f.close()
        
