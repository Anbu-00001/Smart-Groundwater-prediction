"""
🌍 REAL-TIME WORLD DATA INTEGRATION ENGINE
Fetches live data from 10+ free APIs for ultra-accurate predictions
"""

import asyncio
import aiohttp
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class RealtimeDataEngine:
    """Fetches real-world data from multiple free APIs"""
    
    def __init__(self):
        # Free API endpoints (no keys required for basic tier)
        self.apis = {
            'nasa_power': 'https://power.larc.nasa.gov/api/temporal/daily/point',
            'open_meteo': 'https://api.open-meteo.com/v1/forecast',
            'open_elevation': 'https://api.open-elevation.com/api/v1/lookup',
            'soilgrids': 'https://rest.isric.org/soilgrids/v2.0/properties/query',
            'usgs_water': 'https://waterservices.usgs.gov/nwis/iv/',
            'weather_api': 'https://api.open-meteo.com/v1/forecast',
            'climate_api': 'https://archive-api.open-meteo.com/v1/archive',
            'dem_api': 'https://api.opentopodata.org/v1/srtm90m',
            'earthquake_api': 'https://earthquake.usgs.gov/fdsnws/event/1/query',
            'soil_moisture': 'https://api.open-meteo.com/v1/flood'
        }
        
    async def fetch_all_data(self, latitude: float, longitude: float) -> Dict[str, Any]:
        """Fetch data from all sources in parallel"""
        
        async with aiohttp.ClientSession() as session:
            tasks = [
                self._fetch_nasa_power(session, latitude, longitude),
                self._fetch_weather_data(session, latitude, longitude),
                self._fetch_climate_history(session, latitude, longitude),
                self._fetch_elevation(session, latitude, longitude),
                self._fetch_soil_data(session, latitude, longitude),
                self._fetch_usgs_groundwater(session, latitude, longitude),
                self._fetch_precipitation(session, latitude, longitude),
                self._fetch_earthquake_data(session, latitude, longitude),
                self._fetch_soil_moisture(session, latitude, longitude)
            ]
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            return {
                'nasa_power': results[0] if not isinstance(results[0], Exception) else {},
                'current_weather': results[1] if not isinstance(results[1], Exception) else {},
                'climate_history': results[2] if not isinstance(results[2], Exception) else {},
                'elevation': results[3] if not isinstance(results[3], Exception) else {},
                'soil_data': results[4] if not isinstance(results[4], Exception) else {},
                'usgs_wells': results[5] if not isinstance(results[5], Exception) else {},
                'precipitation': results[6] if not isinstance(results[6], Exception) else {},
                'seismic_activity': results[7] if not isinstance(results[7], Exception) else {},
                'soil_moisture': results[8] if not isinstance(results[8], Exception) else {},
                'timestamp': datetime.utcnow().isoformat(),
                'location': {'latitude': latitude, 'longitude': longitude}
            }
    
    async def _fetch_nasa_power(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """NASA POWER API - Solar, Temperature, Humidity data"""
        try:
            end_date = datetime.now().strftime('%Y%m%d')
            start_date = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
            
            params = {
                'parameters': 'T2M,PRECTOTCORR,RH2M,ALLSKY_SFC_SW_DWN,WS2M',
                'community': 'RE',
                'longitude': lon,
                'latitude': lat,
                'start': start_date,
                'end': end_date,
                'format': 'JSON'
            }
            
            async with session.get(self.apis['nasa_power'], params=params, timeout=15) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    parameters = data.get('properties', {}).get('parameter', {})
                    
                    return {
                        'avg_temperature': np.mean(list(parameters.get('T2M', {}).values())) if 'T2M' in parameters else None,
                        'total_precipitation': np.sum(list(parameters.get('PRECTOTCORR', {}).values())) if 'PRECTOTCORR' in parameters else None,
                        'avg_humidity': np.mean(list(parameters.get('RH2M', {}).values())) if 'RH2M' in parameters else None,
                        'avg_solar': np.mean(list(parameters.get('ALLSKY_SFC_SW_DWN', {}).values())) if 'ALLSKY_SFC_SW_DWN' in parameters else None,
                        'avg_windspeed': np.mean(list(parameters.get('WS2M', {}).values())) if 'WS2M' in parameters else None,
                        'source': 'NASA POWER API'
                    }
        except Exception as e:
            logger.error(f"NASA POWER API error: {e}")
            return {}
    
    async def _fetch_weather_data(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """Open-Meteo - Current weather conditions"""
        try:
            params = {
                'latitude': lat,
                'longitude': lon,
                'current_weather': 'true',
                'hourly': 'temperature_2m,relativehumidity_2m,precipitation,weathercode'
            }
            
            async with session.get(self.apis['open_meteo'], params=params, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    current = data.get('current_weather', {})
                    
                    return {
                        'temperature': current.get('temperature'),
                        'windspeed': current.get('windspeed'),
                        'weathercode': current.get('weathercode'),
                        'time': current.get('time'),
                        'source': 'Open-Meteo Weather API'
                    }
        except Exception as e:
            logger.error(f"Weather API error: {e}")
            return {}
    
    async def _fetch_climate_history(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """Open-Meteo Archive - Historical climate data (5 years)"""
        try:
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=1825)).strftime('%Y-%m-%d')  # 5 years
            
            params = {
                'latitude': lat,
                'longitude': lon,
                'start_date': start_date,
                'end_date': end_date,
                'daily': 'temperature_2m_mean,precipitation_sum,relativehumidity_2m_mean'
            }
            
            async with session.get(self.apis['climate_api'], params=params, timeout=15) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    daily = data.get('daily', {})
                    
                    temps = daily.get('temperature_2m_mean', [])
                    precip = daily.get('precipitation_sum', [])
                    humidity = daily.get('relativehumidity_2m_mean', [])
                    
                    return {
                        'avg_temperature_5yr': np.nanmean([t for t in temps if t is not None]) if temps else None,
                        'total_precipitation_5yr': np.nansum([p for p in precip if p is not None]) if precip else None,
                        'avg_humidity_5yr': np.nanmean([h for h in humidity if h is not None]) if humidity else None,
                        'data_points': len(temps),
                        'source': 'Open-Meteo Climate Archive (5 years)'
                    }
        except Exception as e:
            logger.error(f"Climate API error: {e}")
            return {}
    
    async def _fetch_elevation(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """OpenTopoData - High-resolution elevation"""
        try:
            params = {
                'locations': f"{lat},{lon}"
            }
            
            async with session.get(self.apis['dem_api'], params=params, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    results = data.get('results', [{}])[0]
                    
                    return {
                        'elevation_m': results.get('elevation'),
                        'dataset': results.get('dataset'),
                        'source': 'OpenTopoData SRTM 90m'
                    }
        except Exception as e:
            logger.error(f"Elevation API error: {e}")
            return {}
    
    async def _fetch_soil_data(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """SoilGrids API - Soil properties"""
        try:
            params = {
                'lon': lon,
                'lat': lat,
                'property': 'clay,sand,silt,phh2o,bdod,soc',
                'depth': '0-5cm,5-15cm,15-30cm',
                'value': 'mean'
            }
            
            async with session.get(self.apis['soilgrids'], params=params, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    properties = data.get('properties', {}).get('layers', [])
                    
                    soil_info = {}
                    for prop in properties:
                        name = prop.get('name')
                        depths = prop.get('depths', [])
                        if depths:
                            values = [d.get('values', {}).get('mean') for d in depths]
                            soil_info[name] = np.mean([v for v in values if v is not None]) if values else None
                    
                    soil_info['source'] = 'ISRIC SoilGrids API'
                    return soil_info
        except Exception as e:
            logger.error(f"Soil API error: {e}")
            return {}
    
    async def _fetch_usgs_groundwater(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """USGS Water Services - Nearby groundwater well data"""
        try:
            # Search for wells within 50km
            params = {
                'format': 'json',
                'bBox': f"{lon-0.5},{lat-0.5},{lon+0.5},{lat+0.5}",
                'siteType': 'GW',
                'siteStatus': 'active'
            }
            
            async with session.get(self.apis['usgs_water'], params=params, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    time_series = data.get('value', {}).get('timeSeries', [])
                    
                    return {
                        'nearby_wells': len(time_series),
                        'has_groundwater_data': len(time_series) > 0,
                        'source': 'USGS Water Services'
                    }
        except Exception as e:
            logger.error(f"USGS API error: {e}")
            return {}
    
    async def _fetch_precipitation(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """Precipitation forecast and history"""
        try:
            params = {
                'latitude': lat,
                'longitude': lon,
                'daily': 'precipitation_sum,rain_sum,snowfall_sum',
                'past_days': 90,
                'forecast_days': 7
            }
            
            async with session.get(self.apis['weather_api'], params=params, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    daily = data.get('daily', {})
                    
                    precip = daily.get('precipitation_sum', [])
                    
                    return {
                        'precipitation_90d': np.sum([p for p in precip[:90] if p is not None]) if precip else None,
                        'precipitation_forecast_7d': np.sum([p for p in precip[90:] if p is not None]) if len(precip) > 90 else None,
                        'source': 'Open-Meteo Precipitation'
                    }
        except Exception as e:
            logger.error(f"Precipitation API error: {e}")
            return {}
    
    async def _fetch_earthquake_data(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """USGS Earthquake API - Seismic activity (affects aquifer structure)"""
        try:
            end_time = datetime.now().isoformat()
            start_time = (datetime.now() - timedelta(days=365*5)).isoformat()
            
            params = {
                'format': 'geojson',
                'starttime': start_time,
                'endtime': end_time,
                'latitude': lat,
                'longitude': lon,
                'maxradiuskm': 200,
                'minmagnitude': 4.0
            }
            
            async with session.get(self.apis['earthquake_api'], params=params, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    features = data.get('features', [])
                    
                    magnitudes = [f['properties']['mag'] for f in features]
                    
                    return {
                        'earthquake_count_5yr': len(features),
                        'max_magnitude': max(magnitudes) if magnitudes else 0,
                        'avg_magnitude': np.mean(magnitudes) if magnitudes else 0,
                        'seismic_risk': 'high' if len(features) > 10 else 'low',
                        'source': 'USGS Earthquake API'
                    }
        except Exception as e:
            logger.error(f"Earthquake API error: {e}")
            return {}
    
    async def _fetch_soil_moisture(self, session: aiohttp.ClientSession, lat: float, lon: float) -> Dict:
        """Soil moisture data"""
        try:
            params = {
                'latitude': lat,
                'longitude': lon,
                'daily': 'soil_moisture_0_to_10cm,soil_moisture_10_to_40cm',
                'past_days': 30
            }
            
            async with session.get(self.apis['soil_moisture'], params=params, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    daily = data.get('daily', {})
                    
                    moisture_0_10 = daily.get('soil_moisture_0_to_10cm', [])
                    moisture_10_40 = daily.get('soil_moisture_10_to_40cm', [])
                    
                    return {
                        'soil_moisture_surface': np.nanmean([m for m in moisture_0_10 if m is not None]) if moisture_0_10 else None,
                        'soil_moisture_deep': np.nanmean([m for m in moisture_10_40 if m is not None]) if moisture_10_40 else None,
                        'source': 'Open-Meteo Soil Moisture'
                    }
        except Exception as e:
            logger.error(f"Soil moisture API error: {e}")
            return {}
    
    def calculate_groundwater_score(self, data: Dict[str, Any]) -> Dict[str, float]:
        """Calculate groundwater potential from real-world data"""
        
        score = 0.0
        confidence = 0.0
        factors = []
        
        # NASA POWER data (30% weight)
        if data.get('nasa_power', {}).get('total_precipitation'):
            precip = data['nasa_power']['total_precipitation']
            precip_score = min(precip / 1000, 1.0) * 30  # Normalize to 1000mm/year
            score += precip_score
            confidence += 30
            factors.append(f"Annual Precipitation: {precip:.1f}mm (NASA)")
        
        # Climate history (20% weight)
        if data.get('climate_history', {}).get('total_precipitation_5yr'):
            precip_5yr = data['climate_history']['total_precipitation_5yr']
            climate_score = min(precip_5yr / 5000, 1.0) * 20  # 5 years
            score += climate_score
            confidence += 20
            factors.append(f"5-Year Precipitation: {precip_5yr:.1f}mm")
        
        # Soil data (15% weight)
        if data.get('soil_data', {}).get('clay'):
            clay = data['soil_data']['clay']
            # Medium clay content is best for water retention
            clay_score = (1 - abs(clay - 30) / 30) * 15
            score += clay_score
            confidence += 15
            factors.append(f"Clay Content: {clay:.1f}%")
        
        # Soil moisture (15% weight)
        if data.get('soil_moisture', {}).get('soil_moisture_deep'):
            moisture = data['soil_moisture']['soil_moisture_deep']
            moisture_score = moisture * 15
            score += moisture_score
            confidence += 15
            factors.append(f"Deep Soil Moisture: {moisture:.2f}")
        
        # Elevation (10% weight)
        if data.get('elevation', {}).get('elevation_m'):
            elevation = data['elevation']['elevation_m']
            # Lower elevations often better for groundwater
            elev_score = max(0, (2000 - elevation) / 2000) * 10
            score += elev_score
            confidence += 10
            factors.append(f"Elevation: {elevation:.0f}m")
        
        # USGS wells (10% weight)
        if data.get('usgs_wells', {}).get('nearby_wells'):
            wells = data['usgs_wells']['nearby_wells']
            well_score = min(wells / 10, 1.0) * 10
            score += well_score
            confidence += 10
            factors.append(f"Nearby Wells: {wells}")
        
        # Normalize score to 0-100
        if confidence > 0:
            normalized_score = (score / confidence) * 100
        else:
            normalized_score = 50.0  # Default if no data
        
        return {
            'groundwater_potential': min(normalized_score, 100.0),
            'confidence': confidence,
            'factors': factors,
            'data_sources_used': len([k for k, v in data.items() if v and k != 'timestamp' and k != 'location'])
        }


# Global instance
realtime_engine = RealtimeDataEngine()
