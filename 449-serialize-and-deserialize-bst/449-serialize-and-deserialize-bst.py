# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    start: 22:34
    end:   23:09
    
    sol 1. serialize: Traverse the bst inorder, save every node value to a string,      -> [2,1,3,4,5] -> "2,1,4,*,5,"*",3"  - TC O(N), SC O(N)
           deserealize: Traverse the string inorder, built the tree from string values  -> "2,1,4,*,5,"*",3" -> [2,1,3] - TC O(N), SC O(N)
                                                                                            ^
           corner cases -> how to process 2-digit, 3 digit, 4 digit values(separate with comma)
    """
    def __init__(self,):
        self.index = 0

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        nodes = [] # 2, 1, 4, *, 5, *, 3, *
        self.inorder_bst_to_str(root, nodes)
        print(",".join(nodes))
        return ",".join(nodes)
    
    def inorder_bst_to_str(self, root, nodes):
        if not root:
            nodes.append("*")
            return
        
        nodes.append(str(root.val))
        self.inorder_bst_to_str(root.left, nodes)
        self.inorder_bst_to_str(root.right, nodes)
        
    def inorder_bst_from_str(self, tree_string):
        if self.index >= len(tree_string):
            return None
        
        val = tree_string[self.index]
        self.index += 1
        if val == "*":
            return None
        
        tree = TreeNode(val)
        tree.left = self.inorder_bst_from_str(tree_string)
        tree.right = self.inorder_bst_from_str(tree_string)
        return tree

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # 2, 1, 4, *, 5, *, 3, *
        #    ^
        # [2,1,3,4,5]
        self.index = 0
        tree = self.inorder_bst_from_str(data.split(","))
        return tree

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans