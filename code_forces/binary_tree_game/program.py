"""
"""



def binary_tree_game(rootNode, tree):

    def countCompleteBinaryTree(node, tree):
        if node is None: return 0

        children = tree.get(node, [])
        if len(children) == 0:
            return 1

        leftChild = children[0]    
        leftCBT = countCompleteBinaryTree(leftChild, tree)
        totalCBT = leftCBT

        if len(children) == 2:
            rightChild = children[1]
            rightCBT = countCompleteBinaryTree(rightChild, tree)
            totalCBT = leftCBT + rightCBT

            if leftCBT and rightCBT:
                totalCBT += 1

        return totalCBT

    totalCBT = countCompleteBinaryTree(rootNode)
    if totalCBT % 2 == 1: return "ALICE"
    else: return "BOB"
