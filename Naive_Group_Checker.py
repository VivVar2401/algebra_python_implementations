from asteval import Interpreter
aeval = Interpreter()

def group_checker(nums, op):
    # Check Closure
    for i in nums:
        for j in nums:
            if op(i, j) not in nums:
                print(f"Not a Group: Fails Closure at {i}, {j}")
                return
    print("Closure found")
    # Check Identity
    identity = "DnE"
    for i in nums:
        if all(op(i, a) == a and op(a, i) == a for a in nums):
            identity = i
            break
    if identity == "DnE":
        print("Not a Group: No Identity")
        return
    print("Identity:",identity)
    
    # Check Inverse
    for i in nums:
        check = False
        for j in nums:
            if op(i, j) == identity:
                check = True
        if check == False:
            print(f"Not a Group: No Inverse for {i}")
            return
    print("Inverses found")
    
    # Check Associativity
    for i in nums:
        for j in nums:
            for k in nums:
                if op(i, op(j,k)) != op(op(i, j), k):
                    print("Not a Group: No Associativity")
                    return
    print("Associativity found")
    print("Is a Group")
    # Check Commutativity
    for i in nums:
        for j in nums:
            if op(i, j) != op(j, i):
                print("Is Not Abelian")
                return
    print("Is Abelian")
    return
    
def execute():
    nums = [int(i) for i in input("Please enter values of a group: ").split()]
    op_inp = input("Please enter your function in terms of x and y: ")
    op = aeval(f"lambda x, y: ({op_inp})")
    group_checker(nums, op)