# 📚 AquaIntel - Quick Reference for UML Class Specifications

## Complete Class Details for Diagram Creation

---

## 1. AdvancedEnsemblePredictor

**File:** `backend/ai/ensemble_predictor.py`  
**Type:** Concrete Class  
**Responsibility:** Combine 5 ML models with intelligent weight optimization

### Attributes
```python
- models: Dict[str, Any]
  └─ Contains: xgboost, lightgbm, catboost, random_forest, neural_net
  
- weights: Dict[str, float]
  └─ xgboost: 0.35
  └─ lightgbm: 0.25
  └─ catboost: 0.20
  └─ random_forest: 0.15
  └─ neural_net: 0.05
  
- performance_history: List[Dict]
  └─ Stores historical performance metrics
  
- is_trained: bool
  └─ Training status flag
```

### Methods
```python
+ __init__()
+ initialize_models()
+ _initialize_neural_network()
+ train_ensemble(X: np.ndarray, y: np.ndarray) → None
+ predict(latitude: float, longitude: float) → Dict[str, float]
+ predict_batch(locations: List[Dict]) → List[Dict]
+ optimize_weights() → Dict[str, float]
+ evaluate_performance(X_test, y_test) → Dict
+ update_weights_from_feedback(feedback: FeedbackRequest) → None
+ get_feature_importance() → Dict[str, float]
+ save_model(filepath: str) → bool
+ load_model(filepath: str) → bool
```

### Return Structure
```python
{
    "success_probability": float (0-100),
    "estimated_depth_m": float,
    "estimated_yield_liters_per_hour": float,
    "confidence_score": float (0-100),
    "risk_level": str,
    "individual_model_predictions": Dict,
    "model_weights": Dict,
    "recommendations": List[str]
}
```

### Dependencies
- xgboost.XGBRegressor
- lightgbm.LGBMRegressor
- catboost.CatBoostRegressor
- sklearn.ensemble.RandomForestRegressor
- Custom NeuralNetwork (or TensorFlow)

---

## 2. SpatialTransformerNetwork

**File:** `backend/ai/deep_learning_models.py`  
**Type:** Concrete Class  
**Responsibility:** Deep learning transformer with attention mechanism

### Attributes
```python
- d_model: int = 256
  └─ Embedding dimension
  
- num_heads: int = 8
  └─ Number of attention heads
  
- num_layers: int = 6
  └─ Number of transformer layers
  
- is_trained: bool
  └─ Training status
  
- attention_weights: np.ndarray (Optional)
  └─ Cached attention weights for visualization
```

### Methods
```python
+ __init__(d_model: int, num_heads: int, num_layers: int)
+ multi_head_attention(query: np.ndarray, key: np.ndarray, 
                       value: np.ndarray, mask: np.ndarray) → np.ndarray
+ _softmax(x: np.ndarray, axis: int) → np.ndarray
+ positional_encoding(seq_len: int) → np.ndarray
+ forward(spatial_features: np.ndarray) → np.ndarray
+ _layer_norm(x: np.ndarray, epsilon: float) → np.ndarray
+ _feed_forward(x: np.ndarray) → np.ndarray
+ predict_groundwater(latitude: float, longitude: float) → Dict
+ get_attention_visualization() → np.ndarray
+ train(training_data: List) → None
```

### Architecture
```
Input Layer
    ↓
Positional Encoding
    ↓
6 Transformer Layers:
  ├─ Multi-Head Attention (8 heads)
  ├─ Layer Normalization
  ├─ Feed-Forward Network (2 layers)
  ├─ Layer Normalization
  └─ Residual Connections
    ↓
Output Layer (Predictor)
```

### Return Structure
```python
{
    "groundwater_score": float (0-100),
    "confidence": float (0-100),
    "attention_patterns": Dict,
    "spatial_insights": str,
    "factors_influencing": List[str]
}
```

---

## 3. LSTMTemporalModel

**File:** `backend/ai/deep_learning_models.py`  
**Type:** Concrete Class  
**Responsibility:** Capture temporal patterns in groundwater time series

