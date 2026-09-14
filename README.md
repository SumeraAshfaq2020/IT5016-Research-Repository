RESEARCH REPOSITORY 

Introduction 

This repository contains my practice and research work for Assessment 3. It demonstrates and explains the programming concepts I have learned through different activities. 

The repository includes Python programs covering basic programming, conditional statements, functions, data structures, validation, and Object-Oriented Programming (OOP). 

The purpose of this repository is to connect my practical work with software design principles and explain how these principles can improve code reading, reuse, maintenance, and organization. 

Programming Concepts  

The following concepts have been demonstrated: 

Variables and data types 

User input and output 

Arithmetic and comparison operators 

Conditional statements (if, Elif, else) 

Functions and function calls 

Parameters and arguments 

Return values 

Local and global variables 

Lists  

Loops 

Input validation and error handling 

Classes and objects 

 Attributes and methods 

Object-Oriented Programming (OOP) 

 

 

 

CODE ANALYSIS 

Basics and Operators 

FILE: 01        Basics_and_Operators/variables_input_output.py 

Python provides different built-in data types and operators for working with values and performing calculations (Python Software Foundation, 2026). 

A simple structure is used to make it understandable for everyone. Meaningful variable names such as first_number, second_number, and addition to display and make the code easier to understand and maintain. 

The program could be improved by adding input validation to handle invalid user input. 

Conditional Statements 

FILE: 02    Conditional_Statements/conditional_statements.py 

This program demonstrates decision-making using if, elif, and else. Conditional statements allow a program to execute different blocks of code depending on whether conditions are true or false (Python Software Foundation, 2026). 

Using conditional statements keeps decision-making logical. The structure can be improved in a big program by placing repeated decision logic inside reusable functions. 

Functions and Variables 

FILE: 03    Functions_and_Variables/functions_parameters.py 

This program demonstrates functions, parameters, arguments, return values, local variables, and global variables. Python functions are defined using the def keyword and can receive parameters and return values (Python Software Foundation, 2026). 

The add_numbers() function separates the calculation from the main program. This improves modularity and allows the function to be reused with different numbers. 

The example also demonstrates the difference between local and global variables. Local variables are associated with the function in which they are created, while variables can also be defined in a wider scope (Python Software Foundation, 2026). 

The program could be improved by adding stronger input validation and handling invalid input. 

Data Structures and Validation 

FILE: 04    Data_Structures_and_Validation/inventory_system.py 

This program demonstrates the use of lists, functions, parameters, return values, variables, arithmetic operations, and a global variable for generating unique item IDs. 

Python lists can store multiple values in a single collection and support operations such as adding and accessing elements (Python Software Foundation, 2026). 

The inventory list allows multiple items to be stored in one collection. The add_inventory_item() function keeps the item-creation process organized and reusable. Calculating the total value using quantity and price demonstrates the use of arithmetic operations in a practical situation. 

The use of separate functions improves modularity because each function has a specific purpose. The program could be improved further by adding stronger input validation and error handling to prevent invalid quantity or price values. 

Object-Oriented Programming  

FILE: 05    Object_Oriented_Programming/banking_system.py 

The Banking System demonstrates Object-Oriented Programming using classes, objects, attributes, methods, and the __init__ method. Python classes provide a way to bundle data and functionality together, while class instances can contain attributes and methods (Python Software Foundation, 2026). 

The Account class keeps account information and banking operations together, while the Customer class stores customer information. This demonstrates encapsulation because related data and behavior are organized within classes. 

Methods such as deposit(), withdraw(), and display_balance() give each class a clear responsibility. This improves modularity and maintainability because changes to one operation can be made without changing the whole program. 

Improvements can be made by adding stronger input validation and separating user interaction from the banking logic. 

 

 

Object-Oriented Programming  

FILE: 05    Object_Oriented_Programming/library_system.py 

The Library Management System demonstrates classes, objects, attributes, methods, lists, loops, and conditional statements. Python classes allow data and functionality to be grouped into objects, with methods providing operations related to those objects (Python Software Foundation, 2026). 

