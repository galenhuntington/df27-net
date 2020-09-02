This is a toy project where I tried training a neural network to
guess whether a set of Y-chromosome STR values from an R1b-DF27+
testee belongs to the subclade Z196+.

To use it, you must have and provide all 111 values, in the standard
FTDNA order.  If values are unknown/missing or not from a DF27+ testee,
the results will of course be meaningless.

If a kit has an unusual number of markers (such as other than four
DYS464 values), it won't work either.  In the future, I may create
networks without this limitation.

Run `net.py` using Python 3.  Enter the values, and it will tell you
what it thinks.  It achieved more than 93%+ accuracy on the test set.

Reference: [R-DF27 project DNA
results](https://www.familytreedna.com/groups/r1b-df27/dna-results)

