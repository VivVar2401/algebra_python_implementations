from asteval import Interpreter
aeval = Interpreter()

def subg_checker(group, subgroup, oper):
    
    for i in subgroup:
        if i not in group:
            print("Not a subgroup")
            return
    for i in subgroup:
        if any(oper(i,j) not in subgroup for j in subgroup):
            print("Not a subgroup")
            return
    print("Subgroup")

def main():
    n = [int(i) for i in input("Group: ").split()]
    op_inp = input("Please enter your function in terms of x and y: ")
    try:
        op = aeval(f"lambda x, y: ({op_inp})")
        subg = [int(i) for i in input("Subgroup: ").split()]
    
        subg_checker(n, subg, op)
    except:
        print("Ensure your input function follows proper mathematical syntax")
