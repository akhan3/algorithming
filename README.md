# Coding bat practice

- Summer 2020 (COVID-19 pandemic)
- URL: https://codingbat.com/java


# Reflections
### `parenBit`
- My solution to `parenBit` was based on propagating a state variable `hot` across
    recursive calls to indicate if we were inside parenthesis.
- So I had to make an aux function that accepted the state variable as an additional
    argument and wrapped it
    inside the main function while initializing it with `false`.
- I thought , while solving the problem, that it could not be done without maintaining state.
- My solution works, though it has 4 `if-else-if` branches in addition to the
    base condition, so can certainly be refactored.
- These habits came from my background in modeling hardware state machines in FPGA,
    a situation which require the programmer to be more explicit in specifying their intent.
-
