# FLEdge Information View

## 1. Overview of the FLEdge Information Flow

FLEdge follows a **hierarchical** approach to collect, manage, and utilize energy-related data:

1. **Building Level (EEM / Building EMaN)**  
   - Collects detailed, real-time energy and environmental data from local sensors, appliances, and meters.  
   - Performs local data validation, transformation, and analysis (e.g., load forecasting, disaggregation, building flexibility).  
   - Stores high-resolution data locally and sends aggregated/summarized data to upper-level EMaN nodes.  
   - Receives demand-response (D/R) directives or optimization strategies from upper levels and acts on them.  

2. **Neighborhood / District / City Level (EMaN)**  
   - Receives aggregated data from multiple Building EMaNs.  
   - Performs higher-level coordination, such as area-level load forecasting, aggregated flexibility calculations, D/R management.  
   - Sends updated or consolidated instructions back down to Building EMaNs (e.g., load shifting, energy storing).  
   - Publishes aggregated / consolidated insights to the Operational Platform.

3. **Operational Platform**  
   - Provides centralized data management, visualization dashboards, user interfaces, and a mobile application.  
   - Stores time-series data, aggregated metrics, logs, and historical insights (may be anonymized or pseudonymized).  
   - Implements role-based access and authentication for building managers, district administrators, etc.  
   - Presents real-time KPI dashboards and orchestrates user interactions (e.g., notifications, action proposals).

4. **External Systems / Enterprise Layer (Optional)**  
   - Interfaces (via standardized APIs) with third-party services (e.g., energy utilities, market platforms, advanced analytics, or municipal IT systems).  
   - Enables integration with broader enterprise workflows (billing, demand-response programs, advanced analytics, etc.).

---

## 2. Main Data Entities and Information Types

Below are key data entities that flow through the system:

1. **Consumption & Generation Data**  
   - **Granularity:** Real-time or near real-time (seconds/minutes).  
   - **Source:** Local meters, sub-meters, sensors (including IoT devices, e.g., smart plugs).  
   - **Usage:**  
     - Building-level optimization (disaggregation, forecasting).  
     - Higher-level aggregated analytics (district/city load balancing).  
     - Display on Operational Platform dashboards.

2. **Occupancy & Comfort Data**  
   - **Granularity:** Typically every few minutes (occupancy sensors, thermostats, temperature/humidity sensors, CO2).  
   - **Source:** Building BMS (Building Management System), occupant mobile app inputs, or sensors.  
   - **Usage:**  
     - Real-time building optimization (HVAC setpoint, occupant comfort strategies).  
     - Demand-response constraints (avoid occupant discomfort).  
     - Visualization to end-users (comfort feedback, user preferences).

3. **Predictive / Forecasted Data**  
   - **Types:** Load forecasts, generation forecasts (e.g., PV output), elasticity indexes, peak load predictions.  
   - **Source:** Prediction modules at building or neighborhood/district level (machine learning models, digital twins).  
   - **Usage:**  
     - Building-level scheduling and real-time control (e.g., deciding when to run certain appliances).  
     - Aggregated neighborhood/district-level D/R planning.  
     - Visualization of short-term and long-term trends on the Operational Platform.

4. **Flexibility & Elasticity Information**  
   - **Granularity:** Periodic updates (e.g., hourly) or event-based.  
   - **Source:** Building Flexibility modules (based on occupant behavior, weather, predicted usage).  
   - **Usage:**  
     - Demand-response orchestration at the building or district level.  
     - Overall energy optimization strategies.

5. **Control and Optimization Data**  
   - **Types:** D/R signals, setpoint adjustments for HVAC, battery charge schedules, scheduling for high-load appliances, etc.  
   - **Source:** DSS modules at each hierarchical level (Building DSS, Neighborhood/District DSS).  
   - **Usage:**  
     - Automated or semi-automated local control commands.  
     - Action proposals shown to building occupants or managers (who can override or consent).  
     - Cross-level coordination (district sending instructions to buildings).

6. **Security & Authentication Data**  
   - **Types:** User identities, tokens, certificates, access control lists, encryption keys.  
   - **Source:** Authentication Layer, token-based RBAC modules.  
   - **Usage:**  
     - Role-based enforcement of data access, device permissions, and user actions.  
     - Secure end-to-end communications between EEM devices, EMaN nodes, and the Operational Platform.

