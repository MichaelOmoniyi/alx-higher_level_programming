# 0x13. JavaScript - Objects, Scopes and Closures
This directory contains javaScript scripting based on classes, scopes and closures.

## Tasks
* [ 0-rectangle.js ](./0-rectangle.js) - Contains empty class Rectangle that defines a rectangle.

* [ 1-rectangle.js ](./1-rectangle.js) - Writes a class Rectangle that defines a rectangle:
    * The class notation must be used in defining your class
    * The constructor takes 2 arguments w and h
    * Initialize the instance attribute width with the value of w
    * Initialize the instance attribute height with the value of h

* [ 2-rectangle.js ](./2-rectangle.js) - Writes a class Rectangle that defines a rectangle:
    * The class notation must be used for defining your class
    * The constructor takes 2 arguments w and h
    * Initialize the instance attribute width with the value of w
    * Initialize the instance attribute height with the value of h
    * If w or h is equal to 0 or not a positive integer, an empty object is created

* [ 3-rectangle.js ](./3-rectangle.js) - Writes a class Rectangle that defines a rectangle:
    * The class notation must be used for defining your class
    * The constructor takes 2 arguments w and h
    * Initialize the instance attribute width with the value of w
    * Initialize the instance attribute height with the value of h
    * If w or h is equal to 0 or not a positive integer, an empty object is created
    * Creates an instance method called print() that prints the rectangle using the character X

* [ 4-rectangle.js ](./4-rectangle.js) - Writes a class Rectangle that defines a rectangle:
    * The class notation must be used for defining your class
    * The constructor takes 2 arguments w and h
    * Initialize the instance attribute width with the value of w
    * Initialize the instance attribute height with the value of h
    * If w or h is equal to 0 or not a positive integer, an empty object is created
    * Creates an instance method called print() that prints the rectangle using the character X
    * Creates an instance method called rotate() that exchanges the width and the height of the rectangle
    * Creates an instance method called double() that multiples the width and the height of the rectangle by 2

* [ 5-square.js ](./5-square.js) - Writes a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
    * The class notation must be used for defining your class and extends
    * The constructor takes 1 argument: size
    * The constructor of Rectangle is be called (by using super())

* [ 6-square.js ](./6-square.js) - Writes a class Square that defines a square and inherits from Square of 5-square.js.:
    * The class notation must be used for defining your class and extends
    * Creates an instance method called charPrint(c) that prints the rectangle using the character c
    * If c is undefined, the character X is used

* [ 7-occurrences.js ](./7-occurrences.js) - Writes a function that returns the number of occurrences in a list:
    * Prototype: exports.nbOccurences = function (list, searchElement)

* [ 8-esrever.js ](./8-esrever.js) - Writes a function that returns the reversed version of a list:
    * Prototype: exports.esrever = function (list)
    * The built-in method reverse is not used.

* [ 9-logme.js ](./9-logme.js) - Writes a function that prints the number of arguments already printed and the new argument value. (see example below)
    * Prototype: exports.logMe = function (item)
    * Output format: <number arguments already printed>: <current argument value>

* [ 10-converter.js ](./10-converter.js) - Writes a function that converts a number from base 10 to another base passed as argument:
    * Prototype: exports.converter = function (base)
