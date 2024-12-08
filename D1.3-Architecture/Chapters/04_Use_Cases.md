<!-- Use Case Table Template.

|Use Case           |                      | 
|-------------------|----------------------|
| Actor             |                      |
|                   |                      |
|                   |                      |
|                   |                      |
|                   |                      |
| Goal              |                      |
| Brief description |                      |
| Precondition      |                      |
| Postcondition     |                      | 

-->


##  <!-- CHAPTER_NUMBER -->X. Dynamic View (Use Case Analyses) 

This section provides a comprehensive examination of the FLEdge platform's operational scenarios through detailed use case analyses. It explores how various system components interact dynamically to achieve specific objectives, such as energy optimization, grid stabilization, and user engagement. 

### UC-01 - Registering on the FLEDge platform 


|Use Case | 1. Registering on the FLEDge platform  | 
|---------|----------------------------------------|
| Actor   |   Pilot user/ Building Manager / District Manager   <br>   Operational Platform Application and Dashboards  <br>   Security and Privacy Layer  |
| Goal    |  Creating an account on the FLEdge platform and providing informed consent  |
| Brief description |  The user provides a username and a password. User will be provided with a registration key that will match the user with the dwelling data in an anonymous way. A few essential additional questions are asked, as first data for the user profile. Furthermore, the user needs to click on a checkbox with a label that indicates that the user consents with participating in the pilot and understands that the usage of the data for the purposes of the FLEdge research will be pseudonymized. A link is provided to a page where the Terms and Conditions are stated.  |
| Precondition |  The user has previously provided information and accepted to participate in the FLEdge pilot platform   |
| Postcondition|  The user account is successfully created, and the confirmation is sent by email  |



### UC-02 - Viewing the aggregated consumption in overview visualization  


|Use Case | 2. Viewing the aggregated consumption and internal conditions in overview visualization  | 
|---------|----------------------------------------|
| Actor   |   Pilot user  <br>   Operational Platform Application and Dashboards  <br>   Security and Privacy Layer     <br>   Middleware     |
| Goal    |  User can access his energy consumption through a visual representation of their aggregated consumption alongside the internal conditions of the dwelling (temperature-humidity-CO2).   |
| Brief description |  User can inspect his consumption by looking at a general overview consisting of an easy-to-understand summarization of the consumption. Users can select different granularity levels (day, week, month) to inspect. Users can navigate the consumption for different periods by selecting the start and ending date.    |
| | **Optional**. The overview may contain basic sensor data (e.g., temperature inside and outside). Alternatively, sensor data may be displayed in a detailed view. |
| Precondition |  The user is logged onto the platform and selects the aggregated energy consumption section. The consumption information has been correctly collected, transmitted, and stored by the system.   |
| Postcondition|  Aggregated consumption information is displayed, the user gets insight of the overall consumption and internal conditions.   |


### UC-03 – Viewing the disaggregated consumption 

|Use Case | 3. Viewing the disaggregated consumption  | 
|---------|----------------------------------------|
| Actor   |   Pilot user  <br>   Operational Platform Application and Dashboards  <br>   Security and Privacy Layer     <br>   Middleware     <br>   Energy Disaggregation and Building Behavior Component |
| Goal    |  Users can gain insight into the energy consumption per device.    |
| Brief description |  UDisaggregated consumption information is presented to the user in an easy-to-use informative way (e.g., in the detailed energy consumption visualization). The disaggregation view will display the kW and kWh consumed by the available devices such as: Fridge, Oven, Water heater, Dishwasher, washing machine, Microwave, Kettle, Dryer, Heat pump, AC, EVs. The devices may vary for the different pilots, depending on the availability of the devices and the sensors.     |
| Precondition |  The user is logged in to the platform and selects the disaggregated energy consumption option. The devices are available and functioning correctly, the consumption information has been collected, transmitted, and stored by the system.    |
| Postcondition|  Disaggregated consumption information is displayed, the user gets insight of the disaggregated energy consumption of the available devices. |


### UC-04 – Checking the status of an appliance or a sensor 