7. **Audit & Logging Data**  
   - **Granularity:** Continuous (events, transactions, system logs).  
   - **Source:** System components at building, neighborhood, district, city, and operational layers.  
   - **Usage:**  
     - Diagnostics, troubleshooting, compliance audits (e.g., GDPR logs, security logs).  
     - Historical analysis for anomaly detection and predictive maintenance.

---

## 3. Data Flows and Interfaces

### 3.1 Building-Level Data Flow

1. **Sensors & Devices → Edge Middleware**  
   - Protocols: BACnet, Modbus, KNX, Bluetooth, EnOcean, zWave, Wi-Fi, Ethernet.  
   - Data: Real-time consumption, environmental metrics, occupant presence.  
   - The Edge Middleware classifies, validates, and normalizes incoming data.

2. **Edge Middleware → Local Processing (Prediction, Disaggregation, Flexibility)**  
   - Data is streamed or batch-processed to modules such as:  
     - Load & Generation Prediction  
     - Disaggregation & Behavior  
     - Building Flexibility  
   - Intermediate results (e.g., predicted load, NILM results) are stored locally and forwarded to the DSS.

3. **Local DSS → (Optional) Action or Control Directives**  
   - The DSS combines real-time data and predictions to propose or directly implement setpoints for HVAC, storage, or appliances.  
   - Action proposals/commands may be shared with the occupant (via the Operational Platform) for manual approval or override.

4. **Building-Level EMaN → Upper-Level EMaN**  
   - Aggregated building data, load forecasts, flexibility values, or requests for D/R coordination are sent upward.  
   - Communication typically via secure REST/gRPC or message queues (e.g., Kafka) with encryption (TLS 1.3).

### 3.2 Neighborhood / District / City Data Flow

1. **Collect Aggregated Data from Multiple Buildings**  
   - Each building publishes summarized metrics (energy consumption, predicted flexibility) to the Neighborhood EMaN.  
   - EMaN nodes store and merge data from multiple lower level nodes.

2. **District-Level Analytics & DSS**  
   - The District EMaN runs forecasting or D/R strategy modules at scale (e.g., aggregated load, expected generation from multiple sites).  
   - Decisions (e.g., peak load shifting, large-scale D/R events) are coordinated across building EMaNs.

3. **City-Level / Upper EMaN**  
   - Similar flow to District but with more aggregated data across multiple District EMaNs.  
   - Provides city-wide or utility-level signals, e.g. large-scale demand-response instructions, or receives signals from external sources (utility, energy markets).

### 3.3 Operational Platform Data Flow

1. **Data Ingestion & Storage**  
   - Time-series data, events, logs from EMaNs are securely transmitted to the central Data Storage Layer.  
   - Data ingestion layer may use an event-driven bus (e.g., Kafka) with topics for building-level data, district-level data, user actions, etc.

2. **User Authentication & Dashboards**  
   - Users (building managers, operators, district admins) authenticate via the Authentication Layer.  
   - Role-based dashboards retrieve relevant data (building-level dashboard, district-level dashboard).  
   - Visualization modules present real-time charts, historical trends, predictions, and DSS actions.

3. **Mobile App**  
   - A simplified interface enabling occupant-level interactions (comfort feedback, preferences, real-time consumption overview).  
   - May push notifications about recommended actions from the local or district DSS.

4. **External Integrations**  
   - APIs (REST/GraphQL) provide data exchange to external energy services, municipal data platforms, or advanced analytics.  
   - Could involve:  
     - **Market Participation:** e.g., energy pricing, bidding into DR programs.  
     - **Third-Party Apps:** Smart city platforms, external building management solutions.

---

## 4. Data Persistence and Security Mechanisms

1. **Local Data Persistence**  
   - Edge devices store locally short-term, high-resolution data (often time-series oriented).  
   - Ensures local autonomy, real-time analytics, and resilience if connectivity to upper layers is temporarily down.

2. **Central Data Storage**  
   - Scalable, possibly cloud-based or on-prem servers.  
   - Retains aggregated or historical data for city/district analysis, long-term storage, advanced analytics, and compliance (GDPR retention policies).

