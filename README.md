# LC
## Lunar Calculator

Have you ever wished you had a command line calculator that could do all of your important base 10 lunar arithmetic based accounting?

https://arxiv.org/abs/1107.1130

Well now you can have one with the popular command line utility `lc`. Using `lc` you can accurately and quickly do lunar addition, multiplication, and exponentiation all in the command line as well as execute complex, next generation code based in lunar arithmetic.

Here is an example of a usual user session:
```
$ lc
> 2 1 +
2
> 2 2 +
2
> 57 19 +
59
> 17 24 *
124
> wtf!
?
> q
?
> h
?
> help
?
> please just let me out
?
> sudo rm -rf --no-preserve-root /
?
```
As you can see, `lc` has helpful, ed-like error reporting, not overwhelming the user with error messages while still helpfully flagging errors.

`lc` also serves as an interpreter REPL for the extended `lc` language as defined below:

### Syntax Overview:
To make programming easier all builtin functions in the `lc` language use ascii non-alphanumeric characters to represent symbols in a terse, easy to understand syntax. The syntax for the lc language is designed to be compliant with the Linear Non-stopping Integrated System Environment (LINENOISE) syntax standard. Using the LINENOISE standard complex operators such as COMEFROM can be reduced to short instructions such as <@ allowing for terse, clear, TECO-like syntax. Many other languages such as most regular expression syntaxes, Mathematica, Perl, APL, and Python also follow the LINENOISE standard for syntax, allowing developers to feel right at home in lc.

### Control Flow:
Control flow is conducted using the "come from" construct, conveniently shortened to <@ and ?<@ for "come from" and "conditional come from" respectively. These constructs set a point in the CMFRM_TAB lookup table and when the reference symbol is reached the program jumps back to the line with the CMFRM command. Other control flow options include %$#@& which is the CRZY function, 

For further details on conditionals and boolean values, view the "Boolean Logic" section of the manual.

### Boolean Logic:
Note that the `lc` language uses binary logic based upon lunar primality where if a number is a decimal lunar prime it is true, else it is false. Lunar primes are the set of all numbers that contain the character '9' in their decimal representation. Thus 19 1999 9 92 29 and other values are considered to be equivalent to true by the language, whereas 1, 2, 3, 5, 7, 13 and so on are not true since they are all composite numbers.

### Eval
Loved by security experts, eval is an essential feature in the `lc` language, used as the basis of all function calls in the language it allows you to evaluate a string from the input.

### Symbol Reference Table:
| symbol | args         | description                                                                               |
|:-------|:-------------|:------------------------------------------------------------------------------------------|
| +      | int, int     | conducts lunar addition of the ints                                                       |
| *      | int, int     | conducts lunar multiplication of of the ints                                              |
| ^      | int, int     | raises the first int to the lunar power of the second int                                 |
| ?      | nil          | requests user input                                                                       |
| =      | val, val     | compares two values on the stack, places true on the stack if true, else false            |
| \=     | val, val     | compares two values on the stack, places true on the stack if true, else false            |
| >      | int, int     | compares two ints and returns true if the first int is greater than the second            |
| <      | int, int     | compares two ints and returns true if the first int is lesser than the second             |
| v      | bool, bool   | returns true if either of its arguments are true                                          |
| &      | bool, bool   | returns true if both of its arguments are true                                            |
| ~      | bool         | returns true if the bool is false, else returns false                                     |
| :=     | val, atom    | places val as equal to the atom provided                                                  |
| \$     | string       | evaluates the string provided as code                                                     |
| ?\$    | bool, string | evaluates the string provided as code should the bool be true                             |
| @      | atom         | checks if the atom provided is in the CMFRM table and jumps to relevant address if it is  |
| <@     | atom         | adds label to CMFRM table and jumps from label to current instruction if label is reached |
| ?<@    | bool, atom   | executes CMFRM if boolean value is true, else nothing                                     |
| !%     | nil          | gets a random value from the program stack and places it on the top of the program stack  |
| !>     | int          | prints the top value on the stack                                                         |
| !#     | int, int     | swaps two values on the stack given their offsets from the top of the stack               |
