#literals is raw data given to variables in python there is 4 literals
#literals means we give value to varibale is called literals
# a=10 #here 10 is literals
# Numeric,String,Boolean,Special 
#Numeric
a=10
b=0b1010 #binary value but o/p is Int
c=0o310#octal
d=0x12c#hexadecimal
print(a,b,c,d);

float_1=3.42#float
float_2=1.5e2#1.5 multiply by 10 to power 2 max number
float_3=1.5e-3#1.5 multiply by 10 to power 2 min or negative no
print(float_1,float_2,float_3)

#Complex under Numberic
x=0+3.14j
print(x,x.imag,x.real)

#String single double inverted but there is no difference in python
#in python there is no char datatype
string='This is single inverted comma'
print(string)

string_2="This is double inverted comma"
print(string_2)
#for multi line use """ """ triple inverted comma
triple_inverted="""Triple inverted comma was used in this statement for more than one line"""
print(triple_inverted)
#unicode like emoji just use U before literals
unicode=u"\U0001f600\U0001F606\U0001F923"
#print(unicode)
#print html raw string just pass r before literals
raw_string=r"raw\n string"
print(raw_string)

#Boolean
a=True+4#true is 1 here is implicit type conversion
b=False+10#false is 0 here is implicit type conversion
print("a",a)
print("b",b)

#Special :- None which means abscance of anything
#as there is no variables declaration is python 
# so we use None to just declare blank will use later on
#f; cannot declare blank getting error
f=None
print(f)