|Use Case           |  4. Checking the status of an Appliance or a Sensor  | 
|-------------------|----------------------|
| Actor             |  Pilot user    <br>  Operational Platform Application and Dashboards   <br>  Security and Data Layer  <br>  Middleware   |
| Goal              | Users can retrieve and inspect information about the status of an appliance or a sensor in the household.  |
| Brief description | Users can retrieve and inspect status information about smart appliances and sensors available. The user selects the device they want to inspect from the list of available devices; the platform displays the corresponding status, measurements, and available information in a simple and understandable manner.  |
| |List of devices that can be identified: Smart plugs/ Electricity meters, Electricity smart meters, Dimming on/off actuators, Occupancy sensors, Environmental sensors, Smart lights, Smart thermostats, Water smart meter, Recirculated water smart meter, Gas smart meter, Demand controlled ventilation, Gateway, Modem, Weather Stations, Indoor Condition Sensors (Temperature, Humidity, CO2) |
| |An example could be included: User selects the weather station, the platform displays information about wind speed, atmospheric pressure, and temperature.  |
| Precondition      |  The user navigates to the appliance status section. Smart appliances and sensors are available and the interfaces for communication are operating correctly.  |
| Postcondition     |  The user visualizes the information of the desired device.  | 


### UC-05 – Calculating and Displaying Optimal HVAC and actuation setpoints.

|Use Case           |  5. Calculating and Displaying Optimal HVAC and actuation setpoints.  | 
|-------------------|----------------------|
| Actor             |  Pilot user    <br>  Operational Platform Application and Dashboards   <br>  Security and Data Layer  <br>  Digital Twin   <br>  Building Energy Resources Optimization<br>  DSS |
| Goal              | The proposed optimal HVAC and actuation (smart plugs) setpoints are calculated and posted.   |
| Brief description | Operational Platform Application receives a notification with an action proposal in order to save energy / improve the comfort level. Suggestion is tailored to their specific context based on sensor data, user profile and user detected behavior. |
| | The Proactive Building Operation will retrieve sensor information through middleware regarding building conditions (indoor conditions, energy consumption profile). The Digital Twin Tools could be used as a simulation engine, in order to test proposed control strategies from Proactive Building Operation. The final proposed control strategy will be pushed to the DSS. 
| |An example: the HVAC setpoint should be set to 20 degrees for the next 30 minutes. |
| Precondition      | Sensors and controllers are available and operating correctly. The sensor and consumption data has been correctly collected, transmitted, and stored by the system and made available for the Proactive Building Operation.   |
| Postcondition     | DSS will collect the optimal policies from each proposed tool in order to design the final control strategy.  | 


### UC-06 – Calculating and Displaying Optimal RES and Storage Actions.


|Use Case           |  6. Calculating and Displaying Optimal RES and Storage Actions   | 
|-------------------|----------------------|
| Actor             | Pilot user    <br>  Operational Platform Application and Dashboards   <br>  Security and Data Layer  <br>  Digital Twin   <br>  Load and Generation Prediction <br>  Building Energy Resources Optimization <br>  DSS |
| Goal              | The proposed optimal RES integration and storage control managements are calculated and posted.    |
| Brief description | The Building Energy Resources Optimization will retrieve sensor information through middleware regarding building conditions (indoor conditions, energy consumption profile and generation profile). Moreover, it will retrieve predictions from Load & Generation Prediction tool. The Digital Twin Tools platform could be used as a simulation engine, in order to test proposed control strategies and moreover provide the projected and simulated energy tariff (if applicable in the area). The final proposed control strategy will be pushed to the DSS. |
| | An example: *For the next 30 minutes use the own-produced energy coming from RES to charge the Storage device.*  |
| Precondition      | Sensors and controllers are available and operating correctly. The sensor, consumption and generation data has been correctly collected, transmitted, and stored by the system and made available for the Proactive RES & Storage Management.  |
| Postcondition     | DSS will collect the optimal policies from each proposed tool in order to design the final control strategy. | 


### UC-07 – Calculating and Displaying Building Elasticity Information.

