#!python3 
import sys , requests , re , threading

if len(sys.argv)<2:
    print("something is wrong !")
    sys.exit()

link = sys.argv[1]
wordlist = sys.argv[2]
wordlistopening = open(wordlist , 'r')
words = wordlistopening.read().splitlines()

code4=re.compile('4\d\d')
code3=re.compile('3\d\d')
code5=re.compile('5\d\d')

  
def dir_bruteforcing():
    print("Press CTRL + C to exit !!\n")
    try:
        for i in words:
            url  = '{0}/{1}'.format(link,i)
            res = requests.get(url)
            status = res.status_code
            co3 = code3.match(str(status))
            co4 = code4.match(str(status))
            co5 = code5.match(str(status))
            if(status == 200 or co3):
                print('Directory found : ' , url)
            elif(co4 or co5):
                pass
            else:
                print('This directory may be forbidden or there is a mistake !')

    except KeyboardInterrupt:
        print('\n ---- Stoping ... !! ')

    wordlistopening.close()

if __name__ == "__main__":
    thread = threading.Thread(target=dir_bruteforcing())
    thread.start()
    thread.join(3)
    