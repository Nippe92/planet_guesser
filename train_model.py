import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier  # Du kan byta till annan modell om du vill
from sklearn.metrics import accuracy_score
import joblib  # För att spara modellen

# 1. Läs in datan
df = pd.read_csv("../dataset/planets.csv")

# 2. Förbered features och labels
X = df.drop(columns=["planet"])  # Alla kolumner utom 'planet' är features
y = df["planet"]                 # 'planet' är det vi vill förutsäga

# 3. Dela upp i träning och test (även om datasetet är litet – för strukturens skull)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4. Träna modellen
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Utvärdera modellen
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Modellens accuracy på testdatan: {accuracy:.2f}")

# 6. Spara modellen
joblib.dump(model, "models/planet_classifier.pkl")
print("Modellen är sparad som models/planet_classifier.pkl")
