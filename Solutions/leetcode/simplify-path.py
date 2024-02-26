class Solution:
    def simplifyPath(self, path: str) -> str:
        newPath = path.split("/")

        pathStack = []

        for char in newPath:
            if char == "..":
              if pathStack:
                pathStack.pop()
            elif char != "" and char != ".":
                pathStack.append(char)
        return "/" + "/".join(pathStack)
        

        