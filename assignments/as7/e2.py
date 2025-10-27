names=set()
while (name:=input("Enter a name: "))!="":
    print("New name added" if name not in names else "Name already exists")
    names.add(name)
print("All names entered:", ", ".join(names))
# --- a/file:///c%3A/Users/LOQ/Documents/webdev/testingtesting/assignments/as7/e2.py
# +++ b/file:///c%3A/Users/LOQ/Documents/webdev/testingtesting/assignments/as7/e2.py
# @@ -1,1 +1,2 @@
# +names=set()