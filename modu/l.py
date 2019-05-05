import os, sys

print ("\033[1;32mMasukan username dan paswrod")
print ("\033[1;31mSalah auto pecah pala kau :v")
print ("\033[0;36mKalau Gak tau Pm gue")
print ("\033[0;36mFb Yordan Penceng")
username = 'starla'
password = 'lojomblo'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("user : ")
        if uname == username:
                pwd = raw_input("pass : ")

                if pwd == password:
                        print "\n\033[1;34mYess kata sandi salah TAPI BOONG ;D",
                        sys.exit()

                else:
                        print "\n\033[1;36msalah goblok paswordlu ;)\033[00m"
                        print "Tebak Ulang\n"
                        restart()

        else:
                print "\n\033[1;36mSAlah Guoblokk maaf ngeggas :v\033[00m"
                print "coba Lagi dong\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()
