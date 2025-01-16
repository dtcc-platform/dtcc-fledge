flowchart LR
    subgraph Building Level
        A1(Edge Middleware) 
        A2(Prediction Layer<br/>(Load & Gen Forecast,<br/>NILM, Elasticity))
        A3(Decision Layer<br/>(DSS))
        A4(Data & Security Layer)
        A1 --> A2
        A2 --> A3
        A3 --> A4
        A4 --> A2
    end

    subgraph Neighborhood / District / City Level
        B1(Middleware Layer)
        B2(Prediction & Simulation Layer<br/>(Aggregated Load & Gen,<br/>Elasticity, D/R Strategy))
        B3(Decision Layer<br/>(DSS))
        B4(Data & Security Layer)
        B1 --> B2
        B2 --> B3
        B3 --> B4
    end

    subgraph Operational Platform
        C1(Authentication Layer)
        C2(Visualization Layer<br/>(Dashboards & Mobile App))
        C3(Data Storage Layer)
    end

    %% Flows among subgraphs
    Building Level --> Neighborhood / District / City Level
    Neighborhood / District / City Level --> Operational Platform
