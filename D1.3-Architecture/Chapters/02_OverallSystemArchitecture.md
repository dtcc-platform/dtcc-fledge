
### 2.1 System Overview

The FLEdge system implements a hierarchical architecture for energy flexibility management, operating across multiple scales from individual buildings to entire cities. At its core, the system utilizes edge computing principles to process and manage energy data locally while enabling coordinated optimization across broader geographical scales.

The architecture follows a distributed approach, with key processing capabilities placed at the edge of the network through the Edge-Energy Management (EEM) devices. These devices interact with building systems and energy resources while maintaining communication with higher-level Energy Management Nodes (EMaN) that coordinate activities at neighborhood, district, and city scales.

This hierarchical structure enables local autonomy while facilitating broader energy optimization goals. Each level in the hierarchy maintains its own decision-making capabilities while participating in coordinated actions through well-defined interfaces and protocols.

### 2.2 Architecture Principles

The FLEdge architecture adheres to several fundamental principles that guide its design and implementation:

#### Decentralization
The system distributes processing and decision-making capabilities across multiple levels, reducing central point failures and enabling local autonomy while maintaining coordinated action toward global objectives.

#### Edge-First Processing
Data processing occurs as close to the source as possible, minimizing latency and network load while enabling rapid response to local conditions.

#### Hierarchical Coordination
While maintaining local autonomy, the system enables coordinated actions across different scales through a well-defined hierarchy of control and communication.

#### Security by Design
Security considerations are integrated at every level, from device-level encryption to system-wide access control and data protection measures.

#### Scalability and Flexibility
The architecture supports dynamic scaling, allowing for the addition of new devices and nodes while maintaining system performance and reliability.

### 2.2 Key Components and Interfaces

The FLEdge system comprises several essential components that work together to deliver comprehensive energy flexibility management:

### 2.2.1 FLEDge Building Level EMaN (Pilot Site Deployment/EEM)

Corresponding to the level of building areas, buildings or apartments, the **Building Level EMaN** includes all the necessary components that will autonomously and automatically manage in real-time local control actions and respective information. End User required interaction will be limited, while self-privacy and autonomy of buildings will be ensured through privacy preserving monitoring mechanisms and infrastructures. The Pilot Site Deployment will interact with the building on a continuous and real time basis, based on present building context (comfort and occupancy evidence or prediction, environmental context etc.).  

The **EEM device** serves as the foundational component of the system, deployed at the building level. It incorporates data collection interfaces for energy meters, sensors, and building management systems. The device features local processing capabilities for real-time analysis and decision-making, including a Decision Support System (DSS) for automated energy optimization. 
Various mechanisms will be deployed in order to assist with operation control and decisions during its operation.
Advanced algorithms and their output knowledge (i.e. building flexibility, well-being estimation, RES & storage status, etc.), will allow to analyse and evaluate the building operational status at real-time and make optimal decisions towards smart proactive building behaviour and services.
In order to securely distribute and exchange information and knowledge within FLEdge framework, External interfaces will be developed and integrated into Building EMaNs for secure end-to-end communications, data protection and privacy-preserving enabling communication with building systems and higher-level EMaN nodes.

This component consists of the following sub-systems:


#### 2.2.1.1 Edge Middleware

This component bridges the gap between the ICT components and the IoT devices providing all the necessary inputs and communication protocols. It will gather heterogeneous information (e.g. energy consumption, indoor environmental conditions, RES & storage information, etc.) from a variety of sensors/ devices (e.g. building systems, legacy appliances and equipment, etc.).  

#### 2.2.1.2 Prediction Layer  

 

#### Energy Load & Generation Prediction 

This module aims to deliver advanced forecasting capabilities for building energy management. It employs machine learning models (XgBoost, LSTM) trained on historical and real-time datasets to predict both energy load and generation with high accuracy. For energy load forecasting, detailed data on building characteristics and usage patterns are utilized, while energy generation forecasting leverages information about photovoltaic systems, including their specifications (e.g., Mono-Si PV panels, orientation, and efficiency). With the integration of time-series data and external factors like weather forecasts, the module supports both short-term and long-term predictions. 

#### Energy Disaggregation and Building Behavior 

The goal of this component is to implement detailed analysis of building energy consumption by breaking down overall usage into appliance-level data using a Non-Intrusive Load Monitoring (NILM) algorithm. It provides insights into occupant behavior and identifies key energy drivers without requiring additional sensors. The module supports flexibility characterization, appliance scheduling, and energy optimization, contributing to smarter energy management. With the base model developed, the module is set to enhance building energy efficiency and integration within the broader FLEdge system. 

