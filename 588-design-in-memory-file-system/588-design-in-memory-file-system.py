class File:
    def __init__(self, file_name, content):
        self.file_name = file_name
        self.content = [content]
        self.is_file = True

class Dir:
    def __init__(self,):
        self.subdirs = defaultdict(Dir)
        self.is_file = False
        

class FileSystem:
    """
     /
      /a
        /b
          /c
          /d = content
      /g
        /f = content
      /h
    
    
    """

    def __init__(self):
        self.dirs = Dir()
        

    def ls(self, path: str) -> List[str]: # /
        parts = path.split("/")
        root = self.dirs
        if path == "/":
            return sorted(root.subdirs[""].subdirs.keys(), key=lambda x: x)
        
        for part in parts: 
            if part not in root.subdirs:
                return []
            root = root.subdirs[part]
        if root.is_file:
            return [root.file_name]
        return sorted(root.subdirs.keys(), key=lambda x: x)

    def mkdir(self, path: str) -> None:  # "/a/b/c"
        parts = path.split("/")
        #print("parts", parts)
        root = self.dirs
        #print("root.subdirs", root.subdirs)
        for part in parts:  # "", "a", "b", "c"
            if part not in root.subdirs:
                root.subdirs[part] = Dir()
            #print(root.subdirs)
            root = root.subdirs[part]
        #print("self.dirs.subdirs", self.dirs.subdirs)

    def addContentToFile(self, filePath: str, content: str) -> None: #"/a/b/d"
        parts = filePath.split("/")
        file_name = parts.pop()
        root = self.dirs
        for part in parts:   # "", "a", "b",
            if part not in root.subdirs:
                root.subdirs[part] = Dir()
            root = root.subdirs[part]
        if file_name in root.subdirs:
            root.subdirs[file_name].content.append(content)
        else:
            root.subdirs[file_name] = File(file_name, content)
        
    def readContentFromFile(self, filePath: str) -> str: #"/a/b/d"
        parts = filePath.split("/")
        root = self.dirs
        for part in parts:
            if part not in root.subdirs:
                return ""
            root = root.subdirs[part]

        return "".join(root.content)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
"""
Test-Cases:
    ["FileSystem","ls","mkdir",      "mkdir",    "mkdir",    "addContentToFile",  "ls", "ls",   "addContentToFile", "readContentFromFile" , "ls", "ls",              "ls",          "ls"]
    [[],          ["/"],["/a/b/c"], ["/a/b/c/f"],["/a/b/c/g"],["/a/b/d","hello"],["/"], ["/a/b"], ["/a/b/d","world"], ["/a/b/d"],             ["/a/b/d"], ["/a/b/c"], ["/a/b/c/f"],["/a/b/d"]]
    ["FileSystem","mkdir","ls","ls","mkdir","ls","ls","addContentToFile","readContentFromFile","ls","readContentFromFile"]
    [[],["/zijzllb"],["/"],["/zijzllb"],["/r"],["/"],["/r"],["/zijzllb/hfktg","d"],["/zijzllb/hfktg"],["/"],["/zijzllb/hfktg"]]
"""