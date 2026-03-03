# 🎨 AquaIntel - UML Diagram Templates & Visual Guides

## Ready-to-Use Mermaid Diagrams for UML Creation

---

## 1. CLASS DIAGRAM - Main Architecture

```mermaid
classDiagram
    class FastAPIApp {
        +predict()
        +predict_transformer()
        +predict_comprehensive()
        +get_satellite()
        +get_geospatial()
        +compare_locations()
    }
    
    class AdvancedEnsemblePredictor {
        -models: Dict
        -weights: Dict
        -performance_history: List
        +initialize_models()
        +predict(lat, lon): Dict
        +optimize_weights()
        +update_weights_from_feedback()
    }
    
    class SpatialTransformerNetwork {
        -d_model: int = 256
        -num_heads: int = 8
        -num_layers: int = 6
        +multi_head_attention()
        +positional_encoding()
        +forward(): ndarray
        +predict_groundwater(): Dict
    }
    
    class LSTMTemporalModel {
        -hidden_units: int = 128
        -num_layers: int = 3
        +predict_temporal_patterns(): Dict
        +forecast_next_values(): ndarray
        +analyze_seasonality(): Dict
    }
    
    class SatelliteDataProcessor {
        -cache: Dict
        -data_sources: Dict
        +fetch_satellite_data(): Dict
        +_fetch_sentinel2(): Dict
        +_fetch_landsat(): Dict
        +_fetch_modis(): Dict
        +_fuse_satellite_sources(): Dict
    }
    
    class GeospatialAnalyzer {
        -dem_cache: Dict
        -geological_db: Dict
        +analyze_location_3d(): Dict
        +_analyze_terrain(): Dict
        +_analyze_geology(): Dict
        +_analyze_hydrology(): Dict
        +_analyze_soil(): Dict
    }
    
    class RealtimeDataEngine {
        -apis: Dict
        +fetch_all_data(): Dict
        +_fetch_nasa_power(): Dict
        +_fetch_weather_data(): Dict
        +_fetch_elevation(): Dict
        +calculate_groundwater_score(): Dict
    }
    
    class QuantumNeuralNetwork {
        -num_qubits: int
        -registers: List
        +create_quantum_circuit()
        +apply_ansatz()
        +optimize_parameters()
        +predict(): Dict
    }
    
    class PredictionRequest {
        +latitude: float
        +longitude: float
        +analysis_depth: str
        +include_satellite: bool
        +include_3d: bool
    }
    
    FastAPIApp --> AdvancedEnsemblePredictor
    FastAPIApp --> SpatialTransformerNetwork
    FastAPIApp --> LSTMTemporalModel
    FastAPIApp --> SatelliteDataProcessor
    FastAPIApp --> GeospatialAnalyzer
    FastAPIApp --> RealtimeDataEngine
    FastAPIApp --> QuantumNeuralNetwork
    FastAPIApp --> PredictionRequest
```

---

## 2. SEQUENCE DIAGRAM - Comprehensive Prediction Flow

