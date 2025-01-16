sequenceDiagram
    participant NeighborhoodEMaN as Neighborhood EMaN
    participant BuildingEEM1 as Building EEM #1
    participant BuildingEEM2 as Building EEM #2
    participant OperationalPlatform as Operational Platform
    
    NeighborhoodEMaN->>BuildingEEM1: DR Directive (e.g. reduce 20% load)
    NeighborhoodEMaN->>BuildingEEM2: DR Directive (e.g. reduce 20% load)
    
    BuildingEEM1->>BuildingEEM1: Evaluate local state<br/>(DSS, occupancy, flexibility)
    BuildingEEM1-->>NeighborhoodEMaN: Acknowledge feasible reduction
    
    BuildingEEM2->>BuildingEEM2: Evaluate local state<br/>(DSS, occupancy, flexibility)
    BuildingEEM2-->>NeighborhoodEMaN: Partial reduction possible
    
    NeighborhoodEMaN->>OperationalPlatform: Log DR event & results
    Note over OperationalPlatform: Updated dashboards show DR statuses
