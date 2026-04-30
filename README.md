# AI-Powered Network Intrusion Detection System (NIDS)

Real-time cybersecurity platform that detects network intrusions using distributed streaming, behavioral analytics, and hybrid machine learning models.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Kafka](https://img.shields.io/badge/Streaming-Kafka-black)
![Spark](https://img.shields.io/badge/Processing-Spark-orange)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-purple)
![PyTorch](https://img.shields.io/badge/DeepLearning-PyTorch-red)
![MLflow](https://img.shields.io/badge/MLOps-MLflow-blue)
![DVC](https://img.shields.io/badge/DataVersioning-DVC-lightgrey)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Kubernetes](https://img.shields.io/badge/Deployment-Kubernetes-blue)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-yellow)

---
## What my project does:
My project is an AI-Powered Network Intrusion Detection System (NIDS) that continuously monitors network traffic in real time and detects malicious activities like DDoS attacks, brute-force attempts, port scanning, and even unknown or zero-day attacks.

It works by capturing network traffic, converting it into flow-level and behavioral features, and passing them through a hybrid AI system that combines supervised models (for known attacks) and anomaly detection models (for unknown patterns). Based on this, it generates a risk score and raises alerts for suspicious activity.

## How it is useful:
Traditional security systems like firewalls rely on predefined rules or signatures, so they often miss new or evolving attacks. My system improves this by:

Detecting unknown threats using anomaly detection
Identifying attack patterns over time (like brute force or lateral movement)
Reducing false positives using ensemble modeling
Providing real-time alerts, helping security teams respond quickly

## Simple real-life analogy:

It’s like a smart security guard in a company who not only checks ID cards (known rules) but also notices unusual behavior—like someone accessing multiple restricted rooms or working at odd hours—and flags it as suspicious.

---
##  System Architecture

![System Architecture](docs/architecture/system_architecture.png)


The system follows a distributed, event-driven architecture where network traffic is continuously processed through multiple stages to enable real-time intrusion detection.

---
#### 1. Traffic Ingestion

Network traffic is simulated using packet generators and attack tools, then streamed into the system via Apache Kafka. This acts as the central event backbone, ensuring scalable and fault-tolerant data ingestion.


#### 2. Packet Parsing & Flow Construction

Incoming packet-level data is parsed and aggregated into flow-level records using a 5-tuple key (source IP, destination IP, ports, protocol). This step converts raw network packets into meaningful communication sessions.


#### 3. Data Standardization

All flows are normalized into a consistent schema, ensuring compatibility across different data sources and eliminating inconsistencies. Schema validation is enforced to maintain data integrity.


#### 4. Feature Engineering Layer

The standardized flows are processed using stateful stream processing to generate multi-level features:

- **Stateless Features** → duration, bytes/sec, packet rate  
- **Behavioral Features** → connection patterns, anomaly indicators (window-based)  
- **Temporal Features** → sequence-based activity over time  
- **Graph Features** → communication relationships between hosts  

This layer transforms raw traffic into model-ready intelligence.


#### 5. Feature Store Integration

Computed features are stored in a centralized feature store, ensuring consistency between training and real-time inference while enabling low-latency feature retrieval.


#### 6. Real-Time Model Inference

Feature vectors are consumed by multiple machine learning models, including supervised classifiers, anomaly detection models, sequence models, and graph-based models.


#### 7. Ensemble Risk Scoring

Predictions from individual models are aggregated using an ensemble layer to compute a final risk score, improving detection robustness and reducing false positives.


#### 8. Alert Generation

Events exceeding a predefined risk threshold are flagged as potential threats and published to alert streams for further analysis.


#### 9. Monitoring & Feedback Loop

The system continuously monitors model performance, detects drift, and incorporates analyst feedback to improve detection accuracy over time.

---

##  Data Pipeline

The data pipeline is responsible for transforming raw network traffic into structured, high-quality flow data suitable for real-time feature engineering and machine learning.

---

###  1. Traffic Generation & Ingestion

Network traffic is simulated using packet-level generators and attack tools, producing both normal and malicious patterns. These events are streamed into Apache Kafka, which serves as a distributed messaging backbone for scalable and fault-tolerant ingestion.

- Supports high-throughput event streaming  
- Decouples data producers and consumers  
- Enables replay and fault recovery  


###  2. Packet Parsing

Raw packet data is parsed to extract relevant fields such as:

- Source and destination IP addresses  
- Ports and protocol information  
- Packet size and TCP flags  
- Timestamp  

This step converts low-level binary packet data into structured event records.


###  3. Flow Construction

Parsed packets are aggregated into flow-level records using a 5-tuple key:

(src_ip, dst_ip, src_port, dst_port, protocol)

Each flow represents a communication session between two endpoints and includes:

- Total packets and bytes  
- Duration of the connection  
- Directional traffic statistics  
- TCP flag counts  

This aggregation provides meaningful context for network behavior analysis.


###  4. Data Standardization

All flow records are normalized into a consistent schema to ensure compatibility across the pipeline. This includes:

- Unit normalization (bytes, time)  
- Protocol mapping (numeric → semantic)  
- Timestamp standardization (UTC)  
- Schema validation  

Invalid or malformed data is redirected to a dead-letter queue (DLQ) for further inspection.


###  5. Streaming to Feature Engineering

The standardized flow records are published to a Kafka topic (`standardized-flows`), which serves as the input for the feature engineering layer.

At this stage, the data is:

- Clean and structured  
- Schema-enforced  
- Ready for real-time processing  

---

##  Feature Engineering

![Feature Engineering Pipeline](docs/architecture/feature_engineering.png)
![Feature Engineering Pipeline](docs/architecture/feature_engineering_2.png)

The feature engineering layer transforms standardized network flows into rich, multi-dimensional representations that capture behavioral patterns, temporal dynamics, and structural relationships within the network.

This layer is critical for enabling accurate and robust intrusion detection, as raw flow data alone is insufficient to identify complex attack patterns.

---

###  1. Stateless Flow Features

Basic features are computed directly from individual flow records without requiring historical context:

- Connection duration  
- Bytes per second  
- Packets per second  
- TCP flag ratios  
- Directional traffic statistics  

These features provide immediate insights into individual network interactions.


###  2. Stateful Behavioral Features

To capture patterns over time, the system performs window-based aggregation using stateful stream processing.

Examples include:

- Number of connections per host (sliding window)  
- Unique destination count  
- Failed connection rate  
- Traffic burst patterns  
- Rare destination detection  

These features help identify behaviors such as:

- Port scanning  
- Brute-force attempts  
- Data exfiltration  


###  3. Temporal Features (Sequence Modeling)

The system maintains time-ordered sequences of network activity for each host.

This enables detection of multi-stage attacks where individual events may appear normal, but their sequence reveals malicious intent.

Used for:

- Attack progression detection  
- Suspicious session behavior  
- Sequential anomaly patterns  


###  4. Graph-Based Features

Network communication is modeled as a dynamic graph:

- Nodes represent hosts (IP addresses)  
- Edges represent communication between hosts  

From this graph, structural features are extracted:

- Degree centrality  
- Betweenness centrality  
- Node anomaly scores  
- Community behavior changes  

These features are particularly effective for detecting:

- Lateral movement  
- Command & Control communication  
- Network-wide anomalies  


###  5. Feature Vector Construction

All feature types are combined into a unified feature vector for each flow or entity.

This ensures:

- Consistent input for machine learning models  
- Rich contextual representation of network behavior  
- Compatibility with both training and real-time inference pipelines  

---

##  Modeling Approach

![Model Architecture](docs/architecture/modeling_pipeline.png)

The system uses a hybrid multi-model architecture to detect a wide range of cyber threats, combining strengths of different machine learning approaches.

Each model is designed to capture a specific type of anomaly or attack pattern, ensuring comprehensive detection coverage.


###  1. Supervised Learning (Known Attacks)

Tree-based models such as XGBoost are used to detect known attack patterns from labeled data.

- Effective for: DDoS, brute force, port scanning  
- Strength: High precision on known threats  
- Limitation: Cannot detect unseen attacks  


###  2. Anomaly Detection (Zero-Day Attacks)

Isolation Forest is used to identify statistical deviations from normal behavior.

- Effective for: Unknown and zero-day attacks  
- Strength: Does not require labeled data  
- Role: Flags unusual patterns missed by supervised models  


###  3. Sequence Modeling (Temporal Behavior)

LSTM-based models analyze sequences of network activity over time.

- Effective for: Multi-stage and evolving attacks  
- Strength: Captures temporal dependencies  
- Role: Detects suspicious activity patterns across sessions  

###  4. Graph-Based Detection (Network Structure)

Graph Neural Networks (GNNs) model communication between hosts as a graph.

- Effective for: Lateral movement, command & control  
- Strength: Captures structural relationships  
- Role: Detects anomalies in network topology  


###  5. Ensemble Risk Scoring

Outputs from all models are combined using an ensemble layer to compute a final risk score.

- Improves detection robustness  
- Reduces false positives  
- Balances strengths of individual models  

---

###  Key Insight

No single model can detect all attack types.  
This hybrid architecture ensures detection across:

- Known threats  
- Unknown anomalies  
- Temporal attack patterns  
- Network-level structural changes  

---

##  Real-Time Inference Pipeline

![Inference Pipeline](docs/architecture/inference_pipeline.png)

The inference pipeline is designed for low-latency, real-time detection of network threats using a distributed, event-driven architecture.

It processes incoming feature streams and generates risk scores with minimal delay.

---

###  1. Feature Stream Consumption

Pre-computed feature vectors are consumed from Kafka (`model-features`) by stateless inference services.

- Enables scalable, parallel processing  
- Decouples feature engineering from model inference  


###  2. Model Inference Services

Each model runs as an independent microservice:

- Supervised model (known attack detection)  
- Anomaly model (zero-day detection)  
- Sequence model (temporal behavior)  
- Graph model (structural anomalies)  

This separation allows:

- Independent scaling  
- Isolated updates  
- Fault tolerance  


###  3. Online Feature Retrieval

If required, additional features are fetched from the online feature store for low-latency enrichment.

- Ensures training-serving consistency  
- Avoids recomputation during inference  


###  4. Ensemble Aggregation

Predictions from all models are combined using an ensemble layer to produce a final risk score.

- Improves robustness  
- Reduces false positives  
- Provides calibrated output  


###  5. Alert Generation

Events exceeding a defined risk threshold are flagged as potential threats.

- Published to alert streams  
- Consumed by monitoring dashboards  

---

###  Key Characteristics

- Stateless microservices for horizontal scalability  
- Low-latency inference pipeline  
- Fault-tolerant, event-driven architecture  
- Decoupled components for independent deployment  

---
##  MLOps & Model Management

![MLOps Pipeline](docs/architecture/mlops_pipeline.png)

The system incorporates a complete MLOps pipeline to ensure reproducibility, version control, and reliable deployment of machine learning models in production.

---

###  1. Data Versioning

Datasets and feature snapshots are versioned to maintain consistency between training runs.

- Ensures reproducibility  
- Tracks data lineage  
- Prevents training-serving mismatch  


###  2. Experiment Tracking

All training experiments are tracked with parameters, metrics, and artifacts.

- Enables comparison across model versions  
- Logs performance metrics (precision, recall, FPR)  
- Stores model artifacts and evaluation results  


###  3. Model Registry

Trained models are registered and versioned before deployment.

- Maintains model lifecycle (Staging → Production → Archived)  
- Supports rollback to previous versions  
- Ensures controlled promotion of models  


###  4. Automated Training Pipeline

Model training is automated and can be triggered by:

- Scheduled retraining  
- Drift detection events  
- Feedback-based updates  

This ensures the system adapts to evolving network behavior.



###  5. CI/CD Integration

Model and service updates are deployed through automated pipelines.

- Code validation and testing  
- Docker image builds  
- Deployment to production environment  


###  6. Model Validation Gate

Before deployment, models are evaluated against predefined thresholds:

- Precision / Recall  
- False Positive Rate  
- Latency constraints  

Only models that meet these criteria are promoted to production.

---

###  Key Characteristics

- Fully reproducible training pipeline  
- Version-controlled models and datasets  
- Automated deployment with rollback support  
- Continuous improvement through retraining  

---


##  Drift Detection & Monitoring

![Drift Monitoring Pipeline](docs/architecture/drift_monitoring.png)

The system continuously monitors data and model behavior to detect drift and ensure long-term reliability in dynamic network environments.

---

###  1. Data Drift

Monitors changes in input feature distributions over time.

- Detects shifts in traffic patterns  
- Compares real-time data with training baseline  
- Prevents degradation due to evolving network behavior  


###  2. Concept Drift

Tracks changes in the relationship between features and predictions.

- Identifies drop in model performance  
- Detects outdated decision boundaries  
- Signals need for retraining  


###  3. Prediction Drift

Monitors the distribution of model outputs.

- Detects unusual spikes in risk scores  
- Identifies unstable model behavior  
- Helps diagnose inference anomalies  


###  4. Alert Drift (Operational Monitoring)

Tracks alert volume and false positive trends.

- Prevents alert fatigue  
- Monitors false positive rate (FPR)  
- Ensures operational effectiveness of the system  


###  5. Drift Response

When drift thresholds are exceeded:

- Alerts are triggered  
- Retraining pipelines are activated  
- Models are re-evaluated and updated  

---

###  Key Characteristics

- Continuous monitoring of data and model performance  
- Automated drift detection with statistical metrics  
- Integration with retraining pipelines  
- Ensures long-term system stability and accuracy  

---
##  Deployment (Kubernetes)

![Kubernetes Deployment](docs/architecture/kubernetes_deployment_1.png)
![Kubernetes Deployment](docs/architecture/kubernetes_deployment_2.png)

The system is deployed using Kubernetes to ensure scalability, high availability, and fault tolerance across all components.

---

###  1. Microservices Architecture

Each component runs as an independent service:

- Ingestion services  
- Streaming and feature processing  
- Model inference services  
- Ensemble and alerting services  
- Monitoring and feedback services  

This enables modular development and independent scaling.


###  2. Containerization

All services are containerized using Docker.

- Ensures consistent runtime environments  
- Simplifies deployment across environments  
- Enables portability and reproducibility  


###  3. Auto-Scaling

Horizontal Pod Autoscaling (HPA) adjusts system capacity based on workload.

- Scales inference services during traffic spikes  
- Maintains low latency under high load  
- Optimizes resource utilization  


###  4. Rolling Updates

New versions of services are deployed without downtime.

- Gradual traffic shift to new instances  
- Safe rollback on failure  
- Continuous delivery support  


###  5. Fault Tolerance & Self-Healing

Kubernetes ensures system resilience:

- Automatic pod restarts on failure  
- Rescheduling on node failure  
- Load balancing across instances  

---

###  6. Resource Management

Each service defines CPU and memory limits.

- Prevents resource contention  
- Ensures stable performance  
- Isolates failures  

---

###  Key Characteristics

- Cloud-native, scalable deployment architecture  
- High availability and fault tolerance  
- Zero-downtime updates  
- Efficient resource utilization  

---

##  Security Hardening

![Security Architecture](docs/architecture/security_architecture_1.png)
![Security Architecture](docs/architecture/security_architecture_2.png)

As a cybersecurity system, the platform is designed with a zero-trust security model to protect data, services, and model integrity.

---

###  1. Secure Communication (TLS / mTLS)

All service-to-service communication is encrypted.

- TLS ensures data confidentiality  
- mTLS enables mutual service authentication  
- Prevents man-in-the-middle attacks  


###  2. Access Control (RBAC)

Role-Based Access Control is enforced across the system.

- Services operate with least privilege  
- Access is restricted based on roles  
- Reduces risk of unauthorized actions  


###  3. API Security

All external endpoints are protected using:

- JWT-based authentication  
- Role-based authorization  
- Rate limiting  

Prevents unauthorized access and abuse.



###  4. Secrets Management

Sensitive credentials are securely managed.

- API keys and tokens are not stored in code  
- Managed via secure secret storage  
- Rotatable and access-controlled  


###  5. Kafka Security

Streaming infrastructure is secured using:

- Authentication (SASL)  
- Encryption (SSL)  
- Topic-level access control  

Prevents unauthorized data injection or access.

---

###  6. Model & Data Protection

The system protects against:

- Model extraction attacks  
- Data poisoning via feedback loops  
- Unauthorized model access  

Strict validation and access controls are enforced.


###  7. Audit Logging

All critical actions are logged:

- API access  
- Model deployments  
- Authentication events  

Enables traceability and incident investigation.

---

###  Key Characteristics

- Zero-trust security architecture  
- End-to-end encryption  
- Strict access control and authentication  
- Protection against model and data attacks  

---

##  Observability & Metrics

![Observability Pipeline](docs/architecture/observability.png)

The system implements full-stack observability to monitor infrastructure health, model performance, and detection effectiveness in real time.

---

###  1. System Metrics

Infrastructure-level metrics are continuously tracked:

- CPU and memory usage  
- Service uptime and error rates  
- Kafka lag and throughput  

Ensures system stability and performance under load.


###  2. Latency Monitoring

End-to-end latency is measured across the pipeline:

- Feature processing latency  
- Model inference time  
- Total detection time  

Maintains real-time detection guarantees.


###  3. Model Performance Metrics

Key ML metrics are tracked:

- Precision and Recall  
- False Positive Rate (FPR)  
- Risk score distribution  

Ensures detection quality and operational reliability.


###  4. Alert Monitoring

Operational metrics are monitored:

- Alerts per minute  
- Severity distribution  
- False positive trends  

Helps prevent alert fatigue and maintain SOC efficiency.


###  5. Logging & Tracing

Structured logs and traces are collected:

- Request-level tracking across services  
- Error diagnostics and debugging  
- End-to-end pipeline visibility  


###  6. Visualization & Dashboards

All metrics are visualized in real time:

- System health dashboards  
- Model performance dashboards  
- Security alert dashboards  

Enables rapid monitoring and decision-making.

---

###  Key Characteristics

- Real-time monitoring of system and model behavior  
- End-to-end visibility across the pipeline  
- Early detection of failures and performance issues  
- Data-driven operational insights  

---

##  Human Feedback Loop

![Feedback Loop](docs/architecture/feedback_loop.png)

The system incorporates a human-in-the-loop feedback mechanism to continuously improve detection accuracy and adapt to evolving threats.

---

###  1. Analyst Feedback Collection

Security analysts review alerts and provide feedback:

- True Positive (valid threat)  
- False Positive (benign activity)  
- Suspicious / requires investigation  

This captures real-world expertise directly from SOC workflows.


###  2. Feedback Validation

All incoming feedback is validated before use:

- Authentication and access control  
- Rate limiting to prevent abuse  
- Detection of anomalous feedback patterns  

Prevents data poisoning and ensures reliability.


###  3. Feedback Storage

Validated feedback is stored as labeled data:

- Linked with model predictions and timestamps  
- Versioned for traceability  
- Used as ground truth for retraining  


###  4. Retraining Integration

Feedback is incorporated into the training pipeline:

- Improves model accuracy over time  
- Reduces false positives  
- Adapts to new attack patterns  

Retraining can be triggered by feedback volume or drift signals.


###  5. Continuous Learning

The system evolves based on real-world usage:

- Learns from analyst corrections  
- Updates detection logic  
- Improves operational efficiency  

---

###  Key Characteristics

- Human-AI collaboration for improved detection  
- Continuous model improvement through feedback  
- Protection against feedback manipulation  
- Adaptive system behavior over time  

---

##  Demo

A visual walkthrough of the system demonstrating real-time data flow, processing, and intrusion detection.

---

###  1. Traffic Simulation

Simulated network traffic (normal + attack patterns) being generated and streamed into the system.

🎬 *Demo:*  
![Live Traffic Simulation](docs/demo/live_traffic_generation.mp4)
![Live Traffic Simulation](docs/demo/live_traffic_generation2.mp4)

---

###  2. Real-Time Kafka Stream

Live streaming of network events through Kafka topics, enabling scalable event-driven processing.

🎬 *Demo:*  
![Kafka Stream](docs/demo/kafka_stream.mp4)


---

###  3. Alert Generation

System detecting suspicious activity and generating alerts based on risk scoring.

🎬 *Demo:*  
![Alerts](docs/demo/alert_generation.mp4)

---

###  4. Live Dashboard Monitoring

Real-time dashboard visualizing traffic patterns, system metrics, and detected anomalies.

🎬 *Demo:*  
![Dashboard](docs/demo/dashboard.mp4)