```mermaid
sequenceDiagram
    participant User
    participant API as FastAPI
    participant Ens as Ensemble
    participant Trans as Transformer
    participant Sat as Satellite
    participant Geo as Geospatial
    participant RealTime as RealtimeAPI
    participant Fusion as Fusion Engine
    
    User->>API: POST /api/v1/predict/comprehensive
    activate API
    
    par Ensemble
        API->>Ens: predict(lat, lon)
        activate Ens
        Ens->>Ens: XGBoost (35%)
        Ens->>Ens: LightGBM (25%)
        Ens->>Ens: CatBoost (20%)
        Ens->>Ens: RandomForest (15%)
        Ens->>Ens: NeuralNet (5%)
        Ens->>Ens: Weighted average
        Ens-->>API: result
        deactivate Ens
    and Transformer
        API->>Trans: predict_groundwater(lat, lon)
        activate Trans
        Trans->>Trans: Positional encoding
        Trans->>Trans: 6 Attention layers
        Trans->>Trans: Multi-head attention
        Trans-->>API: result
        deactivate Trans
    and Satellite
        API->>Sat: fetch_satellite_data(lat, lon)
        activate Sat
        Sat->>Sat: Fetch Sentinel-2
        Sat->>Sat: Fetch Landsat
        Sat->>Sat: Fetch MODIS
        Sat->>Sat: Fuse sources
        Sat-->>API: result
        deactivate Sat
    and Geospatial
        API->>Geo: analyze_location_3d(lat, lon)
        activate Geo
        Geo->>Geo: Terrain analysis
        Geo->>Geo: Geology analysis
        Geo->>Geo: Hydrology analysis
        Geo->>Geo: Soil analysis
        Geo-->>API: result
        deactivate Geo
    and RealTime
        API->>RealTime: fetch_all_data(lat, lon)
        activate RealTime
        RealTime->>RealTime: NASA POWER
        RealTime->>RealTime: USGS Water
        RealTime->>RealTime: Open-Meteo
        RealTime->>RealTime: SoilGrids
        RealTime->>RealTime: Aggregate
        RealTime-->>API: result
        deactivate RealTime
    end
    
    API->>Fusion: Combine results
    activate Fusion
    Fusion->>Fusion: Weight: 35% Ens, 25% Trans, 20% Sat, 15% Geo, 5% Real
    Fusion->>Fusion: Calculate confidence
    Fusion->>Fusion: Determine risk level
    Fusion-->>API: fused_result
    deactivate Fusion
    
    API-->>User: Comprehensive response
    deactivate API
```

---

## 3. USE CASE DIAGRAM

```mermaid
graph TD
    User((User))
    Admin((Admin))
    System((AquaIntel System))
    
    User -->|1. Make Prediction| Pred["Predict Groundwater<br/>at Location"]
    User -->|2. View Results| View["View Prediction<br/>Results"]
    User -->|3. Compare| Comp["Compare Two<br/>Locations"]
    User -->|4. Feedback| Feed["Provide Drilling<br/>Feedback"]
    
    Admin -->|Monitor| Health["Check System<br/>Health"]
    Admin -->|Analyze| Analytics["View API<br/>Analytics"]
    Admin -->|Optimize| Opt["Optimize Model<br/>Weights"]
    
    Pred -->|Uses| Ens["Ensemble<br/>Predictor"]
    View -->|Uses| Vis["Visualization<br/>Engine"]
    Comp -->|Uses| Ens
    Feed -->|Triggers| Learn["Adaptive<br/>Learning"]
    
    Learn -->|Updates| Weights["Model<br/>Weights"]
    Weights -->|Improves| Ens
    
    Pred -->|Fetches| Data["Real-Time<br/>Data APIs"]
    Pred -->|Analyzes| Sat["Satellite<br/>Data"]
    Pred -->|Analyzes| Geo["Geospatial<br/>3D Data"]
```

---

## 4. COMPONENT DIAGRAM

```mermaid
graph LR
    Browser["Web Browser<br/>Frontend"]
    
    subgraph API["FastAPI Server"]
        Routes["API Routes<br/>& Handlers"]
        Validation["Request<br/>Validation"]
    end
    
    subgraph ML_ENGINE["ML & AI Engine"]
        Ensemble["Ensemble<br/>Predictor"]
        Transformer["Transformer<br/>Network"]
        LSTM["LSTM<br/>Model"]
        QuantumNN["Quantum NN<br/>Optimizer"]
    end
    
    subgraph DATA_PROC["Data Processing"]
        Satellite["Satellite<br/>Processor"]
        Geospatial["Geospatial<br/>Analyzer"]
        RealTime["Real-Time<br/>Data Engine"]
    end
    
    subgraph EXTERNAL["External APIs"]
        API1["NASA POWER"]
        API2["USGS Water"]
        API3["Open-Meteo"]
        API4["SoilGrids & Others"]
    end
    
    Browser -->|HTTP Requests| Routes
    Routes --> Validation
    Validation --> Ensemble
    Validation --> Transformer
    Validation --> LSTM
    Validation --> QuantumNN
    
    Ensemble --> Satellite
    Transformer --> Geospatial
    LSTM --> RealTime
    
    Satellite --> EXTERNAL
    Geospatial --> EXTERNAL
    RealTime --> API1
    RealTime --> API2
    RealTime --> API3
    RealTime --> API4
    
    Ensemble --> Browser
    Transformer --> Browser
    LSTM --> Browser
```

