from code import Solution, Solution2

def main():
    tests = [121,
            -121,
            10,
            -101]
    answers = [True,False,False,False]

    for i,t in enumerate(tests):
        result = Solution().isPalindrome(t)
        if result == answers[i]:
            print('{} Passed'.format(i+1))
        else:
            print('{} Failed'.format(i+1))

if __name__=="__main__":
    main()