def main():
    T = set((n * (n + 1) / 2) for n in range(2, 180000))
    P = set((n * ((3 * n) - 1) / 2) for n in range(2, 180000))
    H = set((n * ((2 * n) - 1)) for n in range(2, 180000))
    for item in T:
        if item in P and item in H:
            print "You found one"
            print item
        else:
            continue
 
if __name__ == '__main__':
    main()