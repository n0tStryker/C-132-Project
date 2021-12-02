temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  if planet_data[1].lower() == "hd 100546 b":
    planet_data_rows.remove(planet_data)

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()

planet_type_values = []
for planet_data in planet_data_rows:
  planet_type_values.append(planet_data[6])

print(list(set(planet_type_values)))

import plotly.express as px
low_gravity_planets = [] 
for index, gravity in enumerate(planet_gravity): 
  if gravity < 10: 
    low_gravity_planets.append(planet_data_rows[index]) 
    
print(len(low_gravity_planets))

planet_masses = []
planet_radii = []
for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radii.append(planet_data[7])

fig = px.scatter(x=planet_radii,y= planet_masses)
fig.show()