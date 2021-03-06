# Filename:                double_stmt.py
# Author:                  Team 13
# Description:             local parser double statements
# Supported Language(s):   Python 3.x
# Time-stamp:              <2012-05-03 19:25:30 plt>

from local.localast import Node  # Node(type, children=None, value=None, line=None)


def p_double_stmt(p):
    """ double_stmt : ID MINUSMINUS %prec MINUSMINUS
                    | ID PLUSPLUS %prec PLUSPLUS"""
    if p[2] == "++":
        value = "%s += 1" % (p[1])
    elif p[2] == "--":
        value = "%s -= 1" % (p[1])
    p[0] = Node("double", None, value)