|Use Case           |  7. Calculating and Displaying Building Elasticity Information | 
|-------------------|----------------------|
| Actor             |  Pilot user / Building manager  <br>  Operational Platform Application and Dashboards  <br>  Middleware  <br>  DBuilding Energy Resources Optimization  <br>  Load & Generation Prediction  <br>   DSS <br>  Building Elasticity & Integrated Proactive Algorithms |
| Goal              | Calculation of building’s elasticity index.  |
| Brief description |  The Building Elasticity & Integrated Proactive Algorithms tool collects the current energy information of the building from the middleware platform. Moreover, it collects the forecasting energy consumption/production from Load & Generation Prediction tool to calculate the finalized elasticity index of the building for the next timesteps. The value is displayed as a notification message.  |
| | *An example: for the next 30 minutes the building energy /elasticity/flexibility index will be of that magnitude.* |
| Precondition      | Sensors and controllers are available and operating correctly. The sensor and consumption data has been correctly collected, transmitted, and stored by the system and made available for the Building Elasticity & Integrated Proactive Algorithms.  |
| Postcondition     | DSS will collect the flexibility/elasticity index. | 



### UC-08 – Calculating and displaying the optimal policy based on multi criterion cost indexes 


|Use Case           |  8. Calculating and displaying the optimal policy based on multi criterion cost indexes. | 
|-------------------|----------------------|
| Actor             |  Pilot user / Building manager  <br>  Operational Platform Application and Dashboards  <br>  Middleware  <br>  Digital Twin Tools  <br>  Load & Generation Prediction  <br>   DSS <br>  Building Elasticity & Integrated Proactive Algorithms |
| Goal              | Calculation of optimal policy for holistic optimization.   |
| Brief description |  The DSS will collect the proposed control strategies from Proactive Building Operation, Building Energy Resources Optimization and Building Elasticity & Integrated Proactive Algorithms and will implement a multi-criterion optimization policy to achieve the best performance for the building based on multiple cost indexes. The policy description is displayed as a notification message.   |
| | *An example: for the next 30 minutes the management policy for the HVACs and the Battery will be the following to save energy, integrate the solar production, take advantage of low electricity prices, and improve the energy flexibility index of the building to facilitate grid operations.* |
| Precondition      | Sensors and controllers are available and operating correctly. The sensor and consumption data has been correctly collected, transmitted, and stored by the system and made available for all the necessary tools.  |
| Postcondition     | Policies for energy use optimization are generated based on multiple criterion and available information sources, policies are saved by the DSS and are used to generate the action proposal to be executed and displayed by the system. | 



---

### UC-09: Receiving a Notification with an Action Proposal for Manual Execution

| **Field**         | **Details**                                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Use Case**      | Receiving a notification with an action proposal for manual execution                                                                         |
| **Actor**         | Pilot user<br>Building manager<br>District manager<br>Operational Platform Application and Dashboards<br>DSS                                                 |
| **Goal**          | User receives a notification with a proposal for a manual execution of an action.                                                            |
| **Brief Description** | User receives a notification with an action proposal for a manual execution of an action in order to save energy/improve the comfort level. Suggestion is tailored to their specific context based on sensor data, user profile, and user detected behavior. The DSS will push action proposals that will be displayed to the user through a notification widget. Example: Turn off the appliance X to save energy. |
| **Precondition**  | Sensors and controllers are available and operating correctly. The sensor and consumption data has been correctly collected, transmitted, and stored by the system and made available for the DSS. |
| **Postcondition** | The proposed action is displayed to the user with instructions about how to execute the action.                                               |

---

### UC-10: Accepting or Rejecting a Notification with an Action Proposal

| **Use Case**    | 10. Accepting or rejecting a notification with an action proposal     |
|--------------------|----------------------------|
| **Actor**         | Pilot user<br>Building manager<br>District manager<br>Operational Platform Application and Dashboards<br>DSS                                                 |
| **Goal**          | User receives a notification with a proposal for accepting or rejecting the action.                                                           |
| **Brief Description** | User receives a notification with a proposal for the execution of an action in order to save energy/improve the comfort level. Suggestion is tailored to their specific context based on sensor data, user profile, and user detected behavior. The user receives an option to accept or reject the action execution. Example: Turn off appliance X to save energy. |
| **Precondition**  | Sensors and controllers are available and operating correctly. The sensor and consumption data has been correctly collected, transmitted, and stored by the system and made available for the DSS. |
| **Postcondition** | The proposed action is accepted or rejected based on the feedback from the user.                                                              |

---

### UC-11: Changing the Execution Policy