### Attributes
```python
- hidden_units: int = 128
  └─ Number of LSTM units per layer
  
- num_layers: int = 3
  └─ Number of stacked LSTM layers
  
- sequence_length: int
  └─ Length of input sequences
  
- is_trained: bool
  └─ Training status
```

### Methods
```python
+ __init__(hidden_units: int, num_layers: int)
+ create_sequences(data: np.ndarray, seq_len: int) → Tuple[np.ndarray, np.ndarray]
+ predict_temporal_patterns(time_series: List[float]) → Dict
+ forecast_next_values(past_values: List[float], steps: int) → np.ndarray
+ analyze_seasonality() → Dict
+ detect_anomalies() → List[Dict]
+ train(training_sequences: np.ndarray, labels: np.ndarray) → None
+ evaluate(test_sequences: np.ndarray) → Dict
```

### Architecture
```
Input Sequence (normalized time series)
    ↓
3 LSTM Layers (128 units each):
  ├─ LSTM Layer 1
  ├─ Dropout (0.2)
  ├─ LSTM Layer 2
  ├─ Dropout (0.2)
  ├─ LSTM Layer 3
  └─ Dropout (0.2)
    ↓
Dense Layer (32 units, ReLU)
    ↓
Output Layer (Prediction)
```

### Return Structure
```python
{
    "temporal_score": float (0-100),
    "seasonality_detected": bool,
    "trend": str ("increasing", "decreasing", "stable"),
    "forecast_values": List[float],
    "anomalies": List[Dict],
    "confidence": float
}
```

---

## 4. QuantumNeuralNetwork

**File:** `backend/ai/quantum_neural_network.py`  
**Type:** Concrete Class + Qubit, QuantumRegister  
**Responsibility:** Quantum-inspired optimization for parameter tuning

### Main Classes

#### Qubit
```python
class Qubit:
    - alpha: complex      # Probability amplitude for |0⟩
    - beta: complex       # Probability amplitude for |1⟩
    
    + __post_init__()
    + measure() → int     # Returns 0 or 1
    + probability() → Tuple[float, float]
```

#### QuantumRegister
```python
class QuantumRegister:
    - num_qubits: int
    - state_vector: np.ndarray (2^num_qubits complex)
    
    + __init__(num_qubits: int)
    + hadamard(qubit_idx: int)          # Superposition
    + phase(qubit_idx: int, angle: float)  # Phase rotation
    + cnot(control: int, target: int)   # Entanglement
    + _apply_single_gate(gate: np.ndarray, qubit_idx: int)
    + measure_all() → int
```

#### QuantumNeuralNetwork
```python
class QuantumNeuralNetwork:
    - num_qubits: int
    - depth: int = 10         # Circuit depth
    - registers: List[QuantumRegister]
    - classifiers: List       # Measurement patterns
    - is_trained: bool
    
    + __init__(num_qubits: int, depth: int)
    + create_quantum_circuit()
    + apply_ansatz(parameters: np.ndarray)
    + optimize_parameters(X: np.ndarray, y: np.ndarray, 
                          epochs: int) → np.ndarray
    + predict(features: np.ndarray) → Dict
    + quantum_tunneling_escape() → bool
    + simulated_annealing(initial_temp: float, 
                          cooling_rate: float) → Dict
    + get_circuit_description() → str
```

### Quantum Gates Implemented
```python
- Hadamard (H): Creates superposition
- CNOT (CX): Creates entanglement
- Phase (Z): Applies phase rotation
- Pauli (X, Y, Z): Basic rotations
```

### Optimization Techniques
```
Simulated Annealing:
  - Initial temperature T₀
  - Cooling rate α (0.95)
  - Probability: exp(-ΔE/T)
  
Quantum Tunneling:
  - Probability to escape local optima: p_tunnel
  - Jump distance: proportional to barrier height
```

### Return Structure
```python
{
    "optimized_parameters": np.ndarray,
    "fitness_score": float,
    "iterations": int,
    "converged": bool,
    "escape_count": int,
    "final_temperature": float
}
```

