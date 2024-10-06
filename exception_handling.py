try:
    num=int(input("Enter the Numerator:"))
    den=int(input("Enter the denominator:"))
    result=num/den
    print(result)
except ValueError as e:
    print(e)  
except ZeroDivisionError:
    print("Denominator can't be zero..") 
except Exception:
    print("Some exception caught..")
finally:
    print("Anyways i execute.")    
print("varattaaaa...")
    

