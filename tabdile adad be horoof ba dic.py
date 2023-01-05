def dawsh(number):
    khorooji=''
    number=str(number)
    #1-9
    if int(number)<10 and int(number)>=1:
        yekan=int(number[0])
        yekan_dic={"0":"","1":"one","2":"two","3":"three","4":"four","5":"five",
        "6":"six","7":"seven","8":"eight","9":"nine"}
    
        for yek in yekan_dic:
            if str(yekan)==yek:
                khorooji+=yekan_dic.get(yek)
        return khorooji
    #10-99
    elif int(number)<100 and int(number)>=10:
        #dahgan
        if int(number[0])>=2:
            dahgan=int(number[0])
            dahgan_dic={"2":"twenty","3":"thirty","4":"forty","5":"fifty",
            "6":"sixty","7":"seventy","8":"eighty","9":"ninety"}
    
            for dah in dahgan_dic:
                if str(dahgan)==dah:
                    khorooji+=dahgan_dic.get(dah)+" "
            yekan=int(number[1])
            yekan_dic={"0":"","1":"one","2":"two","3":"three","4":"four","5":"five",
            "6":"six","7":"seven","8":"eight","9":"nine"}
    
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji
    
        elif int(number[0])==1:
            yekan=int(number[1])
            yekan_dic={"0":"ten","1":"eleven","2":"twelve","3":"thirteen","4":"fourteen","5":"fifteen",
            "6":"sixteen","7":"seventeen","8":"eighteen","9":"nineteen"}
    
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji
        
        elif int(number[0])==0:
            yekan=int(number[1])
            yekan_dic={"0":"","1":"one","2":"two","3":"three","4":"four","5":"five",
            "6":"six","7":"seven","8":"eight","9":"nine"}
    
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji
    
    #100-999
    elif int(number)<1000 and int(number)>=100:
        #sagan
        sadgan=int(number[0])
        sadgan_dic={"0":"","1":"one hundred","2":"two hundred","3":"three hundred","4":"four hundred","5":"five hundred",
        "6":"six hundred","7":"seven hundred","8":"eight hundred","9":"nine hundred"}
        
        for sad in sadgan_dic:
            if str(sadgan)==sad:
                khorooji+=sadgan_dic.get(sad)+" "
        
        if int(number[1])>=2:
            dahgan=int(number[1])
            dahgan_dic={"2":"twenty","3":"thirty","4":"forty","5":"fifty",
            "6":"sixty","7":"seventy","8":"eighty","9":"ninety"}
        
            for dah in dahgan_dic:
                if str(dahgan)==dah:
                    khorooji+=dahgan_dic.get(dah)+" "
            yekan=int(number[2])
            yekan_dic={"0":"","1":"one","2":"two","3":"three","4":"four","5":"five",
            "6":"six","7":"seven","8":"eight","9":"nine"}
        
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji
        
        elif int(number[1])==1:
            yekan=int(number[2])
            yekan_dic={"0":"ten","1":"eleven","2":"twelve","3":"thirteen","4":"fourteen","5":"fifteen",
            "6":"sixteen","7":"seventeen","8":"eighteen","9":"nineteen"}
            
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji
        
        elif int(number[1])==0:
            yekan=int(number[2])
            yekan_dic={"0":"","1":"one","2":"two","3":"three","4":"four","5":"five",
            "6":"six","7":"seven","8":"eight","9":"nine"}
            
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji
    # 1000-9999
    elif int(number)>=1000:
        hezargan=int(number[0])
        hezargan_dic={"1":"one thousand","2":"two thousand","3":"three thousand","4":"four thousand","5":"five thousand",
        "6":"six thousand","7":"seven thousand","8":"eight thousand","9":"nine thousand"}
        
        for hezar in hezargan_dic:
            if str(hezargan)==hezar:
                khorooji+=hezargan_dic.get(hezar)+" "
        
        #sadgan

        sadgan=int(number[1])
        sadgan_dic={"0":"","1":"one hundred","2":"two hundred","3":"three hundred","4":"four hundred","5":"five hundred",
        "6":"six hundred","7":"seven hundred","8":"eight hundred","9":"nine hundred"}
        
        for sad in sadgan_dic:
            if str(sadgan)==sad:
                if sad!='0':
                    khorooji+=sadgan_dic.get(sad)+" "

        if int(number[2])>=2:
            dahgan=int(number[2])
            dahgan_dic={"2":"twenty","3":"thirty","4":"forty","5":"fifty",
            "6":"sixty","7":"seventy","8":"eighty","9":"ninety"}
            
            for dah in dahgan_dic:
                if str(dahgan)==dah:
                    khorooji+=dahgan_dic.get(dah)+" "
            yekan=int(number[3])
            yekan_dic={"0":"","1":"one","2":"two","3":"three","4":"four","5":"five",
            "6":"six","7":"seven","8":"eight","9":"nine"}
            
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji

        elif int(number[2])==1:
            yekan=int(number[3])
            yekan_dic={"0":"ten","1":"eleven","2":"twelve","3":"thirteen","4":"fourteen","5":"fifteen",
            "6":"sixteen","7":"seventeen","8":"eighteen","9":"nineteen"}
            
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji

        elif int(number[2])==0:
            yekan=int(number[3])
            yekan_dic={"0":"","1":"one","2":"two","3":"three","4":"four","5":"five",
            "6":"six","7":"seven","8":"eight","9":"nine"}
            
            for yek in yekan_dic:
                if str(yekan)==yek:
                    khorooji+=yekan_dic.get(yek)
            return khorooji

# number=4512

number=int(input('please enter an integer between 1 and 9999: '))
print(dawsh(number))