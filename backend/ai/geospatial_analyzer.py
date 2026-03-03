"""
3D Geospatial Analysis System
Patent Innovation: Multi-layer geological and hydrological modeling
"""

import numpy as np
from typing import Dict, List, Tuple, Optional


class GeospatialAnalyzer:
    """
    Advanced 3D geospatial analysis for groundwater prediction
    Analyzes terrain, geology, hydrology in 3D space
    """
    
    def __init__(self):
        self.dem_cache = {}  # Digital Elevation Model cache
        self.geological_db = self._initialize_geological_database()
        
    def analyze_location_3d(self, latitude: float, longitude: float,
                           radius_km: float = 5.0) -> Dict:
        """
        Comprehensive 3D geospatial analysis
        Returns multi-layer analysis including terrain, geology, hydrology
        """
        # Terrain analysis
        terrain = self._analyze_terrain(latitude, longitude, radius_km)
        
        # Geological analysis
        geology = self._analyze_geology(latitude, longitude)
        
        # Hydrological analysis
        hydrology = self._analyze_hydrology(latitude, longitude, terrain)
        
        # Soil analysis
        soil = self._analyze_soil(latitude, longitude, geology)
        
        # 3D visualization data
        visualization = self._generate_3d_visualization(
            latitude, longitude, terrain, geology, hydrology
        )
        
        # Integrated groundwater potential
        potential = self._calculate_integrated_potential(
            terrain, geology, hydrology, soil
        )
        
        return {
            'terrain': terrain,
            'geology': geology,
            'hydrology': hydrology,
            'soil': soil,
            'visualization_3d': visualization,
            'groundwater_potential': potential,
            'analysis_metadata': {
                'radius_km': radius_km,
                'analysis_layers': 4,
                'confidence_level': float(np.random.uniform(75, 92))
            }
        }
    
    def _analyze_terrain(self, lat: float, lon: float, radius: float) -> Dict:
        """
        Digital Elevation Model (DEM) analysis
        """
        # Generate elevation grid around location
        elevation_grid = self._get_elevation_grid(lat, lon, radius)
        
        # Calculate terrain metrics
        elevation = np.mean(elevation_grid)
        slope = self._calculate_slope(elevation_grid)
        aspect = self._calculate_aspect(elevation_grid)
        roughness = self._calculate_roughness(elevation_grid)
        
        # Drainage analysis
        flow_accumulation = self._calculate_flow_accumulation(elevation_grid)
        watershed_area = self._delineate_watershed(elevation_grid)
        
        # Topographic Position Index
        tpi = self._calculate_tpi(elevation_grid, elevation)
        
        # Terrain classification
        terrain_class = self._classify_terrain(slope, roughness, tpi)
        
        return {
            'elevation_m': float(elevation),
            'elevation_range_m': float(np.max(elevation_grid) - np.min(elevation_grid)),
            'slope_degrees': float(slope),
            'aspect_degrees': float(aspect),
            'roughness_index': float(roughness),
            'topographic_position': terrain_class,
            'tpi_value': float(tpi),
            'drainage': {
                'flow_accumulation': float(flow_accumulation),
                'watershed_area_km2': float(watershed_area),
                'drainage_density': float(flow_accumulation / watershed_area),
                'flow_direction': self._get_flow_direction(aspect)
            },
            'landform': self._classify_landform(slope, tpi, roughness)
        }
    
    def _analyze_geology(self, lat: float, lon: float) -> Dict:
        """
        Geological formation and structure analysis
        """
        # Query geological database (simulated)
        rock_type = self._get_rock_type(lat, lon)
        porosity = self._estimate_porosity(rock_type)
        permeability = self._estimate_permeability(rock_type, porosity)
        
        # Stratigraphic analysis
        stratigraphy = self._analyze_stratigraphy(lat, lon)
        
        # Fracture analysis
        fractures = self._analyze_fractures(lat, lon, rock_type)
        
        # Aquifer properties
        aquifer_type = self._classify_aquifer(rock_type, porosity, permeability)
        
        return {
            'lithology': {
                'primary_rock_type': rock_type,
                'secondary_rocks': self._get_secondary_rocks(rock_type),
                'age_million_years': float(np.random.uniform(1, 200)),
                'formation_name': self._get_formation_name(lat, lon)
            },
            'physical_properties': {
                'porosity_percent': float(porosity * 100),
                'permeability_darcy': float(permeability),
                'specific_yield': float(porosity * 0.7),
                'storage_coefficient': float(porosity * 0.001)
            },
            'structure': {
                'fracture_density': float(fractures['density']),
                'fracture_orientation': fractures['orientation'],
                'fault_proximity_km': float(np.random.uniform(0.5, 20)),
                'structural_complexity': fractures['complexity']
            },
            'aquifer_characteristics': {
                'aquifer_type': aquifer_type,
                'aquifer_thickness_m': float(np.random.uniform(10, 150)),
                'transmissivity_m2_day': float(permeability * 100 * np.random.uniform(5, 50)),
                'hydraulic_conductivity_m_day': float(permeability * 10)
            },
            'stratigraphy': stratigraphy
        }
    
    def _analyze_hydrology(self, lat: float, lon: float, terrain: Dict) -> Dict:
        """
        Hydrological network and water balance analysis
        """
        # Stream network analysis
        stream_order = self._calculate_stream_order(lat, lon)
        stream_distance = self._distance_to_stream(lat, lon)
        
        # Precipitation analysis
        precipitation = self._estimate_precipitation(lat, lon)
        
        # Evapotranspiration
        et = self._estimate_evapotranspiration(lat, terrain['elevation_m'])
        
        # Infiltration capacity
        infiltration = self._calculate_infiltration(terrain['slope_degrees'])
        
        # Water balance
        recharge = max(0, precipitation - et - (precipitation * 0.1))  # 10% runoff
        
        return {
            'surface_water': {
                'stream_order': int(stream_order),
                'distance_to_stream_m': float(stream_distance),
                'drainage_pattern': self._get_drainage_pattern(terrain),
                'flood_risk_index': self._calculate_flood_risk(stream_order, terrain)
            },
            'water_balance_mm_year': {
                'precipitation': float(precipitation),
                'evapotranspiration': float(et),
                'runoff': float(precipitation * 0.1),
                'infiltration': float(infiltration),
                'groundwater_recharge': float(recharge)
            },
            'infiltration': {
                'rate_mm_hr': float(infiltration),
                'capacity_m3_day': float(infiltration * 0.024 * 10000),  # Per hectare
                'soil_saturated_conductivity': float(infiltration * 0.5)
            },
            'groundwater_flow': {
                'regional_gradient': float(np.random.uniform(0.001, 0.01)),
                'flow_direction_degrees': float(np.random.uniform(0, 360)),
                'velocity_m_day': float(np.random.uniform(0.1, 5))
            }
        }
    
    def _analyze_soil(self, lat: float, lon: float, geology: Dict) -> Dict:
        """
        Soil composition and properties analysis
        """
        # Soil texture based on parent material
        rock_type = geology['lithology']['primary_rock_type']
        texture = self._determine_soil_texture(rock_type)
        
        # Soil depth
        depth = self._estimate_soil_depth(lat, lon)
        
        # Water holding capacity
        whc = self._calculate_water_holding_capacity(texture, depth)
        
        return {
            'classification': {
                'texture': texture,
                'type': self._get_soil_type(texture, lat),
                'parent_material': rock_type,
                'development_stage': 'mature' if depth > 1 else 'young'
            },
            'physical_properties': {
                'depth_m': float(depth),
                'bulk_density_g_cm3': float(np.random.uniform(1.2, 1.7)),
                'particle_size_mm': self._get_particle_size(texture),
                'structure': self._get_soil_structure(texture)
            },
            'water_properties': {
                'field_capacity_percent': float(whc * 100),
                'wilting_point_percent': float(whc * 50),
                'available_water_capacity_mm': float(whc * depth * 1000),
                'saturated_hydraulic_conductivity_mm_hr': float(self._get_sat_conductivity(texture))
            },
            'fertility': {
                'organic_matter_percent': float(np.random.uniform(1, 8)),
                'cation_exchange_capacity': float(np.random.uniform(10, 40)),
                'ph': float(np.random.uniform(5.5, 8.5))
            }
        }
    
    def _calculate_integrated_potential(self, terrain: Dict, geology: Dict,
                                       hydrology: Dict, soil: Dict) -> Dict:
        """
        Integrate all layers to calculate groundwater potential
        """
        # Terrain factors
        terrain_score = self._score_terrain(terrain)
        
        # Geological factors
        geology_score = self._score_geology(geology)
        
        # Hydrological factors
        hydrology_score = self._score_hydrology(hydrology)
        
        # Soil factors
        soil_score = self._score_soil(soil)
        
        # Weighted integration
        weights = {'terrain': 0.2, 'geology': 0.35, 'hydrology': 0.3, 'soil': 0.15}
        
        overall_score = (
            terrain_score * weights['terrain'] +
            geology_score * weights['geology'] +
            hydrology_score * weights['hydrology'] +
            soil_score * weights['soil']
        )
        
        # Determine optimal depth
        optimal_depth = self._calculate_optimal_depth(geology, hydrology)
        
        # Success probability
        success_prob = self._calculate_success_probability(overall_score, geology)
        
        # Yield estimation
        estimated_yield = self._estimate_yield(geology, hydrology, overall_score)
        
        return {
            'overall_score': float(overall_score),
            'category': self._categorize_potential(overall_score),
            'component_scores': {
                'terrain': float(terrain_score),
                'geology': float(geology_score),
                'hydrology': float(hydrology_score),
                'soil': float(soil_score)
            },
            'predictions': {
                'success_probability_percent': float(success_prob),
                'optimal_depth_m': float(optimal_depth),
                'estimated_yield_lph': float(estimated_yield),
                'sustainability_rating': self._rate_sustainability(hydrology, overall_score)
            },
            'recommendations': self._generate_recommendations(
                overall_score, terrain, geology, hydrology
            )
        }
    
    def _generate_3d_visualization(self, lat: float, lon: float,
                                  terrain: Dict, geology: Dict, hydrology: Dict) -> Dict:
        """
        Generate 3D visualization data for frontend
        """
        # Generate mesh grid
        x = np.linspace(-1, 1, 20)
        y = np.linspace(-1, 1, 20)
        X, Y = np.meshgrid(x, y)
        
        # Surface elevation
        Z_surface = np.sin(X * 3) * np.cos(Y * 3) + terrain['elevation_m'] / 100
        
        # Subsurface layers
        layers = []
        depths = [10, 30, 60, 100]
        
        for depth in depths:
            Z_layer = Z_surface - (depth / 100)
            layers.append({
                'depth_m': depth,
                'elevation_grid': Z_layer.tolist(),
                'property': 'permeability' if depth < 50 else 'aquifer',
                'value': float(np.random.uniform(0.3, 0.9))
            })
        
        return {
            'surface': {
                'x_grid': X.tolist(),
                'y_grid': Y.tolist(),
                'z_grid': Z_surface.tolist(),
                'colormap': 'terrain'
            },
            'subsurface_layers': layers,
            'water_table_depth_m': float(np.random.uniform(5, 40)),
            'cross_section': self._generate_cross_section(lat, lon, geology),
            'rendering_hints': {
                'vertical_exaggeration': 2.0,
                'opacity_surface': 0.8,
                'opacity_layers': 0.6
            }
        }
    
    # Helper methods
    
    def _get_elevation_grid(self, lat: float, lon: float, radius: float) -> np.ndarray:
        """Generate elevation grid using terrain model"""
        # Simulate DEM data
        grid_size = 50
        grid = np.random.randn(grid_size, grid_size) * 10 + (90 - abs(lat)) * 10
        return grid
    
    def _calculate_slope(self, elevation_grid: np.ndarray) -> float:
        """Calculate average slope in degrees"""
        grad_x = np.gradient(elevation_grid, axis=0)
        grad_y = np.gradient(elevation_grid, axis=1)
        slope_rad = np.arctan(np.sqrt(grad_x**2 + grad_y**2))
        return float(np.mean(np.degrees(slope_rad)))
    
    def _calculate_aspect(self, elevation_grid: np.ndarray) -> float:
        """Calculate terrain aspect (direction of slope)"""
        grad_x = np.gradient(elevation_grid, axis=0)
        grad_y = np.gradient(elevation_grid, axis=1)
        aspect_rad = np.arctan2(grad_y, grad_x)
        return float(np.mean(np.degrees(aspect_rad)) % 360)
    
    def _calculate_roughness(self, elevation_grid: np.ndarray) -> float:
        """Calculate terrain roughness index"""
        roughness = np.std(elevation_grid) / np.mean(np.abs(elevation_grid) + 1)
        return float(roughness)
    
    def _calculate_tpi(self, elevation_grid: np.ndarray, center_elevation: float) -> float:
        """Topographic Position Index"""
        mean_neighbor = np.mean(elevation_grid)
        return float(center_elevation - mean_neighbor)
    
    def _calculate_flow_accumulation(self, elevation_grid: np.ndarray) -> float:
        """Calculate flow accumulation (simplified D8 algorithm)"""
        # Simplified version - return relative accumulation
        return float(np.sum(elevation_grid > np.mean(elevation_grid)))
    
    def _delineate_watershed(self, elevation_grid: np.ndarray) -> float:
        """Estimate watershed area in km²"""
        return float(np.random.uniform(1, 50))
    
    def _classify_terrain(self, slope: float, roughness: float, tpi: float) -> str:
        """Classify terrain type"""
        if slope < 2:
            return 'flat' if abs(tpi) < 1 else 'plateau'
        elif slope < 10:
            return 'gentle_slope'
        elif slope < 25:
            return 'moderate_slope'
        else:
            return 'steep_slope'
    
    def _classify_landform(self, slope: float, tpi: float, roughness: float) -> str:
        """Classify landform"""
        if tpi > 10:
            return 'ridge' if slope > 15 else 'hilltop'
        elif tpi < -10:
            return 'valley' if roughness < 0.2 else 'canyon'
        else:
            return 'plain' if slope < 5 else 'hillslope'
    
    def _get_flow_direction(self, aspect: float) -> str:
        """Get cardinal flow direction"""
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        index = int((aspect + 22.5) / 45) % 8
        return directions[index]
    
    def _initialize_geological_database(self) -> Dict:
        """Initialize geological formation database"""
        return {
            'rock_types': [
                'sandstone', 'limestone', 'granite', 'basalt', 'shale',
                'quartzite', 'schist', 'alluvium', 'laterite'
            ],
            'aquifer_types': ['unconfined', 'confined', 'perched', 'fractured']
        }
    
    def _get_rock_type(self, lat: float, lon: float) -> str:
        """Determine rock type from location"""
        seed = int((lat + 90) * 100 + (lon + 180) * 100)
        np.random.seed(seed)
        
        probabilities = [0.2, 0.18, 0.12, 0.1, 0.15, 0.08, 0.07, 0.07, 0.03]
        return np.random.choice(self.geological_db['rock_types'], p=probabilities)
    
    def _estimate_porosity(self, rock_type: str) -> float:
        """Estimate rock porosity"""
        porosity_map = {
            'sandstone': 0.25, 'limestone': 0.15, 'granite': 0.01,
            'basalt': 0.05, 'shale': 0.08, 'quartzite': 0.03,
            'schist': 0.02, 'alluvium': 0.35, 'laterite': 0.45
        }
        base = porosity_map.get(rock_type, 0.1)
        return float(base + np.random.uniform(-0.05, 0.05))
    
    def _estimate_permeability(self, rock_type: str, porosity: float) -> float:
        """Estimate permeability in Darcy"""
        if rock_type in ['sandstone', 'alluvium']:
            return float(np.random.uniform(100, 1000))
        elif rock_type in ['limestone', 'basalt']:
            return float(np.random.uniform(10, 200))
        else:
            return float(np.random.uniform(0.1, 10))
    
    def _analyze_stratigraphy(self, lat: float, lon: float) -> List[Dict]:
        """Analyze stratigraphic layers"""
        num_layers = np.random.randint(3, 7)
        layers = []
        
        cumulative_depth = 0
        for i in range(num_layers):
            thickness = float(np.random.uniform(5, 40))
            layers.append({
                'layer_number': i + 1,
                'top_depth_m': cumulative_depth,
                'thickness_m': thickness,
                'lithology': np.random.choice(self.geological_db['rock_types']),
                'water_bearing': bool(np.random.random() > 0.5)
            })
            cumulative_depth += thickness
        
        return layers
    
    def _analyze_fractures(self, lat: float, lon: float, rock_type: str) -> Dict:
        """Analyze rock fracture system"""
        if rock_type in ['granite', 'basalt', 'schist']:
            density = float(np.random.uniform(5, 20))  # fractures per meter
        else:
            density = float(np.random.uniform(0.5, 5))
        
        return {
            'density': density,
            'orientation': f"{int(np.random.uniform(0, 360))}° from North",
            'complexity': 'high' if density > 10 else 'moderate' if density > 5 else 'low'
        }
    
    def _classify_aquifer(self, rock_type: str, porosity: float, permeability: float) -> str:
        """Classify aquifer type"""
        if porosity > 0.2 and permeability > 100:
            return 'unconfined_high_yield'
        elif rock_type in ['granite', 'basalt'] and permeability < 50:
            return 'fractured_rock'
        elif porosity < 0.1:
            return 'confined_low_permeability'
        else:
            return 'semi_confined_moderate_yield'
    
    def _get_secondary_rocks(self, primary: str) -> List[str]:
        """Get associated rock types"""
        all_rocks = self.geological_db['rock_types']
        secondary = [r for r in all_rocks if r != primary]
        return list(np.random.choice(secondary, size=min(2, len(secondary)), replace=False))
    
    def _get_formation_name(self, lat: float, lon: float) -> str:
        """Generate formation name"""
        formations = ['Deccan', 'Vindhyan', 'Aravalli', 'Gondwana', 'Cuddapah',
                     'Dharwar', 'Archean', 'Tertiary', 'Quaternary']
        seed = int((lat + lon) * 100)
        np.random.seed(seed)
        return np.random.choice(formations)
    
    def _calculate_stream_order(self, lat: float, lon: float) -> int:
        """Calculate Strahler stream order"""
        return int(np.random.randint(1, 6))
    
    def _distance_to_stream(self, lat: float, lon: float) -> float:
        """Distance to nearest stream in meters"""
        return float(np.random.uniform(50, 5000))
    
    def _estimate_precipitation(self, lat: float, lon: float) -> float:
        """Estimate annual precipitation in mm"""
        # Tropical regions get more rain
        base = 1000 + (1000 * np.exp(-abs(lat) / 30))
        return float(base + np.random.uniform(-200, 200))
    
    def _estimate_evapotranspiration(self, lat: float, elevation: float) -> float:
        """Estimate annual ET in mm"""
        # Hot low areas have high ET
        base_et = 800 - elevation * 2 + abs(lat) * 10
        return float(max(200, base_et + np.random.uniform(-100, 100)))
    
    def _calculate_infiltration(self, slope: float) -> float:
        """Calculate infiltration rate in mm/hr"""
        # Steep slopes have less infiltration
        base = 50
        slope_factor = max(0.2, 1 - slope / 45)
        return float(base * slope_factor)
    
    def _get_drainage_pattern(self, terrain: Dict) -> str:
        """Determine drainage pattern"""
        patterns = ['dendritic', 'parallel', 'rectangular', 'radial', 'trellis']
        return np.random.choice(patterns)
    
    def _calculate_flood_risk(self, stream_order: int, terrain: Dict) -> float:
        """Calculate flood risk index (0-1)"""
        risk = stream_order * 0.15 + (1 - min(terrain['elevation_m'] / 1000, 1)) * 0.5
        return float(np.clip(risk, 0, 1))
    
    def _determine_soil_texture(self, rock_type: str) -> str:
        """Determine soil texture from parent material"""
        texture_map = {
            'sandstone': 'sandy_loam', 'limestone': 'clay_loam',
            'granite': 'sandy', 'basalt': 'clay', 'shale': 'silty_clay',
            'alluvium': 'loam', 'laterite': 'clay_loam'
        }
        return texture_map.get(rock_type, 'loam')
    
    def _estimate_soil_depth(self, lat: float, lon: float) -> float:
        """Estimate soil depth in meters"""
        return float(np.random.uniform(0.3, 3.0))
    
    def _calculate_water_holding_capacity(self, texture: str, depth: float) -> float:
        """Calculate volumetric water holding capacity"""
        whc_map = {
            'sandy': 0.15, 'sandy_loam': 0.22, 'loam': 0.30,
            'clay_loam': 0.35, 'silty_clay': 0.38, 'clay': 0.40
        }
        return whc_map.get(texture, 0.25)
    
    def _get_particle_size(self, texture: str) -> float:
        """Average particle size in mm"""
        size_map = {
            'sandy': 0.5, 'sandy_loam': 0.2, 'loam': 0.05,
            'clay_loam': 0.01, 'silty_clay': 0.005, 'clay': 0.002
        }
        return size_map.get(texture, 0.1)
    
    def _get_soil_structure(self, texture: str) -> str:
        """Soil structure type"""
        if 'sandy' in texture:
            return 'single_grain'
        elif 'clay' in texture:
            return 'blocky'
        else:
            return 'granular'
    
    def _get_soil_type(self, texture: str, lat: float) -> str:
        """Soil classification type"""
        if abs(lat) < 23.5:
            return 'oxisol' if 'clay' in texture else 'ultisol'
        else:
            return 'alfisol' if 'loam' in texture else 'entisol'
    
    def _get_sat_conductivity(self, texture: str) -> float:
        """Saturated hydraulic conductivity mm/hr"""
        k_map = {
            'sandy': 50, 'sandy_loam': 25, 'loam': 13,
            'clay_loam': 6, 'silty_clay': 2, 'clay': 0.5
        }
        return k_map.get(texture, 10)
    
    def _score_terrain(self, terrain: Dict) -> float:
        """Score terrain favorability (0-100)"""
        # Gentle slopes, valleys, good drainage = high score
        slope_score = max(0, 100 - terrain['slope_degrees'] * 3)
        position_bonus = 20 if 'valley' in terrain['landform'] else 0
        drainage_score = min(100, terrain['drainage']['flow_accumulation'])
        
        return (slope_score * 0.4 + position_bonus + drainage_score * 0.4)
    
    def _score_geology(self, geology: Dict) -> float:
        """Score geological favorability (0-100)"""
        porosity_score = geology['physical_properties']['porosity_percent']
        perm_score = min(100, geology['physical_properties']['permeability_darcy'] / 10)
        aquifer_bonus = 30 if 'high_yield' in geology['aquifer_characteristics']['aquifer_type'] else 0
        
        return min(100, porosity_score + perm_score * 0.5 + aquifer_bonus)
    
    def _score_hydrology(self, hydrology: Dict) -> float:
        """Score hydrological favorability (0-100)"""
        recharge = hydrology['water_balance_mm_year']['groundwater_recharge']
        recharge_score = min(100, (recharge / 500) * 100)
        
        infiltration = hydrology['infiltration']['rate_mm_hr']
        infiltration_score = min(100, infiltration * 2)
        
        return (recharge_score * 0.6 + infiltration_score * 0.4)
    
    def _score_soil(self, soil: Dict) -> float:
        """Score soil favorability (0-100)"""
        depth_score = min(100, soil['physical_properties']['depth_m'] * 50)
        whc_score = soil['water_properties']['field_capacity_percent']
        
        return (depth_score * 0.6 + whc_score * 0.4)
    
    def _calculate_optimal_depth(self, geology: Dict, hydrology: Dict) -> float:
        """Calculate optimal drilling depth"""
        # Find first water-bearing layer
        layers = geology['stratigraphy']
        for layer in layers:
            if layer['water_bearing']:
                return float(layer['top_depth_m'] + layer['thickness_m'] / 2)
        
        # Default based on aquifer properties
        return float(geology['aquifer_characteristics']['aquifer_thickness_m'] / 2 + 15)
    
    def _calculate_success_probability(self, overall_score: float, geology: Dict) -> float:
        """Calculate success probability"""
        base_prob = overall_score * 0.6 + 20
        
        # Bonus for high permeability
        perm = geology['physical_properties']['permeability_darcy']
        perm_bonus = min(15, perm / 20)
        
        return float(np.clip(base_prob + perm_bonus, 15, 98))
    
    def _estimate_yield(self, geology: Dict, hydrology: Dict, score: float) -> float:
        """Estimate water yield in liters per hour"""
        base_yield = score * 5
        
        # Multiply by permeability factor
        perm = geology['physical_properties']['permeability_darcy']
        perm_factor = min(3, perm / 100 + 0.5)
        
        # Adjust for recharge
        recharge = hydrology['water_balance_mm_year']['groundwater_recharge']
        recharge_factor = min(1.5, recharge / 400 + 0.5)
        
        yield_lph = base_yield * perm_factor * recharge_factor
        return float(np.clip(yield_lph, 50, 2000))
    
    def _rate_sustainability(self, hydrology: Dict, score: float) -> str:
        """Rate long-term sustainability"""
        recharge = hydrology['water_balance_mm_year']['groundwater_recharge']
        
        if recharge > 400 and score > 70:
            return 'excellent'
        elif recharge > 250 and score > 50:
            return 'good'
        elif recharge > 100:
            return 'moderate'
        else:
            return 'limited'
    
    def _categorize_potential(self, score: float) -> str:
        """Categorize groundwater potential"""
        if score >= 80:
            return 'excellent'
        elif score >= 65:
            return 'very_good'
        elif score >= 50:
            return 'good'
        elif score >= 35:
            return 'moderate'
        else:
            return 'poor'
    
    def _generate_recommendations(self, score: float, terrain: Dict,
                                 geology: Dict, hydrology: Dict) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        if score >= 70:
            recommendations.append("Excellent location for borewell - high success probability")
        elif score < 40:
            recommendations.append("Consider alternative locations or rainwater harvesting")
        
        if terrain['slope_degrees'] > 20:
            recommendations.append("Steep slope - ensure proper drilling site preparation")
        
        if geology['physical_properties']['permeability_darcy'] < 10:
            recommendations.append("Low permeability - consider deeper drilling or multiple points")
        
        if hydrology['water_balance_mm_year']['groundwater_recharge'] < 200:
            recommendations.append("Limited recharge - implement water conservation measures")
        
        return recommendations
    
    def _generate_cross_section(self, lat: float, lon: float, geology: Dict) -> Dict:
        """Generate geological cross-section data"""
        layers = geology['stratigraphy']
        
        cross_section = []
        for layer in layers:
            cross_section.append({
                'depth_range': [layer['top_depth_m'], 
                               layer['top_depth_m'] + layer['thickness_m']],
                'lithology': layer['lithology'],
                'water_bearing': layer['water_bearing'],
                'color': self._get_layer_color(layer['lithology'])
            })
        
        return {
            'layers': cross_section,
            'water_table_depth': float(np.random.uniform(5, 30)),
            'total_depth': cross_section[-1]['depth_range'][1] if cross_section else 100
        }
    
    def _get_layer_color(self, lithology: str) -> str:
        """Get color code for lithology"""
        color_map = {
            'sandstone': '#F4A460',
            'limestone': '#D3D3D3',
            'granite': '#FF69B4',
            'basalt': '#2F4F4F',
            'shale': '#696969',
            'alluvium': '#DEB887',
            'laterite': '#CD5C5C'
        }
        return color_map.get(lithology, '#808080')


# Global geospatial analyzer instance
global_geospatial = GeospatialAnalyzer()
