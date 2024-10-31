import os
import random
import pandas
from argparse import ArgumentParser

def make_parquet_files(outdir, n_files):
    # each file has 100 rows
    n_rows = 10000
    os.makedirs(outdir, exist_ok=True)
    for i in range(n_files):
        df = pandas.DataFrame({
            'col_0': [random.random() for _ in range(n_rows)],
            'col_1': [random.choice(['A', 'B', 'C']) for _ in range(n_rows)],
            'col_2': [random.randint(1, 1000) for _ in range(n_rows)]
        })
        df.to_parquet(f'{outdir}/data_{i}.parquet')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('outdir', type=str)
    parser.add_argument('n_files', type=int)
    args = parser.parse_args()
    make_parquet_files(args.outdir, args.n_files)