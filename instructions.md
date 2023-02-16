# Designing a Simple 2d Vector Class

## Instructions

- 2/14/23
    - Before changing **anything**, check out a new branch in which to work.

    - Write an `__init__` method for `Vector2d` that has positional parameters for the `x` and `y` components that correspond to the *instance variables* `self.x` and `self.y`

    - Write a `__repr__` method for the `Vector2d` class. A good general rule for `repr` is that it should produce a string similar to the code used to create the object it describes. For example, `repr(Vector2d(3,4))` could produce `'Vector2d(x=3, y=4)'`.

    - Write a `__str__` method for the `Vector2d` class such that `str(Vector2d(3, 4))` would return `'3i + 4j'`. (**i** and **j** are what many physicists and engineers use to denote the x and y directions)

    - Write an `__abs__` function that takes `self` as its only argument and returns the length of the hypotenuse of the right triangle with legs equal to `self.x` and `self.y`. For example, `abs(Vector2d(3, 4))` should return `5.0`.

    - Once you've finished today's work, commit your changes and push them to **your** repository.

- 2/16/23

    - The `__neg__` method determines the behavior of the *unary minus* (leading minus sign) on a `Vector2d` object.Write a `__neg__` method that takes `self` as its only argument and returns a `Vector2d` object with the signs for `x` and `y` negated. For example, `-Vector2d(3, 4)` would return `Vector2d(-3, -4)`.

    - The `__add__` method determines how the '+' symbol works between two `Vector2d` objects. Write an `__add__` method that has two arguments, `self` and `other`, and produces a `Vector2d` object with the correct components. Remember that when we add vectors, we simply add their like components. For example: `Vector2d(3, 4) + Vector2d(1, -1)` should return `Vector2d(4, 3)`, since `3 + 1 = 4` and `4 + -1 = 3`.

    - Once you've finished the day's work, commit your changes and push them to **your** repository.