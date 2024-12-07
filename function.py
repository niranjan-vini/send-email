def clean():
    with open (".txt","r") as file:
        todo=file.readlines()
        return todo

def bag(list):
    with open (".txt","w") as file :
        file.writelines(list)
