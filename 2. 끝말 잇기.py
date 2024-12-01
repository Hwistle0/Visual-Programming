word=['apple']
i=0
while True:
    user=input("%s 끝말 잇기?"%word[i])
    user_len=len(user)
    if user_len>5:
        print('단어가 길어요(%s의 끝말을 이으세요)'%word[i])
    elif user_len<5:
        print('단어가 짧아요(%s의 끝말을 이으세요)'%word[i])
    else:
        f=open('dict_test.TXT','r')
        while True:
            line=f.readline()
            if not line:
                print('사전에 없는 단어입니다.(%s의 끝말을 이으세요)'%word[i])
                break
            if line =="":
                break
            if line[-1]=='\n':
                line=line[:-1]
            line_sp=line.split(':')
            line_f=line_sp[0].rstrip()
            word2=word[i]
            word_len=len(word)
            
            if user in word:
                print('중복된 단어입니다.(%s의 끝말을 이으세요)'%word[i])
                break
            else :
                if user == line_f :
                    if user[0]==word2[-1]:
                        if 'n' in line_sp[1]:
                            word.append(user)
                            i+=1
                            print('정답입니다.(%s의 끝말을 이으세요)'%word[i])
                            break
                        else :
                            print('명사가 아닙니다. (%s의 끝말을 이으세요)'%word[i])
                            break
                    elif user[0]!=word2[-1]:
                        print('삑. 끝말잇기가 안되는 단어입니다.(%s의 끝말을 이으세요)'%word[i])
                        break
            
f.close()
    
            
                    