| **Use Case**      | 11. Changing the execution policy               |
|--------------------|--------------------------------------------|
| **Actor**         | Pilot user<br>Building manager<br>District manager<br>Operational Platform Application and Dashboards<br>DSS                                                 |
| **Goal**          | User can change the action execution policy.   |
| **Brief Description** | The user can change the policy about the execution of actions by giving or removing the permission to the DSS to execute the actions. User has the possibility to apply the change of the permission for a defined period (an hour, a day, a week, or custom). User can decide to change the policy for all the actions of DSS or for a specific module. |
| **Precondition**  | The DSS has generated a policy for the user.  |
| **Postcondition** | The action execution policy is changed. |

---

### UC-12: Monitoring Building Load Forecasting

| **Use Case**      | 12. Monitoring building load forecasting                            |
|--------------------|--------------|
| **Actor**         | Building manager<br>DSS<br>Building Elasticity<br>Load and Generation Prediction<br>Operational Platform Application and Dashboards                          |
| **Goal**          | The user can monitor the building load forecasting for the next day (or current) through a visual representation.                             |
| **Brief Description** | The user monitors the building load prediction through a visual representation to learn and understand how and why the system predicts their energy-related behavior like the presented one. Furthermore, the load forecasting information will be utilized by the flexibility (elasticity) engine, which is essential information for its calculation. |
| **Precondition**  | Proper interfaces with load forecasting will be available to transmit information.                                                            |
| **Postcondition** | The user visualizes the current and next day(s) predictions related to the building demand.                                                   |

---

### UC-13: Smart Heating Management

| **Use Case**      | 13. Smart Heating Management                                                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | EEM device<br>Pilot user<br>Building manager<br>District manager<br>DSS<br>Middleware<br>Proactive Building Operation<br>Energy price dataset |
| **Goal**          | Optimize heating to ensure indoor comfort, improve energy efficiency, and minimize cost.                                                      |
| **Brief Description** | The EEM device detects low indoor temperatures and identifies inefficient heating patterns. It optimizes heating schedules using energy price fluctuations, outdoor weather conditions, and room occupancy data. Example: Pre-heating during low-cost periods. |
| **Precondition**  | High heating costs due to systems operating without optimizing for occupancy, energy prices, or outdoor temperatures.                         |
| **Postcondition** | Heating costs are reduced, maintaining indoor comfort and improving energy efficiency.                                                        |

---

### UC-14: Energy Supply Optimization

| **Use Case**      | 14. Energy Supply Optimization                                                                                                                    |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | EEM device<br>Pilot user<br>Building manager<br>District manager<br>Household appliances<br>Building Energy Resources Optimization<br>Energy price dataset |
| **Goal**          | Efficient energy usage during absence of RES, balancing load, and reducing energy costs.                                                      |
| **Brief Description** | The EEM system shifts energy-intensive activities to off-peak hours, leveraging demand-response strategies for efficient scheduling. Ensures critical appliances operate efficiently while minimizing waste. Example: Laundry scheduled during off-peak times. |
| **Precondition**  | Renewable energy sources are unavailable, leading to reliance on conventional supplies with high peak usage.                                   |
| **Postcondition** | Energy usage is optimized, non-essential activities shifted to off-peak periods, reducing costs and waste while maintaining efficiency.         |

---

### UC-15: Peak Load Shifting

| **Use Case**      | 15. Peak Load Shifting                                                                                                                             |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | Pilot user<br>Building manager<br>Household appliances<br>Middleware<br>EEM device<br>Local grid system<br>DSS<br>Energy price database     |
| **Goal**          | Reduce electricity usage during peak hours, stabilize the local grid, and lower energy bills.                                                  |
| **Brief Description** | The EEM device minimizes peak-hour energy usage by recommending or automating optimizations, respecting user control. Example: Suggest shifting dishwashing to off-peak hours. |
| **Precondition**  | High electricity usage during peak hours strains the grid, with appliances operating without considering energy price fluctuations.            |
| **Postcondition** | Peak-hour consumption reduced, local grid stability improved, and electricity costs lowered while maintaining user control.                    |

---

### UC-16: Building-Wide Heating Optimization

| **Use Case**      | 16. Building-Wide Heating Optimization                                                                                                            |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | Pilot user<br>Building manager<br>District manager<br>EEM device<br>Middleware<br>DSS<br>HVAC system<br>Energy price database               |
| **Goal**          | Optimize heating at the building level to reduce energy consumption and costs while balancing comfort.                                        |
| **Brief Description** | Aggregates heating data across units, analyzing energy prices and demand to optimize schedules while providing actionable insights to managers and residents. Example: Shifting heating to off-peak periods. |
| **Precondition**  | High energy consumption during winter due to inefficient heating practices and independent operation of systems.                              |
| **Postcondition** | Energy consumption and costs reduced, comfort balanced across the building, and heating schedules optimized based on dynamic pricing.          |

