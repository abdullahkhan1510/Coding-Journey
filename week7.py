
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if not "." in ip:
         return False
    parts = ip.split(".")
    if not len(parts) == 4:
         return False
    prt1, prt2, prt3, prt4 = parts
    try: 
        prt1 = int(prt1)
        prt2 = int(prt2)
        prt3 = int(prt3)
        prt4 = int(prt4)
    except ValueError:
         return False
    if prt1 < 0 or prt1 > 255:
        return False
    elif prt2 < 0 or prt2 > 255:        
        return False
    elif prt3 < 0 or prt3 > 255:
            return False
    elif prt4 < 0 or prt4 > 255:
            return False
    else:
         return True
    
if __name__ == "__main__":
    main()