---

## 5. SatelliteDataProcessor

**File:** `backend/ai/satellite_processor.py`  
**Type:** Concrete Class  
**Responsibility:** Multi-source satellite imagery fusion

### Attributes
```python
- cache: Dict[str, Any]
  └─ Caches satellite data for 24 hours
  
- data_sources: Dict[str, Dict]
  └─ sentinel2: {resolution: 10, bands: 13}
  └─ landsat8: {resolution: 30, bands: 11}
  └─ modis: {resolution: 250, bands: 7}
```

### Methods
```python
+ fetch_satellite_data(latitude: float, longitude: float,
                       start_date: Optional[str],
                       end_date: Optional[str]) → Dict
+ _fetch_sentinel2(lat: float, lon: float, start, end) → Dict
+ _fetch_landsat(lat: float, lon: float, start, end) → Dict
+ _fetch_modis(lat: float, lon: float, start, end) → Dict
+ _fuse_satellite_sources(sentinel: Dict, landsat: Dict, 
                          modis: Dict) → Dict
+ _calculate_ndvi(nir: np.ndarray, red: np.ndarray) → np.ndarray
+ _calculate_ndwi(nir: np.ndarray, swir: np.ndarray) → np.ndarray
+ _calculate_evi(nir, red, blue) → np.ndarray
+ _calculate_moisture_stress(bands: Dict) → float
+ _calculate_thermal_indices(bands: Dict) → Dict
+ _quality_assessment(data: Dict) → float (0-100)
+ cache_data(key: str, data: Dict, ttl: int)
+ clear_cache()
```

### Satellite Data Sources

**Sentinel-2 (10m)**
```python
{
    'blue': Band B2 (490nm),
    'green': Band B3 (560nm),
    'red': Band B4 (665nm),
    'nir': Band B8 (842nm),
    'nir_narrow': Band B8A (865nm),
    'red_edge1': Band B5 (705nm),
    'red_edge2': Band B6 (740nm),
    'red_edge3': Band B7 (783nm),
    'swir1': Band B11 (1610nm),
    'swir2': Band B12 (2190nm),
    'indices': {
        'ndvi': Vegetation,
        'ndwi': Water,
        'evi': Enhanced Vegetation
    }
}
```

**Landsat-8 (30m)**
```python
{
    'coastal': Band 1 (443nm),
    'blue': Band 2 (480nm),
    'green': Band 3 (560nm),
    'red': Band 4 (655nm),
    'nir': Band 5 (865nm),
    'swir1': Band 6 (1610nm),
    'swir2': Band 7 (2200nm),
    'thermal1': Band 10 (10900nm),
    'thermal2': Band 11 (12000nm),
    'indices': {
        'ndbi': Modified NDBI,
        'ndmi': Modified NDVI,
        'lst': Land Surface Temp,
        'thermal_signature': Pattern
    }
}
```

### Return Structure
```python
{
    'sources': List[str],          # ["Sentinel-2", "Landsat", "MODIS"]
    'fused_data': Dict,
    'vegetation_score': float,
    'moisture_score': float,
    'thermal_signature': Dict,
    'quality': float (0-100),
    'confidence': float (0-100),
    'acquisition_date': str,
    'cloud_coverage': float
}
```

---

## 6. GeospatialAnalyzer

**File:** `backend/ai/geospatial_analyzer.py`  
**Type:** Concrete Class  
**Responsibility:** 3D geospatial multi-layer analysis

### Attributes
```python
- dem_cache: Dict[str, np.ndarray]
  └─ Digital Elevation Model data cache
  
- geological_db: Dict
  └─ Geological formations database
```

### Methods - Terrain Analysis
```python
+ _analyze_terrain(lat: float, lon: float, radius: float) → Dict
  ├─ _get_elevation_grid() → np.ndarray
  ├─ _calculate_slope() → float (degrees)
  ├─ _calculate_aspect() → float (degrees)
  ├─ _calculate_roughness() → float
  ├─ _calculate_flow_accumulation() → np.ndarray
  ├─ _delineate_watershed() → float (km²)
  ├─ _calculate_tpi() → float (Topographic Position Index)
  └─ _classify_terrain() → str
```

