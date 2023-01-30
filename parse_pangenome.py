import re, sys, getopt, statistics, os
import pandas as pd

# The input TSV file is not the pan-genome file produced when running GENESPACE, but the "pangenome" object written into a TSV file.

pg_df = pd.read_csv(sys.argv[1], sep='\t')

# 1. Get the number of single-species orthogroups - entries represented by a single species.

filtered_df = pg_df[(pg_df.iloc[:, 3:].notnull().sum(axis=1) == 1)]
filtered_df['combined'] = filtered_df.iloc[:, 3:].astype(str).apply('_'.join, axis=1)
print(f'total single-species orthogroups: {filtered_df.shape[0]} \n')

# 2. Get the number of singletons - entries represented by a single gene from a single species.
## a. Get the total number of singletons.

filtered_df = filtered_df[(filtered_df['combined'].str.contains('\|') < 1)]

print(f'overall singletons: {filtered_df.shape[0]} \n')

## b. Get the number of singletons for each organism in the pan-genome.

for col in filtered_df.iloc[:, 3:-1]:
    print(f'{col} : {filtered_df[col].notnull().sum()}')

# 3. Get the number of orthogroups with at least one gene from each annotation present

filtered_df = pg_df[(pg_df.iloc[:, 3:].notnull().sum(axis=1) == len(pg_df.columns)-3)]
filtered_df['combined'] = filtered_df.iloc[:, 3:].astype(str).apply('_'.join, axis=1)
print(f'orthogroups with all annotations present: {filtered_df.shape[0]} \n')

# 4. Get the number of single-copy orthogroups - where each entry contains a single gene from each species.

filtered_df = filtered_df[(filtered_df['combined'].str.contains('\|') < 1)]

print(f'overall single-copy orthogroups: {filtered_df.shape[0]} \n')
