# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #use a list as a stack, append to push, pop to pop,use a loop to see all tokens, push integers and use the pop command to complete the operations
    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9

    stack = []

    for token in tokens:
        if token=="+":
            b=stack.pop()
            a=stack.pop()
            stack.append(a+b)
        elif token=="-":
            b=stack.pop()
            a=stack.pop()
            stack.append(a-b)
        elif token=="*":
            b=stack.pop()
            a=stack.pop()
            stack.append(a*b)
        elif token=="/":
            b=stack.pop()
            a=stack.pop()
            stack.append(int(a/b))
        else:
            stack.append(int(token))

    return stack[0]
    pass


def decode_string(s):
    # Outline:
    #   turn stack into a list, track string and count, loop through the characters in s, consider multip digit numbers, [ save everything with push, ] pop the saved stuff and repeat
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"

    stack_string=[]
    stack_count=[]
    current_string=""
    count=0

    for ch in s:
        if ch in "0123456789":
            count=count*10+int(ch)
        elif ch=="[":
            stack_string.append(current_string)
            stack_count.append(count)
            current_string=""
            count=0
        elif ch=="]":
            repeat_times=stack_count.pop()
            prev_string=stack_string.pop()
            current_string=prev_string+current_string*repeat_times
        else:
            current_string=current_string+ch
    return current_string
    pass


def daily_temperatures(temps):
    # Outline:
    #   make answer list full of 0's, make empty stack as a list, loop through days, while loops for when stack isnt empty and temp is warmerthe top stck, push index rro stack and return answwr after its been replaced
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    n = len(temps)
    answer=[0]*n
    stack=[]

    for i in range(n):
        while len(stack)>0 and temps[i]> temps [stack[-1]]:
            prev_day=stack.pop()
            answer[prev_day]=i-prev_day
        stack.append(i)
    return answer

    pass


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   make a list of 0's the same length as temps, loop through each day, make a while loop ( stack isnt empty and temp is warmerthan the top temp in the stack), pop and reset answer, push the current temp on the stack to be saved fpr later, return answer.
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
