# Coding bat practice

- Summer 2020 (COVID-19 pandemic)
- URL: https://codingbat.com/java


# Reflections

### General points
- I used `String.indexOf() == 0` method throughout to check for a matching
    character or substring at the beginning of the string at hand.
    In retrospect, however, I should have used `String.startsWith()` method instead because
    it would have taken O(1) as opposed to O(n) for `indexOf()`.

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
- Then I looked at the official solution and it blew my mind that they solved the problem
    in a completely stateless manner.
- There I learned the technique that after reaching the opening parentheses via head pointer,
     tail pointer can also be advanced to reach for the closing parentheses.
- This was such an elegant solution and was contained in 2 if branches and a base case.
- Interestingly, in such situations, the base case was towards the end after the
    recursive conditions fall through and just returned the remaining string after the
    head and tail pointers trimmed it to just what was required.

### `strCopies`
- Similar was the case for `strCopies` in which I had to count the number of copies,
    so I thought that it could not be done without maintaining a counter (state).
- It was illuminating to see that the official solution again managed to solve it
    without maintaining any state.
- They elegantly decremented argument `n` in recursive calls when a substring match
    was detected and terminated recursion as soon as n reached zero. __Mind = blown!__
