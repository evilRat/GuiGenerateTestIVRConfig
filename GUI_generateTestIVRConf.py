# encoding:utf-8

import tkinter as tk

class Gui(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("testIVR配置文件生成器    --by kongzheng")
        self.root.geometry('1000x800')
        self.frame_root = tk.LabelFrame(self.root)
        self.frame_input = tk.LabelFrame(bg='gray',width=500,height=800,text='inputParam')
        self.frame_output = tk.LabelFrame(bg='white',width=500,height=800,text='outputParam')
        
        
        self.root.url_label = tk.Label(self.frame_input,text='Url',font=('Arial', 12))
        self.root.url_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.actioncode_label = tk.Label(self.frame_input,text='ActionCode',font=('Arial', 12))
        self.root.actioncode_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.mobile_label = tk.Label(self.frame_input,text='Mobile',font=('Arial', 12))
        self.root.mobile_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.field1_label = tk.Label(self.frame_input,text='Field1',font=('Arial', 12))
        self.root.field1_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.field2_label = tk.Label(self.frame_input,text='Field2',font=('Arial', 12))
        self.root.field2_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.field3_label = tk.Label(self.frame_input,text='Field3',font=('Arial', 12))
        self.root.field3_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.field4_label = tk.Label(self.frame_input,text='Field4',font=('Arial', 12))
        self.root.field4_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.field5_label = tk.Label(self.frame_input,text='Field5',font=('Arial', 12))
        self.root.field5_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.field6_label = tk.Label(self.frame_input,text='Field6',font=('Arial', 12))
        self.root.field6_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.field7_label = tk.Label(self.frame_input,text='Field7',font=('Arial', 12))
        self.root.field7_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.field8_label = tk.Label(self.frame_input,text='Field8',font=('Arial', 12))
        self.root.field8_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.outParamNum_label = tk.Label(self.frame_input,text='outParamNum',font=('Arial', 12))
        self.root.outParamNum_entry = tk.Entry(self.frame_input,width=50,textvariable='')

        self.root.outPut_text = tk.Text(self.frame_output,width=70,height=780)

    def cleanParam(self,list):
        #print(list)
        resList = []
        for i in range(0,len(list)):
            #print(list[i][1])
            if list[i][1] == '':
                continue
            else:
                resList.append(list[i])
        return resList
                
    def doGenerate(self,list):
        string = '[DtProxy]\nTestIVRID = 301\nDtProxyIP = 198.115.167.11\nDtProxyID = 221\nLogSize = 2\nAppSvr = 0\nDataSource = icdboss\nByteOrder = 0\n\n'
        string += '[SP_CALL1]\nSPName = I_SCE_CommonInterFace\nTimeout = 6000\n\n'

        for i in range(0,len(list)):
            if list[i][0] != 'outParamNum':
                string += 'DataType' + str(i+1) + ' = 50\n'
                string += 'ParaType' + str(i+1) + ' = 0\n'
                string += 'DataLen' + str(i+1) + ' = 50\n'
                string += 'Data' +str(i+1) + ' = ' + list[i][1] + '\n\n'
            else:
                for j in range(i,len(list)+int(list[-1][1])-1):
                    string += 'DataType' + str(j+1) + ' = 20\n'
                    string += 'ParaType' + str(j+1) + ' = 1\n'
                    string += 'DataLen' + str(j+1) + ' = 20\n'
                    string += 'Data' +str(j+1) + ' = ' + '\n\n'
        print(string)
        self.root.outPut_text.delete(1.0,tk.END)
        self.root.outPut_text.insert(1.0,string)

    def clickGenerate(self):

        self.label_text_url = self.root.url_label.cget("text")
        self.label_text_actioncode = self.root.actioncode_label.cget("text")  
        self.label_text_mobile = self.root.mobile_label.cget("text")
        self.label_text_field1 = self.root.field1_label.cget("text")
        self.label_text_field2 = self.root.field2_label.cget("text")
        self.label_text_field3 = self.root.field3_label.cget("text")
        self.label_text_field4 = self.root.field4_label.cget("text")
        self.label_text_field5 = self.root.field5_label.cget("text")
        self.label_text_field6 = self.root.field6_label.cget("text")
        self.label_text_field7 = self.root.field7_label.cget("text")
        self.label_text_field8 = self.root.field8_label.cget("text")
        self.label_text_outParamNum = self.root.outParamNum_label.cget("text")

        
        self.val_url=self.root.url_entry.get()
        self.val_actioncode=self.root.actioncode_entry.get()
        self.val_mobile=self.root.mobile_entry.get()
        self.val_field1=self.root.field1_entry.get()
        self.val_field2=self.root.field2_entry.get()
        self.val_field3=self.root.field3_entry.get()
        self.val_field4=self.root.field4_entry.get()
        self.val_field5=self.root.field5_entry.get()
        self.val_field6=self.root.field6_entry.get()
        self.val_field7=self.root.field7_entry.get()
        self.val_field8=self.root.field8_entry.get()
        self.val_outParamNum=self.root.outParamNum_entry.get()
        
        print(self.label_text_url + '='+self.val_url+'\n'+self.label_text_actioncode+'='+self.val_actioncode+'\n'+self.label_text_mobile+'='+self.val_mobile+'\n'+
              self.label_text_field1+'='+self.val_field1+'\n'+self.label_text_field2+'='+self.val_field2+'\n'+self.label_text_field3+'='+self.val_field3+'\n'+
              self.label_text_field4+'='+self.val_field4+'\n'+self.label_text_field5+'='+self.val_field5+'\n'+self.label_text_field6+'='+self.val_field6+'\n'+
              self.label_text_field7+'='+self.val_field7+'\n'+self.label_text_field8+'='+self.val_field8+'\n'+self.label_text_outParamNum+'='+self.val_outParamNum+'\n')
        paramList = [self.label_text_url,self.val_url],[self.label_text_actioncode,self.val_actioncode],[self.label_text_mobile,self.val_mobile],[self.label_text_field1,self.val_field1],[self.label_text_field2,self.val_field2],[self.label_text_field3,self.val_field3],[self.label_text_field4,self.val_field4],[self.label_text_field5,self.val_field5],[self.label_text_field6,self.val_field6],[self.label_text_field7,self.val_field7],[self.label_text_field8,self.val_field8],[self.label_text_outParamNum,self.val_outParamNum]
        print(paramList)
        print(self.cleanParam(paramList))
        self.doGenerate(self.cleanParam(paramList))

    def clickReset(self):
        self.root.url_entry.delete(0,tk.END)
        self.root.actioncode_entry.delete(0,tk.END)
        self.root.mobile_entry.delete(0,tk.END)
        self.root.field1_entry.delete(0,tk.END)
        self.root.field2_entry.delete(0,tk.END)
        self.root.field3_entry.delete(0,tk.END)
        self.root.field4_entry.delete(0,tk.END)
        self.root.field5_entry.delete(0,tk.END)
        self.root.field6_entry.delete(0,tk.END)
        self.root.field7_entry.delete(0,tk.END)
        self.root.field8_entry.delete(0,tk.END)
        

    def pcakSubGroup(self):
        self.frame_input.grid(row=0,column=0)
        self.frame_input.grid_propagate(0)
        self.frame_output.grid(row=0,column=1)
        self.frame_output.grid_propagate(0)
        
        self.root.url_label.grid(row=0,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.url_entry.grid(row=0,column=1,padx=10,pady=10)
        
        self.root.actioncode_label.grid(row=1,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.actioncode_entry.grid(row=1,column=1,padx=10,pady=10)

        self.root.mobile_label.grid(row=2,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.mobile_entry.grid(row=2,column=1,padx=10,pady=10)

        self.root.field1_label.grid(row=3,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.field1_entry.grid(row=3,column=1,padx=10,pady=10)

        self.root.field2_label.grid(row=4,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.field2_entry.grid(row=4,column=1,padx=10,pady=10)

        self.root.field3_label.grid(row=5,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.field3_entry.grid(row=5,column=1,padx=10,pady=10)
        
        self.root.field4_label.grid(row=6,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.field4_entry.grid(row=6,column=1,padx=10,pady=10)

        self.root.field5_label.grid(row=7,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.field5_entry.grid(row=7,column=1,padx=10,pady=10)

        self.root.field6_label.grid(row=8,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.field6_entry.grid(row=8,column=1,padx=10,pady=10)

        self.root.field7_label.grid(row=9,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.field7_entry.grid(row=9,column=1,padx=10,pady=10)

        self.root.field8_label.grid(row=10,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.field8_entry.grid(row=10,column=1,padx=10,pady=10)

        self.root.outParamNum_label.grid(row=11,column=0,sticky=tk.E,padx=10,pady=10)
        self.root.outParamNum_entry.grid(row=11,column=1,padx=10,pady=10)

        self.root.outPut_text.grid(row=1,column=0,padx=10,sticky=tk.W,pady=10)

        tk.Button(self.frame_input,text='Generate',width='20',command=self.clickGenerate).grid(row=12,column=0,columnspan=2,padx=10,pady=10)
        tk.Button(self.frame_input,text='Reset',width='20',command=self.clickReset).grid(row=13,column=0,columnspan=2,padx=2,pady=10)

        




def main():
    gui = Gui()
    gui.pcakSubGroup()
    tk.mainloop()
   

if __name__ == "__main__":
    main()
