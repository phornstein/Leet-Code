from code import Solution

def main():

    cases = ["III","LVIII","MCMXCIV"]
    results = [3,58,1994]

    for i,c in enumerate(cases):
        temp = Solution().romanToIntZip(c)
        #if Solution().romanToInt(c) == results[i]:
        if temp == results[i]:
            print('True')
        else:
            print('False {} {} {}'.format(temp,c,results[i]))

if __name__ == "__main__":
    main()

