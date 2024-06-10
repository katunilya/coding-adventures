from __future__ import annotations

import random
from collections import deque
from dataclasses import dataclass, field
from typing import Iterable, Self, cast

import rich


@dataclass(slots=True)
class TreeNode[_TValue]:
    value: _TValue
    parent: TreeNode[_TValue] | None = None
    children: list[TreeNode[_TValue]] = field(init=False, default_factory=list)

    def add_child(self, value: _TValue) -> Self:
        self.children.append(TreeNode(value=value, parent=self))
        return self

    def iter_children(self, *, reverse: bool = False) -> Iterable[TreeNode[_TValue]]:
        for _child in reversed(self.children) if reverse else self.children:
            yield _child


def iter_bfs[_TValue](root: TreeNode[_TValue]) -> Iterable[TreeNode[_TValue]]:
    _queue = deque()

    _queue.append(root)

    while _queue:
        _current = _queue.popleft()
        _current = cast(TreeNode[_TValue], _current)

        yield _current

        for _child in _current.iter_children():
            _queue.append(_child)


def iter_dfs[_TValue](root: TreeNode[_TValue]) -> Iterable[_TValue]:
    _queue = deque()

    _queue.append(root)

    while _queue:
        _current = _queue.popleft()
        _current = cast(TreeNode[_TValue], _current)

        yield _current

        for _child in _current.iter_children(reverse=True):
            _queue.appendleft(_child)


if __name__ == "__main__":
    _root = TreeNode(0).add_child(1).add_child(2).add_child(3)

    for _child in _root.iter_children():
        for _i in range(1, random.randint(1, 3) + 1):
            _child.add_child(_child.value * 10 + _i)

    rich.print(_root)
    for _node in iter_dfs(_root):
        print(_node.value, _node.parent)