---

### UC-17: Backup Energy Management

| **Use Case**      | 17. Backup Energy Management                                                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | EEM device<br>Middleware<br>DSS<br>Local grid system<br>Building Energy Resources Optimization                                               |
| **Goal**          | Ensure uninterrupted operations during RES unavailability and reduce non-essential energy consumption.                                        |
| **Brief Description** | Switches dynamically to stored or grid power during RES downtime, prioritizing resources to critical functions while reducing non-essential consumption. Example: Use stored energy on windless days. |
| **Precondition**  | RES unavailable due to unfavorable weather, with reliance shifting to grid or stored energy.                                                  |
| **Postcondition** | Critical operations maintained, stored energy utilized efficiently, and non-essential energy consumption minimized.                            |

---

### UC-18: Demand Response Participation

| **Use Case**      | 18. Demand Response Participation                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | Pilot user<br>Building manager<br>District manager<br>DSS<br>Local grid system<br>EEM device<br>Proactive Building Operation                 |
| **Goal**          | Minimize energy strain on the grid during peak hours by reducing non-essential building energy consumption while maintaining tenant comfort.   |
| **Brief Description** | The building's EEM system interacts with city-level demand-response signals to adjust non-essential energy use, such as dimming lighting or optimizing HVAC operations. Provides actionable recommendations to occupants for reducing consumption during peak periods. |
| **Precondition**  | The building experiences power overload during peak hours, with unchecked non-essential energy use.                                            |
| **Postcondition** | Non-essential energy consumption is reduced, grid strain is minimized, and tenant comfort is maintained.                                       |

---

### UC-19: District-Level Load Balancing

| **Use Case**      | 19. District-Level Load Balancing                                                                                                                  |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | EMaN nodes<br>DSS<br>Building Energy Resources Optimization<br>District grid system                                                           |
| **Goal**          | Balance energy consumption across the district by redistributing available RES and avoiding grid strain while meeting critical energy needs.   |
| **Brief Description** | EMaN coordinates energy usage by predicting demand and resource shortfalls, prioritizing critical needs. Provides actionable insights for district managers to balance energy consumption effectively. |
| **Precondition**  | Insufficient renewable energy across the district, causing imbalances in energy distribution and grid strain.                                   |
| **Postcondition** | Energy consumption is balanced, renewable resources are redistributed effectively, and district managers receive actionable recommendations.   |

---

### UC-20: Energy Resilience for Construction Zones

| **Use Case**      | 20. Energy Resilience for Construction Zones                                                                                                       |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | DSS<br>Building Energy Resources Optimization<br>Backup energy system<br>Middleware                                                          |
| **Goal**          | Ensure reliable energy delivery to residential areas by mitigating power fluctuations caused by construction-related disturbances.             |
| **Brief Description** | The system monitors energy disturbances linked to construction activity and deploys district-level energy storage or backup systems to stabilize energy supply. Prevents outages and maintains reliability. |
| **Precondition**  | Construction activities causing power fluctuations, leading to potential outages or unstable energy delivery to residential areas.             |
| **Postcondition** | Energy delivery stabilized, residential areas shielded from disturbances, and backup systems effectively deployed to maintain reliability.     |

---

### UC-21: District Peak Load Reduction

| **Use Case**      | 21. District Peak Load Reduction                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | Pilot user<br>EMaN nodes<br>Building management system<br>Proactive building operation system                                                  |
| **Goal**          | Reduce overall district energy demand during peak periods by recommending optimized energy usage schedules.                                   |
| **Brief Description** | EMaN nodes monitor energy fluctuations, forecast potential disruptions, and provide recommendations to reduce peak demand. Includes shifting non-essential operations like HVAC systems to off-peak times. |
| **Precondition**  | Over-demand during peak hours strains the district energy grid, with energy-intensive systems operating inefficiently.                          |
| **Postcondition** | Energy demand is reduced during peak periods, grid strain minimized, and non-essential operations shifted to off-peak times.                   |

---

### UC-22: Community RES Sharing

