'''

encourages developers to avoid duplicating code in a system. The main idea behind DRY is to reduce redundancy and promote efficiency by ensuring that a particular piece of knowledge or logic exists in only one place within a codebase. When developers adhere to the DRY principle, they aim to create reusable components, functions, or modules that can be utilized in various parts of the codebase. This not only makes the code more maintainable but also minimizes the chances of errors since changes or updates only need to be made in one location.

DRY is closely related to the concept of modular programming and the creation of functions, classes, or modules that encapsulate specific functionality. By following DRY, developers can enhance code readability, decrease the likelihood of bugs caused by inconsistent updates, and facilitate easier maintenance and collaboration within a development team. An alternative principle, the "Single Responsibility Principle" (SRP), is often mentioned in conjunction with DRY. SRP suggests that a module, class, or function should have only one reason to change, further emphasizing the need for focused, modular, and reusable code. Together, DRY and SRP contribute to creating more robust and maintainable software systems.

'''


# ❌ Repeated string escaping
def save_user_bad(name):
    with open("u.txt","a") as f:
        f.write(name.replace("\n","") + "\n")

def save_post_bad(title):
    with open("p.txt","a") as f:
        f.write(title.replace("\n","") + "\n")

# ✅ DRY: factor out common cleanup
def sanitize(s): return s.replace("\n","")

def save_user(name):
    with open("u.txt","a") as f:
        f.write(sanitize(name) + "\n")

def save_post(title):
    with open("p.txt","a") as f:
        f.write(sanitize(title) + "\n")
