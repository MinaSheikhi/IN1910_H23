import pstats


def main():
    stats = pstats.Stats("drunk.cprof")
    # Sorter på total tid og viser topp 10
    stats.sort_stats(pstats.SortKey.TIME).print_stats(10)
    # Sorter på total tid og viser kun metoder i filen drunk.py
    stats.sort_stats(pstats.SortKey.TIME).print_stats("drunk.py")
    # breakpoint()


if __name__ == "__main__":
    main()
