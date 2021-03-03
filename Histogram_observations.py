# examine distribution of observations
for i in col_names:
    observations = df[i]
    plt.figure(figsize=(9, 5))
    sns.distplot(observations, kde=True)
    # 1 SD left and right of mean (68% of observations)
    plt.axvline(np.mean(observations) + np.std(observations), color="black")
    plt.axvline(np.mean(observations) - np.std(observations), color="black")
    # 2 SD left and right of mean (95% of observations)
    plt.axvline(np.mean(observations) + (np.std(observations) * 2), color="blue")
    plt.axvline(np.mean(observations) - (np.std(observations) * 2), color="blue")
    # 3 SD left and right of mean (99.7% of observations)
    plt.axvline(np.mean(observations) + (np.std(observations) * 3), color="red")
    plt.axvline(np.mean(observations) - (np.std(observations) * 3), color="red")

    plt.title("Histogram of Observations")
    plt.xlabel("Observed value")
    plt.ylabel("KDE")  # use if kde=True
    # plt.ylabel("Observation frequency")     #use if kde=False
    plt.show()

    print('\n')
    print('++++', i, '++++')
    print('mean =', np.mean(observations))
    great3SD = (np.mean(observations) + (np.std(observations)) * 3)
    less3SD = (np.mean(observations) - (np.std(observations)) * 3)
    print('3 SD above mean =', great3SD)
    print('3 SD below mean =', less3SD)