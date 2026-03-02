---

# 🔄 Pipeline Strategy & Data Flow

This project follows an artifact-driven pipeline strategy.  
Each stage consumes structured inputs and produces structured outputs (artifacts).  
No stage directly depends on internal logic of another stage.

This ensures modularity, testability, and scalability.

---

## 📊 High-Level Flow

MongoDB  
   ↓  
Data Ingestion  
   ↓  
Data Validation  
   ↓  
Data Transformation  
   ↓  
Model Training  
   ↓  
Model Evaluation  
   ↓  
Model Pusher  
   ↓  
Saved Model Artifact  
   ↓  
Flask Prediction API  
   ↓  
User Prediction Output  

---

## 🧠 Detailed Stage Connections

### 1️⃣ Data Ingestion
Connects:
- Source → MongoDB
- Output → Raw data artifact (train/test split)

Produces:
- DataIngestionArtifact

---

### 2️⃣ Data Validation
Consumes:
- DataIngestionArtifact

Validates:
- Schema
- Column consistency
- Missing values
- Data integrity

Produces:
- DataValidationArtifact

If validation fails, pipeline stops.

---

### 3️⃣ Data Transformation
Consumes:
- DataValidationArtifact

Performs:
- Feature engineering
- Encoding
- Scaling
- Preprocessing pipeline creation

Produces:
- DataTransformationArtifact
- Preprocessor object

---

### 4️⃣ Model Trainer
Consumes:
- Transformed dataset
- Preprocessor object

Performs:
- Model training
- Hyperparameter evaluation
- Metric calculation

Logs to:
- MLflow (parameters, metrics, artifacts)

Produces:
- Trained model artifact

---

### 5️⃣ Model Evaluation
Consumes:
- Trained model
- Validation dataset

Compares:
- Current model vs previous best (if exists)

Decision:
- If performance improves → approve
- If not → reject

Produces:
- ModelEvaluationArtifact

---

### 6️⃣ Model Pusher
Consumes:
- Approved model

Pushes:
- Final serialized model to storage
- Updates model registry (if configured)

Produces:
- Deployment-ready model file

---

## 🚀 Inference Flow (Separate from Training)

User Request  
   ↓  
Flask API (app.py)  
   ↓  
Load Saved Model  
   ↓  
Apply Preprocessor  
   ↓  
Generate Prediction  
   ↓  
Return Result  

Important:
Training and inference pipelines are fully separated.  
The inference layer never retrains the model.

---

## 📦 Artifact Strategy

Each stage returns a structured Artifact object.

Why?

- Prevents hidden dependencies  
- Makes debugging easier  
- Enables pipeline re-runs from intermediate stages  
- Makes cloud execution reproducible  

Artifacts act as contracts between pipeline stages.

---

## 🧪 Where MLflow Connects

MLflow hooks into:

- Model Trainer stage
- Model Evaluation stage

It logs:
- Hyperparameters
- Evaluation metrics
- Trained model file
- Experiment metadata

This enables:
- Reproducibility
- Version comparison
- Auditability

---

## ☁️ Where Deployment Connects

Deployment layer connects to:

- Final saved model artifact
- Docker container
- Flask inference API

AWS App Runner pulls:
- GitHub repository
- Dockerfile
- Environment variables

Then builds and exposes:
Public prediction endpoint

---

## 🎯 Why This Strategy Matters

This pipeline design:

- Prevents tight coupling
- Allows independent testing of stages
- Supports scaling individual components
- Makes retraining easier
- Enables CI/CD integration
- Supports future model registry systems

This is how production ML systems are designed — as connected, traceable, modular stages.