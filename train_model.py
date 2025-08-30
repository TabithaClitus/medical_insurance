import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv("insurance_clean.csv")

# 2. Features & Target
X = pd.get_dummies(df.drop(columns=["charges"]), drop_first=True)  # Encode categorical
y = df["charges"]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Define model
gbr = GradientBoostingRegressor(random_state=42)

# 5. Hyperparameter grid
param_grid = {
    "n_estimators": [100, 200],
    "learning_rate": [0.05, 0.1],
    "max_depth": [3, 4]
}

# 6. GridSearchCV
grid_search = GridSearchCV(
    estimator=gbr,
    param_grid=param_grid,
    cv=3,
    scoring="r2",
    n_jobs=-1,
    verbose=1
)

# 7. Fit model
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_

# 8. Predictions
y_pred = best_model.predict(X_test)

# 9. Evaluation
print("Best Parameters:", grid_search.best_params_)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R²:", r2_score(y_test, y_pred))

# 10. Save model + column order
with open("gbr_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

with open("gbr_columns.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print("✅ Model & columns saved successfully!")

