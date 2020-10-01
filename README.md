# python_text_prediction
Python text-prediction program based on an input corpus.

This program takes a text file and generates
a sentence based on the writing style of the
corpus using a stochastic selection over the
frequency of words following one another. It
can either take a filename from the command
line or use a default file, set in the main()
function.

The main() function is deliberately simple;
the bulk of the work is done by the
go(filename) function so it is easily
available to other programs, rather than
being necessarily stand-alone.
