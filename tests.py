import pytest
from tree import Tree

@pytest.fixture
def simple_tree():
    tree = Tree()
    for i in range(1, 11):
        tree.add(i)
    return tree

def test_in_tree(simple_tree):
    node = simple_tree.find(5)
    assert node is not None and node.data == 5

def test_not_in_tree(simple_tree):
    assert simple_tree.find(20) is None