---

## 5. DEPLOYMENT DIAGRAM

```mermaid
graph TD
    Client["Client Machine<br/>Web Browser"]
    
    subgraph Deployment1["Advanced Backend<br/>main.py"]
        FastAPI1["FastAPI + Uvicorn"]
        TF["TensorFlow<br/>2.15.0"]
        Torch["PyTorch<br/>2.1.1"]
        XGB["XGBoost"]
        All["All dependencies"]
    end
    
    subgraph Deployment2["Standalone<br/>main_standalone.py"]
        FastAPI2["FastAPI + Uvicorn"]
        Simple["Simplified Rules<br/>& Logic"]
        Minimal["Minimal deps"]
    end
    
    subgraph Deployment3["Advanced NoLib<br/>main_advanced.py"]
        FastAPI3["FastAPI + Uvicorn"]
        Advanced["Advanced Logic<br/>No Heavy Libs"]
        Medium["Medium deps"]
    end
    
    ExternalAPIs["10+ External APIs<br/>Real-Time Data"]
    
    Client -->|HTTPS| Deployment1
    Client -->|HTTPS| Deployment2
    Client -->|HTTPS| Deployment3
    
    FastAPI1 --> TF
    FastAPI1 --> Torch
    FastAPI1 --> XGB
    
    FastAPI2 --> Simple
    FastAPI3 --> Advanced
    
    Deployment1 --> ExternalAPIs
    Deployment2 --> ExternalAPIs
    Deployment3 --> ExternalAPIs
    
    style Deployment1 fill:#e1f5ff
    style Deployment2 fill:#f3e5f5
    style Deployment3 fill:#e8f5e9
```

---

## 6. STATE DIAGRAM - Prediction Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Idle
    
    Idle -->|User Input| Validating: latitude, longitude\nanalysis_depth
    
    Validating -->|Valid| Fetching: Request received
    Validating -->|Invalid| Error: Invalid input
    Error --> [*]
    
    Fetching -->|Parallel| Ensemble_Run
    Fetching -->|Parallel| Transformer_Run
    Fetching -->|Parallel| Satellite_Run
    Fetching -->|Parallel| Geospatial_Run
    Fetching -->|Parallel| RealTime_Run
    
    Ensemble_Run -->|Complete| Waiting
    Transformer_Run -->|Complete| Waiting
    Satellite_Run -->|Complete| Waiting
    Geospatial_Run -->|Complete| Waiting
    RealTime_Run -->|Complete| Waiting
    
    Waiting -->|All Complete| Fusion
    
    Fusion -->|Combine Results| Scoring
    Scoring -->|Calculate Confidence| Optimization
    Optimization -->|Quantum Annealing| ResponseGen
    
    ResponseGen -->|Generate JSON| Success
    Success --> [*]
    
    note right of Validating
        Validate request
        Check bounds
        Authenticate
    end note
    
    note right of Ensemble_Run
        XGBoost
        LightGBM
        CatBoost
        RF, NN
    end note
    
    note right of Fusion
        Weight: 35% Ens
        25% Trans
        20% Sat
        15% Geo
        5% Real
    end note
