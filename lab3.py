from re import I


list = [2019,6082360,5241460,2018,5751450,5020040,2017,5458450,4786260,2016,5205750,4550400,2015,4856460,4435530,2014,4546950,4271400,2013,4358060,4108150,2012,4252490,3892040,2011,4149300,3668849,2010,4090350,3487796,2009,3987320,3306604,2008,3891030,3122170,2007,3768420,2955814,2006,3668400,2791155,2005,3635790,2631177,2004,3596560,2480557,2003,3542880,2347628,2002,3443530,2228834,2001,3321090,2109832,2000,3198270,2013684,1999,3077790,1925483,1998,2954190,1839151,1997,2823810,1764602,1996,2687780,1694710,1995,2536730,1608438]
years=[]
elder_list = []
k = 0
for i in list:
    if i%3 == 0:
        years.append(i)
    elif i%3 == 1:
        elder_list.append(i)
    # elif i%3 == 2:
    #     elder_list[k] += i
    #     k += 1
print(years)
print(elder_list)