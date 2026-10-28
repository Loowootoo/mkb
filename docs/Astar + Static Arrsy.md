以下是 **完整整合 A* 演算法 + 靜態陣列優先隊列** 的 C 程式碼，並附上 **詳細註解** 說明每個步驟的原理和實現方式。

---

## 📌 程式碼概述

- **網格大小**：`GRID_H x GRID_W`（可自訂）。
- **靜態陣列優先隊列**：使用 `MinHeap` 結構，內部使用 **靜態 1D 陣列** 存放節點。
- **A* 核心**：
    - 使用 **曼哈頓距離** 作為啟發式函數 `h(n)`。
    - **開放列表（Open List）**：使用最小堆積（`MinHeap`）。
    - **封閉列表（Closed List）**：使用 2D 陣列 `closed[GRID_H][GRID_W]` 標記是否已探索。
    - **父節點追蹤**：使用 2D 陣列 `parent[GRID_H][GRID_W]` 記錄路徑。

---

## 🔧 完整程式碼（附註解）

```c
#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

// --- 定義網格大小 ---
#define GRID_H 8  // 網格高度
#define GRID_W 8  // 網格寬度
#define MAX_HEAP_SIZE (GRID_H * GRID_W)  // 最大堆積大小 = 網格總格數

// --- 定義節點結構 ---
typedef struct {
    int x, y;       // 節點座標
    int f, g, h;    // f = g + h（A* 的總成本）
} Node;

// --- 定義最小堆積結構（優先隊列） ---
typedef struct {
    Node array[MAX_HEAP_SIZE];  // 靜態陣列存放節點
    int size;                     // 目前堆積大小
} MinHeap;

// --- 定義網格地圖（0=可通行，1=障礙物） ---
int grid[GRID_H][GRID_W] = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 1, 0, 0, 0, 1, 0, 0},
    {0, 1, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 1, 0, 1, 0, 0},
    {0, 0, 0, 1, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 1, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0}
};

// --- 起點和目標 ---
#define START_X 0
#define START_Y 0
#define GOAL_X 7
#define GOAL_Y 7

// --- 封閉列表（標記是否已探索） ---
bool closed[GRID_H][GRID_W] = {false};

// --- 父節點追蹤（用於回溯路徑） ---
Node parent[GRID_H][GRID_W];

// --- 方向（上下左右） ---
const int dx[] = {-1, 1, 0, 0};  // x 方向的變化量
const int dy[] = {0, 0, -1, 1};  // y 方向的變化量

// --- 函數宣告 ---
void initMinHeap(MinHeap *heap);
void swap(Node *a, Node *b);
void heapify(MinHeap *heap, int idx);
void insert(MinHeap *heap, Node node);
Node extractMin(MinHeap *heap);
bool isEmpty(MinHeap *heap);
int manhattanDistance(int x1, int y1, int x2, int y2);
bool isValid(int x, int y);
bool isGoal(int x, int y);
void aStar(MinHeap *openList);
void printPath(Node path[], int pathLength);

// --- 主函數 ---
int main() {
    MinHeap openList;
    initMinHeap(&openList);

    // 起點節點
    Node start = {START_X, START_Y, 0, 0, manhattanDistance(START_X, START_Y, GOAL_X, GOAL_Y)};
    start.f = start.g + start.h;

    // 將起點加入開放列表
    insert(&openList, start);

    // 執行 A* 演算法
    aStar(&openList);

    return 0;
}

// --- 初始化最小堆積 ---
void initMinHeap(MinHeap *heap) {
    heap->size = 0;
}

// --- 交換兩個節點 ---
void swap(Node *a, Node *b) {
    Node temp = *a;
    *a = *b;
    *b = temp;
}

// --- 向下調整（Heapify）：確保父節點 ≤ 子節點 ---
void heapify(MinHeap *heap, int idx) {
    int smallest = idx;
    int left = 2 * idx + 1;  // 左子節點索引
    int right = 2 * idx + 2; // 右子節點索引

    // 比較左子節點
    if (left < heap->size && heap->array[left].f < heap->array[smallest].f) {
        smallest = left;
    }
    // 比較右子節點
    if (right < heap->size && heap->array[right].f < heap->array[smallest].f) {
        smallest = right;
    }
    // 如果最小值不是當前節點，交換並遞迴調整
    if (smallest != idx) {
        swap(&heap->array[idx], &heap->array[smallest]);
        heapify(heap, smallest);
    }
}

// --- 插入節點到堆積 ---
void insert(MinHeap *heap, Node node) {
    if (heap->size == MAX_HEAP_SIZE) {
        printf("堆積已滿，無法插入！\n");
        return;
    }
    // 新節點加在堆積末端
    heap->array[heap->size] = node;
    int i = heap->size;
    heap->size++;

    // 向上調整（Bubble Up）：確保父節點 ≤ 子節點
    while (i != 0 && heap->array[(i - 1) / 2].f > heap->array[i].f) {
        swap(&heap->array[i], &heap->array[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

// --- 提取最小 f 值的節點 ---
Node extractMin(MinHeap *heap) {
    Node emptyNode = {-1, -1, INT_MAX, INT_MAX, INT_MAX};
    if (heap->size == 0) {
        return emptyNode;
    }
    // 根節點是最小值
    Node root = heap->array[0];
    // 將最後一個節點移到根節點
    heap->array[0] = heap->array[heap->size - 1];
    heap->size--;
    // 向下調整
    heapify(heap, 0);
    return root;
}

// --- 判斷堆積是否為空 ---
bool isEmpty(MinHeap *heap) {
    return heap->size == 0;
}

// --- 計算曼哈頓距離（啟發式函數 h(n)） ---
int manhattanDistance(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

// --- 判斷座標是否有效（在網格內且非障礙物） ---
bool isValid(int x, int y) {
    return (x >= 0 && x < GRID_H && y >= 0 && y < GRID_W && grid[x][y] == 0);
}

// --- 判斷是否到達目標 ---
bool isGoal(int x, int y) {
    return (x == GOAL_X && y == GOAL_Y);
}

// --- A* 演算法主函數 ---
void aStar(MinHeap *openList) {
    // 初始化父節點（用於回溯路徑）
    for (int i = 0; i < GRID_H; i++) {
        for (int j = 0; j < GRID_W; j++) {
            parent[i][j].x = -1;
            parent[i][j].y = -1;
        }
    }

    while (!isEmpty(openList)) {
        // 1. 從開放列表中提取 f 最小的節點
        Node current = extractMin(openList);
        int currentX = current.x;
        int currentY = current.y;

        // 2. 如果是目標，回溯路徑並結束
        if (isGoal(currentX, currentY)) {
            // 回溯路徑
            Node path[MAX_HEAP_SIZE];
            int pathLength = 0;
            Node temp = current;
            while (temp.x != -1 && temp.y != -1) {
                path[pathLength++] = temp;
                temp = parent[temp.x][temp.y];
            }
            // 反轉路徑（從起點到目標）
            for (int i = 0; i < pathLength / 2; i++) {
                swap(&path[i], &path[pathLength - 1 - i]);
            }
            printPath(path, pathLength);
            return;
        }

        // 3. 將當前節點加入封閉列表
        closed[currentX][currentY] = true;

        // 4. 探索鄰居
        for (int i = 0; i < 4; i++) {
            int newX = currentX + dx[i];
            int newY = currentY + dy[i];

            // 5. 判斷鄰居是否有效且未被探索
            if (isValid(newX, newY) && !closed[newX][newY]) {
                // 6. 計算 g, h, f
                int newG = current.g + 1;  // 移動成本（假設每步成本為 1）
                int newH = manhattanDistance(newX, newY, GOAL_X, GOAL_Y);
                int newF = newG + newH;

                // 7. 判斷鄰居是否已在開放列表中
                bool inOpenList = false;
                for (int j = 0; j < openList->size; j++) {
                    if (openList->array[j].x == newX && openList->array[j].y == newY) {
                        inOpenList = true;
                        // 如果新的 g 值更小，更新 f 和 g
                        if (newG < openList->array[j].g) {
                            openList->array[j].g = newG;
                            openList->array[j].f = newF;
                            parent[newX][newY] = current;  // 更新父節點
                            // 重新排序堆積（簡單方法：重新插入並刪除舊節點）
                            // 此處為了簡化，直接重新插入
                            Node updatedNode = {newX, newY, newF, newG, newH};
                            insert(openList, updatedNode);
                        }
                        break;
                    }
                }

                // 8. 如果不在開放列表中，加入新節點
                if (!inOpenList) {
                    Node neighbor = {newX, newY, newF, newG, newH};
                    parent[newX][newY] = current;  // 記錄父節點
                    insert(openList, neighbor);
                }
            }
        }
    }

    // 如果開放列表為空且未找到目標
    printf("無法找到路徑！\n");
}

// --- 列印路徑 ---
void printPath(Node path[], int pathLength) {
    printf("找到路徑（從起點到目標）：\n");
    for (int i = 0; i < pathLength; i++) {
        printf("(%d, %d)", path[i].x, path[i].y);
        if (i < pathLength - 1) {
            printf(" -> ");
        }
    }
    printf("\n");
}
```

