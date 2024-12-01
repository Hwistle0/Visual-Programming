
def cal_tp(city):
    city_temp+=city[3*i+1]
    city_pre+=city[3*i+2]
    j+=1
    city_temp_avr=city_temp/28
    city_pre_avr=city_pre/38
    m=[city_temp_avr,city_pre_avr]
    return m
        
def cal(city):
    city_len=len(city)
    city_m_avr=[]
    for i in range(0,city_len):
        if '-01-' in city[i*3]:
            m1=cal_tp(city)
            city_m_avr.append(m1)
        elif '-02-' in city[i*3]:
            m2=cal_tp(city)
            city_m_avr.append(m2)
        elif '-03-' in city[i*3]:
            m3=cal_tp(city)
            city_m_avr.append(m3)
        elif '-04-' in city[i*3]:
            m4=cal_tp(city)
            city_m_avr.append(m4)
        elif '-05-' in city[i*3]:
            m5=cal_tp(city)
            city_m_avr.append(m5)
        elif '-06-' in city[i*3]:
            m6=cal_tp(city)
            city_m_avr.append(m6)
        elif '-07-' in city[i*3]:
            m7=cal_tp(city)
            city_m_avr.append(m7)
        elif '-08-' in city[i*3]:
            m8=cal_tp(city)
            city_m_avr.append(m8)
        elif '-09-' in city[i*3]:
            m9=cal_tp(city)
            city_m_avr.append(m9)
        elif '-10-' in city[i*3]:
            m10=cal_tp(city)
            city_m_avr.append(m10)
        elif '-11-' in city[i*3]:
            m11=cal_tp(city)
            city_m_avr.append(m11)
        elif '-12-' in city[i*3]:
            m12=cal_tp(city)
            city_m_avr.append(m12)
        return city_m_avr

        
def a(year):
    while True:
        f.readline()
        v=f.readline()
        if not v:break
        if v =="":
            break
        if v[-1]=='\n':
            v=v[:-1]
        s=v.split(',')
        if user == s[1]:
            if year in s[2]:
                city.append(s[2])
                city.append(float(s[3]))
                city.append(float(s[6]))
    city_2016=cal(city)
    return city_2016
                
city=[]    
user=input('도시를 선택하세요')
f=open('Weather.csv','r')

city_2016=a('2016')
for a in range(0,12):
    print('2016년 %d월 3%d 3%d'%(a+1,city_2016[a][0],city_2016[a][1])

city_2017=a('2017')
for a in range(0,12):
    print('2017년 %d월 3%d 3%d'%(a+1,city_2017[a][0],city_2017[a][1])

city_2018=a('2018')
for a in range(0,12):
    print('2018년 %d월 3%d 3%d'%(a+1,city_2018[a][0],city_2018[a][1])

city_2019=a('2019')
for a in range(0,12):
    print('2019년 %d월 3%d 3%d'%(a+1,city_2019[a][0],city_2019[a][1])

city_2020=a('2020')
for a in range(0,4):
    print('2016년 %d월 3%d 3%d'%(a+1,city_2020[a][0],city_2020[a][1])
    


    while True:
        f.readline()
        v=f.readline()
        if not v:break
        if v =="":
            break
        if v[-1]=='\n':
            v=v[:-1]
        s=v.split(',')
        if user == s[1]:
            if '2017' in s[2]:
                city.append(s[2])
                city.append(float(s[3]))
                city.append(float(s[6]))
    city_2017=cal(city)
    for a in range(0,12):
        print('2017년 %d월 3%d 3%d'%(a+1,city_2017[a][0],city_2017[a][1])


    while True:
        f.readline()
        v=f.readline()
        if not v:break
        if v =="":
            break
        if v[-1]=='\n':
            v=v[:-1]
        s=v.split(',')
        if user == s[1]:
            if '2018' in s[2]:
                city.append(s[2])
                city.append(float(s[3]))
                city.append(float(s[6]))
    city_2018=cal(city)
    for a in range(0,12):
        print('2018년 %d월 3%d 3%d'%(a+1,city_2018[a][0],city_2018[a][1])
    


    while True:
        f.readline()
        v=f.readline()
        if not v:break
        if v =="":
            break
        if v[-1]=='\n':
            v=v[:-1]
        s=v.split(',')
        if user == s[1]:
            if '2019' in s[2]:
                city.append(s[2])
                city.append(float(s[3]))
                city.append(float(s[6]))
    city_2019=cal(city)
    for a in range(0,12):
        print('2019년 %d월 3%d 3%d'%(a+1,city_2019[a][0],city_2019[a][1])

    while True:
        f.readline()
        v=f.readline()
        if not v:break
        if v =="":
            break
        if v[-1]=='\n':
            v=v[:-1]
        s=v.split(',')
        if user == s[1]:
            if '2020' in s[2]:
                city.append(s[2])
                city.append(float(s[3]))
                city.append(float(s[6]))
    city_2020=cal(city)
    for a in range(0,):
        print('2020년 %d월 3%d 3%d'%(a+1,city_2020[a][0],city_2020[a][1])

    
f.close()
    



        
        
        
        
        

