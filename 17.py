import sys
import math

idx = {}
idx[1]=3
idx[2]=3
idx[3]=5
idx[4]=4
idx[5]=4
idx[6]=3
idx[7]=5
idx[8]=5
idx[9]=4
idx[10]=3
idx[11]=6
idx[12]=6
idx[13]=8
idx[14]=8
idx[15]=7
idx[16]=7
idx[17]=9
idx[18]=8
idx[19]=8
idx[20]=6
idx[21]=9
idx[22]=9
idx[23]=11
idx[24]=10
idx[25]=10
idx[26]=9
idx[27]=11
idx[28]=11
idx[29]=10
idx[30]=6
idx[31]=9
idx[32]=9
idx[33]=11
idx[34]=10
idx[35]=10
idx[36]=9
idx[37]=11
idx[38]=11
idx[39]=10
idx[40]=5
idx[41]=8
idx[42]=8
idx[43]=10
idx[44]=9
idx[45]=9
idx[46]=8
idx[47]=10
idx[48]=10
idx[49]=9
idx[50]=5
idx[51]=8
idx[52]=8
idx[53]=10
idx[54]=9
idx[55]=9
idx[56]=8
idx[57]=10
idx[58]=10
idx[59]=9
idx[60]=5
idx[61]=8
idx[62]=8
idx[63]=10
idx[64]=9
idx[65]=9
idx[66]=8
idx[67]=10
idx[68]=10
idx[69]=9
idx[70]=7
idx[71]=10
idx[72]=10
idx[73]=12
idx[74]=11
idx[75]=11
idx[76]=10
idx[77]=12
idx[78]=12
idx[79]=11
idx[80]=6
idx[81]=9
idx[82]=9
idx[83]=11
idx[84]=10
idx[85]=10
idx[86]=9
idx[87]=11
idx[88]=11
idx[89]=10
idx[90]=6
idx[91]=9
idx[92]=9
idx[93]=11
idx[94]=10
idx[95]=10
idx[96]=9
idx[97]=11
idx[98]=11
idx[99]=10
idx[100]=10

def callength(value):
    global idx
    if value == 1000:
        return 11
    elif value > 100:   
        if(value % 100) == 0:
            return idx[int(value / 100)] + 7
        else:
            return idx[int(value / 100)] + 7 + 3 + callength(value % 100)
    else:
        return idx[value]
buf = 0
for x in range(1, 1001):
    buf += callength(x)
    
print(buf)