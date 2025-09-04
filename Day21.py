
def insert_at_bottom(stack, item):
    if not stack:  
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)

recursion
def reverse_stack(stack):
    if not stack:   stack
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)



stack1 = [3, 2, 1]
reverse_stack(stack1)
print("Case 1 Output:", stack1)   


stack2 = [5]
reverse_stack(stack2)
print("Case 2 Output:", stack2)   


stack3 = [-5, -10, -15]
reverse_stack(stack3)
print("Case 3 Output:", stack3)   


stack4 = []
reverse_stack(stack4)
print("Case 4 Output:", stack4)   


stack5 = [3, 3, 3]
reverse_stack(stack5)
print("Case 5 Output:", stack5)   
  