### Methods - Geology Analysis
```python
+ _analyze_geology(lat: float, lon: float) → Dict
  ├─ _get_geological_formations() → List[str]
  ├─ _calculate_lithology_score() → float (0-100)
  ├─ _estimate_porosity_permeability() → Dict
  │   └─ porosity: float (%)
  │   └─ permeability: float (m/day)
  ├─ _calculate_groundwater_table_depth() → float (m)
  └─ _estimate_aquifer_thickness() → float (m)
```

### Methods - Hydrology Analysis
```python
+ _analyze_hydrology(lat: float, lon: float, 
                     terrain: Dict) → Dict
  ├─ _calculate_runoff_coefficient() → float
  ├─ _analyze_stream_network() → Dict
  ├─ _calculate_recharge_potential() → float (0-100)
  ├─ _identify_discharge_areas() → List[Dict]
  ├─ _calculate_base_flow() → float (m³/s)
  └─ _calculate_hydrological_risk() → float (0-100)
```

### Methods - Soil Analysis
```python
+ _analyze_soil(lat: float, lon: float, 
                geology: Dict) → Dict
  ├─ _get_soil_properties() → Dict
  │   └─ clay: float (%)
  │   └─ sand: float (%)
  │   └─ silt: float (%)
  ├─ _calculate_water_retention() → float
  ├─ _calculate_infiltration_rate() → float (mm/hr)
  └─ _calculate_permeability() → float (m/day)
```

### Methods - Visualization & Integration
```python
+ _generate_3d_visualization() → Dict
+ _calculate_integrated_potential() → Dict
+ analyze_location_3d(lat: float, lon: float, 
                      radius_km: float) → Dict
```

### Return Structure
```python
{
    'terrain': {
        'elevation_m': float,
        'slope_degrees': float,
        'aspect_degrees': float,
        'roughness_index': float,
        'drainage': {...}
    },
    'geology': {
        'lithology': str,
        'porosity': float,
        'permeability': float,
        'aquifer_thickness': float
    },
    'hydrology': {
        'recharge_potential': float,
        'runoff_coefficient': float,
        'base_flow': float
    },
    'soil': {
        'clay_content': float,
        'infiltration_rate': float,
        'water_retention': float
    },
    'groundwater_potential': float (0-100),
    'confidence': float (0-100)
}
```

---

## 7. RealtimeDataEngine

**File:** `backend/services/realtime_data_apis.py`  
**Type:** Concrete Class  
**Responsibility:** Async fetching from 10+ live APIs

### Attributes
```python
- apis: Dict[str, str]
  └─ nasa_power: 'https://power.larc.nasa.gov/api/...'
  └─ open_meteo: 'https://api.open-meteo.com/v1/forecast'
  └─ open_elevation: 'https://api.open-elevation.com/...'
  └─ soilgrids: 'https://rest.isric.org/soilgrids/...'
  └─ usgs_water: 'https://waterservices.usgs.gov/nwis/iv/'
  └─ climate_api: 'https://archive-api.open-meteo.com/...'
  └─ dem_api: 'https://api.opentopodata.org/v1/srtm90m'
  └─ earthquake_api: 'https://earthquake.usgs.gov/fdsnws/...'
  └─ soil_moisture: 'https://api.open-meteo.com/v1/flood'
  └─ weather_api: 'https://api.open-meteo.com/v1/forecast'
```

