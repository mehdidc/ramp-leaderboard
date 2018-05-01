# ramp-leaderboard

This is a simple command line to display the leaderboard of local
submissions.
  
  
## Install
  
  ```pip install git+https://github.com/mehdidc/ramp-leaderboard```
  
## Usage

You will first need to have a RAMP kit, e.g., like 
https://github.com/ramp-kits/iris :

```> git clone https://github.com/ramp-kits/iris && cd iris```

Then, we will need to train your submissions, making sure
we save the scores and the predictions:

```> ramp_test_submission --submission starting_kit --save-y-preds```

```> ramp_test_submission --submission random_forest_10_10 --save-y-preds```


Once the submissions are trained, we are ready to use `ramp-leaderboard`:

```
> ramp_leaderboard

+----+---------------------+--------------+--------------+--------------+
|    | submission          | train_acc    | valid_acc    | test_acc     |
+====+=====================+==============+==============+==============+
|  1 | random_forest_10_10 | 1.00 ± 0.000 | 0.95 ± 0.000 | 0.90 ± 0.021 |
+----+---------------------+--------------+--------------+--------------+
|  0 | starting_kit        | 0.61 ± 0.026 | 0.65 ± 0.000 | 0.62 ± 0.083 |
+----+---------------------+--------------+--------------+--------------+
```

By default only one default metric is displayed, but it is customizable:

```
> ramp_leaderboard --metric=nll
+----+---------------------+--------------+--------------+--------------+
|    | submission          | train_nll    | valid_nll    | test_nll     |
+====+=====================+==============+==============+==============+
|  0 | starting_kit        | 0.98 ± 0.197 | 0.59 ± 0.069 | 0.76 ± 0.041 |
+----+---------------------+--------------+--------------+--------------+
|  1 | random_forest_10_10 | 0.02 ± 0.007 | 0.12 ± 0.008 | 0.20 ± 0.019 |
+----+---------------------+--------------+--------------+--------------+
```

We could also display specific columns:

```
> ramp_leaderboard --cols=train_acc,train_nll,valid_nll

+----+---------------------+--------------+--------------+--------------+
|    | submission          | train_acc    | train_nll    | valid_nll    |
+====+=====================+==============+==============+==============+
|  1 | random_forest_10_10 | 1.00 ± 0.000 | 0.02 ± 0.007 | 0.12 ± 0.008 |
+----+---------------------+--------------+--------------+--------------+
|  0 | starting_kit        | 0.61 ± 0.026 | 0.98 ± 0.197 | 0.59 ± 0.069 |
+----+---------------------+--------------+--------------+--------------+

```


Type `ramp_leaderboard --help` to get more info about the available commands.