3. **Data Encryption & Privacy**  
   - **At Rest:** AES-256 encryption for local device storage (edge or central).  
   - **In Transit:** TLS 1.3 with mutual authentication (mTLS) for building-level to EMaN, EMaN to Operational Platform, etc.  
   - **Privacy Controls:** Pseudonymization, privacy-preserving data minimization.  
   - **Role-Based Access:** Only authorized roles (e.g., building manager, occupant) can view/change relevant data.

4. **Logging & Auditing**  
   - All data operations, system events, control actions are logged (with timestamps, user/device ID).  
   - Logs used for compliance (GDPR logs access), debugging, forensics, and continuous improvement.

---

## 5. Key Information Exchanges

| **Information Flow**                           | **Producers**                               | **Consumers**                              | **Purpose**                                                       |
|-------------------------------------------------|---------------------------------------------|--------------------------------------------|-------------------------------------------------------------------|
| Real-time building data                         | Sensors, edge devices (Middleware)          | Local EEM modules (Prediction, DSS)        | Local optimization, real-time analytics                           |
| Aggregated usage & flexibility                 | Building EMaN                               | Neighborhood / District EMaN               | Multi-building optimization, load balancing                       |
| Demand Response instructions / signals          | District EMaN (or city-level)               | Building EMaNs, local DSS                  | Coordinated load shifting, peak demand management                |
| Occupant feedback & preferences                | Mobile app, occupant device                 | Local DSS, building-level database         | DSS personalization, occupant comfort constraints                 |
| Notifications & action proposals               | DSS modules (Building/District)             | Occupants, building managers               | Encourage manual or automated action to optimize usage           |
| Historical data (long-term)                    | Local EMaNs, Operational Platform           | Central Data Storage, analytics modules    | Trend analysis, advanced ML, city-wide insights                   |
| Security & Authentication                      | Authentication service (token mgmt)         | All system components                      | Ensuring authorized data access and secure communications         |
| External market / utility data (optional)       | Market operator, external APIs              | EMaNs, Operational Platform                | Real-time pricing, external DR events, external analytics         |

---

## 6. Data Quality, Validation, and Governance

1. **Data Quality Checks**  
   - **Validation at Ingress:** Edge Middleware verifies sensor data consistency (e.g., missing fields, out-of-range values).  
   - **Anomaly Detection:** Local analytics flags potential sensor failures or anomalies (e.g., power spikes).

2. **Data Classification & Governance**  
   - **Classification:** Data labeled as personal (occupant data), device-level, aggregated, or anonymized.  
   - **Governance:** Access policies (RBAC) and retention policies align with privacy regulations (GDPR).  
   - **Ownership:** Building managers own building-level data; city/district-level data is aggregated for operational use.

3. **Traceability & Audit Trails**  
   - Each data record from ingestion to storage is linked to timestamps, data source ID, and processing steps.  
   - A comprehensive log of transformations ensures transparency for validation, troubleshooting, or compliance.

---

## 7. Summary

- **Local Autonomy vs. Global Coordination**  
  Data primarily originates at the building level. Local EEM components handle real-time analytics and immediate control while also sending summarized information upward to coordinate with Neighborhood/District/City EMaNs.

- **Security & Privacy by Design**  
  Each data exchange—whether occupant feedback, sensor data, or aggregated metrics—relies on secure, privacy-preserving mechanisms. Encryption, authentication, and role-based policies protect both personal and operational data.

- **Scalable, Hierarchical Data Architecture**  
  From building-level time-series databases to city-level aggregated repositories, FLEdge’s information flow supports scaling from single-building pilot sites to entire districts or cities.

- **Integration with External Systems**  
  Standard APIs and protocols (REST, GraphQL, MQTT, BACnet, Modbus) allow for interoperability with third-party systems, energy markets, and municipal infrastructures, facilitating advanced functionalities such as grid balancing, automated demand response, and cross-domain analytics.

In short, this **FLEdge Information View** illustrates how data is collected, validated, processed, and exchanged among the hierarchical levels (Building → Neighborhood → District → City → Operational Platform). This end-to-end chain underpins the project’s goal: delivering real-time optimization, robust decision support, effective demand-response strategies, and secure, user-friendly data management.
