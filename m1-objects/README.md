# Notes on M1

The example contains a base main file as well as a class header (which needs getters and setters)

Counterexample: (what we're not doing)
parallel arrays / vectors would be like this:
- list of course names (string)
- list of course codes (string)
- list of credit values (int)

the issue here is that the correspondence is by index. For example
"Data Structures", "C++", "C++"
"CSC 249-0901", "CSC 134-0001", "CSC 134-0901"
3, 3, 3

if I sort the names alphabetically, they no longer match up with their associated data!

so instead I'd want to make *objects* which contain all the data for a course
and once I've done that, put those in a list

Object 1: "Data Structures", "CSC 249-0901", 3
Object 2: "C++", "CSC 134-0001", 3
Object 3: "C++", "CSC 134-0901", 3

# getters and setters

Now we want to make the objects manage their internal state
reminder: objects have state (variables) and behavior (methods)

We will start with the existing Course.h, and below the definition, start
implementing each of the needed functions.
see reference from Gaddis C++ Language Companion page 99-100

# topics to come back to
* default constructor vs. parameter constructors
* ... is one the "right" way? it depends