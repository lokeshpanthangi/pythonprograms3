from collections import deque

# Initialize history and forward stack
history = deque(maxlen=5)
forward_stack = deque()

# Add New Page
def add_new_page(url):
    history.append(url)
    forward_stack.clear()  # Clear forward stack when a new page is added

# Go Back
def go_back():
    if history:
        last_page = history.pop()
        forward_stack.append(last_page)

# Go Forward
def go_forward():
    if forward_stack:
        last_backed_out_page = forward_stack.pop()
        history.append(last_backed_out_page)

# Maintain State
def print_state():
    print("Current History:", list(history))
    print("Forward Stack:", list(forward_stack))

# Example Usage
add_new_page("page1.com")
add_new_page("page2.com")
add_new_page("page3.com")
add_new_page("page4.com")
add_new_page("page5.com")
add_new_page("page6.com")  # This will remove "page1.com" from history
print_state()

go_back()
print_state()

go_forward()
print_state()