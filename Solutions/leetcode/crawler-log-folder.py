class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folderStack = []
        for i in range(len(logs)):
            if logs[i] != "../" and logs[i] != "./":
                folderStack.append(logs[i]) 
            elif logs[i] == "../" and len(folderStack) > 0:
                folderStack.pop()
        return len(folderStack)

        