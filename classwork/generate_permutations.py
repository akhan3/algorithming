#!/usr/bin/env python3


def generate_permutations(S, s=0):
    if s == len(S):
        print(S)
        return
    for k, _ in enumerate(S[s:]):
        swap(S, s, s + k)
        generate_permutations(S, s + 1)
        swap(S, s, s + k)


def swap(S: list, s: int, k: int):
    tmp = S[k]
    S[k] = S[s]
    S[s] = tmp


if __name__ == "__main__":
    generate_permutations(list("abc"))
    print("----------------------------------------------------")
    generate_permutations([10, 20, 30, 40])
