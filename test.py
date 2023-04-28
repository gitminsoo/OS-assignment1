#%%
import matplotlib.pyplot as plt

# 데이터
categories = ['A', 'B', 'C', 'D']
start_values1 = [10, 15, 20, 25]
end_values1 = [18, 28, 35, 42]
start_values2 = [12, 18, 22, 28]
end_values2 = [20, 30, 38, 46]

# 막대 길이 계산
width_values1 = [end - start for start, end in zip(start_values1, end_values1)]
width_values2 = [end - start for start, end in zip(start_values2, end_values2)]

# 겹치는 가로 막대 그래프 그리기
plt.barh(categories, width_values1, left=start_values1, alpha=0.7, label='Dataset 1')
plt.barh(categories, width_values2, left=start_values2, alpha=0.7, label='Dataset 2')

# 축 레이블, 범례, 그리드 설정
plt.xlabel('Value')
plt.ylabel('Category')
plt.legend(loc='best')
plt.grid(axis='x')

# 그래프 출력
plt.show()

# %%
