from collections import deque

issuing_book_line = deque()

print("Students queuing to be issued boooks")
issuing_book_line.append("Ezekiel")
issuing_book_line.append("Munyendo")
issuing_book_line.append("Ateya")

print("Current line from front to the rear:  {list(issuing_book_line)}\n")
print("Rules for issuing books is (First in First out!!)")

first_issued = issuing_book_line.popleft()
print(f"{first_issued } got a book entitled (Captured by Raiders)")
print(f"Remaing students are: {list(issuing_book_line)}\n")

second_issued = issuing_book_line.popleft()
print(f"{second_issued } got a book entitled (MOnkey Town)")
print(f"Remaing student is: {list(issuing_book_line)}\n")

print("A new student joins the queue!!")
issuing_book_line.append("Hellen")
print(f"Hellen joined the queue from the rear:")
print(f"Current queue => {list(issuing_book_line)}")