```

---

## 7. ACTIVITY DIAGRAM - Comprehensive Prediction

```mermaid
graph TD
    Start([Start: User Request]) --> Parse[Parse Request<br/>lat, lon, depth]
    
    Parse --> DecideDepth{Analysis Depth?}
    
    DecideDepth -->|Quick| QuickMode["Run: Ensemble Only"]
    DecideDepth -->|Standard| StandardMode["Run: Ensemble +<br/>Transformer"]
    DecideDepth -->|Comprehensive| CompMode["Run: All Models +<br/>Satellite + 3D"]
    
    QuickMode --> Ens_Quick["Ensemble Prediction<br/>100-200ms"]
    StandardMode --> Ens_Std["Ensemble Prediction"]
    StandardMode --> Trans_Std["Transformer Prediction"]
    CompMode --> Ens_Comp["Ensemble Prediction"]
    CompMode --> Trans_Comp["Transformer Prediction"]
    CompMode --> Sat_Comp["Satellite Processing<br/>Sentinel2, Landsat"]
    CompMode --> Geo_Comp["Geospatial Analysis<br/>3D Layers"]
    CompMode --> Real_Comp["Real-Time APIs<br/>10+ sources"]
    
    Ens_Quick --> Gather1["Gather Results"]
    Ens_Std --> Gather2["Gather Results"]
    Trans_Std --> Gather2
    
    Ens_Comp --> Gather3["Gather Results"]
    Trans_Comp --> Gather3
    Sat_Comp --> Gather3
    Geo_Comp --> Gather3
    Real_Comp --> Gather3
    
    Gather1 --> Fuse1["Fuse Results<br/>50% Ens"]
    Gather2 --> Fuse2["Fuse Results<br/>60% Ens, 40% Trans"]
    Gather3 --> Fuse3["Fuse Results<br/>35% Ens, 25% Trans,<br/>20% Sat, 15% Geo, 5% Real"]
    
    Fuse1 --> Calc1["Calculate<br/>Confidence"]
    Fuse2 --> Calc2["Calculate<br/>Confidence"]
    Fuse3 --> Calc3["Calculate<br/>Confidence"]
    
    Calc1 --> Format["Format JSON<br/>Response"]
    Calc2 --> Format
    Calc3 --> Format
    
    Format --> Return["Return to<br/>Frontend"]
    Return --> End([End])
    
    style QuickMode fill:#c8e6c9
    style StandardMode fill:#fff9c4
    style CompMode fill:#ffccbc
```

---

## 8. PACKAGE DIAGRAM

```mermaid
graph TB
    subgraph Frontend["Frontend Package"]
        HTML["HTML Pages<br/>index, dashboard,<br/>predictions, etc."]
        CSS["Styling<br/>styles.css"]
        JS["API Client<br/>api-client.js"]
    end
    
    subgraph API_Layer["API Layer Package"]
        MainPy["main.py<br/>Advanced Backend"]
        StandalonePy["main_standalone.py<br/>Self-Contained"]
        AdvancedPy["main_advanced.py<br/>No Dependencies"]
    end
    
    subgraph ML_Package["ML & AI Package"]
        Ensemble["ensemble_predictor.py<br/>5 Models"]
        DL["deep_learning_models.py<br/>Transformer + LSTM"]
        Quantum["quantum_neural_network.py<br/>Quantum Optimization"]
    end
    
    subgraph Data_Package["Data Processing Package"]
        Satellite["satellite_processor.py<br/>Multi-Source Fusion"]
        Geospatial["geospatial_analyzer.py<br/>3D Analysis"]
        RealTime["realtime_data_apis.py<br/>10+ APIs"]
    end
    
    subgraph External["External Services Package"]
        NASA["NASA POWER"]
        USGS["USGS Water"]
        OM["Open-Meteo"]
        SG["SoilGrids"]
        OT["OpenTopoData"]
        EQ["USGS Earthquake"]
        SM["Soil Moisture"]
    end
    
    Frontend -->|HTTP| API_Layer
    API_Layer -->|Uses| ML_Package
    API_Layer -->|Uses| Data_Package
    ML_Package -->|Feeds to| API_Layer
    Data_Package -->|Fetches from| External
    
    style Frontend fill:#e1f5fe
    style API_Layer fill:#fff3e0
    style ML_Package fill:#f3e5f5
    style Data_Package fill:#e8f5e9
    style External fill:#fce4ec
