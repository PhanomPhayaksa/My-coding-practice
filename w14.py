def CountDown(Form,to):
 ans = 0
 fm = 0
 tm = 0
 fd = 0
 td = 0
 fy = 0
 ty = 0
 jan = 0
 feb = 0
 mar = 0
 april = 0
 may = 0
 june = 0
 july = 0 
 august = 0
 sep = 0
 October = 0
 Nov = 0
 Dec = 0


 if Form[0:2].isdigit():
    fd = Form[0:2]
 else:
    fd = Form[0:1]
    return ans
 if Form[2:4].isdigit():
    fm = Form[2:4]
 else:
    fm = Form[3:5]
    return ans
 if Form[5:10].isdigit():
    fy = Form[5:10]
 else:
    fy = Form[6:10]
 if to[0:2].isdigit():
    td = to[0:2]
 else:
    td = to[0:1]
    return ans
 if to[2:4].isdigit():
    tm = to[2:4]
 else:
    tm = to[3:5]
 if to[5:10].isdigit():
    ty = to[5:10]
 else:
    ty = to[6:10]
 if fy and ty %4 == 0 and fy and ty %100 != 0:
    feb == 29
 if fy and ty %400 == 0 and fy and ty %100 == 0:
    feb == 29
 if (fd,fm,fy) != (td,tm,ty):
    


    return ans

     