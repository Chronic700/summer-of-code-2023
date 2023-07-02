from rt import RandomForest
from rt import phone_data
import random
import warnings
warnings.simplefilter(action='ignore',category=RuntimeWarning)


Our_forest=RandomForest(phone_data,800)
print()
print('==============================================================')
print('Initiating program, this may take a few minutes')
print('==============================================================')
Our_forest.forest_maker()

company_id={'adcom': 0, 'alcatel': 1, 'angage': 2, 'apple': 3, 'blackbear': 4, 'blackzone': 5, 'coolpad': 6, 'detel': 7, 'easyfone': 8, 'forme': 9, 'geotel': 10, 'gfive': 11, 'gionee': 12, 'good': 13, 'google': 14, 'grabo': 15, 'greenberri': 16, 'greenberry': 17, 'honor': 18, 'huawei': 19, 'ikall': 20, 'infinix': 21, 'iqoo': 22, 'ismart': 23, 'itel': 24, 'jio': 25, 'jivi': 26, 'karbonn': 27, 'kechaoda': 28, 'kxd': 29, 'lava': 30, 'lg': 31, 'marq': 32, 'mi': 33, 'micromax': 34, 'moto': 35, 'motorola': 36, 'mtr': 37, 'mu': 38, 'muphone': 39, 'nokia': 40, 'oppo': 41, 'panasonic': 42, 'philips': 43, 'poco': 44, 'realme': 45, 'redmi': 46, 'rokea': 47, 'salora': 48, 'samsung': 49, 'snexian': 50, 'ssky': 51, 'tecno': 52, 'tork': 53, 'uismart': 54, 'vivo': 55}
model_id={'a115': 0, '5v': 1, 'a310': 2, 'a312': 3, 'iphone11': 4, 'iphone12': 5, 'iphone7plus': 6, 'iphonese': 7, 'iphonexr': 8, 'iphone12promax': 9, 'iphone11pro': 10, 'iphone12pro': 11, 'a1penphone': 12, 'i7trio': 13, 'b310': 14, 'ecox': 15, 'hammer': 16, 'porsche911': 17, 's13': 18, 'shine': 19, 'turbo353': 20, 'mega5s': 21, 'd1guru': 22, 'marvel': 23, 'duosn2': 24, 'duos1900': 25, 'n1': 26, 'rocket': 27, 'k9flip': 28, 'a1': 29, 'a2': 30, 'i1': 31, 'i2': 32, 'u106': 33, 'u220combooftwo': 34, 'u220+': 35, 'u229': 36, 'u707': 37, 'f8neo': 38, 'max': 39, 'f11': 40, 'maxpro': 41, 'one5605': 42, 'oneg2mini': 43, 'onemagic': 44, 'pixel4a': 45, '220': 46, 'eluga': 47, 'g106': 48, 'g310vibration': 49, 'g312': 50, 'hulk': 51, 'nord': 52, 'f1': 53, 'm2mini': 54, '20': 55, 'y9prime2019': 56, 'k4': 57, 'k6': 58, 'k18new': 59, 'k38plus': 60, 'k444': 70, 'k48': 62, 'k666': 63, 'k130new': 64, 'k14new': 65, 'k2180': 66, 'k22': 67, 'k33new': 68, 'k3312': 69, 'k50': 71, 'k666+': 72, 'k1000': 73, 'k220': 74, 'k400': 75, 'hot10': 76, 'note7': 77, 'smart4plus': 78, 'smart5': 79, 'smarthd2021': 80, 'zero8i': 81, 's5pro': 82, 'hot9': 83, 'hot9pro': 84, '3': 85, 'i1supreme': 86, 'a48': 87, 'ace': 88, 'it2163': 91, 'it2161': 90, 'it2173': 92, 'it5026': 93, 'it5260': 94, 'it5607': 95, 'it5618n': 96, 'magic2max': 97, 'muzik400': 98, 'power110': 99, 'power400': 100, 'power410': 101, 'u10': 102, 'a25pro': 103, 'vision1': 104, 'vision1pro': 105, 'f320b': 106, 'jiophone': 107, '12m-xl': 108, 'n300new': 109, 'x57iselfie': 110, 'kphone1': 111, 'k106s': 112, 'k140pop': 113, 'k19rock': 114, 'k310n': 115, 'k7power': 116, 'k9': 117, 'k9mini': 118, 'k9power': 119, 'k-pebble': 120, 'k-stylo': 121, 'kx10i': 122, 'kx1': 123, 'kx1indian': 127, 'kx19': 125, 'kx1i': 126, 'kx23': 128, 'kx26': 129, 'kx26i': 130, 'kx3': 131, 'kx5': 132, 'a31': 237, 'a26': 134, 'a27': 135, 'a29': 136, 'k06': 137, 'k1': 138, 'k10': 139, 'k102': 140, 'k108': 141, 'k111': 142, 'k112': 143, 'k115': 144, 'k123': 145, 'k2': 146, 'k20': 147, 'k28': 148, 'k30': 149, 'k33': 150, 'k35': 151, 'k-55plus': 152, 'k60': 153, 'k66plus': 154, 'k-9': 155, 'c1': 156, 'm2+': 157, 'm3+': 158, 'p2': 159, '34plus': 160, '34ultra': 161, 'a1josh': 162, 'a1super': 163, 'a1200': 164, 'a3': 165, 'a5': 166, 'a72020': 167, 'a9': 168, 'arc22': 169, 'flip': 170, 'gem': 171, 'gemwave/gem': 172, 'h1hero600': 173, 'hero600+': 174, 'hero600s': 175, 'pulse': 176, 'pulse1': 177, 'z66': 178, 'z61pro': 179, 'k42': 180, 'byflipkart110magic': 181, '10i': 182, 'j1': 183, 'x1i-2017': 184, 'x378': 185, 'x380': 186, 'x381': 187, 'x382': 188, 'x388': 189, 'x412': 190, 'x419': 191, 'x421': 192, 'x512': 193, 'x741': 194, 'x744': 195, 'x746': 196, 'x748': 197, 'x749': 198, 'x750': 199, 'x752': 200, 'x754': 201, 'x756': 202, 'x807': 203, 'x809': 204, 'x817': 205, 'g5g': 206, 'g30': 207, 'e7power': 208, 'e7plus': 209, 'g10power': 210, 'g8powerlite': 211, 'g9': 212, 'g9power': 213, 'ferrari': 214, 'm370': 215, 'm5000': 216, 'm230': 217, 'm380': 218, '105ds': 219, '105ds2020': 220, '105ss': 221, '105ss2020': 222, '110ds2020': 223, '125ds2020': 224, '150ds2020': 225, '216ds2020': 226, '225': 227, '3310ds2020': 228, '5310ds2020': 229, 'ta-1010/105': 230, 'ta-1174/ta-1299': 231, '2.4': 232, '3.4': 233, 'a12': 234, 'a15': 235, 'a15s': 236, 'a33': 238, 'a52020': 239, 'a52': 240, 'a53': 241, 'a5s': 242, 'f15': 243, 'f17pro': 244, 'f19pro': 245, 'reno2f': 246, 'a1k': 247, 'a11k': 248, 'f17': 249, 'a92020': 250, 'f19pro+': 251, 'elugai6': 252, 'elugai7': 253, 'elugai8': 254, 'e102a': 255, 'c3': 256, 'm2': 257, 'm2pro': 258, 'm3': 259, 'x2': 260, 'x3': 261, '3i': 262, '6i': 263, 'c2': 264, 'narzo20pro': 265, 'narzo30pro5g': 266, 'narzo30a': 267, '5pro': 268, '6': 269, '7': 270, 'narzo10': 271, 'narzo10a': 272, 'x': 273, 'x3superzoom': 274, '5i': 275, '6pro': 276, '7pro': 277, '7i': 278, 'c12': 279, 'c15': 280, 'c15qualcommedition': 281, 'narzo20': 282, 'narzo20a': 283, 'x75g': 284, 'c11': 285, 'note6a': 286, 'note8': 287, 'note8a': 288, 'note9': 289, 'note9power': 290, 'note9prime': 291, 'note9a': 292, 'note9i': 293, 'notego': 294, 'note10': 295, 'note8pro': 296, 'note9pro': 297, 'note9promax': 298, 'note8adual': 299, 'note5a': 300, 'note10promax': 301, 'r222': 302, 'atom': 303, 'vishaal': 304, 'galaxya10s': 305, 'galaxya12': 306, 'galaxya21s': 307, 'galaxya31': 308, 'galaxya32': 309, 'galaxya51': 310, 'galaxyf41': 311, 'galaxym01': 312, 'galaxym02': 313, 'galaxym11': 314, 'galaxym21': 315, 'galaxym31': 316, 'galaxym51': 317, 'guru1200': 318, 'gurufmplus': 319, 'gurufmplussm-b110e/d': 320, 'gurugt': 321, 'gurumusic2': 322, 'gurumusic2sm-b310e': 323, 'm01core': 324, 'm02s': 325, 'm31prime': 326, 'metro313': 327, 'metro313dualsim': 328, 'galaxya71': 329, 'galaxyf62': 330, 'galaxym01s\xa0': 331, 'galaxym40': 332, 'm31s': 333, 'galaxym01s': 334, 'bold511': 335, 'guru312': 336, 'guru5500': 337, 'rock': 338, 's-20eco': 339, 'pova': 340, 'camon16': 341, 'spark6go': 342, 'sparkgo2020': 343, 'sparkpower2air': 344, 'camon15': 345, 'sparkpower2': 346, 'spark5pro': 347, 't13banana': 348, 't19shine': 349, 't27power': 350, 't3': 351, 'x9': 352, 'ui06': 353, 'ui-06': 354, 's1': 355, 's1pro': 356, 'v19': 357, 'v20se': 358, 'y12s': 359, 'y20': 360, 'y20g': 361, 'y30': 362, 'y31': 363, 'y91i': 364, 'z1pro': 365, 'v17pro': 366, 'y20a': 367, 'y20i': 368, 'y50': 369, 'y11': 370, 'y12': 371, 'y15': 372, 'z1x': 373, 'y51': 374, 'y51a': 375, 'v20': 376, 'v202021': 377, 'v20pro': 378}
colour_id={'black':0,'white':1,'red':2,'blue':3,'green':4,'orange':5,'violet':6,'purple':7,'grey':8,'cream':9,'yellow':10,'gold':11,'silver':12}