The Book, Member, and Library classes have different responsibilities. The Library class manages books and members, while the Book and Member classes store related information. 

Using separate classes improves organization and readability. The borrow_book() and return_book() methods provide specific operations, which supports modularity and makes the program easier to maintain. 

The program could be improved by adding input validation, checking whether a member exists before borrowing, and preventing invalid return operations. 

Software Design Principles 

The code in this repository demonstrates several software design principles that can help make programs easier to understand, reuse, test, and maintain. 

1. Modularity 

Modularity means dividing a program into smaller parts that perform specific tasks. Breaking software into separate components can make individual parts easier to understand, modify, and maintain. 

The functions used in the Functions, Inventory, and OOP programs demonstrate modularity. For example, the add_inventory_item() function is responsible for creating and storing an inventory item, while display_inventory() is responsible for displaying the stored information. 

Using smaller modules makes the code easier to understand and modify. 

 

 

 

2. Single Responsibility 

The Single Responsibility Principle means that a function or class should have a clear and focused responsibility. 

This principle can be seen in the banking and library programs. For example, the deposit() method is responsible for adding money, while the withdraw() method handles withdrawals. 

Keeping responsibilities separate makes the code easier to maintain and reduces unnecessary changes. 

3. Reusability 

Reusable code can be used more than once without rewriting the same logic. Functions are useful for this purpose because the same function can be called with different arguments (Python Software Foundation, 2026). 

Functions such as add_numbers() and add_inventory_item() demonstrate reusability because they accept parameters and can work with different values. 

Using functions and methods instead of repeating code improves efficiency and makes future changes easier. 

4. Readability 

Readable code is easier for other programmers to understand. 

Meaningful names such as first_number, second_number, inventory, account_number, and borrowed_books make the purpose of variables clear. 

Comments are also used throughout the programs to explain important sections of the code. Python's documentation also recommends clear naming, comments, spacing, and documentation strings as good programming practices (Python Software Foundation, 2026). 

5. Maintainability 

Maintainable code is easier to update, fix, and improve. 

The programs are separated into functions and classes where appropriate. This means that a particular part of the program can be changed without rewriting the entire program. 

For example, additional banking operations could be added as methods to the Account class. 

Using smaller, well-organized functions and classes can support easier maintenance as a program grows. 

 

6. Encapsulation 

Encapsulation is an important OOP concept where related data and behavior are grouped together inside a class. Python classes provide a mechanism for bundling data and functionality together (Python Software Foundation, 2026). 

The Banking System demonstrates this through the Account class, which stores account information and provides methods such as deposit(), withdraw(), and display_balance(). 

The Library System also uses encapsulation by grouping book information inside the Book class and member information inside the Member class. 

 

Design Patterns 

Design patterns are common and reusable approaches to solving recurring software design problems. They provide general solutions or blueprints rather than complete programs. 

 

Strategy Pattern 

The Strategy Pattern is a behavioural design pattern that separates different algorithms or behaviors so that they can be used interchangeably. 

The Banking System has separate methods such as deposit() and withdraw() for different banking operations. Although the current program does not fully implement the Strategy Pattern, separate operations show an opportunity for this type of design. 

For a larger banking application, different transaction behaviors could be separated into their own strategies. This could make the system easier to extend when new transaction types are added. 

Design Pattern and My Practice 

My current programs are beginner-level examples, so they mainly demonstrate programming principles rather than complete design pattern implementations. 

Through research, I learned that design patterns provide general solutions to recurring design problems and can become more useful as software becomes larger and more complex. 

For my current practice, focusing on modularity, single responsibility, reusability, readability, maintainability, and encapsulation provides a strong foundation for using design patterns in future projects. 

References / Research Sources 

The following sources were used to research Python programming concepts, Object-Oriented Programming, software design principles, programming practices, and design patterns. 

Python Software Foundation (2026).  

https://docs.python.org/3/tutorial/controlflow.html 

 

Python Software Foundation (2026)​Click or tap here to enter text.​ 

​​https://docs.python.org/3/tutorial/classes.html​ 

 

 
