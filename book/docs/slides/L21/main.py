import matplotlib.pyplot as plt
import pandas as pd


def main():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/thohan88/covid19-nor-data/1d53c3ed8b6bc404eef54956e07deaea76c8ef1a/data/01_infected/msis/municipality_wide.csv"
    )
    breakpoint()


if __name__ == "__main__":
    main()