```

---

## 9. TIMING DIAGRAM - Response Times

```
Prediction Type      | Ensemble | Transformer | Satellite | Geospatial | Real-Time | Fusion | Total
---------------------|----------|-------------|-----------|------------|-----------|--------|--------
Quick (Ensemble)     | 100-200ms|             |           |            |           | 10ms   | ~220ms
Standard (E+T)       | 100-200ms| 150-300ms  |           |            |           | 15ms   | ~500ms
Comprehensive        | 100-200ms| 150-300ms  | 3-5s      | 2-4s       | 2-3s      | 50ms   | ~5-15s
```

---

## 10. DATA FLOW DIAGRAM - Real-Time Integration

```mermaid
graph LR
    User[User Request]
    
    User -->|lat, lon| Engine["RealtimeDataEngine<br/>fetch_all_data()"]
    
    Engine -->|Async Task 1| NASA["NASA POWER<br/>365-day history<br/>Climate data"]
    Engine -->|Async Task 2| USGS["USGS Water<br/>Groundwater wells<br/>Water levels"]
    Engine -->|Async Task 3| OM["Open-Meteo<br/>Current weather<br/>5-year archive"]
    Engine -->|Async Task 4| SG["SoilGrids<br/>Soil props 3 depths<br/>Clay, sand, silt"]
    Engine -->|Async Task 5| OT["OpenTopoData<br/>Elevation<br/>SRTM 90m"]
    Engine -->|Async Task 6| EQ["USGS Earthquake<br/>5-year seismic<br/>Magnitude data"]
    Engine -->|Async Task 7| SM["Soil Moisture<br/>Surface + deep<br/>30-day history"]
    Engine -->|Async Task 8| PRECIP["Precipitation<br/>90-day history<br/>7-day forecast"]
    
    NASA -->|asyncio.gather()| Aggregate["Aggregate Results<br/>10+ data sources"]
    USGS -->|asyncio.gather()| Aggregate
    OM -->|asyncio.gather()| Aggregate
    SG -->|asyncio.gather()| Aggregate
    OT -->|asyncio.gather()| Aggregate
    EQ -->|asyncio.gather()| Aggregate
    SM -->|asyncio.gather()| Aggregate
    PRECIP -->|asyncio.gather()| Aggregate
    
    Aggregate --> Scoring["Calculate<br/>Groundwater<br/>Score"]
    
    Scoring -->|30% Weight| Precip_Score["Precipitation<br/>Score"]
    Scoring -->|20% Weight| Climate_Score["Climate<br/>History Score"]
    Scoring -->|15% Weight| Soil_Score["Soil<br/>Composition"]
    Scoring -->|15% Weight| Moisture_Score["Soil Moisture<br/>Score"]
    Scoring -->|10% Weight| Elev_Score["Elevation<br/>Score"]
    Scoring -->|10% Weight| Wells_Score["USGS Wells<br/>Proximity"]
    
    Precip_Score --> Final["Final Groundwater<br/>Potential Score<br/>0-100"]
    Climate_Score --> Final
    Soil_Score --> Final
    Moisture_Score --> Final
    Elev_Score --> Final
    Wells_Score --> Final
    
    Final --> Output["Return to<br/>Prediction Engine"]
```

---

## 11. OBJECT DIAGRAM - Example Instance

```mermaid
graph TD
    Pred["prediction_instance<br/>:PredictionRequest"]
    Pred -->|lat| Lat["13.0827"]
    Pred -->|lon| Lon["80.2707"]
    Pred -->|depth| Depth["comprehensive"]
    Pred -->|satellite| Sat["true"]
    Pred -->|3d| 3D["true"]
    
    Result["result_instance<br/>:PredictionResponse"]
    Result -->|success| Success["87.2%"]
    Result -->|depth| DepthEst["47.1m"]
    Result -->|yield| Yield["1320 L/hr"]
    Result -->|confidence| Conf["94.1%"]
    Result -->|risk| Risk["low"]
    
    Ens["ensemble_instance<br/>:AdvancedEnsemblePredictor"]
    Ens -->|xgb_weight| XW["0.35"]
    Ens -->|lgb_weight| LW["0.25"]
    Ens -->|cat_weight| CW["0.20"]
    Ens -->|rf_weight| RW["0.15"]
    Ens -->|nn_weight| NW["0.05"]
    Ens -->|trained| Trained["true"]
