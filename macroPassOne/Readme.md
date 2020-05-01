# Implementation of PASS-1 Macro Processor and updation of its database. MDT,MNT,ALA and MDTC,MNTC.

A Macro instruction is the notational convenience for the programmer. For every occurrence of macro the whole macro body or macro block of statements gets expanded in the main source code. Thus Macro instructions makes writing code more convenient.
Silent features of Macro Processor:

•	Macro represents a group of commonly used statements in the source programming language.
•	Macro Processor replace each macro instruction with the corresponding group of source language statements. This is known as expansion of macros.
•	Using Macro instructions programmer can leave the mechanical details to be handled by the macro processor.
•	Macro Processor designs are not directly related to the computer architecture on which it runs.
•	Macro Processor involves definition, invocation and expansion.

Macro Processor is a program that lets you define the code that is reused many times giving it a specific Macro name and reuse the code by just writing the Macro name only.
There are three main steps of using a macro.

1.Define the macro name
2.Give it's definition
3.Use the macro name from with in the program anywhere to use it's definetion (this step is called macro call)
