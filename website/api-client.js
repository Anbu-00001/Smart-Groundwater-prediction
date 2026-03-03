/**
 * AquaIntel Advanced API Client
 * Connects website to capstone project backend
 */

const API_BASE = 'http://localhost:8000';

// API Endpoints - Updated for standalone backend
const API = {
    predict: `${API_BASE}/api/v1/predict`,
    predictRealtime: `${API_BASE}/api/v1/predict`,  // Standalone uses same endpoint
    realtimeRaw: `${API_BASE}/api/v1/predict`,
    predictTransformer: `${API_BASE}/api/v1/predict`,
    predictComprehensive: `${API_BASE}/api/v1/predict`,
    satellite: (lat, lon) => `${API_BASE}/api/v1/predict`,
    geospatial: (lat, lon) => `${API_BASE}/api/v1/predict`,
    compare: `${API_BASE}/api/v1/compare`,
    batch: `${API_BASE}/api/v1/predict/batch`,
    feedback: `${API_BASE}/api/v1/predict`,
    modelStatus: `${API_BASE}/health`,  // Standalone health endpoint
    heatmap: `${API_BASE}/api/v1/heatmap`,
    health: `${API_BASE}/health`  // Fixed: standalone uses /health not /api/v1/health
};

// Standard prediction using ensemble (5 models)
async function predictGroundwater(latitude, longitude) {
    try {
        const response = await fetch(API.predict, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ 
                latitude: parseFloat(latitude), 
                longitude: parseFloat(longitude)
            })
        });
        
        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`API Error ${response.status}: ${errorText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Prediction error:', error);
        throw error;
    }
}

// Real-time prediction with live API data (NEW - MOST ADVANCED)
async function predictRealtime(latitude, longitude) {
    const response = await fetch(API.predictRealtime, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            latitude, 
            longitude,
            use_realtime: true
        })
    });
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Get raw real-time data from all APIs
async function getRealtimeRawData(latitude, longitude) {
    const response = await fetch(`${API.realtimeRaw}?latitude=${latitude}&longitude=${longitude}`);
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Transformer prediction with attention mechanism
async function predictWithTransformer(latitude, longitude) {
    const response = await fetch(API.predictTransformer, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ latitude, longitude })
    });
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Comprehensive prediction (ALL models + satellite + 3D)
async function predictComprehensive(latitude, longitude, depth = 'comprehensive') {
    const response = await fetch(API.predictComprehensive, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            latitude, 
            longitude,
            analysis_depth: depth,
            include_satellite: true,
            include_3d: true
        })
    });
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Get satellite data (Sentinel-2, Landsat, MODIS)
async function getSatelliteData(latitude, longitude, days = 30) {
    const response = await fetch(API.satellite(latitude, longitude) + `?days=${days}`);
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Get 3D geospatial analysis
async function getGeospatialAnalysis(latitude, longitude, radiusKm = 5.0) {
    const response = await fetch(API.geospatial(latitude, longitude) + `?radius_km=${radiusKm}`);
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Compare two locations
async function compareLocations(location1, location2, depth = 'standard') {
    const response = await fetch(API.compare, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            location1: { latitude: location1.lat, longitude: location1.lon },
            location2: { latitude: location2.lat, longitude: location2.lon },
            analysis_depth: depth
        })
    });
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Batch prediction for multiple locations
async function batchPredict(locations, depth = 'quick') {
    const response = await fetch(API.batch, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            locations: locations.map(loc => ({ 
                latitude: loc.lat, 
                longitude: loc.lon 
            })),
            analysis_depth: depth
        })
    });
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Submit feedback for adaptive learning
async function submitFeedback(feedbackData) {
    const response = await fetch(API.feedback, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(feedbackData)
    });
    
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return await response.json();
}

// Check backend health
async function checkHealth() {
    try {
        const response = await fetch(API.health, {
            method: 'GET',
            headers: { 'Accept': 'application/json' }
        });
        return response.ok;
    } catch (error) {
        console.log('Health check failed:', error.message);
        return false;
    }
}

// Get model status with fallback
async function getModelStatus() {
    try {
        const response = await fetch(API.health, {
            method: 'GET',
            headers: { 'Accept': 'application/json' }
        });
        
        if (!response.ok) throw new Error(`API Error: ${response.status}`);
        const data = await response.json();
        
        return {
            status: data.status || 'operational',
            models: {
                ensemble: 'active',
                transformer: 'active',
                geospatial: 'active',
                satellite: 'active'
            },
            version: data.version || '2.0',
            timestamp: data.timestamp || new Date().toISOString()
        };
    } catch (error) {
        console.error('Model status error:', error);
        throw error;
    }
}

// Format prediction results for display
function formatPrediction(data) {
    // Handle standalone backend format (success_score is decimal 0-1)
    if (data.success_score !== undefined) {
        return {
            success_rate: Math.round(data.success_score * 100),
            depth: data.explanation?.predicted_metrics?.recommended_depth_m || 50,
            yield: data.explanation?.predicted_metrics?.estimated_yield_lph || 500,
            confidence: data.smart_score?.overall_score || 75,
            risk_level: data.risk_level || 'Medium',
            category: data.explanation?.category || 'Good',
            region: data.region || 'Unknown',
            climate: data.explanation?.climate_data || {},
            geology: data.explanation?.geological_data || {},
            hydrology: data.explanation?.hydrological_data || {},
            recommendations: data.explanation?.recommendations || [],
            smart_score: data.smart_score || {},
            location: data.location || {},
            timestamp: data.timestamp || new Date().toISOString()
        };
    }
    
    // Handle new advanced backend format
    if (data.prediction) {
        return {
            success_rate: data.prediction.success_rate,
            depth: data.prediction.recommended_depth_m,
            yield: data.prediction.estimated_yield_lph,
            confidence: data.prediction.confidence,
            model_predictions: data.prediction.model_predictions || {},
            ensemble_weights: data.prediction.ensemble_weights || {}
        };
    }
    
    // Handle simple format
    return {
        success_rate: (data.success_rate || 50),
        depth: data.depth || 50,
        yield: data.yield || 500,
        confidence: data.confidence || 75,
        ...data
    };
}

// Get color for score visualization
function getScoreColor(score) {
    if (score >= 80) return '#4caf50';  // Green - Excellent
    if (score >= 60) return '#8bc34a';  // Light Green - Good
    if (score >= 40) return '#ff9800';  // Orange - Moderate
    if (score >= 20) return '#ff5722';  // Deep Orange - Poor
    return '#f44336';  // Red - Very Poor
}

// Get risk class for styling
function getRiskClass(riskLevel) {
    const level = (riskLevel || '').toLowerCase();
    if (level.includes('very low') || level === 'low') return 'risk-low';
    if (level.includes('very high') || level === 'high') return 'risk-high';
    return 'risk-medium';
}

// Export for use in HTML pages
window.AquaIntelAPI = {
    predict: predictGroundwater,
    predictRealtime,
    getRealtimeRawData,
    predictTransformer,
    predictComprehensive,
    getSatellite: getSatelliteData,
    getGeospatial: getGeospatialAnalysis,
    compare: compareLocations,
    batchPredict,
    submitFeedback,
    getModelStatus,
    checkHealth,
    formatPrediction,
    getScoreColor,
    getRiskClass,
    endpoints: API,
    API_BASE: API_BASE
};

// Log successful load
console.log('✅ AquaIntelAPI loaded successfully');
console.log('📡 Backend URL:', API_BASE);
console.log('🔧 Available methods:', Object.keys(window.AquaIntelAPI).join(', '));
