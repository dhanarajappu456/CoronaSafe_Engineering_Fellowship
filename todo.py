import sys as s
import os
from datetime import datetime as dt
class todo:
    def __init__(self):
        path=os.getcwd()+'\\'
        temp = []       
        if(len(s.argv)==1 or s.argv[1] == 'help'):
         s.stdout.buffer.write('Usage :-\n'.encode())
         s.stdout.buffer.write('{0:26}{1:<0}\n'.format(r'$ ./todo add "todo item"', '# Add a new todo').encode())
         s.stdout.buffer.write('{0:26}{1:<0}\n'.format(r'$ ./todo ls', '# Show remaining todos').encode())
         s.stdout.buffer.write('{0:26}{1:<0}\n'.format(r'$ ./todo del NUMBER', '# Delete a todo').encode())
         s.stdout.buffer.write('{0:26}{1:<0}\n'.format(r'$ ./todo done NUMBER', '# Complete a todo').encode())
         s.stdout.buffer.write('{0:26}{1:<0}\n'.format(r'$ ./todo help', '# Show usage').encode())
         s.stdout.buffer.write('{0:26}{1:<0}\n'.format(r'$ ./todo report', '# Statistics').encode())
        elif(s.argv[1]=='add'):
            lines = []
            if(len(s.argv)>=3):
             if(len(s.argv) > 3):
              s.argv[2] = s.argv[2][1:]
              s.argv[len(s.argv)-1] = s.argv[len(s.argv)-1][:-1]
              string = " ".join(s.argv[2:])
             elif(len(s.argv)==3):
              string = s.argv[2].strip("'")
             print('Added todo: "{}"'.format(string))
             f = open(path+'todo.txt', 'a+')
             f.write(string+'\n')
             f.close()
            else:
                print("Error: Missing todo string. Nothing added!")
        
        elif(s.argv[1] == 'ls'):

             try:
                f = open(path+'todo.txt', 'r')
             except:
                print('There are no pending todos!')
                exit()
             lines = f.readlines()
             cnt = len(lines)
             for i in lines[::-1]:
               s.stdout.buffer.write("[{0}] {1}\n".format(cnt, i[:len(i)-1]).encode())
               cnt -= 1
             f.close()        
        elif(s.argv[1] == 'del'):
            try:
                no = int(s.argv[2])
            except:
                print("Error: Missing NUMBER for deleting todo.")
                s.exit()
            f = open(path+'todo.txt', 'r')
            
            lines = f.readlines()         
            if(no>=1 and no<=len(lines)):
                f.close()
                print('Deleted todo #{}'.format(no))
                del lines[no-1] 
                f = open(path+'todo.txt', 'w+')
                for i in lines:
                    f.write(i)
                f.close()
            else:
                print('Error: todo #{} does not exist. Nothing deleted.'.format(no))
        elif(s.argv[1]=='done'):
            try:
                no = int(s.argv[2])
            except:
                print("Error: Missing NUMBER for marking todo as done.")
                s.exit()
            f = open(path+'todo.txt', 'r')
            lines = f.readlines()
            f.close()
            if(no>=1 and no<=len(lines)):
                f=open(path+'todo.txt','w')
                f2=open(path+'done.txt','a+')        
                print('Marked todo #{} as done.'.format(no))
                f2.write('x  '+str(dt.now())[:10]+'  '+lines[no-1])
                del lines[no-1]
                for i in lines:
                    f.write(i)
                f.close()       
                f2.close()
            else:
                print('Error: todo #{} does not exist.'.format(no))        
        elif(s.argv[1]=='report'):
            f=open(path+'todo.txt','r')
            f2=open(path+'done.txt','r')
            pending=len(f.readlines())
            completed=len(f2.readlines())       
            f.close()
            f2.close()
            print('{0} Pending : {1} Completed : {2}'.format(str(dt.now())[:10],pending,completed))
if __name__=='__main__':
    todo()

'''
This code is by Dhanaraj S
Rajiv Gandhi Institute Of Technology,Kottayam
for more checkout my github
https://github.com/dhanarajappu456
'''

    
    
    
