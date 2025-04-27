##write a python program which accepts a side of a regular n-sided polygon.
##Your program should compute the total sum of internal angles (in degrees).

##Example, a polygon of 3 sides, has 180 degrees sum of internal angles.
##A 6—sided polygon has a sum of 720 degrees and so on.

##The formuLa (n—2) x 180 gives the sum of all measures ot the angles of an n-sided polygon.

n = int(input("Enter the number of sides of the polygon: "))
formula = (n - 2) * 180
print("Total sum of internal angles: ", formula, "degrees")