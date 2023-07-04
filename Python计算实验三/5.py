def printgraph():
    def print1():
      print('+','+','+',sep='----',end='\n')
    def print2():
            print('|','|','|',sep='    ',end='\n')
    for i in range(2):
        print1()
        for i in range(4):
            print2()
    print1()
if __name__=='__main__':
    printgraph()
