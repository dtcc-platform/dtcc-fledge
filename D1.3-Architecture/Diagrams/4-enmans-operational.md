flowchart LR
    subgraph FLEdge_EMaNs[FLEdge EMaNs]
        EMaN1("Building
        EMaNs")
        EMaN2("Neighborhood
        EMaN")
        EMaN3("District / City
        EMaN")
    end
    
    subgraph Operational_Platform[Operational Platform]
        OP1("Authentication
        Layer")
        OP2("Visualization Layer
        Dashboards & Mobile App")
        OP3(Central Data Storage)
        OP4("External APIs
        Integration")
    end
    EMaN1 -- "Data, Logs, Summaries" --> OP3
    EMaN2 -- "Aggregated Data, DR events" --> OP3
    EMaN3 -- "Aggregated Data, DR events" --> OP3
    OP3 -- "Historical Data, Analytics" --> OP2
    OP2 -- "Users' Inputs, Preferences" --> OP3
    OP2 --> OP1
    OP4 -- "Pricing / Utility Data" --> OP3
    OP3 -- "Distilled Data, analytics" --> EMaN3
    EMaN3 --> EMaN2 --> EMaN1
