# Summary of 29_CatBoost_GoldenFeatures_Stacked

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 7
- **rsm**: 0.8
- **loss_function**: RMSE
- **eval_metric**: RMSE
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 5

## Optimized metric
rmse

## Training time

12.5 seconds

### Metric details:
| Metric   |      Score |
|:---------|-----------:|
| MAE      |  4.61752   |
| MSE      | 41.351     |
| RMSE     |  6.43048   |
| R2       |  0.711069  |
| MAPE     |  0.0709184 |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