## 📝 程式碼註解說明

---

### 🔹 1. 定義和全域變數

- **`GRID_H` 和 `GRID_W`**：網格的高度和寬度。
- **`MAX_HEAP_SIZE`**：最小堆積的最大大小（等於網格總格數）。
- **`Node` 結構**：存放節點的座標 `(x, y)` 和 A* 的成本 `f`, `g`, `h`。
- **`MinHeap` 結構**：使用 **靜態陣列** 存放節點，並追蹤堆積大小。
- **`grid`**：2D 陣列表示地圖（`0`=可通行，`1`=障礙物）。
- **`closed`**：2D 陣列標記節點是否已被探索。
- **`parent`**：2D 陣列記錄每個節點的父節點（用於回溯路徑）。
- **`dx` 和 `dy`**：方向陣列（上下左右）。

---

### 🔹 2. 最小堆積（優先隊列）的實現

- **`initMinHeap`**：初始化堆積（`size = 0`）。
- **`swap`**：交換兩個節點。
- **`heapify`**：向下調整堆積，確保父節點 ≤ 子節點。
- **`insert`**：插入新節點到堆積，並向上調整。
- **`extractMin`**：提取最小 `f` 值的節點，並向下調整。
- **`isEmpty`**：判斷堆積是否為空。

---

