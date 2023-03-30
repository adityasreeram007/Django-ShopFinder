import math
def findInRadius(r,lat,lon,shops):
   resultSet=[]
   lat1=lat
   lon1=lon
   for shop in shops:
      lat2 = float(getattr(shop,"latitude"))
      lon2=float(getattr(shop,"longtitude"))
      
      R = 6371e3
      φ1 = lat1 * math.pi/180 
      φ2 = lat2 * math.pi/180
      Δφ = (lat2-lat1) * math.pi/180
      Δλ = (lon2-lon1) * math.pi/180

      a = math.sin(Δφ/2) * math.sin(Δφ/2) +math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2)
      c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

      d = R * c / 1000
      
      if d<=r:
         resultSet.append(shop)
   return resultSet
   # resultSet=[]
   # lat = lat * math.pi/180
   # R = 6371000
   # for shop in shops:
   #    # print(getattr(shop,"shopName"))
   #    # print(shop.get("name"))
   #    lat1 = float(getattr(shop,"latitude")) * math.pi/180
   #    lon = (lon-float(getattr(shop,"longtitude"))) * math.pi/180
   #    print(lat,lat1,lon)
      
   #    # print( math.sin(lat)*math.sin(lat1) + math.cos(lat)*math.cos(lat1) * math.cos(lon))
   #    d = math.acos( math.sin(lat)*math.sin(lat1) + math.cos(lat)*math.cos(lat1) * math.cos(lon) ) * R / 1000
   #    print("dist",d)
   #    if d<=r:
   #       resultSet.append(shop)
   # return resultSet


