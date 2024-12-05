## Functional and Non-Functional Requirements

This section describes the identified functional and non-functional requirements for the components of FLEdge. Additionally, identifies and lists data requirement when they are considered relevant. 

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

###  <!-- CHAPTER_NUMBER -->X.1 Building Level EMaN (Pilot Site Deployment/EEM)

####  <!-- CHAPTER_NUMBER -->X.1.1 Functional Requirements

##### **Edge Middleware**

| | |
|-----------|-------------|
| ID:                 | Middleware-1|
| Title:              | Data Classification|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | Input data classification to groups/lists according to their type. |
| Rationale:    | |

|  |  |
|-----------|-------------|
| ID:                 | Middleware-2|
| Title:              | Data Validation|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The ability for a system to indicate failures of components/sensors - the need to validate data as it comes in.|
| Rationale:    | |

|  |  |
|-----------|-------------|
| ID:                 | Middleware-3|
| Title:              | Secure and Robust DSS decision execution |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | TThe middleware devices must ensure that the decisions taken and sent by the DSS will be implemented during the next operation timestep|
| Rationale:    | |

|  |  |
|-----------|-------------|
| ID:                 | Middleware-4|
| Title:              | Secure remote updates for the firmware and software of the Middleware |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | Roll a test update for firmware and software |
| Rationale:    | |

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

##### **Prediction Layer** 

###### **Energy Load & Generation Prediction**
| | |
|-----------|-------------|
| ID:                 | Load-Generation-1|
| Title:              | Load and Production Forecast calculation|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The component will calculate and share the forecasts regarding the load/energy consumption of the building, as well as the production / PV  generation. |
| Rationale:    | |

|  |  |
|-----------|-------------|
| ID:                 | Load-Generation-2|
| Title:              | Continuous Support of Proactive RES and Storage management tools|
| Priority:           | Should have |
| Tentative Schedule: | M(X)|
| Description:        | The component shall continuously feed information and prediction scenarios to Resources Optimization component and to DSS regarding the projected energy consumption and energy production |
| Rationale:    | |

###### **Energy Disaggregation and Building Behavior** 


| | |
|-----------|-------------|
| ID:                 | Disaggregation-1|
| Title:              | Deliver the fully functional NILM FLEdge approach |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The component shall implement a non-intrusive load monitoring algorithm for disaggregating the overall building’s energy consumption to the level of individual devices/appliances’ energy consumption |
| Rationale:    | |


|           |  |
|-----------|-------------|
| ID:                 | Disaggregation-2|
| Title:              | Continuous Support of Proactive RES and Storage management tools|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The component shall continuously feed information and prediction scenarios to Resources Optimization component and to DSS regarding the projected energy consumption and energy production |
| Rationale:    | |

###### **Building Energy Flexibility**

|           |  |
|-----------|-------------|
| ID:                 | Building-Elasticity-1|
| Title:              | Continuous calculation of building elasticity |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The component will calculate and share the forecasts regarding the energy status and the energy elasticity of the building. The calculated information will be fed to the DSS and published to the upper EMaN. |
| Rationale:    | |



###### **Building Energy Resources Optimization**

|           |  |
|-----------|-------------|
| ID:                 | RES-Optimization-1|
| Title:              | Automated Optimal Decision Making for RES integration |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The optimization module should use optimal control for calculating the optimal use and integration of renewables. It will send the proposed optimal policy to DSS |
| Rationale:    | |

|           |  |
|-----------|-------------|
| ID:                 | RES-Optimization-2|
| Title:              | Automated Optimal Decision Making for Battery management |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The resource optimization management should use optimal control for calculating the optimal use and integration of storage devices. It will send the proposed optimal policy to DSS |
| Rationale:    | |


<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->


##### **Decision Layer** 

###### **Decision Support System (DSS)**

|           |  |
|-----------|-------------|
| ID:                 | DSS-1|
| Title:              | Automated Decision Making for HVAC, RES and Storage Management |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The component should make the control, prediction and behavioral decisions and recommendations for the building operation to the users or the building managers. |
| Rationale:    | Optimal control decisions/recommendations will be calculated according to guidelines from upper tier nodes and will be applied to the actuators of the building.  |


