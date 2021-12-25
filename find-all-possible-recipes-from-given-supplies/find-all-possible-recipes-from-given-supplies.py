class Solution:
    NOT_VISITED = 0
    VISITED = 1
    VISITING = 2
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        Approach:
            Topological sort
        
        Examples
        ["bread","sandwich","burger"], 
        ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], 
        supplies = ["yeast","flour","meat"]
        
        
        burger: ["sandwich","meat","bread"]
        sandwich: ["bread","meat"]
        bread: ["yeast","flour", sandwich]
        
        status:
            bread: NOT_VISITED  # VISITING   
            sandwich: NOT_VISITED 
            burger: NOT_VISITED
            
            yeast: VISITED
            meat: VISITED
            flour: VISITED
            
        TC O(V+E)
        SC O(V+E)
        """
        
        ingredients_graph = {recipe: ingredients[i] for i, recipe in enumerate(recipes)}
        status = {recipe: self.NOT_VISITED for i, recipe in enumerate(recipes)}

        for supply in supplies:
            status[supply] = self.VISITED
        
        made_recipies = []
        for recipe in recipes:
            possible = self.dfs(recipe, ingredients_graph, status)
            if possible: made_recipies.append(recipe)
        return made_recipies
    
    
    def dfs(self, node, graph, status):
        if node not in status:
            return False
        
        if status[node] == self.VISITING:
            return False
        if status[node] == self.VISITED:
            return True

        status[node] = self.VISITING
        for next_node in graph.get(node, []):
            possible = self.dfs(next_node, graph, status)
            if not possible: return False

        status[node] = self.VISITED
        return True

        
        