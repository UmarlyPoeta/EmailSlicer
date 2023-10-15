import re 
import sys



def main():
    email=input("Whats your email: ")
    print(EmailSlicer(email))


def EmailSlicer(e):
    s=dict()
    time=re.search(r"([\w\d_]+)@([\w.]+.[\w.]+)",e,flags=re.IGNORECASE)
    if time:
        s["username"]=time.group(1)
        s["domain"]=time.group(2)
        return s
    else:
        raise ValueError


if __name__=="__main__":
    main()