day=int(input('Enter Day :'))
month=int(input('Enter Month :'))
year=int(input('Enter Year :'))


if day<=27 and month<=12:
    day=day+1
    print(day,month,year)
elif day==28:
    if month==2:
        if year%4==0 and year%100!=0:
            day=day+1
            print(day,month,year)
        elif year%100==0:
            day=1
            month=month+1
            print(day,month,year)
        elif year%400==0:
            day=day+1
            print(day,month,year)
        else:
            day=1
            month=month+1
            print(day,month,year)    
    else:
        day=day+1
        print(day,month,year)
elif day==29:
    if month==2:
        if year%4==0 and year%100!=0:
            day=1
            month=month+1
            print(day,month,year)
        elif year%100==0:
            print("not possible")
            
        elif year%400==0:
            day=1
            month=month+1
            print(day,month,year)
        else:
            print("not possible")
    else:
        day=day+1
        print(day,month,year)
   
elif day==30:
    if month==4 or month==6 or month==9 or month==11:
        day=1
        month=month+1
        print(day,month,year)
    else:
        day=day+1
        print(day,month,year)
elif day==31:
    if month==12:
        day=1
        month=1
        year=year+1
        print(day,month,year)
        print("Wish You A Happy New Year")
    else:
        day=1
        month=month+1
        print(day,month,year)
else:
    print("Invalid")
