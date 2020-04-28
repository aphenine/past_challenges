# Atkis Coding Test

## All

Programs are self-executing modules.

Unit tests are in the tests directory and use the UnitTest framework.

Note: All file paths are currently hard-coded for this challenge.  All paths are assumed to be from the project root, 
so please set up your environment accordingly.  The paths have been designed to work on Windows and *Nix machines.    

## Median

Given an input file, produce (to the stdout) a list of the medians, as running values during the computation.

Notes: uses bisect to speed up insertion into the sorted array (otherwise, it takes forever to run large umber test cases).

## Mouse vs Mouse

A program to take in sentences and work out whether the mouse in question is a computer mouse or an animal.

I don't know enough about language processing to solve this elegantly, so I've gone for a brute-force first approach 
which passes all the tests.  It manages to do this by checking certain words in the sentence and working out whether 
the word is computer or animal related.  There are undoubtedly more elegant ways to do this.