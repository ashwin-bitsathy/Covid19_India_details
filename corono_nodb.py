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
        id =0
        for t in tr_elements:
                    if(flag==0):
                        flag=1
                        continue
                    name=t.text_content()
                    op = str(name)
                    op = " ".join(op.split())
                    id+=1
                    x = {
                       "State":op,
                       "_id":id
                    }
                    col.append(x)
                    
        
        
        for it in col:
            if(it['_id']==ip+5):
                print("state: "+it['State'][2:-7]+'\n')
                print("Total Confirmed cases (Indian National) :"+it['State'][-7])
                print("Total Confirmed cases ( Foreign National ) :"+it['State'][-5])
                print("Cured/Discharged/Migrated :"+it['State'][-3])
                print("deaths at the State :"+it['State'][-1])
   
        
    except:
        print("Code must be debugged")
   

print("1    Andhra Pradesh")
print("2    Chhattisgarh")
print("3    Delhi")
print("4    Gujarat")
print("5    Haryana")
print("6    Himachal Pradesh")
print("7    Karnataka")
print("8    Kerala")
print("9    Madhya Pradesh")
print("10   Maharashtra")        
print("11   Odisha")
print("12   Puducherry  ")
print("13  Punjab")  
print("14  Rajasthan")   
print("15  Tamil Nadu ") 
print("16  Telengana")  
print("17  Chandigarh")  
print("18  Jammu and Kashmir ") 
print("20  Uttar Pradesh ") 
print("21  Uttarakhand") 
print("22  West Bengal \n")
i = int(input("Enter the State Id: "))
y(i)



        
            

            
        