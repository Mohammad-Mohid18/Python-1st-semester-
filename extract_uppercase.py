# Python program to extract uppercase letters
def extract(str):
    def uppercase(chr):
        return 'A' <= chr <= 'Z'
    
    upper_letters = filter(uppercase,[chr for i in str for chr in i])
    ans = ''
    for i in upper_letters:
        ans += i
    return ans

list = ['heLlo','WoRld','Its','pYthon']
result = extract(list)
print(result)
