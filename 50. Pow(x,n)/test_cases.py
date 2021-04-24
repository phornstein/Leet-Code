from code import Solution

def main():

    tests = [[2.00000,10]]

    answers = [1024.00000]

    for i,t in enumerate(tests):
        result = Solution().myPow(t[0],t[1])
        if result == answers[i]:
            print('{} Pass'.format(i+1))
        else:
            print('{} Fail'.format(i+1))

if __name__=="__main__":
    main()

