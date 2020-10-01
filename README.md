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


Source for 'text.txt' (Gettysburg address): https://rmc.library.cornell.edu/gettysburg/good_cause/transcript.htm#:~:text=%22Fourscore%20and%20seven%20years%20ago,so%20dedicated%2C%20can%20long%20endure.

Source for 'text2.txt' (The Iliad): http://www.gutenberg.org/files/2199/2199-h/2199-h.htm
