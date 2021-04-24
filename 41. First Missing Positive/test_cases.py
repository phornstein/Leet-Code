
from code import Solution

def main():
    tests = [[1,2,0],
            [3,4,-1,1],
            [7,8,9,11,12],
            [1],
            [3],
            [-1,-2,-60,40,43]]

    answers = [3,2,1,2,1,1]

    for i,t in enumerate(tests):
        result = Solution().firstMissingPositive(t)
        if result == answers[i]:
            print('{} Pass'.format(i+1))
        else:
            print('{} Fail'.format(i+1))

if __name__=="__main__":
    main()