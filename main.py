import re 
import sys



def main():
    email=input("Whats your email: ")
    print(EmailSlicer(email))


def EmailSlicer(e):
    time=re.search(r"([\w\d_]+)@([\w.]+.[\w.]+)",e,flags=re.IGNORECASE)
    if time:
        return {"username":time.group(1),"domain":time.group(2)}
    else:
        raise ValueError


if __name__=="__main__":
    main()