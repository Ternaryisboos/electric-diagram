_author_ = 'Yansuirong'
#dao bao 
import sys
#def lei
def test():
    #sys.argv function(han shu)
    args = sys .argv
    #if judge(pan duan) args == 1
    if len(args) == 1:
        #zhi xing 
           print('Hello,word!!')
    elif len(args) == 2:
            print("Hello,%s" % args[1])
    else:
             print('T00 many arguments!')

if _author_ == '_yangsuirong_':
    test()