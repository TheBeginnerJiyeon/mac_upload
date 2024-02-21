import turtle

value=[30*i-225 for i in range(16)]

value2=-225
for i in value:
    if i>=30:
        value2=i
        break
        

print(value2)