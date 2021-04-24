from code import Solution

def main():

    tests = [([1,3],[2]),
            ([1,2],[3,4]),
            ([0,0],[0,0]),
            ([],[1]),
            ([2],[])]
    answers = [2.00000,2.5000,0.00000,1.00000,2.00000]

    for i,t in enumerate(tests):
        result = Solution().findMedianSortedArrays(t[0],t[1])
        if result == answers[i]:
            print('{} Passed'.format(i+1))
        else:
            print('{} Failed'.format(i+1))

if __name__=="__main__":
    main()