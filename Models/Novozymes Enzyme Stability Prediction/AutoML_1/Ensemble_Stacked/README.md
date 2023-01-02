# Summary of Ensemble_Stacked

[<< Go back](../README.md)


## Ensemble structure
| Model                              |   Weight |
|:-----------------------------------|---------:|
| 11_Xgboost_Stacked                 |        5 |
| 29_CatBoost_GoldenFeatures         |        1 |
| 29_CatBoost_GoldenFeatures_Stacked |        8 |
| 5_Default_LightGBM_Stacked         |        9 |
| Ensemble                           |        4 |

### Metric details:
| Metric   |      Score |
|:---------|-----------:|
| MAE      |  4.59878   |
| MSE      | 40.7008    |
| RMSE     |  6.37972   |
| R2       |  0.715612  |
| MAPE     |  0.0707334 |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
