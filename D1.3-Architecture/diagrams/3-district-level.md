flowchart TB
    subgraph Multiple_Buildings[Multiple Buildings]
        Bldg1(Building EEm #1)
        Bldg2(Building EEm #2)
        BldgN(Building EEm #N)
    end
    
    subgraph District_EMaN[District EMaN]
        DistMW(Middleware Layer)
        DistPred("Prediction & Simulation
        (Aggregated Load, DR Strategy)")
        DistDSS("Decision Layer
        (DSS)")
    end
    Bldg1 -- "Summaries, Flex Info" --> DistMW
    Bldg2 -- "Summaries, Flex Info" --> DistMW
    BldgN -- "Summaries, Flex Info" --> DistMW
    DistMW --> DistPred
    DistPred --> DistDSS
    DistDSS --> DistMW
    DistMW -->|"DR Directives,
    Load Shifting"| Bldg1
    DistMW -->|"DR Directives,
    Load Shifting"| Bldg2
    DistMW -->|"DR Directives,
    Load Shifting"| BldgN
