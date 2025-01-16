sequenceDiagram
    participant DistrictEMaN as District EMaN
    participant BuildingEEM1 as Building EEM #1
    participant BuildingEEM2 as Building EEM #2
    participant OperationalPlatform as Operational Platform
    
    DistrictEMaN->>BuildingEEM1: DR Request (reduce 20% load)
    DistrictEMaN->>BuildingEEM2: DR Request (reduce 20% load)
    
    BuildingEEM1->>BuildingEEM1: Evaluate local state<br/>(DSS, occupancy, flexibility)
    BuildingEEM1-->>DistrictEMaN: Acknowledge feasible reduction
    
    BuildingEEM2->>BuildingEEM2: Evaluate local state<br/>(DSS, occupancy, flexibility)
    BuildingEEM2-->>DistrictEMaN: Partial reduction possible
    
    DistrictEMaN->>OperationalPlatform: Log DR event & results
    Note over OperationalPlatform: Updated dashboards show DR statuses
