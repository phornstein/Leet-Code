from code import Solution

def main():

    cases = [[1,1,2],[0,0,1,1,1,2,2,3,3,4],[1],[]]
    results = [2,5,1,0]

    for i,c in enumerate(cases):
        if Solution().removeDuplicates(c) == results[i]:
            print('True')
        else:
            print('False {} {}'.format(c,results[i]))

if __name__ == "__main__":
    main()

