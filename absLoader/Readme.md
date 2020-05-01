# Design of an Absolute Loader

There are two types of loaders, relocating and absolute. The absolute loader is the simplest and quickest of the two. The loader loads the file into memory at the location specified by the beginning portion (header) of the file, then passes control to the program. If the memory space specified by the header is currently in use, execution cannot proceed, and the user must wait until the requested memory becomes free.

Allocation, linking, relocation are function of absolute loader besides loading.

An absolute loader is the simplest of loaders. Its function is simply to take the output of the assembler and load it into memory. The output of the assembler can be stored on any machine-readable form of storage, but most commonly it is stored on punched cards or magnetic tape, disk, or drum.

Loader:-
A loader is a system program, which takes the object code of a program as input and prepares it for execution. Programmers usually define the program to be loaded at some predefined location in the memory. But this loading address given by the programmer is not being coordinated with the OS.

Relocation:-
Relocation is the process of assigning load addresses to position-dependent, but locatable code of a program and adjusting the code and data in the program to reflect the assigned addresses.

Linking:-
Linker is a program that takes one or more objects generated by a compiler and combines them into a single executable program. Loader is the part of an operating system that is responsible for loading programs from executable into memory, preparing them for execution and then executing them.