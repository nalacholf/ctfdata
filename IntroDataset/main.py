import os
import sys
import numpy as np
import pandas as pd

DEFAULT_PATH = "./200M_women.csv"
DEFAULT_RESULT_COLUMN = "Result"
DEFAULT_RUNNER = "Merlene OTTEY"

def import_data(csv_path):
    df = pd.read_csv(csv_path)
    rows_count, columns_count = df.shape
    print(f'df has {rows_count} rows and {columns_count} columns')
    return df

def average_fastness(df, result_column):
    mean_result = np.mean(df[result_column])
    return mean_result

def runner_stats(df, name, result_column):
    runner_df = df.loc[df["Name"] == name]
    fastest_time = min(runner_df[result_column])
    slowest_time = max(runner_df[result_column])
    mean_time = np.mean(runner_df[result_column])
    df_other_runners = df.loc[df["Name"] != name]
    mean_time_other_runners = np.mean(df_other_runners[result_column])
    return fastest_time, slowest_time, mean_time, mean_time_other_runners

def main(csv_path= None, result_column= None, runner_name = None):        
    print(f'Running {sys.argv[0]} on {csv_path}')
    df = import_data(csv_path)
    mean_result = average_fastness(df, result_column)
    print(f'The mean running time across all rows {round(mean_result, 1)}')
    fastest_time, slowest_time, mean_time, mean_time_other_runners = runner_stats(df, runner_name, result_column)
    print(f'Best, Worst times for {runner_name}:  {round(fastest_time, 1)}, {round(slowest_time, 1)}')
    print(f'Average time for {runner_name}:  {round(mean_time, 2)}')
    print(f'Average time for runners except {runner_name}:  {round(mean_time_other_runners, 2)}')
    print(f'∆:  {round(mean_time_other_runners, 2)}')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
        assert(os.path.isfile(csv_path))
    else:
        csv_path = DEFAULT_PATH
        print(f'No dataset provided, running {sys.argv[0]} on {csv_path}')

    if len(sys.argv) > 2:
        result_column = sys.argv[2]
    else:
        result_column = DEFAULT_RESULT_COLUMN
        print(f'No results column provided, running {sys.argv[0]} with result_colun {result_column}')

    if len(sys.argv) > 3:
        runner_name = sys.argv[3]
    else:
        runner_name = DEFAULT_RUNNER
        print(f'No runner provided, running {sys.argv[0]} with runner {runner_name}')
    

    main(csv_path, result_column, runner_name) 
