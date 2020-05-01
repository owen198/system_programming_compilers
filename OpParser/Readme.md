# Design and Implementation of Operator Precedence Parser.

A grammar that is used to define mathematical operators is called an operator grammar or operator precedence grammar. Such grammars have the restriction that no production has either an empty right-hand side (null productions) or two adjacent non-terminals in its right-hand side.
An operator precedence parser is a bottom-up parser that interprets an operator grammar. This parser is only used for operator grammars. Ambiguous grammars are not allowed in any parser except operator precedence parser.
There are two methods for determining what precedence relations should hold between a pair of terminals:

1.	Use the conventional associativity and precedence of operator.
2.	The second method of selecting operator-precedence relations is first to construct an unambiguous grammar for the language, a grammar that reflects the correct associativity and precedence in its parse trees.

This parser relies on the following three precedence relations: ⋖, ≐, ⋗

a ⋖ b This means a “yields precedence to” b.
a ⋗ b This means a “takes precedence over” b.
a ≐ b This means a “has same precedence as” b.

Operator precedence parsers usually do not store the precedence table with the relations; rather they are implemented in a special way. Operator precedence parsers use precedence functions that map terminal symbols to integers, and the precedence relations between the symbols are implemented by numerical comparison. The parsing table can be encoded by two precedence functions f and g that map terminal symbols to integers. We select f and g such that:

1.	f(a) < g(b) whenever a yields precedence to b
2.	f(a) = g(b) whenever a and b have the same precedence
3.	f(a) > g(b) whenever a takes precedence over b
