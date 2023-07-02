import csv
rows=[]
with open("C:\\Users\\Shikhar Gupta\\Desktop\\Mobile Phone1.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
            rows.append(row)
#del(rows[0])
# print(len(rows))
# for i in range(len(rows)):
#     if rows[i][1][-2:]=='GB':
#         rows[i][1]=int(rows[i][1][:-3])
#         #continue
#     if rows[i][2][-2:]=='GB':
#         rows[i][2]=int(rows[i][2][:-3])
#         continue
#     if rows[i][1][-2:]=='MB':
#         rows[i][1]=int(rows[i][1][:-3])/1024
#         #continue
#     if rows[i][2][-2:]=='MB':
#         print(i,rows[i][2])
#         rows[i][2]=int(rows[i][2][:-3])/1024
#         continue
#     try:
#         if rows[i][1][-2:]=='KB':
#             rows[i][1]=0
#             #continue
#     except:
#         rows[i][1]=0
#         #continue
#     try:
#         if rows[i][2][-2:]=='KB':
#             rows[i][2]=0
#             continue
#     except:
#         rows[i][2]=0
#         continue
#     #print(rows[i][1])
# for i in range(len(rows)):
#     print(i)
#     rows[i][-1]=int(rows[i][-1])
#     if rows[i][-2]=='':
#         print(i,rows[i][-1])
#         rows[i][-2]=1.21*rows[i][-1]
#     rows[i][-2]=int(rows[i][-2])
# #print(rows[3][-2])


# for i in range(len(rows)):
#      rows[i][3]=int(rows[i][3])
#      rows[i][4]=int(rows[i][4])
#      rows[i][5]=float(rows[i][5])

# count=0
# for i in range(len(rows)):
'''



Black=0
White=1
Res=2
Blue=3
Green=4
Orange=5
Violet=6
Purple=7
Grey=8
Cream=9
Yellow=10
Gold=11
Silver=12




'''
#     if '(' in rows[i][0]:
#         ind='('.find(rows[i][0])
#         #s=rows[i][0][ind:]
#         if 'Black' in rows[i][0]:
#             rows[i].append(0)
#             count+=1
#             continue
#         if 'White' in rows[i][0]:
#             rows[i].append(1)
#             count+=1
#             continue
#         if 'Red' in rows[i][0]:
#             rows[i].append(2)
#             count+=1
#             continue
#         if 'Blue' in rows[i][0]:
#             rows[i].append(3)
#             count+=1
#             continue
#         if 'Green' in rows[i][0]:
#             rows[i].append(4)
#             count+=1
#             continue
#         if 'Orange' in rows[i][0]:
#             rows[i].append(5)
#             count+=1
#             continue
#         if 'Violet' in rows[i][0]:
#             rows[i].append(6)
#             count+=1
#             continue
#         if 'Purple' in rows[i][0]:
#             rows[i].append(7)
#             count+=1
#             continue
#         if 'Grey' in rows[i][0]:
#             rows[i].append(8)
#             count+=1
#             continue
#         if 'Cream' in rows[i][0]:
#             rows[i].append(9)
#             count+=1
#             continue
#         if 'Yellow' in rows[i][0]:
#             rows[i].append(10)
#             count+=1
#             continue
#         if 'Gold' in rows[i][0]:
#             rows[i].append(11)
#             count+=1
#             continue
#         if 'Silver' in rows[i][0]:
#             rows[i].append(12)
#             count+=1
#             continue
#     else:
#         rows[i].append(0)
#         count+=1
#         continue
# print(count)

# for i in range(len(rows)):
#        m=0
#        while m<len(rows[i][0]) and rows[i][0][m]!=' ':
#               m+=1
#        rows[i].append(rows[i][0][:m])
#        m+=1
#        while m<len(rows[i][0]) and rows[i][0][m]==' ':
#               m+=1
#        rows[i].append(rows[i][0][:m])
#        n=m
#        while n<len(rows[i][0]) and rows[i][0][n]!='(':
#               n+=1
#        while rows[i][0][n-1]==' ':
#               n-=1 
#        rows[i].append(rows[i][0][m:n])
# for i in range(len(rows)):
#        rows[i][0]=rows[i][0][:-1]
#        if rows[i][0]=='Redmi':
#               rows[i][1]='Note '+str(rows[i][1])
#        if rows[i][0]=='I' :
#               rows[i][1]=rows[i][1][5:]
# for i in range(len(rows)):
#        if rows[i][0]=='Redmi' and 'Note Note' in rows[i][1]:
#               rows[i][1]=rows[i][1][5:]
# for i in range(len(rows)):
#        rows[i][0]=rows[i][0].lower()
#        rows[i][1]=rows[i][1].lower()


company_id={'adcom': 0, 'alcatel': 1, 'angage': 2, 'apple': 3, 'blackbear': 4, 'blackzone': 5, 'coolpad': 6, 'detel': 7, 'easyfone': 8, 'forme': 9, 'geotel': 10, 'gfive': 11, 'gionee': 12, 'good': 13, 'google': 14, 'grabo': 15, 'greenberri': 16, 'greenberry': 17, 'honor': 18, 'huawei': 19, 'i kall': 20, 'infinix': 21, 'iqoo': 22, 'ismart': 23, 'itel': 24, 'jio': 25, 'jivi': 26, 'karbonn': 27, 'kechaoda': 28, 'kxd': 29, 'lava': 30, 'lg': 31, 'marq': 32, 'mi': 33, 'micromax': 34, 'moto': 35, 'motorola': 36, 'mtr': 37, 'mu': 38, 'muphone': 39, 'nokia': 40, 'oppo': 41, 'panasonic': 42, 'philips': 43, 'poco': 44, 'realme': 45, 'redmi': 46, 'rokea': 47, 'salora': 48, 'samsung': 49, 'snexian': 50, 'ssky': 51, 'tecno': 52, 'tork': 53, 'uismart': 54, 'vivo': 55}
model_id={'a115': 0, '5v': 1, 'a310': 2, 'a312': 3, 'iphone 11': 4, 'iphone 12': 5, 'iphone 7 plus': 6, 'iphone se': 7, 'iphone xr': 8, 'iphone 12 pro max': 9, 'iphone 11 pro': 10, 'iphone 12 pro': 11, 'a1 pen phone': 12, 'i7 trio': 13, 'b310': 14, 'eco x': 15, 'hammer': 16, 'porsche 911': 17, 's13': 18, 'shine': 19, 'turbo 353': 20, 'mega 5s': 21, 'd1 guru': 22, 'marvel': 23, 'duos n2': 24, 'duos1900': 25, 'n1': 26, 'rocket': 27, 'k9 flip': 28, 'a1': 29, 'a2': 30, 'i1': 31, 'i2': 32, 'u106': 33, 'u220 combo of two': 34, 'u220+': 35, 'u229': 36, 'u707': 37, 'f8 neo': 38, 'max': 39, 'f11': 40, 'max pro': 41, 'one 5605': 42, 'one g2 mini': 43, 'one magic': 44, 'pixel 4a': 45, '220': 46, 'eluga': 47, 'g106': 48, 'g310 vibration': 49, 'g312': 50, 'hulk': 51, 'nord': 52, 'f1': 53, 'm2 mini': 54, '20': 55, 'y9 prime 2019': 56, 'k4': 57, 'k6': 58, 'k 18 new': 59, 'k 38 plus': 60, 'k 444': 61, 'k 48': 62, 'k 666': 63, 'k130 new': 64, 'k14 new': 65, 'k2180': 66, 'k22': 67, 'k33 new': 68, 'k3312': 69, 'k444': 70, 'k50': 71, 'k666+': 72, 'k1000': 73, 'k220': 74, 'k400': 75, 'hot 10': 76, 'note 7': 77, 'smart 4 plus': 78, 'smart 5': 79, 'smart hd 2021': 80, 'zero 8i': 81, 's5 pro': 82, 'hot 9': 83, 'hot 9 pro': 84, '3': 85, 'i1 supreme': 86, 'a48': 87, 'ace': 88, 'it 2163': 89, 'it2161': 90, 'it2163': 91, 'it2173': 92, 'it5026': 93, 'it5260': 94, 'it5607': 95, 'it5618n': 96, 'magic2 max': 97, 'muzik 400': 98, 'power 110': 99, 'power 400': 100, 'power 410': 101, 'u10': 102, 'a25 pro': 103, 'vision1': 104, 'vision 1 pro': 105, 'f320b': 106, 'jiophone': 107, '12m-xl': 108, 'n300 new': 109, 'x57i selfie': 110, 'k phone 1': 111, 'k106s': 112, 'k140 pop': 113, 'k19 rock': 114, 'k310n': 115, 'k7 power': 116, 'k9': 117, 'k9 mini': 118, 'k9 power': 119, 'k-pebble': 120, 'k-stylo': 121, 'kx 10i': 122, 'kx1': 123, 'kx1 indian': 124, 'kx19': 125, 'kx1i': 126, 'kx1indian': 127, 'kx23': 128, 'kx26': 129, 'kx26i': 130, 'kx3': 131, 'kx5': 132, 'a 31': 133, 'a26': 134, 'a27': 135, 'a29': 136, 'k 06': 137, 'k1': 138, 'k10': 139, 'k102': 140, 'k108': 141, 'k111': 142, 'k112': 143, 'k115': 144, 'k123': 145, 'k2': 146, 'k20': 147, 'k28': 148, 'k30': 149, 'k33': 150, 'k35': 151, 'k-55 plus': 152, 'k60': 153, 'k66 plus': 154, 'k-9': 155, 'c1': 156, 'm2+': 157, 'm3+': 158, 'p2': 159, '34 plus': 160, '34 ultra': 161, 'a1 josh': 162, 'a1 super': 163, 'a1200': 164, 'a3': 165, 'a5': 166, 'a7 2020': 167, 'a9': 168, 'arc 22': 169, 'flip': 170, 'gem': 171, 'gem wave / gem': 172, 'h1 hero 600': 173, 'hero 600+': 174, 'hero 600s': 175, 'pulse': 176, 'pulse1': 177, 'z66': 178, 'z61 pro': 179, 'k42': 180, 'by flipkart 110 magic': 181, '10i': 182, 'j1': 183, 'x1i-2017': 184, 'x378': 185, 'x380': 186, 'x381': 187, 'x382': 188, 'x388': 189, 'x412': 190, 'x419': 191, 'x421': 192, 'x512': 193, 'x741': 194, 'x744': 195, 'x746': 196, 'x748': 197, 'x749': 198, 'x750': 199, 'x752': 200, 'x754': 201, 'x756': 202, 'x807': 203, 'x809': 204, 'x817': 205, 'g 5g': 206, 'g30': 207, 'e7 power': 208, 'e7 plus': 209, 'g10 power': 210, 'g8 power lite': 211, 'g9': 212, 'g9 power': 213, 'ferrari': 214, 'm370': 215, 'm5000': 216, 'm 230': 217, 'm380': 218, '105 ds': 219, '105 ds 2020': 220, '105 ss': 221, '105 ss 2020': 222, '110 ds 2020': 223, '125 ds 2020': 224, '150 ds 2020': 225, '216 ds 2020': 226, '225': 227, '3310 ds 2020': 228, '5310 ds 2020': 229, 'ta-1010/105': 230, 'ta-1174 / ta-1299': 231, '2.4': 232, '3.4': 233, 'a12': 234, 'a15': 235, 'a15s': 236, 'a31': 237, 'a33': 238, 'a5 2020': 239, 'a52': 240, 'a53': 241, 'a5s': 242, 'f15': 243, 'f17 pro': 244, 'f19 pro': 245, 'reno2 f': 246, 'a1k': 247, 'a11k': 248, 'f17': 249, 'a9 2020': 250, 'f19pro+': 251, 'eluga i6': 252, 'eluga i7': 253, 'eluga i8': 254, 'e102a': 255, 'c3': 256, 'm2': 257, 'm2 pro': 258, 'm3': 259, 'x2': 260, 'x3': 261, '3i': 262, '6i': 263, 'c2': 264, 'narzo 20 pro': 265, 'narzo 30 pro 5g': 266, 'narzo 30a': 267, '5 pro': 268, '6': 269, '7': 270, 'narzo 10': 271, 'narzo 10a': 272, 'x': 273, 'x3 superzoom': 274, '5i': 275, '6 pro': 276, '7 pro': 277, '7i': 278, 'c12': 279, 'c15': 280, 'c15 qualcomm edition': 281, 'narzo 20': 282, 'narzo 20a': 283, 'x7 5g': 284, 'c11': 285, 'note 6a': 286, 'note 8': 287, 'note 8a': 288, 'note 9': 289, 'note 9 power': 290, 'note 9 prime': 291, 'note 9a': 292, 'note 9i': 293, 'note go': 294, 'note 10': 295, 'note 8 pro': 296, 'note 9 pro': 297, 'note 9 pro max': 298, 'note 8a dual': 299, 'note 5a': 300, 'note 10 pro max': 301, 'r222': 302, 'atom': 303, 'vishaal': 304, 'galaxy a10s': 305, 'galaxy a12': 306, 'galaxy a21s': 307, 'galaxy a31': 308, 'galaxy a32': 309, 'galaxy a51': 310, 'galaxy f41': 311, 'galaxy m01': 312, 'galaxy m02': 313, 'galaxy m11': 314, 'galaxy m21': 315, 'galaxy m31': 316, 'galaxy m51': 317, 'guru 1200': 318, 'guru fm plus': 319, 'guru fm plus sm-b110e/d': 320, 'guru gt': 321, 'guru music 2': 322, 'guru music 2 sm-b310e': 323, 'm01 core': 324, 'm02s': 325, 'm31 prime': 326, 'metro 313': 327, 'metro 313 dual sim': 328, 'galaxy a71': 329, 'galaxy f62': 330, 'galaxy m01s\xa0': 331, 'galaxy m40': 332, 'm31s': 333, 'galaxy m01s': 334, 'bold 511': 335, 'guru 312': 336, 'guru 5500': 337, 'rock': 338, 's-20 eco': 339, 'pova': 340, 'camon 16': 341, 'spark 6 go': 342, 'spark go 2020': 343, 'spark power 2 air': 344, 'camon 15': 345, 'spark power 2': 346, 'spark 5 pro': 347, 't13 banana': 348, 't19 shine': 349, 't27 power': 350, 't3': 351, 'x9': 352, 'ui06': 353, 'ui-06': 354, 's1': 355, 's1 pro': 356, 'v19': 357, 'v20 se': 358, 'y12s': 359, 'y20': 360, 'y20g': 361, 'y30': 362, 'y31': 363, 'y91i': 364, 'z1pro': 365, 'v17pro': 366, 'y20a': 367, 'y20i': 368, 'y50': 369, 'y11': 370, 'y12': 371, 'y15': 372, 'z1x': 373, 'y51': 374, 'y51a': 375, 'v20': 376, 'v20 2021': 377, 'v20 pro': 378}
# companies=[]
# models=[]
# for i in range(len(rows)):
#        if rows[i][0] not in companies:
#         companies.append(rows[i][0])
#        if rows[i][1] not in models: 
#         models.append(rows[i][1])
# company2id={u:j for j,u in enumerate(companies)}
# model2id={v:k for k,v in enumerate(models)}
# print(company2id)
# print(model2id)
# for i in range(len(rows)):
#        rows[i].append(company2id[rows[i][0]])
#        rows[i].append(model2id[rows[i][1]])


'''56 unique companies
378 unique models'''


for i in range(len(rows)):
        rows[i][0], rows[i][1], rows[i][4], rows[i][5], rows[i][7], rows[i][8], rows[i][9] = int(rows[i][0]), int(rows[i][1]), int(rows[i][4]), int(rows[i][5]), int(rows[i][7]), int(rows[i][8]), int(rows[i][9])
        rows[i][2], rows[i][3], rows[i][6]=float(rows[i][2]), float(rows[i][3]), float(rows[i][6])
with open("C:\\Users\\Shikhar Gupta\\Desktop\\Mobile Phone1.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
import csv
rows=[]
with open("C:\\Users\\Shikhar Gupta\\Desktop\\Mobile Phone1.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
            rows.append(row)
#del(rows[0])
# print(len(rows))
# for i in range(len(rows)):
#     if rows[i][1][-2:]=='GB':
#         rows[i][1]=int(rows[i][1][:-3])
#         #continue
#     if rows[i][2][-2:]=='GB':
#         rows[i][2]=int(rows[i][2][:-3])
#         continue
#     if rows[i][1][-2:]=='MB':
#         rows[i][1]=int(rows[i][1][:-3])/1024
#         #continue
#     if rows[i][2][-2:]=='MB':
#         print(i,rows[i][2])
#         rows[i][2]=int(rows[i][2][:-3])/1024
#         continue
#     try:
#         if rows[i][1][-2:]=='KB':
#             rows[i][1]=0
#             #continue
#     except:
#         rows[i][1]=0
#         #continue
#     try:
#         if rows[i][2][-2:]=='KB':
#             rows[i][2]=0
#             continue
#     except:
#         rows[i][2]=0
#         continue
#     #print(rows[i][1])
# for i in range(len(rows)):
#     print(i)
#     rows[i][-1]=int(rows[i][-1])
#     if rows[i][-2]=='':
#         print(i,rows[i][-1])
#         rows[i][-2]=1.21*rows[i][-1]
#     rows[i][-2]=int(rows[i][-2])
# #print(rows[3][-2])


# for i in range(len(rows)):
#      rows[i][3]=int(rows[i][3])
#      rows[i][4]=int(rows[i][4])
#      rows[i][5]=float(rows[i][5])

# count=0
# for i in range(len(rows)):
'''



Black=0
White=1
Res=2
Blue=3
Green=4
Orange=5
Violet=6
Purple=7
Grey=8
Cream=9
Yellow=10
Gold=11
Silver=12




'''
#     if '(' in rows[i][0]:
#         ind='('.find(rows[i][0])
#         #s=rows[i][0][ind:]
#         if 'Black' in rows[i][0]:
#             rows[i].append(0)
#             count+=1
#             continue
#         if 'White' in rows[i][0]:
#             rows[i].append(1)
#             count+=1
#             continue
#         if 'Red' in rows[i][0]:
#             rows[i].append(2)
#             count+=1
#             continue
#         if 'Blue' in rows[i][0]:
#             rows[i].append(3)
#             count+=1
#             continue
#         if 'Green' in rows[i][0]:
#             rows[i].append(4)
#             count+=1
#             continue
#         if 'Orange' in rows[i][0]:
#             rows[i].append(5)
#             count+=1
#             continue
#         if 'Violet' in rows[i][0]:
#             rows[i].append(6)
#             count+=1
#             continue
#         if 'Purple' in rows[i][0]:
#             rows[i].append(7)
#             count+=1
#             continue
#         if 'Grey' in rows[i][0]:
#             rows[i].append(8)
#             count+=1
#             continue
#         if 'Cream' in rows[i][0]:
#             rows[i].append(9)
#             count+=1
#             continue
#         if 'Yellow' in rows[i][0]:
#             rows[i].append(10)
#             count+=1
#             continue
#         if 'Gold' in rows[i][0]:
#             rows[i].append(11)
#             count+=1
#             continue
#         if 'Silver' in rows[i][0]:
#             rows[i].append(12)
#             count+=1
#             continue
#     else:
#         rows[i].append(0)
#         count+=1
#         continue
# print(count)

# for i in range(len(rows)):
#        m=0
#        while m<len(rows[i][0]) and rows[i][0][m]!=' ':
#               m+=1
#        rows[i].append(rows[i][0][:m])
#        m+=1
#        while m<len(rows[i][0]) and rows[i][0][m]==' ':
#               m+=1
#        rows[i].append(rows[i][0][:m])
#        n=m
#        while n<len(rows[i][0]) and rows[i][0][n]!='(':
#               n+=1
#        while rows[i][0][n-1]==' ':
#               n-=1 
#        rows[i].append(rows[i][0][m:n])
# for i in range(len(rows)):
#        rows[i][0]=rows[i][0][:-1]
#        if rows[i][0]=='Redmi':
#               rows[i][1]='Note '+str(rows[i][1])
#        if rows[i][0]=='I' :
#               rows[i][1]=rows[i][1][5:]
# for i in range(len(rows)):
#        if rows[i][0]=='Redmi' and 'Note Note' in rows[i][1]:
#               rows[i][1]=rows[i][1][5:]
# for i in range(len(rows)):
#        rows[i][0]=rows[i][0].lower()
#        rows[i][1]=rows[i][1].lower()


company_id={'adcom': 0, 'alcatel': 1, 'angage': 2, 'apple': 3, 'blackbear': 4, 'blackzone': 5, 'coolpad': 6, 'detel': 7, 'easyfone': 8, 'forme': 9, 'geotel': 10, 'gfive': 11, 'gionee': 12, 'good': 13, 'google': 14, 'grabo': 15, 'greenberri': 16, 'greenberry': 17, 'honor': 18, 'huawei': 19, 'i kall': 20, 'infinix': 21, 'iqoo': 22, 'ismart': 23, 'itel': 24, 'jio': 25, 'jivi': 26, 'karbonn': 27, 'kechaoda': 28, 'kxd': 29, 'lava': 30, 'lg': 31, 'marq': 32, 'mi': 33, 'micromax': 34, 'moto': 35, 'motorola': 36, 'mtr': 37, 'mu': 38, 'muphone': 39, 'nokia': 40, 'oppo': 41, 'panasonic': 42, 'philips': 43, 'poco': 44, 'realme': 45, 'redmi': 46, 'rokea': 47, 'salora': 48, 'samsung': 49, 'snexian': 50, 'ssky': 51, 'tecno': 52, 'tork': 53, 'uismart': 54, 'vivo': 55}
model_id={'a115': 0, '5v': 1, 'a310': 2, 'a312': 3, 'iphone 11': 4, 'iphone 12': 5, 'iphone 7 plus': 6, 'iphone se': 7, 'iphone xr': 8, 'iphone 12 pro max': 9, 'iphone 11 pro': 10, 'iphone 12 pro': 11, 'a1 pen phone': 12, 'i7 trio': 13, 'b310': 14, 'eco x': 15, 'hammer': 16, 'porsche 911': 17, 's13': 18, 'shine': 19, 'turbo 353': 20, 'mega 5s': 21, 'd1 guru': 22, 'marvel': 23, 'duos n2': 24, 'duos1900': 25, 'n1': 26, 'rocket': 27, 'k9 flip': 28, 'a1': 29, 'a2': 30, 'i1': 31, 'i2': 32, 'u106': 33, 'u220 combo of two': 34, 'u220+': 35, 'u229': 36, 'u707': 37, 'f8 neo': 38, 'max': 39, 'f11': 40, 'max pro': 41, 'one 5605': 42, 'one g2 mini': 43, 'one magic': 44, 'pixel 4a': 45, '220': 46, 'eluga': 47, 'g106': 48, 'g310 vibration': 49, 'g312': 50, 'hulk': 51, 'nord': 52, 'f1': 53, 'm2 mini': 54, '20': 55, 'y9 prime 2019': 56, 'k4': 57, 'k6': 58, 'k 18 new': 59, 'k 38 plus': 60, 'k 444': 61, 'k 48': 62, 'k 666': 63, 'k130 new': 64, 'k14 new': 65, 'k2180': 66, 'k22': 67, 'k33 new': 68, 'k3312': 69, 'k444': 70, 'k50': 71, 'k666+': 72, 'k1000': 73, 'k220': 74, 'k400': 75, 'hot 10': 76, 'note 7': 77, 'smart 4 plus': 78, 'smart 5': 79, 'smart hd 2021': 80, 'zero 8i': 81, 's5 pro': 82, 'hot 9': 83, 'hot 9 pro': 84, '3': 85, 'i1 supreme': 86, 'a48': 87, 'ace': 88, 'it 2163': 89, 'it2161': 90, 'it2163': 91, 'it2173': 92, 'it5026': 93, 'it5260': 94, 'it5607': 95, 'it5618n': 96, 'magic2 max': 97, 'muzik 400': 98, 'power 110': 99, 'power 400': 100, 'power 410': 101, 'u10': 102, 'a25 pro': 103, 'vision1': 104, 'vision 1 pro': 105, 'f320b': 106, 'jiophone': 107, '12m-xl': 108, 'n300 new': 109, 'x57i selfie': 110, 'k phone 1': 111, 'k106s': 112, 'k140 pop': 113, 'k19 rock': 114, 'k310n': 115, 'k7 power': 116, 'k9': 117, 'k9 mini': 118, 'k9 power': 119, 'k-pebble': 120, 'k-stylo': 121, 'kx 10i': 122, 'kx1': 123, 'kx1 indian': 124, 'kx19': 125, 'kx1i': 126, 'kx1indian': 127, 'kx23': 128, 'kx26': 129, 'kx26i': 130, 'kx3': 131, 'kx5': 132, 'a 31': 133, 'a26': 134, 'a27': 135, 'a29': 136, 'k 06': 137, 'k1': 138, 'k10': 139, 'k102': 140, 'k108': 141, 'k111': 142, 'k112': 143, 'k115': 144, 'k123': 145, 'k2': 146, 'k20': 147, 'k28': 148, 'k30': 149, 'k33': 150, 'k35': 151, 'k-55 plus': 152, 'k60': 153, 'k66 plus': 154, 'k-9': 155, 'c1': 156, 'm2+': 157, 'm3+': 158, 'p2': 159, '34 plus': 160, '34 ultra': 161, 'a1 josh': 162, 'a1 super': 163, 'a1200': 164, 'a3': 165, 'a5': 166, 'a7 2020': 167, 'a9': 168, 'arc 22': 169, 'flip': 170, 'gem': 171, 'gem wave / gem': 172, 'h1 hero 600': 173, 'hero 600+': 174, 'hero 600s': 175, 'pulse': 176, 'pulse1': 177, 'z66': 178, 'z61 pro': 179, 'k42': 180, 'by flipkart 110 magic': 181, '10i': 182, 'j1': 183, 'x1i-2017': 184, 'x378': 185, 'x380': 186, 'x381': 187, 'x382': 188, 'x388': 189, 'x412': 190, 'x419': 191, 'x421': 192, 'x512': 193, 'x741': 194, 'x744': 195, 'x746': 196, 'x748': 197, 'x749': 198, 'x750': 199, 'x752': 200, 'x754': 201, 'x756': 202, 'x807': 203, 'x809': 204, 'x817': 205, 'g 5g': 206, 'g30': 207, 'e7 power': 208, 'e7 plus': 209, 'g10 power': 210, 'g8 power lite': 211, 'g9': 212, 'g9 power': 213, 'ferrari': 214, 'm370': 215, 'm5000': 216, 'm 230': 217, 'm380': 218, '105 ds': 219, '105 ds 2020': 220, '105 ss': 221, '105 ss 2020': 222, '110 ds 2020': 223, '125 ds 2020': 224, '150 ds 2020': 225, '216 ds 2020': 226, '225': 227, '3310 ds 2020': 228, '5310 ds 2020': 229, 'ta-1010/105': 230, 'ta-1174 / ta-1299': 231, '2.4': 232, '3.4': 233, 'a12': 234, 'a15': 235, 'a15s': 236, 'a31': 237, 'a33': 238, 'a5 2020': 239, 'a52': 240, 'a53': 241, 'a5s': 242, 'f15': 243, 'f17 pro': 244, 'f19 pro': 245, 'reno2 f': 246, 'a1k': 247, 'a11k': 248, 'f17': 249, 'a9 2020': 250, 'f19pro+': 251, 'eluga i6': 252, 'eluga i7': 253, 'eluga i8': 254, 'e102a': 255, 'c3': 256, 'm2': 257, 'm2 pro': 258, 'm3': 259, 'x2': 260, 'x3': 261, '3i': 262, '6i': 263, 'c2': 264, 'narzo 20 pro': 265, 'narzo 30 pro 5g': 266, 'narzo 30a': 267, '5 pro': 268, '6': 269, '7': 270, 'narzo 10': 271, 'narzo 10a': 272, 'x': 273, 'x3 superzoom': 274, '5i': 275, '6 pro': 276, '7 pro': 277, '7i': 278, 'c12': 279, 'c15': 280, 'c15 qualcomm edition': 281, 'narzo 20': 282, 'narzo 20a': 283, 'x7 5g': 284, 'c11': 285, 'note 6a': 286, 'note 8': 287, 'note 8a': 288, 'note 9': 289, 'note 9 power': 290, 'note 9 prime': 291, 'note 9a': 292, 'note 9i': 293, 'note go': 294, 'note 10': 295, 'note 8 pro': 296, 'note 9 pro': 297, 'note 9 pro max': 298, 'note 8a dual': 299, 'note 5a': 300, 'note 10 pro max': 301, 'r222': 302, 'atom': 303, 'vishaal': 304, 'galaxy a10s': 305, 'galaxy a12': 306, 'galaxy a21s': 307, 'galaxy a31': 308, 'galaxy a32': 309, 'galaxy a51': 310, 'galaxy f41': 311, 'galaxy m01': 312, 'galaxy m02': 313, 'galaxy m11': 314, 'galaxy m21': 315, 'galaxy m31': 316, 'galaxy m51': 317, 'guru 1200': 318, 'guru fm plus': 319, 'guru fm plus sm-b110e/d': 320, 'guru gt': 321, 'guru music 2': 322, 'guru music 2 sm-b310e': 323, 'm01 core': 324, 'm02s': 325, 'm31 prime': 326, 'metro 313': 327, 'metro 313 dual sim': 328, 'galaxy a71': 329, 'galaxy f62': 330, 'galaxy m01s\xa0': 331, 'galaxy m40': 332, 'm31s': 333, 'galaxy m01s': 334, 'bold 511': 335, 'guru 312': 336, 'guru 5500': 337, 'rock': 338, 's-20 eco': 339, 'pova': 340, 'camon 16': 341, 'spark 6 go': 342, 'spark go 2020': 343, 'spark power 2 air': 344, 'camon 15': 345, 'spark power 2': 346, 'spark 5 pro': 347, 't13 banana': 348, 't19 shine': 349, 't27 power': 350, 't3': 351, 'x9': 352, 'ui06': 353, 'ui-06': 354, 's1': 355, 's1 pro': 356, 'v19': 357, 'v20 se': 358, 'y12s': 359, 'y20': 360, 'y20g': 361, 'y30': 362, 'y31': 363, 'y91i': 364, 'z1pro': 365, 'v17pro': 366, 'y20a': 367, 'y20i': 368, 'y50': 369, 'y11': 370, 'y12': 371, 'y15': 372, 'z1x': 373, 'y51': 374, 'y51a': 375, 'v20': 376, 'v20 2021': 377, 'v20 pro': 378}
# companies=[]
# models=[]
# for i in range(len(rows)):
#        if rows[i][0] not in companies:
#         companies.append(rows[i][0])
#        if rows[i][1] not in models: 
#         models.append(rows[i][1])
# company2id={u:j for j,u in enumerate(companies)}
# model2id={v:k for k,v in enumerate(models)}
# print(company2id)
# print(model2id)
# for i in range(len(rows)):
#        rows[i].append(company2id[rows[i][0]])
#        rows[i].append(model2id[rows[i][1]])


'''56 unique companies
378 unique models'''


for i in range(len(rows)):
        rows[i][0], rows[i][1], rows[i][4], rows[i][5], rows[i][7], rows[i][8], rows[i][9] = int(rows[i][0]), int(rows[i][1]), int(rows[i][4]), int(rows[i][5]), int(rows[i][7]), int(rows[i][8]), int(rows[i][9])
        rows[i][2], rows[i][3], rows[i][6]=float(rows[i][2]), float(rows[i][3]), float(rows[i][6])
with open("C:\\Users\\Shikhar Gupta\\Desktop\\Mobile Phone1.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
