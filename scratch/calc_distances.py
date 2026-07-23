import math

# Coordinates: RA in hours, Dec in degrees, dist in pc
# HD 101065 (Przybylski's Star)
p_ra_h, p_ra_m, p_ra_s = 11, 37, 37
p_dec_d, p_dec_m, p_dec_s = -46, 42, 35
p_dist = 109.0

p_ra = (p_ra_h + p_ra_m/60.0 + p_ra_s/3600.0) * 15.0 # in degrees
p_dec = p_dec_d - p_dec_m/60.0 - p_dec_s/3600.0 # negative dec

def to_cartesian(ra_deg, dec_deg, r_pc):
    ra_rad = math.radians(ra_deg)
    dec_rad = math.radians(dec_deg)
    x = r_pc * math.cos(dec_rad) * math.cos(ra_rad)
    y = r_pc * math.cos(dec_rad) * math.sin(ra_rad)
    z = r_pc * math.sin(dec_rad)
    return x, y, z

p_x, p_y, p_z = to_cartesian(p_ra, p_dec, p_dist)

targets = [
    {"name": "Gaia BH1", "ra_h": 17, "ra_m": 28, "ra_s": 41, "dec_d": 0, "dec_m": -34, "dec_s": -51, "dist": 477.6},
    {"name": "Gaia BH2", "ra_h": 13, "ra_m": 50, "ra_s": 0, "dec_d": -59, "dec_m": -14, "dec_s": -20, "dist": 1160.0},
    {"name": "HR 6819 (System)", "ra_h": 18, "ra_m": 17, "ra_s": 7, "dec_d": -56, "dec_m": -1, "dec_s": -24, "dist": 340.0}
]

print(f"Przybylski's Star (HD 101065): {p_dist} pc")

for t in targets:
    t_ra = (t["ra_h"] + t["ra_m"]/60.0 + t["ra_s"]/3600.0) * 15.0
    # handle negative dec correctly
    sgn = -1 if t["dec_d"] <= 0 else 1
    t_dec = t["dec_d"] + sgn*abs(t["dec_m"])/60.0 + sgn*abs(t["dec_s"])/3600.0
    
    t_x, t_y, t_z = to_cartesian(t_ra, t_dec, t["dist"])
    
    dist_3d = math.sqrt((t_x - p_x)**2 + (t_y - p_y)**2 + (t_z - p_z)**2)
    print(f"{t['name']}: {dist_3d:.2f} pc away from HD 101065")
