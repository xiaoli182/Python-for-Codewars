# 该文件主要用来进行 Codewars 代码的测试

# ------------------------------------------
def disemvowel(string):
    test = 'aoeiuAOEIU'
    for i in test:
        string = string.replace(i, '')
    return string

test = "This website is for losers LOL!"
print(disemvowel(test))

translator = str.maketrans({key: None for key in "aeiouAEIOU"})
print(type(translator))

cac = str.maketrans('','','aeiouAEIOU')
print(cac)

print(test.translate(str.maketrans('','','aeiouAEIOU')))