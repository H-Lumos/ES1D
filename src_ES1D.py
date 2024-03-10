# 1d 静电程序
import numpy as npy
import matplotlib.pyplot as plt


# 从粒子到网格分配电荷的一阶权重法
def particle_to_cell(np, nc):
    """
    从粒子到网格分配电荷的一阶权重法
    :param np: number of particles
    :param nc: number of cells
    """

    delta_x = 1  # length of cell  # TODO(rainzer) 再定义一个缺省参数，不赋值的时候默认为1，否则定义为网格间距

    xp = npy.round(npy.random.uniform(0, nc, size=np), 2)  # 在网格中随机生成粒子位置
    print('xp =', xp)
    list_xp = [0] * (nc + 1)  # 列表储存格点分配的电荷

    for element_xp in xp:  # 一阶权重法计算网格分配到的电荷
        index_floor = int(npy.floor(element_xp))
        index_ceil = int(npy.ceil(element_xp))
        list_xp[index_floor] = list_xp[index_floor] + npy.ceil(element_xp) - element_xp
        list_xp[index_ceil] = list_xp[index_ceil] + element_xp - npy.floor(element_xp)

    list_xp = npy.round(list_xp, 2)
    selected_elements = list_xp[1:-1]  # 使用列表切片获取第二个到倒数第二个元素
    average = sum(selected_elements) / len(selected_elements)  # 计算平均值

    print(list_xp)
    print(selected_elements)
    print('avg = ', npy.round(average, 2))  # 每个格点平均分配到的电荷

    data_array = npy.array(selected_elements)  # 把列表转换成numpy数组
    # 创建x轴数据（可以使用NumPy的arange函数生成等间隔的数据）
    x = npy.arange(len(data_array))
    # # 使用Matplotlib绘制折线图
    # plt.plot(x, data_array, marker='o', linestyle='-')
    errors = data_array - average  # 误差数组
    plt.scatter(x, data_array)
    # 绘制误差线
    for i, error in enumerate(errors):  # i获得当前循环的索引，error获得当前索引对应的值
        plt.plot([x[i], x[i]], [data_array[i], average], color='gray', linestyle='--')
    # 绘制均值线
    plt.axhline(y=average, color='red', linestyle='--')
    # 在图中显示平均值
    plt.text(x[-1], npy.around(average, 2), f'avg = {average}', ha='left', va='bottom', color='red')
    # 添加标题和标签
    plt.title('Scatter Plot with Errors')
    plt.xlabel('Grid Point')
    plt.ylabel('Value')
    # 显示图形
    plt.show()


# 利用一阶权重法计算网格点分配到的电荷
particle_to_cell(10000,100)  # (粒子数，网格数)
