# Totally-Good-Permutations
-------------------------------------------
Online python compiler
-------------------------------------------

Imagine you have an alphabet of n distinct letters. There are of course n! permutations of this alphabet. For simplicity in this kata we will always use the first n letters from the uppercase alphabet 'ABCDEF...XYZ'.

Now imagine that you are also given a list of "bad subpermutations", each of length 1 <= length <= n.

For example if n=7 then alphabet = 'ABCDEFG', and you could be given bads = ['BA','CF','EFA','DGFECB'].

We shall say that an individual permutation of alphabet is "totally good" if - when viewed as a string - it does not contain any of the given bad subpermutations as a substring.

For a given bads list, how many of the n! permutations of alphabet are totally good ?

Example
Let's take n=3, so alphabet = 'ABC', and bads = ['AB','CA'].

Then, considering all n! = 3! = 6 permutations of 'ABC' as strings we have:

'ABC' # contains 'AB' from bads as a substring
'ACB' # does not contain 'AB', does not contain 'CA', so: TOTALLY GOOD
'BAC' # TOTALLY GOOD
'BCA' # contains 'CA' from bads
'CAB' # contains 'CA', 'AB' from bads
'CBA' # TOTALLY GOOD
So for this given bads list, only 3 of the permutations of alphabet are totally good.

Inputs and Outputs
You will be given an alphabet as a string of n distinct characters. For simplicity we will work with the first n letters from the uppercase alphabet, and with 3 <= n <= 26, so a valid input might be the string 'ABCDEFGH' with n=8 for example.

You will also be given a list of strings, bads, representing the bad subpermutations as defined above.

To avoid boring input validation, you can be sure that:

all elements in bads will be distinct, so e.g. ['ABC','ABC'] will not occur.
none of the elements in bads list will contain repeated letters, e.g. a string like 'DDACB' will never appear in bads since clearly it can't appear in any permutation of the distinct letters 'ABCDE' for example.
none of the elements in bads list will contain letters that are not in the input alphabet - for example, if alphabet = 'ABCD' then bads will not contain 'ABZ' or 'ZYXK' etc. since these have some or all of their letters that do not belong to 'ABCD'.
You must return an integer, the count of how many of the n! permutations of alphabet are totally good, given the bads list as defined above.

Performance requirements
I have tried to arrange the fixed tests in order of "tricky-ness" for your convenience while solving - hopefully you will fail them "in order" and understand what is going wrong step by step.

The basic tests will be all with small to medium sized alphabets, n <= 8, and with small bads lists with around 4 to 10 elements: this is so that you can debug using brute force approach, if needed.

The full tests will involve up to n=26 alphabets and bads lists with up to 12 elements, such that brute force approaches will time out.

Acknowledgements
Thanks to @monadius, @Voile, and @dfhwze for early testing, for suggestions and feedback, and to @monadius again for speeding up the reference solution.

Similar katas
I thought of this kata while trying several approaches when working on these 2 difficult katas:

The position of a digital string in a infinite digital string

Permutation-free strings

It didn't help me directly, but it did up being a fun problem in its own right. If you get stuck on this, maybe working on the above 2 will help? Or if you solved this easily, maybe you'll enjoy those 2?


