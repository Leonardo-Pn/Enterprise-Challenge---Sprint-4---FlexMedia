# Enterprise-Challenge---Sprint-4---FlexMedia
# 🎯 TÓTEM INTELIGENTE FLEXMEDIA

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![AI](https://img.shields.io/badge/AI-Scikit--learn-orange.svg)](https://scikit-learn.org/)

## 📌 Sobre o Projeto

O **Tótem Inteligente Flexmedia** é uma solução inovadora que combina **Inteligência Artificial**, **interação multimodal** e **análise de dados** para criar uma experiência imersiva em museus, centros culturais e espaços educacionais. O sistema permite que visitantes interajam através de texto, botões e imagens, recebendo respostas personalizadas geradas por IA.

### 🚀 Principais Funcionalidades

- **🤖 Classificação de Sentimentos com IA** - Analisa textos e identifica emoções (Positivo, Neutro, Curioso, Negativo)
- **📸 Visão Computacional** - Processa imagens para detectar presença, composição de grupo e expressões
- **💬 Interação Multimodal** - Suporte a texto, botões interativos e captura de imagem
- **📊 Dashboard Analítico** - Métricas em tempo real com gráficos interativos
- **🗄️ Banco de Dados Estruturado** - Armazenamento completo de todas as interações
- **📈 API RESTful** - Endpoints para integração com outros sistemas

## 🏗️ Arquitetura do Sistema
┌─────────────────────────────────────────────────────────────┐
│ Frontend (HTML/CSS/JS) │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │ Texto │ │ Imagem │ │ Botões │ │Dashboard │ │
│ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ │
└───────┼─────────────┼─────────────┼─────────────┼──────────┘
│ │ │ │
▼ ▼ ▼ ▼
┌─────────────────────────────────────────────────────────────┐
│ API Flask (backend/app.py) │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ Endpoints REST (/api/interact, /metrics) │ │
│ └──────────────────────────────────────────────────────┘ │
└───────┬─────────────┬─────────────┬─────────────────────────┘
│ │ │
▼ ▼ ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Modelo IA    │ │    SQLite DB │ │  OpenCV/PIL  │
│ Classificação│ │   Interações │ │   Análise    │
│ Sentimentos  │ │    Métricas  │ │  Visual      │
└──────────────┘ └──────────────┘ └──────────────┘
