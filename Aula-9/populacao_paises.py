america = [\
           ['Brasil', 212559426],\
           ['Colombia', 50882891],\
           ['Argentina', 45195774],\
           ['Peru', 33050325],\
           ['Venezuela', 28435940],\
           ['Chile', 19116201],\
           ['Equador', 1764054],\
           ['Bolivia', 11673021],\
           ['Paraguai', 7132538],\
           ['Uruguai', 3473730],\
           ['Guiana', 786552],\
           ['Suriname', 588552]\
]

PopTotalAmeSul = 0

for p in range (len (america)):
    print (america [p][0], 'poulação é', america [p][1])
    PopTotalAmeSul = PopTotalAmeSul + america [p][1]

print ('A população total da America do Sul e', PopTotalAmeSul)