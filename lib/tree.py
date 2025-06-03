class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._dfs(self.root, id)

    def _dfs(self, node, target_id):
        # Base case: current node matches the target id
        if node["id"] == target_id:
            return node

        # Recursive case: check each child
        for child in node.get("children", []):
            result = self._dfs(child, target_id)
            if result:
                return result

        # If not found
        return None
