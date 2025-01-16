flowchart LR
    subgraph Building_Level[Building Level]
        A1(Edge Middleware) 
        A2("Prediction Layer
        (Load & Gen Forecast,
        Disaggregation, Elasticity)")
        A3("Decision Layer
        (DSS)")
        A4(Data & Security Layer)
        A1 --> A2
        A2 --> A3
        A3 --> A4
        A4 --> A2
    end
    subgraph Neighborhood_District_City[Neighborhood / District / City Level]
        B1(Middleware Layer)
        B2("Prediction & Simulation Layer
        (Aggregated Load & Gen,
        Elasticity, D/R Strategy)")
        B3("Decision Layer
        (DSS)")
        B4(Data & Security Layer)
        B1 --> B2
        B2 --> B3
        B3 --> B4
    end
    subgraph Operational_Platform[Operational Platform]
        C1(Authentication Layer)
        C2("Visualization Layer
        (Dashboards & Mobile App)")
        C3(Data Storage Layer)
    end
    Building_Level --> Neighborhood_District_City
    Neighborhood_District_City --> Operational_Platform
