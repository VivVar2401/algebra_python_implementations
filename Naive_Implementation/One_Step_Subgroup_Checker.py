from asteval import Interpreter
aeval = Interpreter()

def find_identity(group, oper):
    for i in group:
        if all(oper(i, j) == j and oper(j, i) == j for j in group):
            return i
    print("NO IDENTITY")
    return "x"

def find_inverse(group, element, oper, ide):
    for i in group:
        if oper(i, element) == ide:
            return i
    print("NO INVERSE FOUND FOR", element)
    return 'x'

def subg_checker(group, subgroup, oper):
    if not subgroup:
        print("Not a subgroup")
        return
    
    ide = find_identity(group, oper)
    if ide == 'x':
        return
    
    for i in subgroup:
        if i not in group:
            print("ELEMENT NOT IN GROUP")
            return
        
    for b in subgroup:
        z = find_inverse(group, b, oper, ide)
        if z == 'x':
            return
        for a in subgroup:
            if oper(a,z) not in subgroup:
                print("Not a subgroup")
                return
            
    print("Is a subgroup")

def main():
    n = [int(i) for i in input("Group: ").split()]
    op_inp = input("Please enter your function in terms of x and y: ")
    op = aeval(f"lambda x, y: ({op_inp})")
    subg = [int(i) for i in input("Subgroup: ").split()]
    
    subg_checker(n, subg, op)
