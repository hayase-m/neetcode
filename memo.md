## Sliding Window Maximum
両端を操作したい→deque
### 工夫点
dequeにはvalueではなくindexをいれる
→この問題はindex,valueの両方が必要。indexをdeque，valueをnums[index]で取得するという役割分担。

## Find the Duplicate Number
### 工夫点
floydのアルゴリズムを使う

## Maximum Subarray
### 工夫点
Kadane's Algorithmを使う

## Diameter of Binary Tree
- dfs
- 帰りがけ順
- 二分木