| **Use Case**      | 22. Community RES Sharing                                                                                                                          |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | Pilot user<br>EMaN nodes<br>Proactive RES<br>DSS<br>Forecasting systems                                                                    |
| **Goal**          | Efficiently manage and optimize the use of local RES across a community during periods of limited renewable generation.                        |
| **Brief Description** | Neighborhood EMaNs facilitate efficient use and sharing of local RES such as solar and wind. Forecasts demand and supply to adjust usage and suggest load adjustments, preventing shortages and encouraging energy efficiency. |
| **Precondition**  | Renewable generation limited during winter, leading to potential shortages in community energy supply.                                         |
| **Postcondition** | RES resources are efficiently utilized, load adjustments prevent shortages, and energy efficiency is encouraged across the community.          |

---


### UC-23: Individual RES Optimization

| **Use Case**      | 23. Individual RES Optimization                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | Pilot user<br>Building manager<br>Middleware<br>Building Energy Resources Optimization                                                          |
| **Goal**          | Maximize the use of locally generated RES for individual building operations.                                                                |
| **Brief Description** | The system monitors the building's RES generation, usage, and storage capabilities. It optimizes local energy production and consumption to maximize self-sufficiency and minimize reliance on external energy sources. |
| **Precondition**  | RES generation and storage infrastructure are available and operational.                                                                     |
| **Postcondition** | Building achieves optimal use of RES, reduces external energy dependency, and enhances energy efficiency.                                      |

---

### UC-24: Distributed Energy Storage Coordination

| **Use Case**      | 24. Distributed Energy Storage Coordination                                                                                                        |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | EMaN nodes<br>Building Energy Resources Optimization<br>District grid system                                                                    |
| **Goal**          | Coordinate distributed energy storage across multiple buildings to improve district-level energy efficiency.                                  |
| **Brief Description** | The system aggregates data from multiple buildings to optimize energy storage utilization. Distributed storage is leveraged to reduce peak demand and support grid stability. |
| **Precondition**  | Distributed storage systems are operational and integrated with the district energy management system.                                        |
| **Postcondition** | Energy storage is effectively coordinated, supporting grid stability and improving district energy efficiency.                                |

---

### UC-25: Load Forecasting and Management

| **Use Case**      | 25. Load Forecasting and Management                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | Pilot user<br>Middleware<br>Load and Generation Prediction<br>DSS                                                                          |
| **Goal**          | Predict and manage energy demand to optimize resource allocation and reduce costs.                                                            |
| **Brief Description** | The system forecasts building energy loads based on historical data and current conditions. Predictions are used to adjust energy usage schedules and allocate resources efficiently. |
| **Precondition**  | Load and generation prediction systems are operational and data is collected and analyzed.                                                    |
| **Postcondition** | Energy demand is accurately forecasted, and resource allocation is optimized, reducing energy costs and waste.                                |

---

### UC-26: Multi-Building Energy Aggregation

| **Use Case**      | 26. Multi-Building Energy Aggregation                                                                                                             |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | EMaN nodes<br>Building Energy Resources Optimization<br>District grid system                                                                    |
| **Goal**          | Aggregate energy data from multiple buildings to improve district-level energy management.                                                   |
| **Brief Description** | The system collects and analyzes energy data from multiple buildings to identify trends and optimize energy distribution. Aggregated data supports district-level decision-making. |
| **Precondition**  | Energy monitoring systems are operational and integrated across multiple buildings.                                                           |
| **Postcondition** | Energy data is aggregated effectively, enabling better district-level energy management and distribution.                                     |

---

### UC-27: Proactive Grid Stabilization

| **Use Case**      | 27. Proactive Grid Stabilization                                                                                                                  |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Actor**         | EMaN nodes<br>DSS<br>Building Energy Resources Optimization<br>District grid system                                                          |
| **Goal**          | Proactively stabilize the grid by managing energy flows and demand-response strategies.                                                      |
| **Brief Description** | The system predicts potential grid instabilities and implements demand-response actions to stabilize energy flows. Strategies include dynamic energy redistribution and peak load reduction. |
| **Precondition**  | Grid monitoring systems are operational, and demand-response infrastructure is in place.                                                     |
| **Postcondition** | Grid stability is proactively maintained, reducing disruptions and ensuring efficient energy management.                                      |

---


