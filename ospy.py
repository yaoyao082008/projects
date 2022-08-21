import os

os.chdir('C:\\Users\\Quanren.Xiong\\Documents\\permutation')
with open('permutations.txt','a') as txt:
    txt.write('1234')
    txt.seek(0)
    txt.write('1243')
