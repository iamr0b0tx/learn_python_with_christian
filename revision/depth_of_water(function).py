def calculate_depth(volume_local, area_local):
    '''takes at volume and area and returns depth'''

    ##claculate depth
    height_local = volume_local / area_local

    return round(height_local, 4)

##declare variables
volume_global = input('Type Volume here (in km3): ') #22_810 #volume in km3
if volume_global == '':
    volume_global = 22_810 #volume in km3

area_global = input('Type Area here (in km2): ') #8_080_464.3 #Area in km2
if area_global == '':
    area_global = 8_080_464.3 #Area in km2

volume_global = float(volume_global)
area_global = float(area_global)

 ##call function to calculate depth
h = calculate_depth(volume_global, area_global)

##display result
print('the depth will be', h, 'km')
