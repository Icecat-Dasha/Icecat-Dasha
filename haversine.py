def haversine(lon1, lat1, lon2, lat2, radius=6371): 
    lat1 = np.radians(lat1) 
    lat2 = np.radians(lat2) 
    lon1 = np.radians(lon1) 
    lon2 = np.radians(lon2) 
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2 
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a)) 
    dists = radius * c 
    return dists