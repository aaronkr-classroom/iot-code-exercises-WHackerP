# 3_set.py
#두 집합 정의
set1 = {1, 2, 3, 'a', "Hello"}
set2 = {"Hello", 3, 4, 5, 'b'}

# 합집합	(union)
union_set = set1 | set2	   # c에서 || = OR, py에서 or

# 교집합 (intersaction)
int_set = set1 & set2	   # c에서 && = and, py에서 and

# 차집합 (difference)
diff_set = set1 - set2

# 대칭 차집합 (symmetric_difference)
sym_diff_set = set1 ^ set2 # 합집합과 교집합의 차집합

print('union:', union_set)
print(f"intersaction: {int_set}")
print(f"difference: {diff_set}")
print(f"symmetric difference: {sym_diff_set}")