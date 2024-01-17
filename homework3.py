class cars:
    def set(self,id,name,lname,gender,brand,year,color,country):
        self.id=id
        self.name=name
        self.lname=lname
        self.gender=gender
        self.brand=brand
        self.year=year
        self.color=color
        self.country=country
    def s(self):
        list=[]
        s=int(input("Nechta ma'lumot kiritmoqchisiz: "))
        for i in range(s):
            id=int(input("\nID: "))
            name=input("Name: ")
            lname=input("Last name: ")
            gender=input("Gender: ")
            brand=input("Brand of car: ")
            year=int(input("Year: "))
            color=input("Color: ")
            country=input("Country: ")
            s1=cars()
            s1.set(id,name,lname,gender,brand,year,color,country)
            list.append(s1)
        a=0
        b=0
        c=0
        for i in list:
            if i.gender=="Male" or i.gender=="male":
               a+=1
            elif i.gender=="Female" or i.gender=="female":
                b+=1
        c=a+b
        n=(a//c)*100
        m=(b//c)*100
        print(f"Erkakalar {n} %")
        print(f"Ayollar {m} %")
        if n>m:
            print(f"Erkakalar ayollardan {n-m} % ga ko'p")
        else:
            print(f"Ayollar Erkaklardan {m-n} % ga ko'p")
        lst=[]
        w=[]
        q=[]
        for i in list:
            lst.append(i.brand)
        for i in range(len(lst)):
            q=[]
            for j in range(i+1,len(lst)):
                if lst[i]==lst[j]:
                    q.append(lst[i])
            if len(q)>len(w):
                w.append(q)
        print("Eng ko'p mashina brendi")
        for i in w:
            print(i)
        print("\n")    
        for i in list:
            if i.year<2005:
                        print(f"""\n
    Kimdan: Auto Test Corp
    Kimga: {i.name} {i.lname}
    Joriy Davlat: {i.country}
Hurmatli {i.name} {i.lname} sizning {i.brand} tomonidan {i.year} da 
ishlab chiqarilgan {i.color} rangli avtomabilingizni Texnik holatini 
tekshirish maqsadida mahalliy Auto Test Corp ofisiga murojat qiling.
""")
s=cars()
s.s()