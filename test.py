import math
from functools import reduce
list1 = ("1a,2b,3c,4d,5e,6f,7g","8h,9i,10j");
list2 = [1,2,3,4,5,6,7,8,9];
name = "hello world name";
age = 18;



# def trim(str1):
#     start = 0;
#     end = len(str1)
#     for i in range(len(str1)):

#         if(str1[i] == ' '):
#             end = i - 1
#             continue
#         if(str1[i] != ' ' and start == 0):
#             start = i
#             continue
#     print(str1[start:end])

# trim("   456dfdf   ")
# i = 0;
# while i < 20:
#     print(i);
#     i = i + 1;
#     if(i == 15):
#         break;


# d = {list1: 1, "b": 2, "c": 3}
# print(d.get('f',-1))

# d.pop("b");
# for key,value in d.items():
#     print(key,value)

# s = set([1, 2, 3, 4, 5, 6, 7, 8, list1])
# print(s);

#print(abs(float("-20.1")))



# def quadratic(a, b, c):
#     ret1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
#     ret2 = (-b - math.sqrt(b*b -4*a*c))/(2*a);
#     return ret1,ret2;
    

# print(print(quadratic(2, 3, 1)))

# def nop():
#     pass

# trouple = {1,2,"a","test","test"};
# def test(**args):
#     # 
#     print(args);


# args = {"trouple":123,"24":"test"};
# test(**args)
# test(x=1, y=2, z=3)
# test(**{"trouple2": 123, "24": "test"})


# def mul(*args):
#     value = 1
#     for i in args:
#         value = value * i
#     return value;

# print(mul(10,20,30,40,50))

# def facttest(n,result):
#     if n == 1:
#         return result
#     return  facttest(n - 1,n * result)

# print(facttest(1000,1))

# def move(n, a, b, c):
#     if n == 1:
#         print(a + "-->" + c)
#     else:
#         move(n-1,a,c,b)
#         print(a + "-->" + c)
#         move(n-1,b,a,c)

# move(4,"A","B","C")


# dic = {"A":1,"B":2,"c":3}
# for i,v in dic.items():
#     print(i,v)

# listnew = ["a","b","c","d","e"]
# for i, v in enumerate(listnew):
#     print(i,v)

# def findMinAndMax(L):
#     if len(L) == 0:
#         return (0, 0)
#     min = L[0];
#     max = 0;
#     for i in L:
#         if i < i:
#             min = i
#         if i >= i:
#             max = i
#     return (min, max)


# print(findMinAndMax([4,5,63,234,0,3432]))

# def f1(str1):
#     print(str1)
#     str1New = list(str1)
#     for i in range(len(str1)):   
#         if i == 0:
#             str1New[i] = str1[i].upper()
#         if i > 0:
#             str1New[i] = str1[i].lower()
#     return ''.join(str1New)


# def normalize(name):
#    ret = list(map(f1, name))
#    return ret


# print(normalize(["sTSsT","sdfs","ertrt"]))

# def sum(x,y):
#     return x + y;

# def prod(L):
    
#     ret = reduce(sum,L)
#     return ret

# print(prod([1,2,3,4,5,6,7,8,9]))
def a(x,y):
        return x * 10 + y;


def aa(x, y):
        return x/10  + y
def b(s):
    if s != ".":
        return int(s)
    return ".";
def str2float(s):
    retList = s.split('.');
    retMap1 = list(map(b, retList[0]))
    retMap2 = list(map(b, retList[1]))
    print(retMap1,  retMap2)

    ret11 = reduce(a, retMap1)
    ret22 = reduce(aa,[0]+ retMap2)
    return ret11 + ret22

print(str2float('2345.1234'))