print()

predict=True

while predict:
    print('Enter Mobile Phone Company:',end=' ')
    company=input().lower()
    e1=company
    company=''
    i=0
    while i<len(e1):
        if e1[i]!=' ':
            company+=e1[i]
        i+=1
    if company not in company_id:
        print()
        print('The algorithm has never seen this company')
        print('Do you wish to change the company or keep it same')
        print('Press "Y" to change:', end=' ')
        ans1=input()
        print()
        
        while ans1=='Y' or ans1=='y' :
            ans1=''
            print('Enter Mobile Phone Company:',end=' ')
            company=input().lower()
            e1=company
            company=''
            i=0
            while i<len(e1):
                if e1[i]!=' ':
                    company+=e1[i]
                i+=1
            if company not in company_id:
                print()
                print('The algorithm has never seen this company')
                print('Do you wish to change the company or keep it same')
                print('Press "Y" to change:', end=' ')
                ans1=input()
                print()
            




    print('Enter Model:', end=' ')
    model=input().lower()
    e2=model
    model=''
    i=0
    while i<len(e2):
        if e2[i]!=' ':
            model+=e2[i]
        i+=1
    if model not in model_id:
        print()
        print('The algorithm has never seen this model')
        print('Do you wish to change the model or keep it same')
        print('Press "Y" to change:', end=' ')
        ans1=input()
        while ans1=='Y' or ans1=='y':
            check1=False
            ans1=''
            print('Enter Model:',end=' ')
            model=input().lower()
            e2=model
            model=''
            i=0
            while i<len(e2):
                if e2[i]!=' ':
                    model+=e2[i]
                i+=1
            if model not in model_id:
                print('The algorithm has never seen this model')
                print()
                print('Do you wish to change the model or keep it same')
                print('Press "Y" to change:',end=' ')
                ans1=input()
                


    print('RAM Memory in GB:', end=' ')
    ram=int(input())

    print('ROM Memory in GB:', end=' ')
    rom=int(input())

    print('Number of Ratings:', end=' ')
    ratings=int(input())

    print('Number of Reviews:', end=' ')
    reviews=int(input())

    print('Rating in Stars in range 0-5:', end=' ')
    stars=float(input())

    print('Colour:', end=' ')
    colour=input().lower()
    i=0
    e3=colour
    colour=''
    while i<len(e3):
        if e3[i]!=' ':
            colour+=e3[i]
        i+=1
    if colour not in colour_id:
        print('The algorithm has never seen this colour, please enter another basic colour')
        print('Colour:', end=' ')
        colour=input().lower()
        while colour not in colour_id:
            i=0
            e3=colour
            colour=''
            while i<len(e3):
                if e3[i]!=' ':
                    colour+=e3[i]
                i+=1
            # if colour not in colour_id:
            #     print('The algorithm has never seen this colour, please enter another basic colour')
    purity=True
    if company in company_id:
        our_company_id=company_id[company]
    else:
        our_company_id=random.randint(0,len(company_id))
        purity=False
    if model in model_id:
        our_model_id=model_id[model]
    else:
        our_model_id=random.randint(0,len(model_id))
        purity=False
    vector=[our_company_id, our_model_id, ram, rom, ratings, reviews, stars, colour_id[colour]]
    
    price=int(Our_forest.make_a_prediction(vector))
    if price%10 in (9,0,1,2,3,4):
        price=((price-9)//10)*10+9
    else:
        price=((price)//10)*10+9
    print()
    print('===========================================')
    if purity:
        print('The predicted price is Rs.', price)
    else:
        print('The predicted price might be Rs.', price)
    print('===========================================')
    print()
    print('Do you wish for another prediction\nPrint "Y" for Yes or press "N" or "any other key" for No')
    reply=input()
    if reply=='Y' or reply=='y':
        pass
    else:
        predict=False