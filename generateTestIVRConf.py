# encoding:utf-8
# python generateTestIVRConf.py  入参数1 入参数2 ... 入参数n-1 出参个数
#                 0                1       2           n-1     n  
import sys
import tkinter
file = open("TestIVR.ini","w")

string = '[DtProxy]\nTestIVRID = 301\nDtProxyIP = 198.115.167.11\nDtProxyID = 221\nLogSize = 2\nAppSvr = 0\nDataSource = icdboss\nByteOrder = 0\n\n'
string += '[SP_CALL1]\nSPName = I_SCE_CommonInterFace\nTimeout = 6000\n'
inParamNumBeginIndex = 1
inParamNumEndIndex = len(sys.argv)-2 #1是脚本名称，n是出参个数，这两个不能计算在内
outParamNum = int(sys.argv[len(sys.argv)-1])
paraNum = len(sys.argv)-2 + outParamNum
print("inParamNumBeginIndex="+str(inParamNumBeginIndex)+' inParamNumEndIndex='+str(inParamNumEndIndex) +' outParamNum='+str(outParamNum)+' paraNum='+str(paraNum))
string += 'ParaNum = ' + str(paraNum) + '\n\n'

for i in range(1, paraNum+1): #range(start,stop,step)包括start，但是不包括stop
    if i <= inParamNumEndIndex:
        string += 'DataType' + str(i) + ' = 50\n'
        string += 'ParaType' + str(i) + ' = 0\n'
        string += 'DataLen' + str(i) + ' = 50\n'
        string += 'Data' +str(i) + ' = ' + sys.argv[i] + '\n\n'
        
    else:
        string += 'DataType' + str(i) + ' = 20\n'
        string += 'ParaType' + str(i) + ' = 1\n'
        string += 'DataLen' + str(i) + ' = 20\n'
        string += 'Data' +str(i) + ' = ' + '\n\n'


file.write(string)
file.close