|           |  |
|-----------|-------------|
| ID:                 | DSS-2|
| Title:              | User is regularly informed for Decision Making |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | Users will be able to overview, approve and change if needed the recommended decisions of the DSS. |
| Rationale:    | Using the Operation Platform, the users or the building managers will be able to validate, check and change if needed the proposed and applied control decision of DSS regarding the building management. This attribute will act as the final fail-safe in the case ICT framework completely fails and propose extreme decisions.|


|           |  |
|-----------|-------------|
| ID:                 | DSS-3|
| Title:              | Continuous Decision Making even if the system cycle or an input is not provided |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | DSS should ensure that control decisions will be made, even in the case the communication with other components is temporarily damaged or inputs from the building network are not available.  |
| Rationale:    | It is crucial to ensure the continuous control of the building devices, even if some components are not operating, providing the necessary simulations or inputs.  |



<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
####  <!-- CHAPTER_NUMBER -->X.1.2 Non-functional Requirements

##### **Edge Middleware**

|   |  |
|-----------|-------------|
| ID:                 | Middleware-5|
| Title:              | Continuous Operation and responsiveness|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The component shall respond in real time operation regardless of the incoming signals|
| Rationale:    | |

|  |  |
|-----------|-------------|
| ID:                 | Middleware-6|
| Title:              | Network Data Classification|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The middleware should classify input data from Ethernet and / or Wi-Fi interface |
| Rationale:    | |

|  |  |
|-----------|-------------|
| ID:                 | Middleware-7|
| Title:              | Wireless Data Classification|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The middleware should classify input data from Wireless interfaces (Bluetooth, EnOcean, zWave) |
| Rationale:    | |

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

##### **Prediction Layer**

###### **Energy Load & Generation Prediction**
| | |
|-----------|-------------|
| ID:                 | Load-Generation-3|
| Title:              |Secure data exchange|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The load and generation component should allow data exchange in a secure manner ensuring data privacy |
| Rationale:    | |

| | |
|-----------|-------------|
| ID:                 | Load-Generation-4|
| Title:              |Training of ML and Deep Learning algorithms of Proactive RES and Storage management tools |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The component successfully should utilise the input data to train the Deep Learning Neural Networks responsible for providing the predictions |
| Rationale:    | |


###### **Energy Disaggregation and Building Behavior** 


| | |
|-----------|-------------|
| ID:                 | Disaggregation-2|
| Title:              | Deliver the fully functional NILM FLEdge approach |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The component shall implement a non-intrusive load monitoring algorithm for disaggregating the overall building’s energy consumption to the level of individual devices/appliances’ energy consumption |
| Rationale:    | |


###### **Building Energy Flexibility**

|           |  |
|-----------|-------------|
| ID:                 | Building-Elasticity-2|
| Title:              | Continuous calculation of building elasticity |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The component will calculate and share the forecasts regarding the energy status and the energy elasticity of the building. The calculated information will be fed to the DSS and published to the upper EMaN. |
| Rationale:    | |




###### **Building Energy Resources Optimization**

|           |  |
|-----------|-------------|
| ID:                 | RES-Optimization-3|
| Title:              | Secure Data Exchange with other Layers |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:       | The optimization module should integrate the information coming from other components ensuring data privacy and security|
| Rationale:    | |

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

##### Decision Layer

###### Decision Support System (DSS)

|           |  |
|-----------|-------------|
| ID:                 | DSS-4|
| Title:              | Secure Data Exchange |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The DSS should allow data exchange in a secure manner ensuring data privacy.  |
| Rationale:    |  |


|           |  |
|-----------|-------------|
| ID:                 | DSS-5|
| Title:              | Reassure Decision Making in a communication error event |
| Priority:           | Should have |
| Tentative Schedule: | M(X)|
| Description:        | The DSS should utilize the data history to make optimal decisions in case current measurements or calculations are not available. In the extreme case that historical data are not enough (or the communication error lasts for long periods), rule-based controllers should be utilized.  |
| Rationale:    |  |

|           |  |
|-----------|-------------|
| ID:                 | DSS-6|
| Title:              | Request feedback from the occupants to validate the performance |
| Priority:           | Should have |
| Tentative Schedule: | M(X)|
| Description:        |  The DSS through the mobile app must collect periodically user preferences and dweller's satisfaction to validate its performance. |
| Rationale:    |  |


<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

