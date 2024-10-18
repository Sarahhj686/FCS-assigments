
def GenerateCombinations(characters,n,str1):
    if n==0 :
        print (str1)
        return
    for element in characters :
        GenerateCombinations(characters,n-1,str1+element)
characters=["a","b","c"]
n=2
str1=""
GenerateCombinations(characters,n,str1)
