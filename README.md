# Strictured Programming

### What is this?
What is [linked](project.pdf) is an experiment where I construct programs according to certain rules. While I do not list what these rules are, the following are a sketch of the sort of rules I have in mind:
* The instruction "verify that a=a" is legal if it occurs after "choose an integer a"
* The instruction "verify that b=a" is legal if it occurs after "verify that a=b"
* The instruction "verify that a=c" is legal if it occurs after "verify that a=b" and "verify that b=c"
* The instruction "verify that (a+b)+c=a+(b+c)" is legal if it occurs after "choose integers a,b,c"

### Why was this made?
I wanted to see whether programs constructed according to certain rules can serve a similar function to mathematical proofs. For example, let A be the 100\*100 matrix containing the multiplication table up to 100. At least to me, seeing the form of procedure 22 allows me to be confident enough to bet that det(A^2)=det(A)^2 without carrying out the necessary computations. And if they should not turn out to be equal, then I would conclude that the rules according to which I made procedure 22 were inappropiate for the purposes of evidence.

### How do I understand this?
The task of understanding the following procedures should be the same as that of understanding any codebase. Hence domain specific knowledge is required, which in this case comprises rational, formal polynomial, and matrix arithmetic as well as inequalities. Otherwise, running a debugger, that is, executing the following procedures step by step on some chosen input(s) and observing their control flows and sequences of program states should be equally helpful in making sense of them.
