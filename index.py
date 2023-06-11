def writeInFile(LengthOfEle,L):
    f=open("demo.txt","a")
    for i in range(0,len(L)-1):
        f.write(f"{L[i]}.{LengthOfEle[i]}\n")
    
    f.close()



L=["one","two","three","four","five"]
LengthOfEle=[len(x) for x in L ]
writeInFile(LengthOfEle,L)

