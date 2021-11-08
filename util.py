class Util:
    def side_factory(self, type, currentNode, graph, targetFound, delay, checkNode):
        if (type == 'left'):
            if (currentNode.x > 0 and not targetFound):
                leftNode = graph.matrix[currentNode.x - 1][currentNode.y];
                if (checkNode(leftNode, currentNode, delay)):
                    print('cheguei ate aq!')
                    return leftNode

        if (type == 'right'):
            if (currentNode.x < 19 and not targetFound):
                rightNode = graph.matrix[currentNode.x + 1][currentNode.y];
                if (checkNode(rightNode, currentNode, delay)):
                    print('cheguei ate aq!')
                    return rightNode

        if (type == 'up'):
            if (currentNode.y > 0 and not targetFound):
                upNode = graph.matrix[currentNode.x][currentNode.y - 1];
                if (checkNode(upNode, currentNode, delay)):
                    print('cheguei ate aq!')
                    return upNode

        if (type == 'down'):
            if (currentNode.y < 19 and not targetFound):
                downNode = graph.matrix[currentNode.x][currentNode.y + 1];
                if (checkNode(downNode, currentNode, delay)):
                    print('cheguei ate aq!')
                    return downNode
