import math
def cal_tp(j):
    global city
    city_temp=0
    city_pre=0
    city_temp+=city[3*j+1]
    city_pre+=city[3*j+2]
    city_temp_avr=city_temp/28
    city_pre_avr=city_pre/28
    m=[city_temp_avr,city_pre_avr]
    return m
        
def cal():
    global city
    city_len=len(city)
    k=math.floor(city_len/3)
    city_m_avr=[]
    for i in range(0,k):
        if '-01-' in city[i*3]:
            m1=cal_tp(i)
            city_m_avr.append(m1)
        elif '-02-' in city[i*3]:
            m2=cal_tp(i)
            city_m_avr.append(m2)
        elif '-03-' in city[i*3]:
            m3=cal_tp(i)
            city_m_avr.append(m3)
        elif '-04-' in city[i*3]:
            m4=cal_tp(i)
            city_m_avr.append(m4)
        elif '-05-' in city[i*3]:
            m5=cal_tp(i)
            city_m_avr.append(m5)
        elif '-06-' in city[i*3]:
            m6=cal_tp(i)
            city_m_avr.append(m6)
        elif '-07-' in city[i*3]:
            m7=cal_tp(i)
            city_m_avr.append(m7)
        elif '-08-' in city[i*3]:
            m8=cal_tp(i)
            city_m_avr.append(m8)
        elif '-09-' in city[i*3]:
            m9=cal_tp(i)
            city_m_avr.append(m9)
        elif '-10-' in city[i*3]:
            m10=cal_tp(i)
            city_m_avr.append(m10)
        elif '-11-' in city[i*3]:
            m11=cal_tp(i)
            city_m_avr.append(m11)
        elif '-12-' in city[i*3]:
            m12=cal_tp(i)
            city_m_avr.append(m12)
    return city_m_avr

        
def read(year):
    global user
    global city
    global f
    city=[]

    f=open('Weather.csv','r')
    while True:
        f.readline()
        v=f.readline()
        if not v:
            break
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
    city_year=cal()
    return city_year
                
   
user=input('도시를 선택하세요\n(Seoul,Busan,Daegu,Gwangju,Incheon,Daejeon,Ulsan,Gyeonggi-do,Gangwon-do,Chungcheongbuk-do,Chungcheongnam-do,Jeollabuk-do, Jeollanam-do,Gyeongsangbuk-do,Gyeongsangnam-do,Jeju-do)')


city_2016=read('2016')
length_1=len(city_2016)
for a in range(12):
    print('2016년 %d월 %.2f %.2f'%(a+1,city_2016[a][0],city_2016[a][1]))

city_2017=read('2017')
length_2=len(city_2017)
for b in range(12):
    print('2017년 %d월 %.2f %.2f'%(b+1,city_2017[b][0],city_2017[b][1]))


city_2018=read('2018')
length_3=len(city_2018)
for c in range(12):
    print('2018년 %d월 %.2f %.2f'%(c+1,city_2018[c][0],city_2018[c][1]))


city_2019=read('2019')
length_4=len(city_2019)
for d in range(12):
    print('2019년 %d월 %.2f %.2f'%(d+1,city_2019[d][0],city_2019[d][1]))


city_2020=read('2020')
length_5=len(city_2020)
for e in range(4):
    print('2016년 %d월 %.2f %.2f'%(e+1,city_2020[e][0],city_2020[e][1]))
        
f.close()
    



        
        
        
        
        

