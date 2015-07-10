def main():

##copied from the internet
    L = []
    for n in range(1, 101):
        for p in range(1, 101):
            x = pow(n, p)
            x = str(x)
            if len(x) == p:
                L.append(p)
                print x
    print "Answer = ", len(L)

