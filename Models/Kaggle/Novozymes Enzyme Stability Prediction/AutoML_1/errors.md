## Error for 11_Default_NearestNeighbors

The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.
Traceback (most recent call last):
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\supervised\base_automl.py", line 1095, in _fit
    trained = self.train_model(params)
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\supervised\base_automl.py", line 380, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\supervised\model_framework.py", line 233, in train
    learner.fit(
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\supervised\algorithms\knn.py", line 50, in fit
    X1, _, y1, _ = train_test_split(
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\sklearn\model_selection\_split.py", line 2583, in train_test_split
    train, test = next(cv.split(X=arrays[0], y=stratify))
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\sklearn\model_selection\_split.py", line 1689, in split
    for train, test in self._iter_indices(X, y, groups):
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\sklearn\model_selection\_split.py", line 2078, in _iter_indices
    raise ValueError(
ValueError: The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 65_NearestNeighbors

The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.
Traceback (most recent call last):
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\supervised\base_automl.py", line 1095, in _fit
    trained = self.train_model(params)
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\supervised\base_automl.py", line 380, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\supervised\model_framework.py", line 233, in train
    learner.fit(
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\supervised\algorithms\knn.py", line 50, in fit
    X1, _, y1, _ = train_test_split(
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\sklearn\model_selection\_split.py", line 2583, in train_test_split
    train, test = next(cv.split(X=arrays[0], y=stratify))
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\sklearn\model_selection\_split.py", line 1689, in split
    for train, test in self._iter_indices(X, y, groups):
  File "C:\Users\10122055\OneDrive - NTT DATA Business Solutions\Projekter\Machine_Learning_Models\.venv\lib\site-packages\sklearn\model_selection\_split.py", line 2078, in _iter_indices
    raise ValueError(
ValueError: The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

