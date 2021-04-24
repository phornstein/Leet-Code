from code import Solution

def main():

    tests = [[1,2,3],
            [0,1],
            [1]]

    answers = [[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
            [[0,1],[1,0]],
            [[1]]]

    for i,t in enumerate(tests):
        result = sorted(Solution().permute(t))
        ans = sorted(answers[i])
        print(result,ans)
        if result == ans:
            print('Pass')
        else:
            print('Fail')

if __name__=="__main__":
    main()