def alpha_beta_search(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    if maximizing_player:
        value = float('-inf')
        for child in get_children(node):
            value = max(value, alpha_beta_search(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = float('inf')
        for child in get_children(node):
            value = min(value, alpha_beta_search(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

def is_terminal(node):
    return isinstance(node, int)

def evaluate(node):
    return node

def get_children(node):
    return [node - 1, node - 2] if isinstance(node, int) and node > 0 else []

# Example usage:
initial_node = 10
alpha = float('-inf')
beta = float('inf')
depth = 4

best_value = alpha_beta_search(initial_node, depth, alpha, beta, True)
print("Best value:", best_value)