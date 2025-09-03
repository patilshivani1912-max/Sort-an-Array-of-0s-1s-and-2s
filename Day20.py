def sorted_insert(stack, element):
    
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    
    temp = stack.pop()
    sorted_insert(stack, element)

   
    stack.append(temp)


def sort_stack(stack):
    
    if not stack:
        return

    
    temp = stack.pop()

    
    sort_stack(stack)

    
    sorted_insert(stack, temp)




stack1 = [3, 1, 4, 2]
sort_stack(stack1)
print(stack1)  

stack2 = [7, 1, 5]
sort_stack(stack2)
print(stack2)  

stack3 = [5]
sort_stack(stack3)
print(stack3)  

stack4 = [-3, 14, 8, 2]
sort_stack(stack4)
print(stack4)  

stack5 = []
sort_stack(stack5)
print(stack5)  

stack6 = [3, 3, 3]
sort_stack(stack6)
print(stack6)  
  
