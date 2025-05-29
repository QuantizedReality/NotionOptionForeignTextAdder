from add_paragraph import add_paragraph
from add_todo import add_todo 
from add_bullet import add_bullet

print("Welcome to SwampCats Notion input thingy!")

token = input("Enter your Notion Internal Integration Secret: ")
page_id = input("Enter your notion page ID: ")

print("\nChoose a block Type:")
print("1. Paragraph")
print("2. To-Do")
print("3. Bullet List")

choice = input("CHOOOSE ONE NOW: ")

text = input("\nWHADDYA WANNA SAY: ")

if choice == "1":
    add_paragraph(token, page_id, text)
elif choice == "2":
    add_todo(token, page_id, text)
elif choice == "3":
    add_bullet(token, page_id, text)
else:
    print("FU#K YOU")

