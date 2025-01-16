flowchart TB
    subgraph On_Premises[On-Premises]
        D1[("Sensors & Appliances
        Electric Meters,
        HVAC, Light, etc.")]
        D2("Edge Middleware
        Data Validation,
        Normalization")
        D3("Prediction Modules
        Load Gen Forecast,
        NILM, Flexibility")
        D4(Local DSS)
    end
    
    D1 --> D2
    D2 --> D3
    D3 --> D4
    D4 -->|Control Signals| D1
    D4 -->|Aggregated Data| EMA[("Neighborhood /
    District EMaN")]
