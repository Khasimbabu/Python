#pip install pynum2word
import num2word
fl = open('C:/Users/kshaik/Documents/Khasim2020/pythonfile1.txt','r')
content=fl.read()
print(content)
fl.close()
fl = open('C:/Users/kshaik/Documents/Khasim2020/pythonfile1.txt','a')
out = num2word.word(content)
print(out)
fl.write(out)
fl.close()
fl = open('C:/Users/kshaik/Documents/Khasim2020/pythonfile1.txt','r')
print(fl.read())
fl.close()



