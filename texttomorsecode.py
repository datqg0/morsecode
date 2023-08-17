#initial data
morse =[""]*366
dictmorse={}
morse[65]=".-"
morse[66]="-..."
morse[67]="-.-."
morse[68]="-.."
morse[69]="."
morse[70]="..-."
morse[71]="--."
morse[72]="...."
morse[73]=".."
morse[74]=".---"
morse[75]="-.-"
morse[76]=".-.."
morse[77]="--"
morse[78]="-."
morse[79]="---"
morse[80]=".--."
morse[81]="--.-"
morse[82]=".-."
morse[83]="..."
morse[84]="-"
morse[85]="..-"
morse[86]="...-"
morse[87]=".--"
morse[88]="-..-"
morse[89]="-.--"
morse[97]=".-"
morse[98]="-..."
morse[99]="-.-."
morse[100]="-.."
morse[101]="."
morse[102]="..-."
morse[103]="--."
morse[104]="...."
morse[105]=".."
morse[106]=".---"
morse[107]="-.-"
morse[108]=".-.."
morse[109]="--"
morse[110]="-."
morse[111]="---"
morse[112]=".--."
morse[113]="--.-"
morse[114]=".-."
morse[115]="..."
morse[116]="-"
morse[117]="..-"
morse[118]="...-"
morse[119]=".--"
morse[120]="-..-"
morse[121]="-.--"
morse[122]="--.."
morse[48]="-----"
morse[49]=".----"
morse[50]="..---"
morse[51]="...--"
morse[52]="....-"
morse[53]="....."
morse[54]="-...."
morse[55]="--..."
morse[56]="---.."
morse[57]="----."
morse[46]=".-.-.-"
morse[44]="--..--"
morse[63]="..--.."
morse[39]=".----."
morse[33]="-.-.--"
morse[47]="-..-."
morse[40]="-.--."
morse[41]="-.--.-"
morse[38]=".-..."
morse[58]="---..."
morse[59]="-.-.-."
morse[61]="-...-"
morse[43]=".-.-."
morse[45]="-....-"
morse[95]="..--.-"
morse[34]=".-..-."
morse[36]="...-..-"
morse[64]=".--.-."
morse[61]="-...-"
morse[224]=".--.-"
morse[228]=".-.-"
morse[229]=".--.-"
morse[261]=".-.-"
morse[230]=".-.-"
morse[263]="-.-.."
morse[265]="-.-.."
morse[231]="-.-.."
morse[273]="..-.."
morse[240]="..--."
morse[233]="..-.."
morse[232]=".-..-"
morse[281]="..-.."
morse[285]="--.-."
morse[293]="----"
morse[309]=".---."
morse[322]=".-..-"
morse[324]="--.--"
morse[241]="--.--"
morse[243]="---."
morse[246]="---."
morse[248]="---."
morse[347]="...-..."
morse[349]="...-."
morse[353]="----"
morse[254]=".--.."
morse[252]="..--"
morse[365]="..--"
for i in range (366):
    if(len(morse[i])>0):
        dictmorse[str(morse[i])]=i

def decode():
    print ("write your text: ")
    s=input()
    print("Your decode is :")
    for i in range (len(s)):
        if(s[i]==' ') :
            print("/",end="")
        elif(i!=len(s)-1):
            print (morse[ord(s[i])],end=" ")
        else:
            print(morse[ord(s[i])])
    print ("DONE")
def translatecode():
    print("write your code : ")
    s = input()
    print("Your text is :")
    out=""
    temp=""
    for i in range (len(s)):
        if(s[i]!=' ' and s[i]!='/'):
            temp+=s[i]
            if(i==len(s)-1):
                out=out+str(chr(dictmorse[temp]))
                temp = ""
        elif(s[i]==' ' and (len(temp))>0):
            out = out + str(chr(dictmorse[temp]))
            temp=""
        if(s[i]=='/'):
            out+=' '
    print(out)
    print("DONE")
print ("1: Text to Code")
print ("2: Code to Text")
typ= int(input())
if (typ==1):
    decode()
else:
    translatecode()