```

---

## 12. COMMUNICATION DIAGRAM

```mermaid
graph TB
    UI["User Interface"]
    
    UI -->|1: request| API["FastAPI<br/>Handler"]
    API -->|2: validate| Validator["Pydantic<br/>Validator"]
    Validator -->|3: ok| API
    API -->|4: execute| Ens["Ensemble<br/>Predictor"]
    API -->|4: execute| Trans["Transformer<br/>Network"]
    API -->|4: execute| Sat["Satellite<br/>Processor"]
    API -->|4: execute| Geo["Geospatial<br/>Analyzer"]
    API -->|4: execute| Real["Real-Time<br/>Engine"]
    
    Ens -->|5a: result| Fusion["Fusion<br/>Engine"]
    Trans -->|5b: result| Fusion
    Sat -->|5c: result| Fusion
    Geo -->|5d: result| Fusion
    Real -->|5e: result| Fusion
    
    Fusion -->|6: fused| API
    API -->|7: format| JSON["JSON<br/>Serializer"]
    JSON -->|8: response| UI
    
    Real -->|fetch| ExtAPI["10+ External<br/>APIs"]
    ExtAPI -->|data| Real
```

---

## 13. COLLABORATION DIAGRAM

```mermaid
graph TB
    Client["Client Browser"]
    
    Client -->|1A| ApiClient["API Client<br/>JavaScript"]
    ApiClient -->|1B| Http["HTTP/HTTPS<br/>Transport"]
    Http -->|1C| FastApi["FastAPI<br/>Server"]
    
    FastApi -->|2A| InputVal["Input<br/>Validator"]
    InputVal -->|2B| Router["Route<br/>Router"]
    
    Router -->|3A| EnsPred["Ensemble<br/>Predictor"]
    Router -->|3B| TransPred["Transformer<br/>Predictor"]
    Router -->|3C| SatProc["Satellite<br/>Data"]
    Router -->|3D| GeoProc["Geospatial<br/>Data"]
    Router -->|3E| RealEng["Real-Time<br/>Engine"]
    
    EnsPred -->|4A| Model1["XGBoost"]
    EnsPred -->|4B| Model2["LightGBM"]
    EnsPred -->|4C| Model3["CatBoost"]
    EnsPred -->|4D| Model4["RF"]
    EnsPred -->|4E| Model5["NN"]
    
    Model1 -->|5| Average["Weighted<br/>Average"]
    Model2 -->|5| Average
    Model3 -->|5| Average
    Model4 -->|5| Average
    Model5 -->|5| Average
    
    Average -->|6A| CombResults["Combine<br/>Results"]
    TransPred -->|6B| CombResults
    SatProc -->|6C| CombResults
    GeoProc -->|6D| CombResults
    RealEng -->|6E| CombResults
    
    CombResults -->|7| Response["Generate<br/>Response"]
    Response -->|8| Client
```

---

## Key Statistics for Your UML Diagrams

- **Total Classes**: 7 main + 20+ supporting
- **Total Methods**: 100+ across all classes
- **Total Attributes**: 50+ data members
- **Relationships**: 40+ (inheritance, composition, aggregation, dependency)
- **External Integrations**: 10+ APIs
- **Data Flow Paths**: 5+ main streams
- **Parallel Process Streams**: 5 (Ensemble, Transformer, Satellite, Geospatial, Real-Time)
- **Asynchronous Operations**: 10+ async methods
- **Total API Endpoints**: 10+
- **Response Time Range**: 100ms - 15 seconds

---

## Tools Recommended for Creating UML Diagrams

1. **Lucidchart** - Complete UML suite
2. **Draw.io** - Free, web-based
3. **Visual Paradigm** - Professional UML
4. **Star UML** - Lightweight, specialized
5. **PlantUML** - Text-based, scriptable
6. **ArchiMate** - Enterprise architecture
7. **Miro** - Collaborative diagramming

---

**All diagrams can be imported into your preferred UML tool!**

