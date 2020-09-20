# Evaluation of First Subsystem
# Random prediction model
import random
import pandas as pd

def random_tuple(actualxy, interval):
    # Generates a random number between
    # a given positive range
    if actualxy[0] == 0 or actualxy[1] == 0:
        return 0, 0
    else:
        return random.randint(0, interval[0]), random.randint(0, interval[1])


def random_prediction(df):
    df_predicted = df.copy()
    interval = (480, 640)
    for row in range(df.shape[0]):
        for i in range(0, len(df.columns[5:]), 2):
            actual_xy = (df.loc[row, df.columns[5:][i]], df.loc[row, df.columns[5:][i + 1]])
            rand_tup = random_tuple(actual_xy, interval)
            df_predicted.loc[row, df.columns[5:][i]] = rand_tup[0]
            df_predicted.loc[row, df.columns[5:][i + 1]] = rand_tup[1]

    return df_predicted


def evaluate(df, df_predicted, threshold):
    correct = 0
    wrong = 0
    for row in range(df.shape[0]):
        for landmark in df.columns[5:]:
            if df_predicted.loc[row, landmark] == 0 and df.loc[row, landmark] == 0:
                dummy = 1
            elif abs(df_predicted.loc[row, landmark] - df.loc[row, landmark]) < threshold:
                correct += 1
            else:
                wrong += 1
    print("The model of landmark extraction accuracy within acceptable margin of " + str(threshold) + " is %" + str(
        correct * 100 / (correct + wrong)))
    return correct, wrong
