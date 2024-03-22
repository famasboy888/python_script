import getpass

def main():
    password=getpass.getpass()
    print(getpass.getuser(),password)

if __name__ == '__main__':
    main()
else:
    quit()