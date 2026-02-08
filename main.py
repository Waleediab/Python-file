import math as m

e = 0.08181919084
a = 6378137.0

choice = False
#input("Enter 1 for Geodetic to Cartesian, or 2 for Cartesian to Geodetic (0 to quit): ")

while choice != "0":

    choice = input("Enter 1 for Geodetic to Cartesian, or 2 for Cartesian to Geodetic (0 to quit): ")

    if choice == "1":

        coord = input("\nEnter the coordinates (Latitude, Longitude, Height): ").strip().split(",")

        lat = m.radians(float(coord[0]))
        long = m.radians(float(coord[1]))
        height = float(coord[2])

        N = a / (m.sqrt(1 - e**2 * m.sin(lat)**2))

        x = (N + height) * m.cos(lat) * m.cos(long)
        y = (N + height) * m.cos(lat) * m.sin(long)
        z = ((1 - e**2) * N + height) * m.sin(lat)

        print("X, Y, Z: " + str(x) + ", " + str(y) + ", " + str(z))

    elif choice == "2":


        coord = input("\nEnter the coordinates (X Y Z): ").strip().split(",")

        x = float(coord[0])
        y = float(coord[1])
        z = float(coord[2])

        long = m.atan2(float(y), float(x))

        p = m.sqrt(float(x)**2 + float(y)**2)
        current_lat = m.atan(float(z)/((1-e**2)*p))

        last_lat = 0

        while abs(current_lat - last_lat) > 0.00000000001:

            last_lat = current_lat

            N = a / (m.sqrt(1 - e**2 * m.sin(last_lat)**2))

            height = (p / m.cos(last_lat)) - N
   
            current_lat = m.atan2(z, p * (1 - e**2 * N / (N + height)))

        print("Latitude, Longitude, Height: " + str(m.degrees(current_lat)) + ", " + str(m.degrees(long)) + ", " + str(height))

    else:
        continue
