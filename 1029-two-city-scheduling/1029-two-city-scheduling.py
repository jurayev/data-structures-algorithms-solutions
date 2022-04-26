class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        [[184,139],,,,,]
        [840,118] [259,770] [448,54] [926,667] [577,469] [184,139]
        a = 2
        b = 0
        
        259 + 577 + 184
        118 + 54 + 667
        """
        
        costs.sort(reverse=True, key=lambda x: abs(x[0]-x[1]))
        
        n = len(costs)
        a_tickets = n // 2
        b_tickets = n // 2
        total_costs = 0
        
        for a_cost, b_cost in costs:
            if a_cost < b_cost:
                if a_tickets > 0:
                    total_costs += a_cost
                    a_tickets -= 1
                else:
                    total_costs += b_cost
                    b_tickets -= 1
            else:
                if b_tickets > 0:
                    total_costs += b_cost
                    b_tickets -= 1
                else:
                    total_costs += a_cost
                    a_tickets -= 1
        return total_costs