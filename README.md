# Arithmetic: A Programmatic Approach

### What is this?
What is [linked](project.pdf) is an experiment where I construct programs according to certain rules. While I do not list what these rules are, the following are a sketch of the sort of rules I have in mind:
* The instruction "verify that a=a" is legal if it occurs after "choose an integer a"
* The instruction "verify that b=a" is legal if it occurs after "verify that a=b"
* The instruction "verify that a=c" is legal if it occurs after "verify that a=b" and "verify that b=c"
* The instruction "verify that (a+b)+c=a+(b+c)" is legal if it occurs after "choose integers a,b,c"

### Why was this made?
I made this because I want to see whether programs constructed according to certain rules can show their own potential to achieve their objectives on different inputs. In other words, I want to see whether programs can be constructed in such a way as to render a correctness proof unnecessary.

### How do I understand this?
The task of understanding the following procedures should be the same as that of understanding any codebase. Hence domain specific knowledge is required, which in this case comprises rational, formal polynomial, and matrix arithmetic as well as inequalities. Otherwise, running a debugger, that is, executing the following procedures step by step on some chosen input(s) and observing their control flows and sequences of program states should be equally helpful in making sense of them.