#### Building Energy Flexibility 

This component will deliver advanced building elasticity prediction algorithms allowing the FLEdge framework to perform D/R strategies based on them. Advanced forecasting techniques (i.e. regression approaches, neural networks, etc.) will exploit time series historical energy consumption, generation and storage information from the buildings, the status of the devices/ appliances, the forecasting information (load and generation) and the current status of the building, in order to create various building elasticity (flexibility) models able to estimate/ forecast the elasticity of the building in real-time. 

#### Building Energy Resources Optimization 

This module focuses on maximizing the efficient use of locally installed renewable energy sources (RES), energy storage systems, and dynamic electricity tariffs. By integrating with the Digital Twin and leveraging advanced self-adaptive control algorithms, it optimizes HVAC and other energy-influencing systems for cost-effective demand response and proactive energy management. The module balances user comfort, grid flexibility, and real-time energy conditions by dynamically adjusting its objective function to align with grid operator requests, user preferences, and energy market conditions. This ensures seamless, efficient, and adaptive energy optimization for buildings. 

 

#### 2.2.1.3 Decision Layer 

 

#### Decision Support System (DSS) 

The module optimizes building operations by integrating energy efficiency strategies with advanced predictive algorithms. Leveraging reinforcement learning techniques like Self-Adapted Advantage-Weighted Actor-Critic (SA-AWAC), it dynamically adjusts energy consumption and HVAC operations based on environmental conditions, thermal comfort, and flexibility metrics. Seamlessly interfacing with Building Management Systems (BMS), the DSS enhances user comfort, reduces energy costs, and adapts to varying building needs, making it a key component of the FLEdge framework for smart, efficient building management. 

 

#### 2.2.1.4 Data and Security Layer 

TODO 

### 2.2.2 Neighbourhood/District/City Level EMaN: 

EMaN nodes operate at three distinct levels - neighborhood, district, and city - each providing increasingly broader coordination capabilities. These nodes aggregate data from lower levels, implement optimization algorithms appropriate to their scope, and manage demand response strategies. 

They feature interfaces for both vertical communication (with other hierarchy levels) and horizontal communication (with peer nodes at the same level).
They also handle energy transactions across various levels leveraging blockchain frameworks like . Hyperledger Fabric's modular architecture and role-based node delineation ensure secure, efficient processing, while Energy Web Chain, tailored to energy-sector applications, provides a decentralized infrastructure optimized for energy trading and coordination. Smart contracts deployed on these platforms could automate transactions, authenticate participant roles, and ensure traceability, facilitating seamless, secure, and transparent energy management operations. 

FLEdge’s Energy Management Nodes (EMaNs), designed to manage operations at the neighborhood, district, and city levels, adhere to a unified architectural template. This consistent design supports identical functionalities at varying scales, utilizing aggregated data from lower-tier nodes to ensure grid stability and optimization. 

Each node is composed of three core components: the Prediction and Simulation Layer, the Decision Layer, and the Middleware Layer, which work together to enable efficient and scalable energy management. 

#### 2.2.2.1 Middleware Layer 

TODO 

#### 2.2.2.2 Prediction & Simulation Layer 

 

#### Energy Elasticity 

The objective of this component is to compute and evaluate the energy flexibility based on the elasticities provided by each lower-tier node associated with the current node. 

#### Energy Load & Generation Prediction  

This module aims to deliver advanced forecasting capabilities for energy management on different scales. It employs models trained on historical and real-time datasets to predict both energy load and generation with high accuracy. With the integration of time-series data and external factors like weather forecasts, the module supports both short-term and long-term predictions. 

#### D/R Strategy 

The primary purpose of this module is to apply demand-response (D/R) strategies at its respective level, guided by the D/R directives issued by upper-tier nodes. 

 

#### 2.2.2.3 Decision Layer 

The Decision Layer is centered around its sole and primary component, the Decision Support System, which serves as the integrative framework for all sub-components within the node. 

 

#### Decision Support System (DSS) 

 Based on the aggregated energy flexibility the DSS module will estimate the status of the neighbourhood (generation, consumption, storage) and implement D/R actions with the buildings’ EEM towards grid stability and a positive energy neighbourhood with zero-net emissions. 

 

#### 2.2.2.4 Data and Security Layer 

TODO 

### 2.2.3 Operational Platform:

It’s the central component of the FLEdge system architecture providing a secure, scalable, and adaptable framework for data collection, visualization, and user actions. At its core, the platform integrates a centralized data hub, advanced authentication mechanisms, and a multi-tiered visualization layer, offering dashboards and a mobile application for continuousn real-time monitoring and control. By interfacing with distributed Energy Management Nodes (EMaNs) at various levels, the Operational Platform facilitates seamless communication between localized energy systems and centralized functionality. This layer consists of the following sub-systems. 

 

#### 2.2.3.1 Authentication Layer 

The Authentication Layer employs a token-based authentication mechanism combined with role-based access control to securely manage user interactions with the system. Upon successful authentication through the mobile app or dashboards, users are issued a secure token which encodes their role and permissions. This token is included in subsequent API requests to ensure that users can access data and perform actions appropriate to their assigned roles, such as viewing historical energy data or interacting with digital twin models. To further enhance communication security, the system can incorporate mutual TLS (mTLS), enabling bidirectional authentication between clients and servers to safeguard sensitive energy data and ensure trusted interactions. This combination ensures robust, scalable, and secure access management across the platform. 

 

#### 2.2.3.2 Visualization Layer 

Includes dashboards for different hierarchical levels—City, District, Neighbourhood, and Building—and a Mobile App interface for accessibility. These dashboards provide insights, visualizations, and tools to monitor and manage energy systems at their respective levels. 

 

#### Neighbourhood, District and City Level Dashboard 

TODO 

 

#### Building Level Mobile Application 

TODO 

 

#### 2.2.3.3 Data Storage Layer 

The Data Storage Layer serves as a centralized and scalable hub for collecting, storing, and processing data from all nodes within the system. Its architecture aims to support high-throughput data ingestion and secure communication, with a focus on flexibility and modularity. Time-series data, such as energy consumption, generation, elasticity, and occupancy metrics, is efficiently stored in a system optimized for temporal data, while relational data structures manage hierarchical metadata and aggregated summaries.  

To ensure compliance with data protection regulations, the system could employ privacy-preserving techniques like data minimization, pseudonymization, encryption, and automated retention policies. Security measures, including encrypted data transfer, access controls based on user roles and node levels, and secure node-to-hub communication using mutual TLS, safeguard the data. The architecture is designed to be adaptable, enabling the integration of different tools and platforms as needed, to ensure long-term scalability and compliance without dependency on specific vendors. 

 

<!-- Decision Support System (DSS)

The DSS operates within both EEM devices and EMaN nodes, providing intelligent decision-making capabilities tailored to each level's requirements. It processes real-time data, applies optimization algorithms, and generates control decisions. The DSS interfaces with both local systems and external components through standardized APIs. -->

### 2.2.4 Communication Infrastructure
A robust communication infrastructure connects all system components, supporting both real-time data exchange and control signals. It implements multiple protocols to accommodate various device types and communication requirements, while ensuring security and reliability.



### 2.4 High-Level Architecture Diagram

[Note: This section would include a detailed architectural diagram showing the hierarchical structure, component relationships, and key interfaces. The diagram should illustrate the following elements:
- EEM devices at the building level
- EMaN nodes at neighborhood, district, and city levels
- Communication paths between components
- Key interfaces and data flows
- Security boundaries and zones
- Major subsystems and their relationships]



### 2.5 Data Flow Architecture

The FLEdge data flow architecture implements a multi-layered approach to information processing and exchange:

Data Collection Layer
At the lowest level, EEM devices collect data from various sources within buildings, including energy meters, environmental sensors, and building management systems. This data undergoes initial processing and validation before being used for local decision-making or forwarded to higher levels.

Local Processing Layer
EEM devices process collected data locally, implementing real-time analysis and control decisions. This layer includes data aggregation, filtering, and local optimization algorithms that operate independently of higher-level systems.

Aggregation and Coordination Layer
EMaN nodes aggregate data from multiple sources, implementing broader optimization strategies and coordination mechanisms. This layer handles data from multiple EEM devices or lower-level EMaN nodes, generating coordinated control decisions and flexibility management strategies.

Enterprise Integration Layer
At the highest level, the system integrates with external enterprise systems, providing data for analysis, reporting, and broader energy management initiatives. This layer implements standardized interfaces for data exchange with external systems while maintaining security and access control.

The data flow architecture ensures efficient information movement throughout the system while maintaining data integrity and security. It implements caching mechanisms at appropriate levels to optimize performance and includes redundancy measures to ensure system reliability.