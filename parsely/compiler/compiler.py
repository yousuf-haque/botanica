from typing import *

from parsely.parser.ast_node import *


class Compiler:
    def __init__(self, ast: ASTNode):
        self._bytecode = []
        self._ast = ast
    def compile(self) -> List[Tuple[str, Optional[int]]]:
        if len(self._bytecode) == 0:
            self._visit(self._ast)
        return self._bytecode

    def _visit(self, node: ASTNode):
        if isinstance(node, Num):
            self._visit_num(node)
        elif isinstance(node, BinOp):
            self._visit_bin_op(node)
        else:
            raise Exception(f'Found unrecognized AST Node type: {node.__class__.__name__}')

    def _visit_num(self, node: Num):
        self._bytecode.append(('PUSH', node.value))

    def _visit_bin_op(self, node: BinOp):

        self._visit(node.left)
        self._visit(node.right)

        if node.op.type == 'PLUS':
            self._bytecode.append(('ADD',))
        else:
            raise Exception(f"Unsupported operator: {node.op.type}")
