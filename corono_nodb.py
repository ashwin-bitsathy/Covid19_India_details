import requests
import lxml.html as lh
 
def y(ip):
 
    try:
        url = 'https://www.mohfw.gov.in/'

        page = requests.get(url)

        doc = lh.fromstring(page.content)

        tr_elements = doc.xpath('//tr')

        col =[]
        
        flag = 0
        boundary =0
        h = "0123456789"

        for t in tr_elements:
                    if(flag==0):
                        flag+=1
                        continue
                    
                        
                        
                    name=t.text_content()
                    op = str(name)
                    op = " ".join(op.split())
                    if(op=="DATE TITLE"):
                        continue
                    sid = ""
                    for i in op:
                        if  i in h:
                            sid+=i
                        else:
                            break

                    for i in op:
                        if(i=='-' or i=='/'):
                            boundary =1
                    if boundary:
                        boundary=0
                        continue


                    x = {
                       "State":op,
                       "_id":sid
                    }
                    
                    
                    col.append(x)


        
        for it in col:
            if(it['_id']==ip):
                print("state: "+it['State'][2:-7]+'\n')
                print("Total Confirmed cases (Indian National) :"+it['State'][-7])
                print("Total Confirmed cases ( Foreign National ) :"+it['State'][-5])
                print("Cured/Discharged/Migrated :"+it['State'][-3])
                print("deaths at the State :"+it['State'][-1])
   
        
    except:
        print("Code must be debugged")
   

print('1 Andhra Pradesh')
print('2 Bihar ')
print('3 Chhattisgarh')
print('4 Delhi') 
print('5 Gujarat')
print('6 Haryana') 
print('7 Himachal Pradesh') 
print('8 Karnataka')
print('9 Kerala') 
print('10 Madhya Pradesh')
print('11 Maharashtra') 
print('12 Odisha') 
print('13 Puducherry') 
print('14 Punjab')
print('15 Rajasthan') 
print('16 Tamil Nadu')
print('17 Telengana')
print('18 Chandigarh') 
print('19 Jammu and Kashmir') 
print('20 Ladakh' )
print('21 Uttar Pradesh' )
print('22 Uttarakhand') 
print('23 West Bengal')
i = input("Enter the State Id: ")
y(i)



        
            

            
        
