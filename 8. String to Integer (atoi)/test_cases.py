from code import Solution

def main():
    tests = ["-91283472332",
            "words and 987",
            "4193 with words",
            "   -42",
            "42",
            "",
            "+-12"]

    answers = [-2147483648,
            0,
            4193,
            -42,
            42,
            0,
            0]

    for i,t in enumerate(tests):
        result = Solution().myAtoi(t)
        if result == answers[i]:
            print('{} Pass'.format(i+1))
        else:
            print('{} Fail'.format(i+1))

if __name__=="__main__":
    main()