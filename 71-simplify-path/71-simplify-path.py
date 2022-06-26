class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        "/home//foo/../bar/baz/../../."
        
        /home
        
        stack approach
        """
        
        dirs = path.split("/")
        dirs = [d for d in dirs if d and d != "."]
        
        final_path = []
        
        for d in dirs:
            if d == "..":
                if final_path:
                    final_path.pop()
            else:
                final_path.append(d)      
        return "/" + "/".join(final_path)