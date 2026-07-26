def ride_fare(base_fare,distance_km,trafic_delay_min):

    cost_per_km=13.0
    cost_per_min= 2.0

    distance_cost= distance_km * cost_per_km
    time_cost = trafic_delay_min * cost_per_min

    total_fare = base_fare + distance_cost + time_cost 

    if trafic_delay_min > 15:
        total_fare = total_fare * 1.20

    return total_fare

ride_1 = ride_fare( 30,5.5,5)
ride_2 = ride_fare( 30,5.5,25)

print("Cloud ride calculation")
print(" Normal Trip fare:  " , round(ride_1,2))
print(" Surge trip fare: ", round( ride_2,2))