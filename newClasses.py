import sys

def getClass(_id, name, _type, title, description):
    return f'''
    /**
     * {title}
     * <p>
     * {description}
     * 
     */
    @JsonProperty("{_id}")
    @JsonPropertyDescription("{description}")
    private {_type} {name};
    '''

def getGetAndSet(_id, name, _type, title, description):
    return f'''
    /**
     * {title}
     * <p>
     * {description}
     * 
     */
    @JsonProperty("{_id}")
    public {_type} get{name[0].upper()}{name[1:]}() {{
        return {name};
    }}

    /**
     * {title}
     * <p>
     * {description}
     * 
     */
    @JsonProperty("{_id}")
    public void set{name[0].upper()}{name[1:]}({_type} {name}) {{
        this.{name} = {name};
    }}
    '''

def getBuilders(namesArray):
    builder = ""
    for names in namesArray:
        builder = builder + f'.append("{names}", {names})'
    print("\n" + builder + "\n")
    builder = ""
    for names in namesArray:
        builder = builder + f'.append({names})'
    print("\n" + builder + "\n")
    builder = ""
    for names in namesArray:
        builder = builder + f'.append({names}, rhs.{names})'
    print("\n" + builder + "\n")



classArray = []

def createNewClass():
    print("\nplease enter the properties of the new class...")
    classDict = {
        "_id": input("id: "),
        "_type": input("type: "),
        "title": input("title: "),
        "description": input("description: ")
    }

    _id = classDict["_id"]

    while _id.find("_") != -1:
        index = _id.find("_")
        _id = _id[:index] + _id[index+1].upper() + _id[index+2:]
    
    classDict["name"] = _id

    classArray.append(classDict)

createNewClass()

while(True):
    print("\nDo the following... \n1: + Add another class \n2: Print classes \n3: Print getters and setters \n4: Print builders \n5: Exit\n")

    action = input("> ")

    if action == "1":
        createNewClass()

    if action == "2":
        for classes in classArray:
            print(getClass(classes["_id"], classes["name"], classes["_type"], classes["title"], classes["description"]))

    elif action == "3":
        for classes in classArray:
            print(getGetAndSet(classes["_id"], classes["name"], classes["_type"], classes["title"], classes["description"]))

    elif action == "4":
        namesArray = []
        for classes in classArray:
            namesArray.append(classes["name"])
        getBuilders(namesArray)
        
    elif action == "5" or action == "exit":
        sys.exit()