####  <!-- CHAPTER_NUMBER -->X.1.3 Data Requirements 

##### **Prediction Layer**

###### **Energy Load & Generation Prediction**
| | |
|-----------|-------------|
| ID:                 | Load-Generation-5|
| Title:              | Required Inputs|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  |The component should be fed with the required historical data on energy production and consumption of the building. Moreover, current and historical weather data will be provided. All the necessary inputs are provided by Middleware|
| Rationale:    | |


| | | 
|-----------|-------------|
| ID:                 | Disaggregation-3|
| Title:              | Required Inputs |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The component requires inputs for: the active and reactive power consumption of the building, as well as the internal conditions of the building. All the necessary inputs will be provided by the middleware. |
| Rationale:    | |

###### **Building Energy Flexibility**

|           |  |
|-----------|-------------|
| ID:                 | Building-Elasticity-3|
| Title:              | Data Interface with DSS |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | Clear definition / list of operational parameters, with coding scheme, to be used for DSS |
| Rationale:    | |


|           |  |
|-----------|-------------|
| ID:                 | Building-Elasticity-4|
| Title:              | Data interface with Load and Generation Prediction |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | Collect and process inputs coming from Load and Generation Prediction. |
| Rationale:    | |


###### **Building Energy Resources Optimization**

|           |  |
|-----------|-------------|
| ID:                 | RES-Optimization-4|
| Title:              | Data interface with Middleware|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | Collect and process inputs coming from Middleware regarding Building internal and external current and historical data, and energy consumption/production. |
| Rationale:    | |

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

##### Decision Layer

###### Decision Support System (DSS)

|           |  |
|-----------|-------------|
| ID:                 | DSS-7|
| Title:              | Data interface with Building Energy Resources Optimization Module |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        |  Collect and process inputs coming from Building Energy Resources Optimization module. |
| Rationale:    |  Necessary inputs in order to take the final control decisions/recommendations|

|           |  |
|-----------|-------------|
| ID:                 | DSS-8|
| Title:              | Data interface with Building Elasticity |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | Collect and process inputs coming from Building Elasticity module. |
| Rationale:    |   Necessary inputs to take the final control decisions/recommendations|


|           |  |
|-----------|-------------|
| ID:                 | DSS-9|
| Title:              | Data interface with Middleware |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | Collect and process inputs coming from Middleware regarding Building internal and external current and historical data, and energy consumption/production. |
| Rationale:    |   Necessary inputs to take the final control decisions/recommendations|

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

###  <!-- CHAPTER_NUMBER -->X.2 Neighbourhood, District and City Level Energy Management Node 

####  <!-- CHAPTER_NUMBER -->X.2.1 Functional Requirements

##### Middleware
<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

##### Prediction & Simulation Layer

###### Energy Load & Generation Prediction
| | |
|-----------|-------------|
| ID:                 | Load-Generation-6|
| Title:              | Load and Production Forecast calculations|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  |The component will calculate and share the forecasts regarding the aggregated load/energy consumption of the neighborhood, District or City.|
| Rationale:    | |

###### Neighborhood and District Energy Flexibility

|           |  |
|-----------|-------------|
| ID:                 | ND-Elasticity-1|
| Title:              | Continuous calculation of N/D elasticity. |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | The component will calculate and share the forecasts regarding the energy status and the energy elasticity of the neighborhood or District. The calculated information will be fed to the DSS and published to the upper EMaN. |
| Rationale:    | |

###### Demand/Response Strategies

|           |  |
|-----------|-------------|
| ID:                 | DR-Strategy-1|
| Title:              | Connectivity to Middleware and DSS |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:        | Developed tool shall be connected with the other subsystems for the proper data flow |
| Rationale:    | |

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

##### Decision Layer

###### Decision Support System (DSS) for Neighborhoods, Districs and City

| | |
|-----------|-------------|
| ID:                 | NDC-DSS-1|
| Title:              | Administrator is regularly informed for Decision Makings|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | Administrators will be able to overview, approve and change if needed the recommended decisions of the DSS.  |
| Rationale:    | Using the Operation Platform, neighborhood, district and city administrators will be able to validate, check and change if needed the proposed and applied control decision of DSS. |

