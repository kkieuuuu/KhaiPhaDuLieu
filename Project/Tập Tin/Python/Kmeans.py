#import thư viện pandas
import pandas as pd

#đọc dữ liệu
df = pd.read_csv('E:/Data Mining/Project/MucDoMuaSam.csv')

#import thư viện sklearn, numpy, matplotlib
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

#Thuật toán Kmeans
kmeans = KMeans(n_clusters=5, n_init=20, random_state=0)
df['cluster'] = kmeans.fit_predict(df[['Tan suat mua hang','So luong san pham', 'Gia tri don hang']])

#In tọa độ tâm cụm 
print(kmeans.cluster_centers_)

#Tạo màu và gán màu cho từng cụm tương ứng
colors = ['#001949', '#5567C9', '#8D9AC5', '#FFC2B8','#E17A8D']
df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2], 3:colors[3], 4:colors[4]})

#Trực quan hóa dữ liệu
fig = plt.figure(figsize=(26 , 6))
axis = fig.add_subplot(131, projection='3d')
axis.scatter(df['So luong san pham'], df['Gia tri don hang'], df['Tan suat mua hang'], c=df.c, s=df['Gia tri don hang']* 2, alpha = 0.8)
axis.set_xlabel('Số lượng sản phẩm')
axis.set_ylabel('Tần suất mua hàng')
axis.set_zlabel('Giá trị đơn hàng')

#Hiển thị Biểu đồ
plt.show()