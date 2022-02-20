import math
import numpy as np

route_list = np.array([
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [3, 0, 0, 0, 0]]) # 初期のノード間の距離のリスト

node_num = len(route_list) #ノードの数

unsearched_nodes = list(range(node_num)) # 未探索ノード
distance = [math.inf] * node_num # ノードごとの距離のリスト
previous_nodes = [-1] * node_num # 最短経路でそのノードのひとつ前に到達するノードのリスト
distance[0] = 0 # 初期のノードの距離は0とする

while(len(unsearched_nodes) != 0): #未探索ノードがなくなるまで繰り返す
    # まず未探索ノードのうちdistanceが最小のものを選択する
    posible_min_distance = math.inf # 最小のdistanceを見つけるための一時的なdistance。初期値は inf に設定。
    posible_min_distance_index = -1 # 最小のdistanceを見つけるための一時的なdistanceのindex。初期値は -1 に設定。
    for node_index in unsearched_nodes: # 未探索のノードのループ
        if posible_min_distance > distance[node_index]:
            posible_min_distance = distance[node_index] # より小さい値が見つかれば更新
            posible_min_distance_index = node_index # indexも更新
    target_min_index =  posible_min_distance_index # 未探索ノードのうちで最小のindex番号
    unsearched_nodes.remove(target_min_index) # ここで探索するので未探索リストから除去

    target_edge = route_list[:, target_min_index] # ターゲットになるノードからのびるエッジのリスト
    for index, route_dis in enumerate(target_edge):
        if route_dis != 0:
            if distance[index] > (distance[ target_min_index] + route_dis):
                distance[index] = distance[ target_min_index] + route_dis # 過去に設定されたdistanceよりも小さい場合はdistanceを更新
                previous_nodes[index] =  target_min_index #　ひとつ前に到達するノードのリストも更新

# 以下で結果の表示

print("-----経路-----")
previous_node = node_num - 1
while previous_node != -1:
    if previous_node !=0:
        print(str(previous_node + 1) + " <- ", end='')
    else:
        print(str(previous_node + 1))
    previous_node = previous_nodes[previous_node]

print("-----距離-----")
print(distance[node_num - 1])