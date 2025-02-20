def unique_elements(arr):
    # შექმნით დიქშენარისგან განმეორებითი ელემენტების სათვალავი
    element_count = {}
    
    # გადავალაგოთ ყველა ელემენტი და აღვნიშნოთ რამდენჯერ გვხვდება თითოეული
    for elem in arr:
        if elem in element_count:
            element_count[elem] += 1
        else:
            element_count[elem] = 1
    
    # გამოვყოთ ის ელემენტები, რომლებიც მხოლოდ ერთხელ გვხვდებიან
    unique = [elem for elem, count in element_count.items() if count == 1]
    
    return unique