### Methods
```python
+ fetch_all_data(latitude: float, longitude: float) → Dict
  (Executes all 9 tasks asynchronously)

+ async _fetch_nasa_power(session, lat, lon) → Dict
  ├─ Temperature (T2M)
  ├─ Precipitation (PRECTOTCORR)
  ├─ Humidity (RH2M)
  ├─ Solar Radiation (ALLSKY_SFC_SW_DWN)
  └─ Wind Speed (WS2M)

+ async _fetch_weather_data(session, lat, lon) → Dict
  ├─ Current temperature
  ├─ Wind speed
  ├─ Weather code
  └─ Hourly data

+ async _fetch_climate_history(session, lat, lon) → Dict
  ├─ 5-year temperature mean
  ├─ Precipitation sum
  └─ Humidity mean

+ async _fetch_elevation(session, lat, lon) → Dict
  └─ Elevation (meters, SRTM 90m)

+ async _fetch_soil_data(session, lat, lon) → Dict
  ├─ Clay (%)
  ├─ Sand (%)
  ├─ Silt (%)
  ├─ pH (H2O)
  ├─ Organic Carbon
  └─ Bulk Density

+ async _fetch_usgs_groundwater(session, lat, lon) → Dict
  ├─ Nearby wells count
  └─ Has groundwater data (bool)

+ async _fetch_precipitation(session, lat, lon) → Dict
  ├─ 90-day history (mm)
  └─ 7-day forecast (mm)

+ async _fetch_earthquake_data(session, lat, lon) → Dict
  ├─ Earthquake count (5 year)
  ├─ Max magnitude
  ├─ Average magnitude
  └─ Seismic risk level

+ async _fetch_soil_moisture(session, lat, lon) → Dict
  ├─ Surface moisture (0-10cm)
  └─ Deep moisture (10-40cm)

+ calculate_groundwater_score(data: Dict) → Dict
  ├─ 30% weight: Annual precipitation
  ├─ 20% weight: 5-year climate
  ├─ 15% weight: Soil composition
  ├─ 15% weight: Soil moisture
  ├─ 10% weight: Elevation
  └─ 10% weight: Nearby wells
```

### Scoring Algorithm

| Factor | Weight | Formula | Range |
|--------|--------|---------|-------|
| Precipitation | 30% | min(precip/1000, 1.0) × 30 | 0-30 |
| Climate History | 20% | min(precip_5yr/5000, 1.0) × 20 | 0-20 |
| Soil Composition | 15% | (1 - abs(clay-30)/30) × 15 | 0-15 |
| Soil Moisture | 15% | moisture × 15 | 0-15 |
| Elevation | 10% | max(0, (2000-elev)/2000) × 10 | 0-10 |
| USGS Wells | 10% | min(wells/10, 1.0) × 10 | 0-10 |
| **Total** | **100%** | **(score/confidence) × 100** | **0-100** |

### Return Structure
```python
{
    'groundwater_potential': float (0-100),
    'confidence': float (sum of weights with data),
    'factors': List[str],
    'data_sources_used': int,
    'timestamp': str (ISO),
    'location': {'latitude': float, 'longitude': float},
    
    'nasa_power': {
        'avg_temperature': float,
        'total_precipitation': float,
        'avg_humidity': float,
        'avg_solar': float,
        'avg_windspeed': float
    },
    'current_weather': {...},
    'climate_history': {...},
    'elevation': {...},
    'soil_data': {...},
    'usgs_wells': {...},
    'precipitation': {...},
    'seismic_activity': {...},
    'soil_moisture': {...}
}
```

---

## 8. FastAPI Application Routes

**File:** `backend/api/main.py`

### Route Specifications