| | |
|-----------|-------------|
| ID:                 | NDC-DSS-2|
| Title:              | Continuous Decision Making even if the system cycle or an input is not provided|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | DSS should ensure that control decisions will be made, even in the case the communication with other components is temporarily damaged or inputs from the network are not available.   |
| Rationale:    | It is crucial to ensure the continuous control of lower tier EMaNs, even if some components are not operating, providing the necessary simulations or inputs.  |

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

####  <!-- CHAPTER_NUMBER -->X.2.2 Non-Functional Requirements

##### Middleware
TODO

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

##### Prediction & Simulation Layer

###### Energy Load & Generation Prediction

| | |
|-----------|-------------|
| ID:                 | Load-Generation-7|
| Title:              | Secure data exchange|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  |The load and generation component should allow data exchange in a secure manner ensuring data privacy.|
| Rationale:    | |

| | |
|-----------|-------------|
| ID:                 | Load-Generation-8|
| Title:              | Training of ML and Deep Learning algorithms of Proactive aggregated management tools|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The component successfully should utilize the input data to train the Deep Learning Neural Networks responsible for providing predictionson aggregated data for each tier. |
| Rationale:    | |


| | |
|-----------|-------------|
| ID:                 | ND-Elasticity-2|
| Title:              | Secure Data Exchange with other components and layers|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The Energy Elasticity component should allow data exchange in a secure manner ensuring data privacy. |
| Rationale:    | |


<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

##### Decision Layer

###### Decision Support System (DSS)

| | |
|-----------|-------------|
| ID:                 | NDC-DSS-3|
| Title:              | Secure Data Exchange |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The DSS should allow data exchange in a secure manner ensuring data privacy.  |
| Rationale:    |   |

| | |
|-----------|-------------|
| ID:                 | NDC-DSS-4|
| Title:              | Reassure Decision Making in a communication error event |
| Priority:           | Should have |
| Tentative Schedule: | M(X)|
| Description:  | The DSS should utilize the data history to make optimal decisions in case current measurements or calculations are not available. In the extreme case that historical data are not enough (or the communication error lasts for long periods), rule-based controllers should be utilized.  |
| Rationale:    | It is crucial to ensure the continuous control of lower tier EMaNs, even if some components are not operating, providing the necessary simulations or inputs.  |

####  <!-- CHAPTER_NUMBER -->X.2.3 Data Requirements

##### Prediction & Simulation Layer

###### Energy Load & Generation Prediction

| | |
|-----------|-------------|
| ID:                 | Load-Generation-9|
| Title:              | Required Inputs|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The component should be fed with the required historical data on energy production and consumption of the building. Moreover, current and historical weather data will be provided. All the necessary inputs are provided by Middleware. |
| Rationale:    | |


###### Neighborhood and District Energy Flexibility

| | |
|-----------|-------------|
| ID:                 | ND-Elasticity-3|
| Title:              | Data Interface with DSS|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | Clear definition / list of operational parameters, with coding scheme, to be used for DSS. |
| Rationale:    | |

###### Demand/Response Strategies

| | |
|-----------|-------------|
| ID:                 | DR-Strategy-2|
| Title:              | Inputs for the D/R Strategy Tool.|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | Both historical data as well as real time data shall be collected from the demo sites focused on building energy production and generation. |
| Rationale:    | |

##### Decision Layer

###### Decision Support System (DSS)

| | |
|-----------|-------------|
| ID:                 | NDC-DSS-5|
| Title:              | Data interface with Energy Elasticity module |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | Collect and process inputs coming from Energy Elasticity module. |
| Rationale:    | Necessary inputs to make the final control decisions / recommendations.  |

| | |
|-----------|-------------|
| ID:                 | NDC-DSS-6|
| Title:              | Data interface with Load & Generation prediction module |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | Collect and process inputs coming from Load & Generation prediction module. |
| Rationale:    | Necessary inputs to make the final control decisions/recommendations.  |

| | |
|-----------|-------------|
| ID:                 | NDC-DSS-7|
| Title:              | Data interface with Middleware |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | Collect and process inputs coming from Middleware regarding internal and external current and historical data, and energy consumption/production. |
| Rationale:    | Necessary inputs to take the final control decisions/recommendations  |


###  <!-- CHAPTER_NUMBER -->X.3 Operational Platform

####  <!-- CHAPTER_NUMBER -->X.3.1 Functional Requirements

