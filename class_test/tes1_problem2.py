# Author: Obaydullah Al Numan
A = float(input())
A_weight = 2
B = float(input())
B_weight = 3
C = float(input())
C_weight = 5
median = (A*A_weight + B*B_weight + C*C_weight) / (A_weight + B_weight + C_weight)
print(f"MEDIAN = {median:.1f}")