import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("dataset.csv")

print("=" * 45)
print("KLASIFIKASI PESAN SPAM")
print("=" * 45)

print(f"Jumlah data: {len(data)}")
print("\nDistribusi label:")
print(data["label"].value_counts())

X = data["pesan"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

prediksi = model.predict(X_test)

print("\nHASIL EVALUASI")
print(f"Accuracy: {accuracy_score(y_test, prediksi):.2f}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        prediksi,
        zero_division=0
    )
)

pesan_baru = [
    "Selamat, Anda memenangkan hadiah gratis",
    "Besok kita belajar bersama di kampus"
]

hasil_prediksi = model.predict(pesan_baru)

print("\nPREDIKSI PESAN BARU")
for pesan, label in zip(pesan_baru, hasil_prediksi):
    print(f"Pesan: {pesan}")
    print(f"Prediksi: {label}\n")
