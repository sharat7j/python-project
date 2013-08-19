import re
def melement(fileName,m):
    file =open(fileName,"r");
    str="";
    for line in file:
        str+=line;
        print line;
    count=len(re.findall(r'\w+', str));
    if(m<count and m!=0):
        str2=re.findall(r'\w+', str);
        theIndex={};
        for letter in str2:
            print letter;
            theIndex[count]=letter;
            count=count-1;
        print theIndex[m];
    else:
        print "m too large and cannot be zero";

            
    
        
