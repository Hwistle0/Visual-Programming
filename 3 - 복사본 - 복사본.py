import math
def cal_tp(j):
    global city
    city_temp=0
    city_pre=0
    city_temp+=city[3*j+1]
    city_pre+=city[3*j+2]
    return city_temp,city_pre
        
def cal():
    global city
    city_len=len(city)
    k=math.floor(city_len/3)
    city_m_avr=[]
    for i in range(0,k):
        if '-01-' in city[i*3]:
            city_temp1=0
            city_pre1=0
            city_temp1+=city[3*i+1]
            city_pre1+=city[3*i+2]
        else: 
            continue
        city_temp_avr1=city_temp1/28
        city_pre_avr1=city_pre1/28
        m1=[city_temp_avr1,city_pre_avr1]
        city_m_avr.append(m1)

        elif '-02-' in city[i*3]:
            city_temp2=0
            city_pre2=0
            city_temp2+=city[3*i+1]
            city_pre2+=city[3*i+2]
        city_temp_avr2=city_temp2/28
        city_pre_avr2=city_pre2/28
        m2=[city_temp_avr2,city_pre_avr2]
        city_m_avr.append(m2)
        elif '-03-' in city[i*3]:
            city_temp3=0
            city_pre3=0
            city_temp3+=city[3*i+1]
            city_pre3+=city[3*i+2]
        city_temp_avr3=city_temp3/28
        city_pre_avr3=city_pre3/28
        m3=[city_temp_avr3,city_pre_avr3]
        city_m_avr.append(m3)
        elif '-04-' in city[i*3]:
            city_temp4=0
            city_pre4=0
            city_temp4+=city[3*i+1]
            city_pre4+=city[3*i+2]
        city_temp_avr4=city_temp4/28
        city_pre_avr4=city_pre4/28
        m4=[city_temp_avr4,city_pre_avr4]
        city_m_avr.append(m4)
        elif '-05-' in city[i*3]:
            city_temp5=0
            city_pre5=0
            city_temp5+=city[3*i+1]
            city_pre5+=city[3*i+2]
        city_temp_avr5=city_temp5/28
        city_pre_avr5=city_pre5/28
        m5=[city_temp_avr5,city_pre_avr5]
        city_m_avr.append(m5)
        elif '-06-' in city[i*3]:
            city_temp6=0
            city_pre6=0
            city_temp6+=city[3*i+1]
            city_pre6+=city[3*i+2]
        city_temp_avr6=city_temp6/28
        city_pre_avr6=city_pre6/28
        m6=[city_temp_avr6,city_pre_avr6]
        city_m_avr.append(m6)
        elif '-07-' in city[i*3]:
            city_temp7=0
            city_pre7=0
            city_temp7+=city[3*i+1]
            city_pre7+=city[3*i+2]
        city_temp_avr7=city_temp7/28
        city_pre_avr7=city_pre7/28
        m7=[city_temp_avr7,city_pre_avr7]
        city_m_avr.append(m7)
        elif '-08-' in city[i*3]:
            city_temp8=0
            city_pre8=0
            city_temp8+=city[3*i+1]
            city_pre8+=city[3*i+2]
        city_temp_avr8=city_temp8/28
        city_pre_avr8=city_pre8/28
        m8=[city_temp_avr8,city_pre_avr8]
        city_m_avr.append(m8)
        elif '-09-' in city[i*3]:
            city_temp9=0
            city_pre9=0
            city_temp9+=city[3*i+1]
            city_pre9+=city[3*i+2]
        city_temp_avr9=city_temp9/28
        city_pre_avr9=city_pre9/28
        m9=[city_temp_avr9,city_pre_avr9]
        city_m_avr.append(m9)
        elif '-10-' in city[i*3]:
            city_temp10=0
            city_pre10=0
            city_temp10+=city[3*i+1]
            city_pre10+=city[3*i+2]
        city_temp_avr10=city_temp10/28
        city_pre_avr10=city_pre10/28
        m10=[city_temp_avr10,city_pre_avr10]
        city_m_avr.append(m10)
        elif '-11-' in city[i*3]:
            city_temp11=0
            city_pre11=0
            city_temp11+=city[3*i+1]
            city_pre11+=city[3*i+2]
        city_temp_avr11=city_temp11/28
        city_pre_avr11=city_pre11/28
        m11=[city_temp_avr11,city_pre_avr11]
        city_m_avr.append(m11)
        elif '-12-' in city[i*3]:
            city_temp12=0
            city_pre12=0
            city_temp12+=city[3*i+1]
            city_pre12+=city[3*i+2]
        city_temp_avr12=city_temp12/28
        city_pre_avr12=city_pre12/28
        m12=[city_temp_avr12,city_pre_avr12]
        city_m_avr.append(12)
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
                
   
user=input('도시를 선택하세요\n(Seoul,Busan,Daegu,Gwangju,Incheon,Daejeon,Ulsan,Gyeonggi-do,Gangwon-do,Chungcheongbuk-do,Chungcheongnam-do,Jeollabuk-do, Jeollanam-do,Gyeongsangbuk-do,Gyeongsangnam-do,Jeju-do')


city_2016=read('2016')
length_1=len(city_2016)
for a in city_2016:
    print(a)

city_2017=read('2017')
length_2=len(city_2017)
for b in range(0,length_2):
    print('2017년 %d월 %.2f %.2f'%(b+1,city_2017[b][0],city_2017[b][1]))


city_2018=read('2018')
length_3=len(city_2018)
for c in range(0,length_3):
    print('2018년 %d월 %.2f %.2f'%(c+1,city_2018[c][0],city_2018[c][1]))


city_2019=read('2019')
length_4=len(city_2019)
for d in range(0,length_4):
    print('2019년 %d월 %.2f %.2f'%(d+1,city_2019[d][0],city_2019[d][1]))


city_2020=read('2020')
length_5=len(city_2020)
for e in range(0,length_5):
    print('2016년 %d월 %.2f %.2f'%(e+1,city_2020[e][0],city_2020[e][1]))
        
f.close()
    



        
        
        
        
        