### 🔹 3. A* 核心函數

- **`manhattanDistance`**：計算曼哈頓距離（啟發式函數 `h(n)`）。
- **`isValid`**：判斷座標是否在網格內且非障礙物。
- **`isGoal`**：判斷是否到達目標。
- **`aStar`**：A* 演算法的主函數：
    1. 從開放列表中提取 `f` 最小的節點。
    2. 如果是目標，回溯路徑並結束。
    3. 將當前節點加入封閉列表。
    4. 探索鄰居，計算 `g`, `h`, `f`。
    5. 如果鄰居不在開放列表中，加入新節點；如果已在開放列表中且新的 `g` 值更小，更新節點。
- **`printPath`**：列印找到的路徑。

---

### 🔹 4. 主函數

- 初始化開放列表（最小堆積）。
- 將起點加入開放列表。
- 執行 A* 演算法。

---

## 📌 範例輸出

假設網格如下（`1` 為障礙物，`0` 為可通行）：

起點 `(0, 0)`，目標 `(7, 7)`，程式輸出可能如下：
```text
0 0 0 0 0 0 0 0
0 1 0 0 0 1 0 0
0 1 0 0 0 0 0 0
0 0 0 1 0 1 0 0
0 0 0 1 0 0 0 0
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```
## 🔍 關鍵點說明

1. **靜態陣列的優點**：
    
    - 不需要 `malloc`，避免動態記憶體分配。
    - 適合小型或固定大小的網格。
2. **A* 的優先隊列**：
    
    - 使用最小堆積來高效提取 `f` 最小的節點。
    - 每次插入和提取的時間複雜度為 **O(log n)**。
3. **啟發式函數**：
    
    - 使用 **曼哈頓距離** 作為 `h(n)`，確保 **可容許性**（不高估真實成本）。
4. **路徑回溯**：
    
    - 使用 `parent` 陣列記錄每個節點的父節點，最後從目標回溯到起點。

---

## 💡 進一步優化

1. **避免重複插入**：
    
    - 目前的實現中，如果鄰居已在開放列表中，會直接重新插入新節點。這可能導致堆積中有重複的節點。
    - 更優的做法是 **更新現有節點的 `f` 和 `g` 值**，然後重新排序堆積（但這需要更複雜的實現，如使用索引映射）。
2. **使用更高效的啟發式函數**：
    
    - 如果允許對角線移動，可以使用 **歐幾里得距離** 或 **對角線距離**。
3. **記憶體優化**：
    
    - 如果網格很大，可以使用 **位元陣列** 來標記 `closed` 和 `parent`，節省記憶體。

---
