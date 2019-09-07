vars = [3,5,7,9,10.5,'Python']
print (vars)
print (len(vars))
print (vars[0])
print (vars[-1])
print (vars[1:3])
vars.remove('Python')
print (vars)

Grad ={"city":"Moscow", "temperature":"20"}
print (Grad["city"])
Grad["temperature"]=int(Grad["temperature"]) - 5
print (Grad)
if "country" in Grad :
    print ("country already exists")
else:    
   Grad.update(country="Russia")
print (Grad)
Grad.update( {'date' : "27.05.2019"} )
print(len(Grad))