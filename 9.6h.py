"""
9.6 Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n-pairs of parentheses.
EXAMPLE:
input: 3 (e.g., 3 pairs of parentheses)
output: ((())), (()()), (())(), ()(()), ()()()

(, left = 1, right = 0
((, left = 2, right = 0
((), left = 2, right = 1
(()(, left = 3, right = 1
(()(), left = 3, right = 2
(()()), left = 3, right = 3

1. Left Paren: As long as we haven't used up all the left parentheses, we can always
insert a left paren.
2. Right Paren: We can insert a right paren as long as it won't lead to a syntax error.
When will we get a syntax error? We will get a syntax error if there are more right parentheses than left.

Because we insert left and right parentheses at each index in the string,
and we never repeat an index, each string is guaranteed to be unique.

"""

def foo(output, open, close, pairs):
    """
    The recursion is taking advantage of the fact that you can never add more opening brackets than the
    desired number of pairs, and you can never add more closing brackets than opening brackets.
    """
    if open == pairs and close == pairs:
        print output
    else:
        if open<pairs:
            foo(output+'(', open+1, close, pairs)
        if close<open:
            foo(output+')', open, close+1, pairs)

foo('$', 0, 0, 3)