```python
class FastAPI_Routes:
    
    [GET] /
    ├─ Returns: {message, version, status, endpoints}
    ├─ Status Code: 200
    └─ Response Time: <10ms
    
    [GET] /api/v1/health
    ├─ Input: None
    ├─ Returns: {status, ai_modules, models_loaded}
    ├─ Status Code: 200
    └─ Response Time: <10ms
    
    [POST] /api/v1/predict
    ├─ Input: PredictionRequest
    ├─ Returns: {success, prediction, model, timestamp}
    ├─ Status Code: 200/500
    └─ Response Time: 100-200ms
    
    [POST] /api/v1/predict/transformer
    ├─ Input: PredictionRequest
    ├─ Returns: {transformer_prediction, temporal_analysis}
    ├─ Status Code: 200/500
    └─ Response Time: 150-300ms
    
    [POST] /api/v1/predict/comprehensive
    ├─ Input: PredictionRequest
    ├─ Returns: {all predictions fused}
    ├─ Status Code: 200/500
    └─ Response Time: 5-15s
    
    [GET] /api/v1/satellite/{lat}/{lon}
    ├─ Input: lat (float), lon (float), days (int, optional)
    ├─ Returns: Satellite analysis
    ├─ Status Code: 200/500
    └─ Response Time: 3-5s
    
    [GET] /api/v1/geospatial/{lat}/{lon}
    ├─ Input: lat (float), lon (float), radius_km (float, optional)
    ├─ Returns: 3D geospatial analysis
    ├─ Status Code: 200/500
    └─ Response Time: 2-4s
    
    [POST] /api/v1/compare
    ├─ Input: ComparisonRequest (2 locations)
    ├─ Returns: Side-by-side comparison
    ├─ Status Code: 200/500
    └─ Response Time: 500ms-1s
    
    [POST] /api/v1/predict/batch
    ├─ Input: BatchPredictionRequest
    ├─ Returns: List of predictions
    ├─ Status Code: 200/500
    └─ Response Time: 100-500ms
    
    [POST] /api/v1/feedback
    ├─ Input: FeedbackRequest
    ├─ Returns: Acknowledgment
    ├─ Status Code: 200/500
    └─ Response Time: 50-100ms
```

---

## 9. Pydantic Models (Request/Response)

```python
class PredictionRequest(BaseModel):
    - latitude: float (Range: -90 to 90)
    - longitude: float 　(Range: -180 to 180)
    - analysis_depth: str (Options: "quick", "standard", "comprehensive")
    - include_satellite: bool (Default: True)
    - include_3d: bool (Default: True)

class FeedbackRequest(BaseModel):
    - latitude: float
    - longitude: float
    - predicted_success: float (0-100)
    - predicted_depth: float (meters)
    - predicted_yield: float (L/hr)
    - actual_success: float (0-100)
    - actual_depth: float (meters)
    - actual_yield: float (L/hr)
    - comments: Optional[str]

class BatchPredictionRequest(BaseModel):
    - locations: List[Dict] (Each: {latitude, longitude})
    - analysis_depth: str (Default: "quick")

class ComparisonRequest(BaseModel):
    - location1: Dict (latitude, longitude)
    - location2: Dict (latitude, longitude)
    - analysis_depth: str (Default: "standard")

class PredictionResponse(BaseModel):
    - success: bool
    - location: Dict (latitude, longitude)
    - prediction: Dict
    - model: str
    - timestamp: str
```

---

## 10. Integration Points & External Dependencies

**External APIs (10+ sources)**
- NASA POWER API
- USGS Water Services
- Open-Meteo
- SoilGrids
- OpenTopoData
- USGS Earthquake
- Soil Moisture APIs
- Precipitation APIs
- Weather APIs
- (Additional regional APIs)

**ML Libraries**
- XGBoost
- LightGBM
- CatBoost
- scikit-learn
- TensorFlow
- PyTorch

**Data Processing**
- NumPy
- SciPy
- Pandas
- GeoPandas
- Rasterio
- Shapely

---

## Summary for UML Creation

| Component | Relationships | Methods | Attributes |
|-----------|----------------|---------|------------|
| Ensemble | Aggregates 5 models | 12 | 3 |
| Transformer | Composes attention | 9 | 4 |
| LSTM | Temporal processing | 8 | 4 |
| Quantum NN | Optimization | 11 | 3 |
| Satellite | Fusion processing | 13 | 2 |
| Geospatial | Multi-layer analysis | 20+ | 2 |
| RealtimeEngine | API integration | 15+ | 1 |
| PredictionRequest | Validation model | Properties only | 5 |

**Total in Project:**
- 8 Main Classes
- 50+ Supporting Classes
- 100+ Methods
- 40+ Relationships
- 10+ External Dependencies

---

**Ready to create all types of UML diagrams with this reference!**

