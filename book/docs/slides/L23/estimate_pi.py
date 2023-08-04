# estimate_pi.py
def estimate_pi(N: int) -> float:
    pi_forth = 0.0
    for n in range(N):
        pi_forth += (-1.0) ** n / (2.0 * n + 1.0)
    return pi_forth * 4


def main(argc: int, argv: list[str]) -> int:
    N = int(argv[1])
    print(f"\u03C0 = {estimate_pi(N)}")
    return 0


if __name__ == "__main__":
    import sys

    main(len(sys.argv), sys.argv)