#####  Building Level Mobile App & Upper-Level Dashboards

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-1|
| Title:              | Anonymity of the users|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The mobile application and the dashboards should grant access to users (building occupants, managers, ICT developers and stakeholders) in anonymous mode  |
| Rationale:    | Using these, building managers, neighborhood, district and city administrators will be able to validate, check and change if needed the proposed and applied control decision of DSS.  |

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-2|
| Title:              | Anonymity of the tracking|
| Priority:           | Should have |
| Tentative Schedule: | M(X)|
| Description:  | The components of this layer should track anonymously the relevant actions that the user is carrying out within the application. The platform should register all the sections of the platform visited by the user during the session, as well as all the relevant actions executed.  |
| Rationale:    | Tracking user actions should allow the analysis of the most frequent used features of the application, and detect recurrent behaviors to support GUI improvement. |

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-3|
| Title:              | Preferences collection|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The application/dashboard shall permit the collection of anonymous user preferences required by other modules for prediction and proactive control.   |
| Rationale:    | User preferences are exploited by the DSS module to drive the predictions and decide among alternative control actions. |

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-4|
| Title:              | Comfort feedback Collection|
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The application/dashboard shall permit the collection of anonymous comfort feedback required by other modules for prediction and proactive control.  |
| Rationale:    | Comfort feedback responses are exploited by the DSS to drive the predictions and decide among alternative control actions. |

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-5|
| Title:              | Data visualization |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The application/dashboard shall visualize all the operational variables necessary for the user to assess the status of the Nodes   |
| Rationale:    | A compact yet informative data visualization interface enables users to understand the operations of the DSS and provide informed feedback. |

##### Authentication & Authorization

| | |
|-----------|-------------|
| ID:                 | Authentication-1 |
| Title:              | Authentication and user credentials |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The platform should manage the authentication and anonymous credentials for the involved entities in the system.    |
| Rationale:    |  |



| | |
|-----------|-------------|
| ID:                 | Authorization-1 |
| Title:              | Authorization based in policies |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The authorization framework should be capable of manage authorization policies to permit or deny access to resources or actions, for the involved entities (devices and services). |
| Rationale:    |  |

##### Data Storage

| | |
|-----------|-------------|
| ID:                 | Encryption-1 |
| Title:              | Data encryption with public key cryptography |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The platform should allow the encryption of sensor/actuation data by public-key cryptography techniques for its later storage.  |
| Rationale:    |  |


####  <!-- CHAPTER_NUMBER -->X.3.2 Non-Functional Requirements


#####  Building Level Mobile App & Upper-Level Dashboards

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-6|
| Title:              | Usability of the application |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  |  The interface should be intuitive, all the messages displayed should be clear and understandable, avoiding technical terms.  |
| Rationale:    | Based on the pilot survey, the users have a medium or high level of digital literacy. A user-friendly interface and clear messages must increase the adoption of the platform |

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-7|
| Title:              | Multi-device support |
| Priority:           | Should have |
| Tentative Schedule: | M(X)|
| Description:  |  The platform interfaces should be usable with devices and Operating Systems  |
| Rationale:    | The user may wish to use the platform both at Home and on the move. Notifications are best delivered on mobile devices. Diagrams and data are best viewed in tables or PC screens |

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-8|
| Title:              | Secure Data Exchange  |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  |  The component should allow data exchange in a secure manner ensuring data privacy.  |
| Rationale:    |  |

| | |
|-----------|-------------|
| ID:                 | Operational-Platform-9|
| Title:              | Continuous data access |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  |  Operational Platform should ensure that control operations must be made, even in the case the communication with other components is temporarily damaged.  |
| Rationale:    |  |


##### Authentication & Authorization

| | |
|-----------|-------------|
| ID:                 | Authentication-2 |
| Title:              | Authentication GDPR compliance |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | The authentication and user credentials management should be compliant with GDPR.    |
| Rationale:    |  |


##### Data Storage

| | |
|-----------|-------------|
| ID:                 | Encryption-2 |
| Title:              | Data encryption GDPR compliance |
| Priority:           | Must have |
| Tentative Schedule: | M(X)|
| Description:  | Encryption of user data should be performed via techniques compliant with the GDPR.   |
| Rationale:    |  |


