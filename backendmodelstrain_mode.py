"""
Treinamento do Modelo de IA para Classificação de Sentimentos
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

print("🤖 TREINAMENTO DO MODELO DE IA - TÓTEM FLEXMEDIA")
print("="*60)

# Base de dados expandida com mais exemplos
data = {
    'texto': [
        # POSITIVOS (30 exemplos)
        "Adorei a exposição", "Muito legal", "Incrível", "Gostei muito", "Fantástico",
        "Maravilhoso", "Excelente experiência", "Show de bola", "Perfeito", "Sensacional",
        "Amei", "Muito bom", "Parabéns", "Top demais", "Espetacular",
        "Que obra linda", "Arte incrível", "Melhor museu", "Experiência única", "Recomendo",
        "Imperdível", "Magnífico", "Brilliant", "Awesome", "Wonderful",
        "Fascinante", "Extraordinário", "Genial", "Surpreendente", "Divertido",
        
        # CURIOSOS (30 exemplos)
        "Como funciona?", "O que é isso?", "Me explique", "Quero saber mais", "Curiosidade",
        "Por quê?", "Como assim?", "Explique melhor", "Qual o significado?", "O que significa?",
        "Como fazer?", "Quando acontece?", "Onde fica?", "Quanto custa?", "Para que serve?",
        "Qual a história?", "Quem criou?", "Como foi feito?", "Qual técnica?", "Que material?",
        "Mostre mais", "Detalhes por favor", "Conte-me mais", "Interessante, e daí?", "Por que isso?",
        "Qual a inspiração?", "Como interpretar?", "O que representa?", "Qual contexto?", "Me surpreenda",
        
        # NEUTROS (20 exemplos)
        "Ok", "Normal", "Mais ou menos", "Não sei", "Interessante",
        "Entendi", "Pode ser", "Tanto faz", "Regular", "Sim",
        "Não", "Talvez", "Vamos ver", "Aguardando", "Hum",
        "Entendo", "Certo", "Compreendo", "Então", "Continua",
        
        # NEGATIVOS (20 exemplos)
        "Não gostei", "Chato", "Entediante", "Ruim", "Poderia ser melhor",
        "Fraco", "Sem graça", "Decepcionante", "Que pena", "Não funciona",
        "Lento", "Bugado", "Confuso", "Difícil de usar", "Desapontador",
        "Péssimo", "Horrível", "Terrível", "Frustrante", "Desnecessário"
    ],
    'sentimento': (
        ["Positivo"] * 30 + ["Curioso"] * 30 + ["Neutro"] * 20 + ["Negativo"] * 20
    )
}

df = pd.DataFrame(data)

print(f"📊 Total de amostras: {len(df)}")
print(f"\n📈 Distribuição das classes:")
print(df['sentimento'].value_counts())

# Pré-processamento
print("\n🔧 Pré-processando dados...")
vectorizer = TfidfVectorizer(
    max_features=150,
    ngram_range=(1, 2),
    stop_words=['a', 'o', 'e', 'é', 'de', 'do', 'da', 'em', 'para']
)

X = vectorizer.fit_transform(df['texto'])
y = df['sentimento']

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"✅ Treino: {X_train.shape[0]} amostras")
print(f"✅ Teste: {X_test.shape[0]} amostras")

# Treinamento
print("\n🤖 Treinando modelo Logistic Regression...")
model = LogisticRegression(
    max_iter=1000,
    random_state=42,
    C=1.0,
    class_weight='balanced'
)
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n" + "="*60)
print("📊 RESULTADOS DO TREINAMENTO")
print("="*60)
print(f"🎯 Acurácia: {accuracy:.2%}")
print(f"\n📋 Relatório de Classificação:")
print(classification_report(y_test, y_pred))

print(f"\n🎲 Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))

# Salvar modelo
model_path = Path(__file__).parent / 'sentiment_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump((model, vectorizer), f)

print(f"\n💾 Modelo salvo em: {model_path}")
print(f"📦 Tamanho do modelo: {model_path.stat().st_size / 1024:.2f} KB")

# Teste com exemplos
print("\n" + "="*60)
print("🧪 TESTE COM EXEMPLOS REAIS")
print("="*60)

test_examples = [
    "Que exposição maravilhosa! Amei cada detalhe",
    "Como funciona esse totem interativo?",
    "Não entendi muito bem, poderia explicar melhor?",
    "Achei meio confuso, poderia ser mais simples"
]

for text in test_examples:
    X_test_example = vectorizer.transform([text])
    prediction = model.predict(X_test_example)[0]
    proba = max(model.predict_proba(X_test_example)[0])
    print(f"\n📝 Texto: '{text}'")
    print(f"🎯 Sentimento: {prediction} (confiança: {proba:.1%})")

print("\n" + "="*60)
print("✅ TREINAMENTO CONCLUÍDO COM SUCESSO!")