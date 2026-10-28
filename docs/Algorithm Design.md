---
title: 遞增法與算法設計
tags:
  - 算法
  - 遞增法
---

Incremental Method

> 不積跬步，無以至千里。不積小流，無以成江海。《荀子》

「遞增法」是符合電腦運作特性的方法。電腦執行程式，一次只做一個動作，完成了一件事才做下一件事。當一個問題太大太多時，化整為零、一個一個解決吧！

> 合抱之木，生於毫末；九層之臺，起於累土；千里之行，始於足下。謹以此句與大家共勉。

### 範例：加總數字

無論電腦再怎麼強，還是得一個一個累加數字。
![[Pasted image 20211016194651.png]]
```c
void summation()
{
    int array[5] = {3, 6, 9, -8, 1};
 
    int sum = 0;
    for (int i=0; i<5; i++)
        sum += array[i];
 
    cout << "總和是" << sum;
}
int summation(int array[], int n)
{
    int sum = 0;
    for (int i=0; i<n; i++)
        sum += array[i];
    return sum;
}
```

### 範例：複製字串
無論電腦再怎麼強，還是得逐字複製。
![[Pasted image 20211016194852.png]]
```c
void copy()
{
    char s[15] = "incremental";
    char t[15];
 
    int i;
    for (i=0; s[i] != '\0'; i++)
        t[i] = s[i];
    t[i] = '\0';
 
    cout << "原本字串" << s;
    cout << "複製之後的字串" << t;
}
void copy(char* s, char* t)
{
    int i;
    for (i=0; s[i]; i++)
        t[i] = s[i];
    t[i] = '\0';
}
```

### 範例：選擇排序法（ Selection Sort ）

找到第一小的數字，放在第一個位置；再找到第二小的數字，放在第二個位置。一次找一個數字，如此下去就會把所有數字按照順序排好了。

![[Pasted image 20211016194944.png]]
```c
void selection_sort()
{
    int array[5] = {3, 6, 9, -8, 1};
 
    for (int i=0; i<5; i++)
    {
        // 從尚未排序的數字當中，找到第i小的數字。
        int min_index = i;
        for (int j=i+1; j<5; j++)
            if (array[j] < array[min_index])
                min_index = j;
 
        // 把第i小的數字，放在第i個位置。
        swap(array[i], array[min_index]);
    }
 
    // 印出排序結果。
    for (int i=0; i<5; i++)
        cout << array[i];
}
void selection_sort(int array[], int n)
{
    for (int i=0; i<n; i++)
    {
        // 從尚未排序的數字當中，找到第i小的數字。
        int min_index = i;
        for (int j=i+1; j<n; j++)
            if (array[j] < array[min_index])
                min_index = j;
 
        // 把第i小的數字，放在第i個位置。
        swap(array[i], array[min_index]);
    }
}
```

### 範例：印出直角三角形

多字成行，多行成直角三角形。由細微的東西開始，一件一件組起來。

![[Pasted image 20211016195041.png]]
```c
// 多字成行
void print_line(int n)  // n 是一行的長度
{
    for (int i=1; i<=n; i++) cout << '@';
    cout << '\n';
}
 
// 多行成直角三角形
void print_triangle(int n)  // n 是行數
{
    for (int i=n; i>=1; i--) print_line(i);
}
UVa 488 10038 10107 10370
```

### 範例：人潮最多的時段（ Interval Partitioning Problem ）

一群訪客參加宴會，我們詢問到每一位訪客的進場時刻與出場時刻，請問宴會現場擠進最多人的時段。

換個角度想，想像會場門口裝著一支監視器。有訪客進入，會場就多一人；有訪客離開，會場就少一人。如此就很容易統計會場人數。遞增的標的是時刻，而不是訪客。

【註：這個技巧在中文網路上暱稱為「離散化」。】
![[Pasted image 20211016195140.png]]
```c
struct Guest {int arrival, leave;} g[10];
 
bool cmp(int i, int j)
{
    return abs(i) < abs(j);
}
 
void maximum_guest()
{
    vector<int> time;
    for (int i=0; i<10; i++)
    {
        time.push_back(+g[i].arrival);
        time.push_back(-g[i].leave);
    }
 
    sort(time.begin(), time.end(), cmp);
 
    int n = 0, maximum = 0;
    for (int i=0; i<time.size(); i++)
    {
        if (time[i] >= 0)
            n++;
        else
            n--;
 
        maximum = max(maximum, n);
    }
    cout << "人潮最多的時段有" << maximum << "人";
}

此處僅找出人數。找出人潮最多的時段，就留給各位自行嘗試吧。

UVa 688 972 10613 10585 10963

UVa 308 837
```

### 範例：儲存座標

遞增的標的，主為點，次為座標軸。
![[Pasted image 20211016195256.png]]
```c
struct Point {float x, y;} p[5] =
{
    {0, 1}, {1, 2}, {3, 0}, {2, 2}, {3, 1}
};
```
遞增的標的，主為座標軸，次為點。
![[Pasted image 20211016195317.png]]
```c
float x[5] = {0, 1, 3, 2, 3};
float y[5] = {1, 2, 0, 2, 1};
```

### 範例：印出轉換成小寫的字串

![[Pasted image 20211016195414.png]]
有需要改變的，只有大寫字母 ── 如果是大寫字母，就轉換成小寫字母並且印出；如果不是大寫字母，就直接印出。
```c
void print_lowercase()
{
    char s[15] = "Hello World!";
 
    for (int i=0; s[i]; i++)
        if (s[i] >= 'A' && s[i] <= 'Z')
            cout << (char)(s[i] - 'A' + 'a');
        else
            cout << s[i];
}
```
也可以一步一步進行：（一）複製一份字串（二）字串轉換成小寫（三）印出字串。
```c
void print_lowercase()
{
    char s[15] = "Hello World!";
    char t[15];
 
    // 第一波：複製一份字串
    for (int i=0; s[i]; i++)
        t[i] = s[i];
 
    // 第二波：字串轉換成小寫
    for (int i=0; s[i]; i++)
        if (t[i] >= 'A' && t[i] <= 'Z')
            t[i] = t[i] - 'A' + 'a';
 
    // 第三波：印出字串
    cout << t;
}
void print_lowercase()
{
    char s[15] = "Hello World!";
    char t[15];
 
    // 每一波的程式碼可以自行包裝成為函式，
    // 亦可套用內建函式庫。
    my_copy(s, t);      // 複製字串
    my_lowercase(t);    // 換成小寫
    cout << t;          // 印出字串
}
```
第一種解法稱作 one-pass ，資料只會讀取一遍。讀取資料的同時，也一口氣處理掉所有事情。

第二種解法稱作 multi-pass ，資料會重複讀取許多遍。所有事情劃分成數個階段，逐步處理，每個階段只專心處理一件事情。

one-pass 的優點是：程式碼簡短、執行時間也短。缺點是：程式碼不易編修。

multi-pass 的優點是：程式碼一目了然，容易編修、測試、除錯；程式碼可以包裝成為函式，也有機會套用內建函式庫。缺點是：需要額外的暫存記憶體。

這兩種方式各有利弊。程式員必須自行取捨。

### 範例：對調數字

利用一個變數，暫存其中一個數字，以便對調。
![[Pasted image 20211016195534.png]]
```c
void swap_int()
{
    int a = 0, b = 1;
 
    // 交換a與b
    int temp = a;
    a = b;
    b = temp;
 
    cout << a << ' ' << b;
}
void swap_int(int& a, int& b)
{
    int temp = a;
    a = b;
    b = temp;
}
```

### 範例：對調陣列

節省記憶體的方法：採用遞增法，逐一對調數字。
![[Pasted image 20211016195604.png]]
```c
void swap_int_array()
{
    int a[5] = {3, 6, 9, -8, 1};
    int b[5] = {9, 8, 7, 6, 5};
 
    // one-pass
    for (int i=0; i<5; i++)
    {
        int temp = a[i];
        a[i] = b[i];
        b[i] = temp;
    }
}
```
浪費記憶體的方法：建立一條陣列，暫存其中一條陣列。
![[Pasted image 20211016195626.png]]
```c
void swap_int_array()
{
    int a[5] = {3, 6, 9, -8, 1};
    int b[5] = {9, 8, 7, 6, 5};
 
    // multi-pass
    int temp[5];
    for (int i=0; i<5; i++) temp[i] = a[i];
    for (int i=0; i<5; i++) a[i] = b[i];
    for (int i=0; i<5; i++) b[i] = temp[i];
}
void swap_int_array()
{
    int a[5] = {3, 6, 9, -8, 1};
    int b[5] = {9, 8, 7, 6, 5};
 
    // multi-pass
    int temp[5];
    my_copy(a, temp);
    my_copy(b, a);
    my_copy(temp, b);
}
```

# Memoization

> 惟事事，乃其有備，有備無患。《書經》

「記憶法」是符合電腦運作特性的方法。電腦擁有大量儲存空間。只要將計算過的數值，儲存於記憶體，往後就能直接使用記憶體儲存的資料，不必再浪費時間重複計算一遍。

> Memoization（Tabulation）
演算法執行過程之中，即時更新數值，儲存於記憶體。
例如堆疊的大小。

> Precomputation（Precalculation）（Preprocessing）
演算法開始之時，預先計算數值，儲存於記憶體。
例如圓周率、字串的長度、質數的表格。
如果要儲存大量的、同性質的數值，我們可以將這些數值整理成一個表格（通常是陣列），以方便查閱 ── 稱作「查詢表 lookup table 」。例如質數表便是一個「查詢表」。

### 範例：陣列大小

使用一個變數，記錄資料數量，以便迅速地增加資料。
![[Pasted image 20211016195814.png]]
```c
void array_size()
{
    int array[100];
    int n = 0;      // 使用一個變數，記錄資料數量。
    array[n++] = 3; // 以便迅速地增加資料。
    array[n++] = 6;
    array[n++] = 9;
    cout << n;
}
```
C++ 程式語言的標準函式庫的 stack ，事實上也額外隱含了一個變數，記錄資料數量。當堆疊塞入資料、彈出資料的時候，也就是呼叫 push 函式、呼叫 pop 函式的時候，就默默更新資料數量。
```c
void stack_size()
{
    stack<int> s;       // C++ STL <stack>
    s.push(1);          // 默默地n++
    s.pop();            // 默默地--n
    cout << s.size();   // 把n印出來
}
```

### 範例：加總數字

利用一個變數，累計數字的總和。
![[Pasted image 20211016195855.png]]
```c
void summation()
{
    int array[5] = {3, 6, 9, -8, 1};
 
    int sum = 0;
    for (int i=0; i<5; i++)
        sum += array[i];
 
    cout << "總和是" << sum;
}
int summation(int array[], int n)
{
    int sum = 0;
    for (int i=0; i<n; i++)
        sum += array[i];
    return sum;
}
```

### 範例：統計字母數量

建立 26 格的陣列，讓字母 a 到 z 依序對應陣列的每一格，作為 lookup table 。一邊讀取字串，一邊累計字母出現次數。
![[Pasted image 20211016195921.png]]
```c 
void count_letter_frequency()
{
    char s[15] = "Hello World!";
    int c[26] = {};
 
    // 字母一律換成小寫
    for (int i=0; s[i]; i++)
        if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = s[i] - 'A' + 'a';
 
    // 統計字母數量
    for (int i=0; s[i]; i++)
        if (s[i] >= 'a' && s[i] <= 'z')
            c[s[i] - 'a']++;
 
    // 印出統計結果
    for (int i=0; i<26; i++)
        cout << char('a'+i) << ':' << c[i] << '\n';
}
UVa 10260 10082 10222 12626
```

### 範例：統計數字數量

當數字範圍太大，無法建立那麼大的陣列，可以改用 hash table 、 binary search tree 等等資料結構作為 lookup table 。
![[Pasted image 20211016195952.png]]
```c
void histogram()
{
    int array[10] =
    {
        1, 3, 4, 10, 11,
        1000000000, 23, 99, 123, 514
    };
//  int c[1000000000] = {};
    map<int, int> c;    // binary search tree
 
    // 統計數字數量
    for (int i=0; i<10; i++)
        c[array[i]]++;
 
    // 印出統計結果
    for (auto i: c)
        cout << i.first << ':' << i.second << '\n';
}
UVa 11572 141
```

### 範例：計數排序法（ Counting Sort ）

建立足夠長的陣列，讓數字對應陣列的每一格，作為 lookup table 。統計每個數字的出現次數。由小到大讀取 lookup table ，順便排序數字。
![[Pasted image 20211016200019.png]]
```c
void counting_sort()
{
    int array[5] = {3, 6, 9, 9, 1};
    int c[9 + 1] = {};
 
    // 統計數字數量
    for (int i=0; i<5; i++)
        c[array[i]]++;
 
    // 由小到大讀取lookup table，順便排序數字。
    for (int j=0, i=0; j<10 && i<5; j++)
        while (c[j] > 0)
        {
            c[j]--;
            array[i++] = j;
        }
}
```

### 範例：求 1 到 n 的全部整數的立方和， n 的範圍由 1 到 10 。
![[Pasted image 20211016200052.png]]

以直接的方式，累加每個立方數。（儘管這個問題有公式解，但是為了方便舉例，所以這裡不採用公式解。）
```c
int sum_of_cubes(int n)
{
    int sum = 0;
    for (int i=1; i<=n; i++)
        sum += i * i * i;
    return sum;
}
 
void print_sum_of_cubes()
{
    int n;
    while (cin >> n && n > 0)
        cout << sum_of_cubes(n);
}
```
使用 Memoization 。建立 11 格的陣列，每一格依序對應 0 到 10 的立方數，作為 lookup table 。一旦計算完畢，就儲存至表格；往後就直接讀取表格，不需重複計算。
```c
int sum_of_cubes(int n)
{
    // 其值為 0 表示沒有存入答案
    static int answer[10 + 1] = {};
 
    // 如果已經計算過，就直接讀取表格的答案。
    if (answer[n] != 0) return answer[n];
 
    // 如果不曾計算過，就計算一遍，儲存答案。
    int sum = 0;
    for (int i=1; i<=n; i++)
        sum += i * i * i;
    return answer[n] = sum;
}
 
void print_sum_of_cubes()
{
    int n;
    while (cin >> n && n > 0)
        cout << sum_of_cubes(n);
}
```
使用 Preprocessing 。
```c
void print_sum_of_cubes()
{
    // 預先建立立方數表格
    int cube[10 + 1];
    for (int i=1; i<=10; i++)
        cube[i] = i * i * i;
 
    int n;
    while (cin >> n && n > 0)
    {
        // 直接讀取表格的立方數
        int sum = 0;
        for (int i=1; i<=n; i++)
            sum += cube[i];
        cout << sum;
    }
}
```
Preprocessing 當然也可以直接算答案啦。
```c
int sum_of_cubes(int n)
{
    int sum = 0;
    for (int i=1; i<=n; i++)
        sum += i * i * i;
    return sum;
}
 
void print_sum_of_cubes()
{
    // 預先計算所有答案
    int answer[10 + 1];
    for (int i=1; i<=10; i++)
        answer[i] = sum_of_cubes(i);
 
    // 直接讀取表格的答案
    int n;
    while (cin >> n && n > 0)
        cout << answer[n];
}
```
最後是 Preprocessing 的極致。
```c
void print_sum_of_cubes()
{
    // 預先計算答案，寫死在程式碼裡面。
    int answer[10 + 1] =
    {
        0, 1, 9, 36, 100, 225,
        441, 784, 1296, 2025, 3025
    };
 
    // 直接讀取表格的答案
    int n;
    while (cin >> n && n > 0)
        cout << answer[n];
}
UVa 10738 10894
```

### 範例：印出方框

建立二維陣列：陣列的格子，依序對應視窗的文字。
![[Pasted image 20211016200226.png]]

不直接印出方框，而是間接填至陣列。不必數空白鍵，只需兩條水平線和兩條垂直線。
```c
void print_square_border()
{
    // 建立記憶體
    char array[5][5];
 
    // 預先填入空白鍵
    for (int i=0; i<5; i++)
        for (int j=0; j<5; j++)
            array[i][j] = ' ';
 
    // 填入方框：兩條水平線、兩條垂直線
    // 即便相互重疊也無所謂
    for (int i=0; i<5; i++) array[0][i] = '@';
    for (int i=0; i<5; i++) array[4][i] = '@';
    for (int i=0; i<5; i++) array[i][0] = '@';
    for (int i=0; i<5; i++) array[i][4] = '@';
 
    // 印出方框
    for (int i=0; i<5; i++)
    {
        for (int j=0; j<5; j++)
            cout << array[i][j];
        cout << '\n';
    }
}
UVa 105 706
```

### 範例：拆開迴圈（ Loop Unrolling ）

![[Pasted image 20211016200304.png]]
迴圈語法的功能是：一段指令，重覆實施數次，但是每次都稍微變動一點點。

事實上，我們可以反璞歸真，拆開迴圈，還原成數行指令。如此一來，就節省了迴圈每次累加變數的時間，也節省了迴圈每次判斷結束條件的時間。

拆開迴圈是一種 Preprocessing ，預先計算迴圈變量、預先計算迴圈結束條件。

拆開迴圈之後，雖然提高了程式的執行速度，但是降低了程式可讀性。程式員必須自行取捨。

# Enumeration

> 愚者千慮，必有一得。《史記》

「枚舉法」利用了電腦無與倫比的計算速度。找到不確定的變數，枚舉所有可能性，逐一判斷正確性。

> Enumerate
一筆一筆列出所有資料。
對應到程式語言的for。

> Search
瀏覽所有資料，找出需要的部份。
對應到程式語言的for加if。
收集充分資訊，就能解決問題。
![[Pasted image 20211016200419.png]]

### 範例：枚舉一百個平方數

採用直接法：依序枚舉數字 1 到 100 ；枚舉過程當中，將數字平方得到平方數。
![[Pasted image 20211016200430.png]]
```c
void generate_squares()
{
    for (int i=1; i<=100; i++)
        cout << i*i << "是平方數";
}
```
採用試誤法：依序枚舉數字 1 到 ∞ ；枚舉過程當中，判斷數字是不是平方數。
![[Pasted image 20211016200451.png]]
```c
void generate_squares()
{
    for (int i=1; i<=100*100; i++)
    {
        int sqrt_i = sqrt(i);
        if (sqrt_i * sqrt_i == i)
            cout << i << "是平方數";
    }
}
```

### 範例：尋找陣列裡的最小值

由小到大枚舉陣列索引值，逐一比較陣列元素。
![[Pasted image 20211016200545.png]]
```c
void find_minimum()
{
    int array[5] = {3, 6, 9, -8, 1};
 
    int min = 2147483647;
    for (int i=0; i<5; i++) // 枚舉索引值
        if (array[i] < min) // 比較元素
            min = array[i]; // 隨時記錄最小值
 
    cout << "最小的數字是" << min;
}
int find_minimum(int array[], int n)
{
    int min = 2147483647;
    for (int i=0; i<n; i++) // 枚舉索引值
        if (array[i] < min) // 比較元素
            min = array[i]; // 隨時記錄最小值
    return min;
}
```

### 範例：尋找陣列裡的特定數字

找到所有特定數字：瀏覽一遍所有數字。
![[Pasted image 20211016200612.png]]
```c
void find_all_number()
{
    int array[5] = {3, 6, 9, -8, 1};
 
    for (int i=0; i<5; i++) // 枚舉
        if (array[i] == 6)  // 搜尋
            cout << i << ':' << array[i] << '\n';
}
```
找到其中一個特定數字：一旦找到，立即停止瀏覽，以節省時間。
![[Pasted image 20211016200631.png]]
```c
void find_number()
{
    int array[5] = {3, 6, 9, -8, 1};
 
    for (int i=0; i<5; i++) // 枚舉
        if (array[i] == 6)  // 搜尋
        {
            cout << i << ':' << array[i];
            break;
        }
}
int find_number(int array[i], int n, int num)
{
    for (int i=0; i<n; i++)
        if (array[i] == num)
            return i;
    return -1;
}
```

### 範例：尋找二維陣列裡的特定數字

![[Pasted image 20211016200705.png]]
多個元素成為一個橫條、多個橫條成為一個陣列。內層先枚舉元素，外層再枚舉橫條，就能枚舉所有元素。

方才是由內而外、由小到大進行思考，其實也可以由外而內、由大到小進行思考：外層先枚舉每一個橫條，內層再枚舉一個橫條的每一個元素，就能枚舉所有元素。
```c
bool find_number(int n)
{
    int array[3][5] =
    {
        {3, 6, 9, -8, 1},
        {2, 4, 6, 8, 10},
        {11, 7, 5, 3, 2}
    };
 
    // 外層枚舉每一個橫條
    for (int i=0; i<3; i++)
        // 內層枚舉一個橫條的每一個元素
        for (int j=0; j<5; j++)
            // 就能枚舉所有元素
            if (array[i][j] == n)
                return true;
    return false;
}
```
此處再介紹一種特別的思考方式：第一層枚舉每一個橫條，第二層枚舉每一個直條，就能枚舉所有直條與橫條的交錯之處。

雖然前後兩個思考方式完全不同，但是前後兩支程式碼卻完全相同。
```c
bool find_number(int n)
{
    int array[3][5] =
    {
        {3, 6, 9, -8, 1},
        {2, 4, 6, 8, 0},
        {7, 5, 3, 2, 1}
    };
 
    // 第一層枚舉每一個橫條
    for (int i=0; i<3; i++)
        // 第二層枚舉每一個直條
        for (int j=0; j<5; j++)
            // 就能枚舉所有橫條與直條交錯之處
            if (array[i][j] == n)
                return true;
    return false;
}
```

### 範例：平面上距離最近的兩個點（ Closest Pair ）

![[Pasted image 20211016200752.png]]
第一層枚舉第一個點，第二層枚舉第二個點。為了避免重複枚舉相同的一對點，第二層只枚舉索引值更高的點。
```c
void closest_pair()
{
    float point[10][2] =
    {
        {3, 3}, {1, 5}, {4, 6}, {2, 8}, {9, 9},
        {2, 1}, {7, 2}, {6, 5}, {9, 4}, {5, 9}
    };
 
    // 距離最近的兩個點的距離
    float d = 1e9;
 
    // 枚舉第一點
    for (int i=0; i<10; i++)
        // 枚舉第二點
        for (int j=i+1; j<10; j++)
        {
            // 計算第一點到第二點的距離
            float dx = point[i][0] - point[j][0];
            float dy = point[i][1] - point[j][1];
            float dij = sqrt(dx * dx + dy * dy);
 
            // 記錄最短的距離
            if (dij < d) d = dij;
        }
    cout << "距離是" << d;
}
```
可以把計算距離的程式碼，抽離出來成為一個函式。好處是程式碼變得清爽許多，增加程式碼可讀性。壞處是大量呼叫函式，導致執行速度變慢。
```c
struct Point {float x, y;};
 
// 計算兩點之間的距離
float dist(Point a, Point b)
{
    float dx = a.x - b.x;
    float dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
}
 
void closest_pair()
{
    Point point[10] =
    {
        {3, 3}, {1, 5}, {4, 6}, {2, 8}, {9, 9},
        {2, 1}, {7, 2}, {6, 5}, {9, 4}, {5, 9}
    };
 
    float d = 1e9; 
    for (int i=0; i<10; i++) 
        for (int j=i+1; j<10; j++)
            // 記錄最短的距離
            d = min(d, dist(point[i], point[j]));
 
    cout << "距離是" << d;
}
```
魚與熊掌不可兼得，這兩種程式碼各有優缺點，沒有絕對的好壞。程式員必須自行取捨。

### 範例：字串搜尋（ String Searching ）

從長字串之中，找到短字串的出現位置。
![[Pasted image 20211016200843.png]]

第一層先枚舉所有可以對齊的位置，第二層再枚舉所有需要對齊的字元。
```c
void string_searching()
{
    char text[15] = "It's a pencil.";
    char pattern[6] = "a pen";
 
    // 枚舉所有可以對齊的位置
    for (int i=0; i<14; i++)
    {
        // 枚舉所有需要對齊的字元
        bool find = true;
        for (int j=0; j<5; j++)
            if (text[i+j] != pattern[j])
                find = false;
 
        if (find)
            cout << "短字串出現在第" << i << "個字元";
    }
}
```
因為短字串不會超出長字串末段，所以第一層枚舉範圍可以再略微縮小。

因為只要一個相異字元，就足以表明對齊位置錯誤，所以第二層的枚舉過程可以提早結束。
```c
void string_searching()
{
    char text[14] = "It's a pencil.";
    char pattern[6] = "a pen";
 
    // 仔細估量枚舉範圍
    for (int i=0; i<14-6+1; i++)
    {
        bool find = true;
        for (int j=0; j<5; j++)
            if (text[i+j] != pattern[j])
            {
                find = false;
                break;
            }
 
        if (find)
            cout << "短字串出現在第" << i << "個字元";
    }
}
```

### 範例：統計字母數量

![[Pasted image 20211016200927.png]]
第一層先枚舉 26 種英文字母，第二層再枚舉字串的所有字元，計算一種字母的數量。
```c
void count_letter()
{
    char s[15] = "Hello World!";
 
    // 字母統一換成小寫
    for (int i=0; s[i]; i++)
        if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = s[i] - 'A' + 'a';
 
    // 枚舉26種英文字母
    for (int i=0; i<26; i++)
    {
        // 枚舉字串的所有字元
        int c = 0;
        for (int j=0; s[j]; j++)
            if (s[j] == 'a' + i)
                c++;
 
        // 印出一種字母的數量
        cout << (char)('a' + i) << ':' << c;
    }
}
```
先前曾經介紹過統計字母數量的範例。先前範例當中，雖然耗費記憶體空間，但是執行速度快 ── 簡單來說就是空間大、時間小。此處範例當中，則是空間小，時間大，恰恰相反。這兩種方式各有優缺點，程式員必須自行取捨。

### 範例：反轉字串

![[Pasted image 20211016200957.png]]
兩個枚舉，一個從頭到尾，一個從尾到頭，步調相同，逐步對調字元。雖然是兩個枚舉，卻只有一個迴圈。
```c
void reverse_string()
{
    char s[15] = "Hello World!";
 
    // 兩個枚舉，一個從頭到尾，一個從尾到頭。
    for (int i=0, j=12; i<j; i++, j--)
        swap(s[i], s[j]);
 
    cout << "反轉之後的字串是" << s;
}
void reverse(char* s)
{
    int n = strlen(s);
    for (int i=0; i<n/2; i++)
        swap(s[i], s[n-1-i]);
}
UVa 1595
```

### 範例：尋找總和為 10 的區間

假設陣列元素只有正數。
![[Pasted image 20211016201024.png]]

兩個枚舉，枚舉區間左端以及枚舉區間右端，都是從頭到尾，保持一左一右，視情況輪流枚舉。雖然是兩個枚舉，卻只有一個迴圈。
```c
void find_interval()
{
    int array[5] = {3, 6, 1, 7, 2};
 
    int sum = 0;
    for (int i=0, j=-1; j<5; )  // 枚舉區間[i, j]
    {
        if (sum > 10)
        {
            // 總和太大，區間左端往右縮短。
            sum -= array[i];
            i++;
        }
        else if (sum < 10)
        {
            // 總和太小，區間右端往右伸長。
            j++;
            sum += array[j];
        }
        else if (sum == 10)
        {
            // 總和剛好，
            // 區間左端往右縮短，
            // 亦得區間右端往右伸長。
            // 任選一種皆可。
//          sum -= array[i];
//          i++;
            j++;
            sum += array[j];
        }
 
        if (sum == 10)
            cout << '[' << i << ',' << j << ']';
    }
}
void find_interval(int array[], int n, int num)
{
    int sum = 0;
    for (int i=0, j=0; j<=n; )  // 枚舉區間[i, j)
    {
        if (sum > num)
            sum -= array[i++];
        else
            sum += array[j++];
 
        if (sum == num)
            cout << '[' << i << ',' << j-1 << ']';
    }
}
```
讀者可以想想看：陣列元素若有零、有負數，是否要調整枚舉方式？
```
UVa 972 10464 11536 11572
```

### 範例：尋找陣列之中的最小值，陣列已經由小到大排序

找到其中一個最小值：經常整理房間，尋找東西就快；預先排序資料，搜尋速度就快。
![[Pasted image 20211016201121.png]]
```c
void find_minimum()
{
    int array[5] = {3, 3, 6, 6, 9};
    cout << "最小的數字是" << array[0];
}
```
找到所有最小值：讀者請自行嘗試。

### 範例：尋找陣列之中的特定數字，陣列已經由小到大排序

找到其中一個特定數字：首先找到陣列中央的數字，依其數字大小，繼續搜尋左半段或者右半段。
![[Pasted image 20211016201147.png]]
```c
void find_number()
{
    int array[15] =
    {
        2, 3, 5, 7, 11,
        13, 17, 19, 23, 29,
        31, 37, 41, 43, 47
    };
 
    int left = 0, right = 15-1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (array[mid] < 29)
            left = mid + 1;     // 繼續搜尋剩下的右半段
        else if (array[mid] > 29)
            right = mid - 1;    // 繼續搜尋剩下的左半段
        else if (array[mid] == 29)
        {
            // 找到了其中一個數字
            cout << mid << ':' << array[mid];
            return;
        }
    }
 
    cout << "找不到29";
}
```
找到所有特定數字：讀者請自行嘗試。

### 範例：平面上距離最近的兩個點（ Closest Pair ）

![[Pasted image 20211016201215.png]]
找到距離最近的其中一對點：預先依照 X 座標排序所有點，搜尋得以略過大量情況。
```c
struct Point {float x, y;};
 
// 計算兩點之間的距離
float dist(Point a, Point b)
{
    float dx = a.x - b.x;
    float dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
}
 
bool cmp(Point a, Point b)
{
    return a.x < b.x;
}
 
void closest_pair()
{
    Point point[10] =
    {
        {3, 3}, {1, 5}, {4, 6}, {2, 8}, {9, 9},
        {2, 1}, {7, 2}, {6, 5}, {9, 4}, {5, 9}
    };
 
    // 依照X座標排序所有點
    sort(point, point+10, cmp);
 
    float d = 1e9; 
    for (int i=0; i<N; i++)
        for (int j=i+1; j<N; j++)
        {
            // 兩個點的X座標已經相距太遠，直接略過，
            // 繼續枚舉下一個左端點。
            if (point[j].x - point[i].x > d) break;
            d = min(d, dist(point[i], point[j]));
        }
 
    cout << "距離是" << d;
}
```
找到距離最近的每一對點：讀者請自行嘗試。

### 範例：英文單字從單數變複數

枚舉各種情況，寫成大量判斷式。
![[Pasted image 20211016201246.png]]
```c
void plural(string s)
{
    int n = s.length();
    if (s.back() == 'y')
        cout << s.substr(0, n-1) << "ies";
    else if (s.back() == 's' || s.back() == 'x')
        cout << s << "es";
    else if (s.substr(n-2) == "sh" || s.substr(n-2) == "ch")
        cout << s << "es";
    else if (s.substr(n-3) == "man")
        cout << s.substr(0, n-3) << "men";
    else
        cout << s << 's';
}
```

### 範例：小畫家倒墨水（ Flood Fill Algorithm ）

電腦圖片可以想成是一張方格紙，每個方格都填著一種顏色。現在要實現小畫家倒墨水的功能：以某一格為起點，只要相鄰方格顏色一樣，就染成同一個顏色。

![[Pasted image 20211016201318.png]]
運用大量指令，枚舉上下左右四個方向；運用遞迴，枚舉相鄰同色方格。

必須避免已經枚舉過的方格又重複枚舉，否則程式在有生之年都不會結束。
```c
int image[10][10];  // 圖片的大小為 10x10
 
void flood(int x, int y, int new_color, int old_color)
{
    if (x>=0 && x<10 && y>=0 && y<10)   // 不能超出邊界
        if (image[x][y] == old_color)   // 同色方格才枚舉
        {
            // 染色
            image[x][y] = new_color;
            // 枚舉上下左右四個方向
            flood(x+1, y, new_color, old_color);
            flood(x-1, y, new_color, old_color);
            flood(x, y+1, new_color, old_color);
            flood(x, y-1, new_color, old_color);
        }
}
 
void ink()
{
    // 在座標(7,6)的方格，淋上1號顏色。
    flood(7, 6, 1, image[7][6]);
}
```
大量指令，亦得寫成一個迴圈。
```c
void flood(int x, int y, int new_color, int old_color)
{
    if (x>=0 && x<10 && y>=0 && y<10)
        if (image[x][y] == old_color)
        {
            image[x][y] = new_color;
 
            // 寫成一個迴圈
            for (int i=0; i<4; i++)
            {
                static int dx[4] = {1, -1, 0, 0};
                static int dy[4] = {0, 0, 1, -1};
                flood(x + dx[i], y + dy[i], new_color, old_color);
            }
        }
}
```
多層判斷式，亦得拆解成一層一層的判斷式。
```c
void flood(int x, int y, int new_color, int old_color)
{
    if (!(x>=0 && x<10 && y>=0 && y<10)) return;
    if (image[x][y] != old_color) return;
 
    image[x][y] = new_color;
 
    for (int i=0; i<4; i++)
    {
        static int dx[4] = {1, -1, 0, 0};
        static int dy[4] = {0, 0, 1, -1};
        flood(x + dx[i], y + dy[i], new_color, old_color);
    }
}
UVa 260 280 352 469 572 601 657 776 782 784 785 871 10267 10336 10946

ICPC 4792 5130
```

### 範例：三維函數繪圖

當問題太過困難，就增加限制，將部分變數改成常數。

一、固定 X 值，計算 Y 值 Z 值；嘗試各種 X 值。

二、固定 Y 值，計算 X 值 Z 值；嘗試各種 Y 值。

三、固定 Z 值，計算 X 值 Y 值；嘗試各種 Z 值。

![[Pasted image 20211016201430.png]]

#### Straightforward Method / Trial and Error

> 「直接法」，直接算出答案。例如按照流程進行得到答案、套用公式計算答案、直接印出答案。
```
UVa 488 10055 10370 10878 10929
```
> 「嘗試錯誤法」、「試誤法」，針對答案進行 Enumerate 與 Search 。有些困難的問題，難以直接推導答案，既然推導不出來，就慢慢測試答案、慢慢驗算吧 ── 確立答案的範圍，窮舉所有可能的答案，再從中搜尋正確答案。
```
UVa 10167 10125 296 846 714
```
直接法和試誤法剛好相反。直接法是由題目本身下手，推導答案；試誤法則是從答案下手，讓答案迎合題目需求。
![[Pasted image 20211016201548.png]]

### 範例：印出直角三角形

![[Pasted image 20211016201638.png]]
先前介紹直接法，現在介紹試誤法。

窮舉一個正方形的所有位置，一一判斷是否屬於三角形區域。
```c
void print_triangle(int n)
{
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
            if (i + j < n)
                cout << '@';
 
        cout << '\n';
    }
}
```

### 範例：印出方框

![[Pasted image 20211016201712.png]]
先前介紹直接法，現在介紹試誤法。

窮舉一個正方形的所有位置，一一判斷是否屬於方框區域。
```c
void print_square_border(int n)
{
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
            if (i == 0 || i == n-1 || j == 0 || j == n-1)
                cout << '@';
            else
                cout << ' ';
 
        cout << '\n';
    }
}
```

# Iterative Method

> 道生一，一生二，二生三，三生萬物。《老子》

繁中「疊代法」、簡中「递推法」。不斷利用目前求得的數值，再求得新數值。
```
UVa 997
```
### 範例：字串變整數

![[Pasted image 20211016201820.png]]
直覺的方式是遞增法。個、十、百、千、萬、 …… ，每個位數分別乘上 10 的次方，通通加起來。此處按照高位數到低位數的順序進行處理，以符合字串的儲存順序。
![[Pasted image 20211016201829.png]]
```c
// 計算字串長度
int string_length(char* s)
{
    int n = 0;
    while (s[n]) n++;
    return n;
}
 
// 計算10的exp次方
int pow10(int exp)
{
    int n = 1;
    for (int i=0; i<exp; i++)
        n *= 10;
    return n;
}
 
void string_to_integer()
{
    char s[10] = "26962869";
 
    // 預先計算字串長度。
    int length = string_length(s);
 
    // 依序處理高位數到低位數。
    int n = 0;
    for (int i=0; i<length; i++)
        n += (s[i] - '0') * pow10(length - 1 - i);
 
    cout << n;
}
```
更好的方式是遞推法！由高位數到低位數、也就是由左到右讀取字串，每讀取一個字元，就將數值乘以十、加上當前字元的對應數字。
![[Pasted image 20211016201852.png]]
```c
void string_to_integer()
{
    char s[10] = "26962869";
 
    int n = 0;
    for (int i=0; s[i]; i++)
        n = n * 10 + s[i] - '0';
 
    cout << n;
}
```
同一個問題，有著不同的解法。有著程式碼很長、執行速度很慢的方法，也有著程式碼很短，執行速度很快的方法。一支程式的好壞，除了取決於正確性和可讀性之外，同時也取決於計算方法。
```
UVa 759
```

### 範例：秦九韶演算法（ Horner's Rule ）

多項式函數，代入數值。一乘一加，不斷更迭，求得函數值。完全不需要次方運算。

![[Pasted image 20211016201938.png]]
### 範例：除法

不斷乘以十、除以除數，就是一種遞推。

![[Pasted image 20211016201953.png]]
### 範例：牛頓法（ Newton's Method ）

找到連續函數等於零的位置。一開始隨便設定一個位置，不斷利用斜率求出下一個位置，就是一種遞推。

Xn+1 = Xn - f(Xn) / f'(Xn)
![[Pasted image 20211016202030.png]]

### 範例： 3n+1 猜想（ Collatz Conjecture ）

猜想的內容是這樣的：有一個整數，如果是偶數，就除以 2 ；如果是奇數，就乘以 3 再加 1 。一個整數不斷這樣操作下去，最後一定會變成 1 。這個操作的過程就是一種遞推。
![[Pasted image 20211016202053.png]]

至今尚未有人能夠證明其正確性。有趣的是，目前也尚未檢查出任何反例。
```
UVa 100 371 694
```

### 範例：生命遊戲（ Cellular Automaton ）

一個二維的方格平面，每個格子都有一個細胞，可能是活的，可能是死的。細胞的生命狀況，隨時間變動，變動規則如下：

> 復活：一個死的細胞，若是它的八個鄰居，有三個細胞是活的，則在下一刻復活。
存活：一個活的細胞，若是它的八個鄰居，有兩個或三個細胞是活的，則在下一刻存活。
死於孤單：一個活的細胞，若是它的八個鄰居，只有零個或一個細胞是活的，則在下一刻死亡。
死於擁擠：一個活的細胞，若是它的八個鄰居，有四個以上的細胞是活的，則在下一刻死亡。

![[Pasted image 20211016202124.png]]
實作時，我們可以弄兩張地圖，第一張地圖儲存現在這個時刻的狀態，第二張地圖儲存下一個時刻的狀態。兩張地圖交替使用，以節省記憶體空間。

細胞的變動規則，包裝成一個函式，讓程式碼易讀。

至今尚未有人能夠預測細胞最終會滅亡或延續。
```c
void go(int x, int y, bool map1[100][100], bool map2[100][100])
{
    int n = 八個鄰居中，還活著的細胞數目;
 
    if (!map1[x][y])
        if (n == 3)                 // 復活
            map2[x][y] = true;
        else                        // 仍舊死亡
            map2[x][y] = map1[x][y];
    else
        if (n == 2 || n == 3)       // 存活
            map2[x][y] = true;
        else if (n == 0 || n == 1)  // 死於孤單
            map2[x][y] = false;
        else if (n >= 4)            // 死於擁擠
            map2[x][y] = false;
}
 
void cellular_automata()
{
    bool map[2][100][100];
 
    map[0][50][50] = true;  // 自行設定一些活的細胞
    map[0][50][51] = true;
    map[0][51][50] = true;
 
    for (int t=0; t<100; ++t)
        for (int x=0; x<100; ++x)
            for (int y=0; y<100; ++y)
                go(x, y, map[t%2], map[(t+1)%2]);
}
UVa 447 457 10443 10507
```

### 範例：蘭頓的螞蟻（ Langton's Ant ）

跟生命遊戲相似，不過這個遊戲更神奇。

> 一、格子有黑與白兩種顏色。
二、螞蟻走入白格則右轉，走入黑格則左轉。
三、螞蟻離開格子時，格子顏色顛倒。

驚人的是，乍看完全沒有規律的路線，卻在 10647 步之後開始循環。原因至今不明。
![[Pasted image 20211016202229.png]]
```
UVa 11664 ICPC 7478 7479
```

### 範例：數學歸納法（ Mathematical Induction ）

數學歸納法的第二步驟，就是證明可不可以遞推！第二步驟的證明過程中一定會用到遞推！

> 1. 先證明 n = 1 成立。（有時候不見得要從1開始。）
2. 假設 n = k 成立，證明 n = k+1 也會成立。
當 1. 2. 得證，就表示 n = 1 ... ∞ 全部都成立。

### 範例：插入排序法（ Insertion Sort ）

從表面上來看是遞增法與枚舉法：第一層是遞增法，逐一把每個數字插入到左方已排序的陣列。第二層是枚舉法，搜尋插入位置；再將大量數字往右挪，以騰出空間插入數字。

但是從另一個角度來看，利用目前排序好的陣列，再求出更長的陣列，其實就是遞推法。

![[Pasted image 20211016202415.png]]

### 範例：以試除法建立質數表

從表面上來看是兩層的枚舉法：第一層先枚舉正整數，一一試驗是否為質數；第二層再枚舉所有已知質數，一一試除。

但是從另一個角度來看，利用目前求得的質數，再求出更多質數，其實就是遞推法。

### 範例：十分逼近法

數線分割成十等份區間，從中找出正確區間，把對應的小數位數添到答案末端，然後不斷十等分下去。

利用目前求得的小數，再求出更多的小數，其實就是遞推法。
![[Pasted image 20211016202450.png]]

### 範例：書塔（ Book Stacking Problem ）

將書本一本一本疊起來，成為一座斜塔，越斜越好。
![[Pasted image 20211016202501.png]]

對於任何一本書來說，其上方所有書本的整體重心，必須落在這本書上，這本書才能平穩地支撐住上方所有書本。

將書本插入到書塔底部，讓書塔的重心落在書本邊緣，就可以讓書塔最斜。插入書本到書塔底部之後，就更新書塔的重心位置，以便稍後插入下一本書本。

不斷插入書本到書塔底部、更新書塔重心，運用先前的書塔求得新的書塔 ── 這段過程就是一種遞推。

### 範例：交卷

考試結束了，學生要交卷，老師要收卷。大家將手上的考卷，不斷傳遞給其他人，不斷匯集給老師。一個人不能同時交卷和收卷，一個人不能同時交卷給多人（搗亂），一個人不能同時向多人收卷（手忙腳亂）。假設每個人交卷速度一致，請讓整個過程越短越好。
![[Pasted image 20211016202523.png]]

每個人隨時都在收卷交卷，一定最省時。老師亦然，一直處於收卷狀態，一定最省時。

遞增的標的，選定為老師。老師每次收卷，直接複製貼上前面幾次收卷的部屬方式，是最好的 ── 這段過程就是一種遞推。

# Recursive Method

> 易有太極，是生兩儀。兩儀生四象，四象生八卦。《易傳》

繁中「遞迴法」、簡中「递归法」。重複運用相同手法，縮減問題範圍，直到釐清細節。
```
UVa 10994 10212 10471 10922
```

### 範例：碎形（ Fractal ）

利用相同手法繪圖，繪圖範圍越來越精細。

圖中的碎形稱作 Sierpinski triangle 。凡是尖端朝上的正三角形，就在當中放置一個尖端朝下的正三角形；放置之後，圖形就變得更細膩，範圍就變得更小了。
![[Pasted image 20211016202611.png]]

圖中的碎形稱作 Kosh snowflake 。一條邊三等分，去除中段，朝外補上兩段，形成尖角。
![[Pasted image 20211016202617.png]]

圖中的碎形稱作 Pythagoras tree 。不斷繪製正方形、直角三角形，看起來像是一棵茂密的樹。
![[Pasted image 20211016202630.png]]
```
UVa 177 10609
```

### 範例：質因數分解（ Integer Factorization ）

不斷抽取出質因數，使數值不斷變小，直到成為質因數。
![[Pasted image 20211016202701.png]]

### 範例： L 形磁磚

有一個邊長為 2 的 3 次方的正方形，右上角缺了一角邊長為 1 的正方形。現在要以 L 形磁磚貼滿這個缺了一角的正方形，該如何貼呢？
![[Pasted image 20211016202716.png]]

巧妙地將一塊 L 形磁磚放在中央的位置，就順利的把正方形切成四個比較小的、亦缺了一角的正方形。接下來只要遞迴處理四個小正方形，就解決問題了。

這個問題也可以改成缺口在任意一處，各位可以想想看怎麼解。
```
UVa 10230
```
### 範例：輾轉相除法（ Euclid's Algorithm ）

兩個數字輪流相除、求餘數，最後就得到最大公因數（ greatest common divisor, gcd ）。相信大家小時候都有學過。
![[Pasted image 20211016202821.png]]

我們可以把最大公因數想像成磚塊、把兩個數字都看成是最大公因數的倍數。

兩數相減所得的差值，一定是最大公因數的倍數。更進一步來說，兩數相除所得的餘數，一定是最大公因數的倍數。輾轉相除法的過程當中，兩數自始至終都是最大公因數的倍數。

運用這個性質，我們把兩數相除、求餘數，使得原始數字不斷縮小，直到得到最大公因數。真是非常巧妙的遞歸法！
```c
// 運用程式語言的迴圈語法。
int gcd(int a, int b)
{
    // 令 a 比 b 大，比較容易思考。
    while (b != 0)
    {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
// 運用程式語言的遞迴語法。
int gcd(int a, int b)
{
    // 令 a 比 b 大，比較容易思考。
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}
```
注意到，遞推法、遞歸法，不等於程式語言中的迴圈、遞迴。遞推法、遞歸法是分析問題的方法，用來得到計算過程、用來得到演算法。至於編寫程式時，我們可以自由地採用迴圈或者遞迴。

### 範例：過橋問題（ Bridge and Torch Problem ）

月黑風高的夜晚，有一座不長不短的獨木橋，只能同時容兩人併行。

此時正好有四個寂寞難耐、悲苦淒涼，事實上是窮極無聊的四個人路經此地。他們手邊僅帶著一支手電筒，想要通過這危險的獨木橋。那橋下可是暗潮洶湧，一失足成千古恨，奔流到海不復回。

幸好四人閒閒沒事就常走這座橋，對路況簡直熟悉到不行，閉著眼睛走都可以，於是乎四人知道自己過橋分別需時 1 分鐘、 2 分鐘、 5 分鐘、 10 分鐘。但是不管他們的腳程不可思議的快、莫名其妙的慢，四人都是貪生怕死之徒，要是手上沒有握著手電筒，誰都不敢過橋；四人也都是視財如命之徒，就是誰也不想浪費錢，去附近的便利商店買支手電筒，寧可摔到水裡隨波逐流環遊世界去。

最後他們只好協議說，一次兩人同時持手電筒過橋，再請其中一人送回手電筒，沒事做的人就在橋邊哭爹喊娘等手電筒回來，如此一來四人最終都能夠順利過橋。

兩人同時過橋時必須配合走得慢的人的速度，請問全員過橋最快要多久時間？

有一些規矩你是知道的，例如不能把手電筒用丟的丟過河，不能四個人疊羅漢一起過橋，不能把橋拆了做木筏之類的。
![[Pasted image 20211016202909.png]]

題目終於說完了，現在來談解題手法：

腳程快的人送手電筒回來那是最好的；相對地，腳程慢的人就應該讓他留在彼岸不要回來。不管先走後走，人人都還是要過橋，所以先試試看把腳程最慢的人送到對岸吧！

當人數眾多，至少四人時，令 A 與 B 是最快與次快， C 與 D 是次慢與最慢。讓最慢的兩個人過橋主要有兩種方式，第一種是 AB 去 A 回、 CD 去 B 回，第二種是 AD 去 A 回、 AC 去 A 回，至於其它方式所花的時間恰好跟這兩種方式一樣。採用比較快的那一種方式，讓最慢的兩個人過橋之後，問題範圍就縮小了。
```c
// 每個人的過橋時間，從小到大排序。
int a[8] = {1, 2, 5, 10, 15, 16, 30, 31};
 
void bridge_and_torch()
{
    int n, t = 0;
    for (n=8-1; n>=3; n-=2)
    {
        int t1 = a[0] + a[1]*2 + a[n];
        int t2 = a[0]*2 + a[n-1] + a[n];
        t += min(t1, t2);
    }
 
    if (n == 2) t += a[0] + a[1] + a[2];
    else if (n == 1) t += a[1];
    else t += a[0];
 
    cout << "所有人過橋的總時間為" << t;
}
```
```
UVa 10037
```

### 範例：不重複組合（ Combination ）

從 N 個人抓 M 個人出來組團，有哪些組團方式呢？
![[Pasted image 20211016202953.png]]

N 個人當中的其中一個人，叫做甲君好了。我們將所有組團方式分類成兩種情形：甲君在團中、甲君不在團中。兩種情形綜合起來就是答案。

甲君在團中：演變成剩下 N-1 個人還要抓 M-1 個人出來組團。

甲君不在團中：演變成剩下 N-1 個人仍要抓 M 個人出來組團。

兩種情形正好等同原問題，問題範圍縮小了，形成遞歸。
```c
// 累計所有組團方式
// 順帶一提，更好的做法是Dynamic Programming。
int combination(int n, int m)
{
    if (n < m) return 0;
    if (m == 0) return 1;
    return combination(n-1, m-1) + combination(n-1, m);
}
// 列出所有組團方式
// 順帶一提，更好的做法是Backtracking。
void combination(int n, int m, vector<int> group)
{
    if (n < m) return;
 
    if (m == 0)
    {
        for (int people: group)
            cout << people << ' ';
        cout << '\n';
        return;
    }
 
    // 甲君不在團中
    combination(n-1, m, group);
 
    // 甲君在團中
    group.push_back(n);
    combination(n-1, m-1, group);
}
```

### 範例：河內塔（ Tower of Hanoi ）

三根柱子、一疊盤子，盤子大小皆不同。盤子中間還得打個洞，這樣盤子才能穿在柱子上。所有盤子都疊在第一根柱子，大的在下面，小的在上面。現在要將整疊盤子移到第三根柱子。每次只能搬動一個盤子到別根柱子，而且大的盤子一定要保持在小的盤子下面。

![[Pasted image 20211016203026.png]]
想要移動最大的盤子到第三根柱子，必須先挪開上方整疊盤子到第二根柱子。移動上方整疊盤子，正好等同原問題，問題範圍縮小了，形成遞歸。

![[Pasted image 20211016203034.png]]
解題過程因而簡化成三個步驟：一、上方整疊盤子移到第二根柱子；二、最大的盤子移到第三根柱子；三、方才的整疊盤子移到第三根柱子。
![[Pasted image 20211016203041.png]]
```c
// 累計步驟數量
int tower_of_hanoi(int n)
{
    if (n == 0) return 0;
    return tower_of_hanoi(n - 1) * 2 + 1;
}
// 列出步驟過程
void move(int n, int s, int t)
{
    if (n == 0) return;
    move(n-1, s, 6-s-t);
    cout << "從" << s << "移到" << t << '\n';
    move(n-1, 6-s-t, t);
}
 
void tower_of_hanoi(int n)
{
    // 所有盤子，從第一根柱子移到第三根柱子。
    move(n, 1, 3);
}
UVa 10017
```

#### 遞推法、遞歸法，一體兩面，同時存在。

遞推法與遞歸法恰好顛倒：遞推法是針對已知，逐步累積，直至周全；遞歸法是針對未知，反覆拆解，直至精確。

遞推法是由小到大，遞歸法是由大到小。
![[Pasted image 20211016203122.png]]

### 範例：秦九韶演算法（ Horner's Rule ）

遞推法是不斷配 x ，擴增已知；遞歸法是不斷提 x ，減少未知。
```
a ⋅ x² + b ⋅ x¹ + c

Iterative Method:
{a} ⋅ x² + b ⋅ x¹ + c
{a, ⋅x} ⋅ x¹ + b ⋅ x¹ + c
{a, ⋅x, +b} ⋅ x¹ + c
{a, ⋅x, +b, ⋅x} + c
{a, ⋅x, +b, ⋅x, +c}

Recursive Method:
{a ⋅ x² + b ⋅ x¹ + c}
{a ⋅ x² + b ⋅ x¹}, +c
{a ⋅ x¹ + b}, ⋅x, +c
{a ⋅ x¹}, +b, ⋅x, +c
{a}, ⋅x, +b, ⋅x, +c
```
雖然遞推法與遞歸法的推理方向是相反的，但是遞推法與遞歸法的計算方向是一樣的，兩者都是由小範圍算到大範圍。
```
Iterative Method:
a, ⋅x, +b, ⋅x, +c

Recursive Method:
a, ⋅x, +b, ⋅x, +c
UVa 498 10268
```

### 範例：巴斯卡三角形（ Pascal's Triangle ）

不重覆組合的所有答案，排列成三角形。
![[Pasted image 20211016203224.png]]

每一格的答案，由左上格（甲君在團中）、右上格（甲君不在團中）相加而得。從上往下是遞推，從下往上是遞歸。

### 範例：爬樓梯

眼前有五階樓梯，一次只能踏一階或踏兩階，那麼爬到五階總共有哪幾種踏法？例如 (1,1,1,1,1) 是其中一種踏法， (1,2,2) 是另一種踏法。

![[Pasted image 20211016203244.png]]
這個問題可以用遞推法，也可以用遞歸法。

首先採用遞推法。試著只爬少少的幾階樓梯，觀察一下踏法。

爬到一階的踏法：很明顯的只有一種， (1) 。

爬到兩階的踏法：有兩種， (1,1) 和 (2) 。

爬到三階的踏法：因為一次只能踏一階或踏兩階，所以只可能從第一階或從第二階踏上第三階。只要綜合 ( 爬到一階的踏法 ,2) 與 ( 爬到兩階的踏法 ,1) ，就是爬到三階的踏法。

爬到四階的踏法：同理，綜合 ( 爬到兩階的踏法 ,2) 與 ( 爬到三階的踏法 ,1) 即得。

遞推下去，就可求出爬到五階的踏法。
```
Forward Iterative Method:
爬到一階　(1)
爬到兩階　(1,1) (2) 
爬到三階　即是(爬到一階,2)與(爬到二階,1)
　　　　　(1,2)
　　　　　(1,1,1) (2,1)
爬到四階　即是(爬到二階,2)與(爬到三階,1)
　　　　　(1,1,2) (2,2)
　　　　　(1,2,1) (1,1,1,1) (2,1,1)
爬到五階　即是(爬到三階,2)與(爬到四階,1)
　　　　　(1,2,2) (1,1,1,2) (2,1,2)
　　　　　(1,1,2,1) (2,2,1) (1,2,1,1) (1,1,1,1,1) (2,1,1,1)
```

前面是採用上樓梯的順序進行遞推，由第一階遞推到第五階。也可以採用下樓梯的順序進行遞推，由第五階遞推到第一階。
```
Backward Iterative Method:
降到四階　(1)
降到三階　(1,1) (2)
降到二階　即是(2,降到四階)與(1,降到三階)
　　　　　(2,1)
　　　　　(1,1,1) (1,2)
降到一階　即是(2,降到三階)與(1,降到二階)
　　　　　(2,1,1) (2,2)
　　　　　(1,2,1) (1,1,1,1) (1,1,2)
降到平面　即是(2,降到二階)與(1,降到一階)
　　　　　(2,2,1) (2,1,1,1) (2,1,2)
　　　　　(1,2,1,1) (1,2,2) (1,1,2,1) (1,1,1,1,1) (1,1,1,2)
```
有一些問題，比如爬樓梯問題，雙向都可以遞推。數值由小到大的方向稱為「正向」或「順向」（ forward ），數值由大到小的方向稱為「反向」或「逆向」（ backward ）。

接著採用遞歸法。由踏出的最後一步開始分析。

要「爬到五階」，最後一步一定是踏上第五階。要踏上第五階，只可能從第四階和第三階踏過來，也就是綜合 ( 爬到四階的踏法 ,1) 與 ( 爬到三階的踏法 ,2) 。

但是我們尚不知如何「爬到四階」和「爬到三階」，所以只好再分別研究「爬到四階」與「爬到三階」。不斷追究到「爬到一階」與「爬到兩階」的時候，就能確認答案了！
```
Forward(?) Recursive Method:
爬到五階　即是(爬到四階,1)與(爬到三階,2)
爬到四階　即是(爬到三階,1)與(爬到二階,2)
爬到三階　即是(爬到二階,1)與(爬到一階,2)
爬到兩階　(2) (1,1)
爬到一階　(1)
```

當然也可以雙向遞歸。就不贅述了。

# Greedy Method

> 今朝有酒今朝醉，明日愁來明日愁。《羅隱．自遣》

> 博觀而約取，厚積而薄發。《蘇軾．稼說送張琥》

「貪心法」。以 Incremental Method 或 Iterative Method 製造答案的方法，大致上分為兩類：

一、填答案：從沒有答案開始，逐步填滿答案。

二、改答案：先隨便弄個答案，逐步修飾答案。

觀察問題特徵，擬定一個看似最好的原則，依照原則填答案、改答案。
```
UVa 120 311 410 514 538 668 757 10148 10201 10249 10366 10382 10440 10602 10716 10718 10982 ICPC 3752 4788
```

### 範例：找零錢

你去商店買東西，你掏出了一張一百元，買了一包 23 元的零食。店員須找零錢給你，但是你希望店員找給你的硬幣數目越少越好，如此口袋會輕一點。那麼店員會給你幾個硬幣呢？

![[Pasted image 20211016203454.png]]
填答案的原則是：先找給你面額較高的硬幣。

金額越少，找給你的硬幣數目也就越少。先找給你面額較高的硬幣，金額下降的最多 ── 如此一來，往後找給你的硬幣數目就一定是最少了。

注意到：當錢幣面額很特別時，這個方法才正確。詳情請參考「 Change-Making Problem 」。

### 範例：文章換行（ Word Wrap ）

一大段的英文段落，適當的將文章換行，讓文字不超過紙張邊界，盡量節省紙張空間。
![[Pasted image 20211016203513.png]]

填答案的原則是：字儘量往前擠，擠不下就換行。

### 範例：騎士周遊問題（ Knight's Tour ）

西洋棋盤上，請找到一條路線，讓騎士恰好經過棋盤上每一格各一次。
![[Pasted image 20211016203530.png]]

填答案的原則是：走向出路選擇較少的格子。如果遇到出路選擇一樣多的格子，就走向位於下方的格子。如果又遇到一樣低的格子，就走向位於左方的格子。

![[Pasted image 20211016203539.png]]
這種填答案的方式，耗盡死路，保留活路，將來走入死胡同的機會就變少了。有一種「置之死地而後生」的味道。

注意到：這個方法不一定會成功。我們根本無法證明這個方法會成功，只是乍看起來比較容易成功。

我們當下所做的最佳決定，以長遠的眼光來看，不一定是最佳決定。儘管貪心法不見得得到正確的、最好的答案，卻是個快速得到答案的好方法。

### 範例：活動選擇問題（ Activity Selection Problem ）

暑假到了，有好多好多有趣的營隊可以參加囉！攀岩、潛水、單車環島團、吉他營、電腦營、 …… ，每個營隊都好有趣，好想每個營隊都參加 ── 可是卻有好多營隊的活動期間都互相卡到，沒辦法同時參加。到底要參加哪些營隊活動才好呢？當然是越多種越好！
![[Pasted image 20211016203609.png]]

填答案的原則很簡單：優先選擇最早結束的活動，就能剩下最多時間來安排其他活動。

仔細分成兩種情況進行討論：一、最早結束的活動，與其他活動的時間不重疊；二、最早結束的活動，與某些活動的時間重疊。

一的狀況下，參加最早結束的活動，顯然是最理想的 ── 憑空多參加了一個活動，又不耽誤到其他活動。

此觀念可以用 Recursive Method 詮釋：去除最早結束的活動、遞迴縮小問題。
![[Pasted image 20211016203620.png]]

二的狀況下，最早結束的活動、以及時間與之重疊的活動當中，只能選擇其中一個參加。此時參加最早結束的活動，得以剩下比較多的時間，仍是最理想的。

此觀念可以用 Recursive Method 詮釋：去除最早結束的活動、去除因而無法參加的活動，遞迴縮小問題。
![[Pasted image 20211016203642.png]]

填答案的原則是：所有活動按照結束時間排序，依序參加活動。如果時間允許就參加，如果時間衝突就不參加。
![[Pasted image 20211016203650.png]]
```
UVa 10020 ICPC 4328 5105
```

### 範例：函數的區域最小值

![[Pasted image 20211016203710.png]]
改答案的原則是：一開始 x 隨意設定一個數值，例如設定 x = 0 。微調 x 值，並且計算 f(x)── 如果 f(x) 減少，就更新 x ；如果 f(x) 沒減少，就不更新 x 。不斷修改 x 值，最後就到達區域最小值。

### 範例：交換相鄰數字的排序法

![[Pasted image 20211016203724.png]]
改答案的原則是：每當發現相鄰兩個數字，左邊數字大於右邊數字，兩個數字就交換位置。

不斷交換位置，導致大數字逐漸往右端移動、小數字逐漸往左端移動，最後一定能完成排序。

讀者可以想想看：交換任意兩個數字的排序法，成立嗎？

順帶一提，排序過程反向操作，可以得到一個結論：排序過的陣列，經由兩兩相鄰交換，一定可以得到各種排列方式。

### 範例：工作排程問題（ Single Machine Scheduling, Minimize the Number of Tardy Jobs ）（ 1||∑Ui ）

有一位苦命上班族，要馬上處理臨時指派的 N 份工作。經驗老到的他，馬上就精準的估計出每份工作各要花掉多少時間，可是每份工作都有不同的完工期限，這造成有些工作可能會來不及完成。他做事專心，要求品質，一次只處理一份工作，一份一份接著做；來不及完成的工作，乾脆放棄不做。

請找出一種排程，讓如期完成的工作最多（也就是讓逾期完成的工作最少），順便讓總工時越短越好。
![[Pasted image 20211016203746.png]]

合理排程之相鄰交換性質：

一個合理排程，其中某兩個如期完成的工作 A 與 B ， A 與 B 緊鄰完成， A 早做 B 晚做， A 期限晚 B 期限早（或期限相同），則 A 與 B 對調位置之後，仍是一個合理排程。分析如下：
```
A與B視作一體進行交換：排程裡的其他工作皆不受影響。
A放到B的位置：A的期限比B還晚，B都能如期完成了，所以A也能如期完成。
B放到A的位置：B提早做，更能如期完成。
```
一個合理排程，不斷地進行相鄰交換，終會形成「工作依照期限排序」的合理排程！反之亦然！小心，不相鄰則不可貿然交換。

因此，我們只需著眼於「工作依照期限排序」的合理排程。
```
UVa 10026 11389
```
填答案的原則是：所有工作依照期限排序，依序加入排程。一次加入一個工作，一旦發現逾期，立即從排程當中抽掉工時最長的工作。
![[Pasted image 20211016203817.png]]
```
已經加入N個工作，排程裡有M個工作。
排程裡的工作，是前N個工作的最佳解。也就是說：
α. 這M個工作，全部如期完成。
β. 前N個工作之中，如期完成的工作數量最多就是M。
γ. 前N個工作之中，這M個工作總工時最短。
```

以數學歸納法證明之。假設 N 成立，當第 N+1 個工作加入排程，有兩種情況。

一、沒有發生逾期：

這 M 個工作，本來就是如期完成、工作數量最多、總工時最短的最佳選擇。第 N+1 個工作加入之後， αβγ 依然成立。

二、發生逾期，立即抽出工時最長的工作：

這 M 個工作，已經能如期完成。抽出工時最長的工作，補上工時稍短（或相等）的第 N+1 個工作，更能如期完成了。 α 成立。

這 M 個工作，總工時已經是最短了，還是無法添加第 N+1 個工作，不得已抽掉一個工作，工作數量已經盡量多了。 β 成立。

抽出工時最長的工作，總工時下降最多。 γ 成立。
```c
struct Job {int time, due;} job[10];
priority_queue<int> pq;
 
bool cmp(Job a, Job b)
{
    return a.due < b.due;
}
 
void Moore_Hodgson()
{
    sort(job, job+10, cmp);
 
    int t = 0;
    for (int i=0; i<10; i++)
    {
        pq.push(job[i].time);
        t += job[i].time;
        if (t > job[i].due) t -= pq.top(), pq.pop();
    }
 
    cout << "如期完成的工作數量，最多為" << pq.size();
    cout << "逾期完成的工作數量，至少為" << 10 - pq.size();
}
struct Job {int time, due;} job[10];
 
bool operator<(Job a, Job b)
{
    return a.due < b.due;
}
 
int heap[10], size = 0;
 
void Moore_Hodgson()
{
    sort(t, t+10);
 
    int t = 0;
    for (int i=0; i<10; i++)
    {
        heap[size++] = job[i].time;
        push_heap(heap, heap+size);
        t += job[i].time;
 
        if (t > job[i].due)
        {
            t -= heap[0];
            pop_heap(heap, heap+size);
            size--;
        }
    }
 
    cout << "如期完成的工作數量，最多為" << size;
    cout << "逾期完成的工作數量，至少為" << 10 - size;
}
UVa 10154 ICPC 3277 4850 8046
```

### 範例：工作排程問題（ 2-Machine Flowshop Scheduling ）（ F2||Cmax ）

兩台機器， N 份工作，一台機器一次只能處理一個工作。每份工作必須先經過初號機處理一段時間，再經過貳號機處理一段時間，才算處理完畢。

請找出一種排程，迅速完成所有工作。
![[Pasted image 20211016203905.png]]
```
1. 建立兩個空的List，叫做L1和L2。
2. 從N個工作、2N個工時當中，不斷挑出工時最短的工作。
   如果最短工時是初號機的工時，該工作加到L1前端。
   如果最短工時是貳號機的工時，該工作加到L2後端。
3. L1 L2，即是排程。
1. 建立兩個空的List，叫做L1和L2。
2. 對每一個工作，若初號機工時小於貳號機工時，該工作加到L1，反之則加到L2。
3. L1照初號機工時由小到大排序。
   L2照貳號機工時由大到小排序。
4. L1 L2，即是排程。
```
```c
int c1[10];
int c2[10];
 
bool cmp1(int i, int j) {return c1[i] < c1[j];}
bool cmp2(int i, int j) {return c2[i] > c2[j];}
 
void Johnson()
{
    vector<int> l1, l2;
    for (int i=0; i<10; i++)
        if (c1[i] < c2[i])
            l1.push_back(i);
        else
            l2.push_back(i);
 
    sort(l1.begin(), l1.end(), cmp1);
    sort(l2.begin(), l2.end(), cmp2);
 
    vector l = l1 + l2;
    int t1 = 0, t2 = 0;
    for (int i=0; i<l.size(); i++)
    {
        t1 += c1[l[i]];
        t2 = max(t1, t2) + c2[l[i]];
    }
    cout << "總完成時間為" << t2 << endl;
}
UVa 11269 11729
```

### 範例：平面上距離最近的兩個點（ Closest Pair ）

採用遞增法，逐次增加一個點；採用枚舉法，計算新點到其他點的距離。每當發現更近的兩個點，下次即可減少橫向搜尋範圍。

運用目前得到的答案，藉此得到更好的答案！可以看作是間接地、改答案的原則。
![[Pasted image 20211016203947.png]]

另外，還可以減少縱向搜尋範圍。除了新點以外，兩點之間的距離，至少都是上次的最短距離，不能太密太擠。在橫向搜尋範圍之內，進行縱向排序（採用即時排序的資料結構，效率較佳），只需檢查新點的上兩點、下兩點，就一定能檢查到半圓內所有點！

儘管無法直接得到正確的點，但是只需檢查少數幾點！可以看作是間接地、填答案的原則。
![[Pasted image 20211016203956.png]]
```
UVa 10245 ICPC 7581
```

# Divide-and-Conquer Method

> 凡治眾如治寡，分數是也。鬥眾如鬥寡，形名是也。《孫子》

「分治法」，分割問題、各個擊破。將一個大問題，分割成許多小問題。如果小問題還是很難，就繼續分割成更小的問題，直到問題變得容易解決。

分割出來的小問題，稱作「子問題 subproblem 」。解決一個問題，等價於解決所有子問題。

用樹狀圖表達原問題與子問題的關係，最好不過！
![[Pasted image 20211016204040.png]]

分治法著重分割問題的方式 ── 要怎麼分割問題，使得子問題簡單又好算？各位讀者可以藉由本文的範例，體會分割問題的方式。

### 範例：分解動作

想要學習「從中場帶球上籃」，我們可以將此動作分割為「跑步運球」、「跑步收球」、「單手將球放入籃框」等動作，分別學習。每一項動作都熟練之後，組合起來便是帶球上籃了。

如果覺得「跑步運球」還是太難，可以更細分成「原地運球」、「走動運球」、「運球時護球」等動作，克服了之後便能夠順利解決「跑步運球」的問題了。
![[Pasted image 20211016204110.png]]

### 範例：方格法求面積

左邊為原問題，右邊放大並細分的圖是其中一個子問題。
![[Pasted image 20211016204141.png]]

### 範例：分類數數

左邊最大的框框是原問題，將原問題的數字進行分類後再統計，分類後的每一個框框都是一個子問題。
![[Pasted image 20211016204206.png]]
```
UVa 11038
```

#### Recursive Method

在分治法當中，亦得遞迴地分割問題，其實就是遞歸法。

![[Pasted image 20211016204239.png]]
程式碼細分為三個階段： Divide 、 Conquer 、 Combine 。 Divide 階段是把原問題分割成小問題， Conquer 階段是解決小問題， Combine 階段是運用小問題的解答，整理出原問題的解答。
![[Pasted image 20211016204247.png]]
```c
divide_and_conquer(原問題)
{
    /* Divide */
    先將原問題分割成許多小問題;
 
    /* Conquer */
    遞迴呼叫函式，求得子問題的解;
    解答1 = divide_and_conquer(子問題1);
    解答2 = divide_and_conquer(子問題2);
    ......
 
    /* Combine */
    用小問題的解答，算出原問題的解答;
    原問題解答 = 解答1 + 解答2 + ......;
 
    return 原問題解答;
}
UVa 620 10101 10144 10998
```

### 範例：合併排序法（ Merge Sort ）

![[Pasted image 20211016204315.png]]
Divide 階段：資料分割成兩堆。

Conquer 階段：兩堆資料各自從事 Merge Sort 。

Combine 階段：兩堆已排序過的資料，合併成一堆。
```c
void merge(int array[], int left, int right, int mid)
{
    int n = right - left + 1;
    int* x = new int[n];
 
    int i = left, j = mid + 1;
    for (int k=0; k<n; k++)
    {
        if      (i == mid + 1)         x[k] = array[j++];
        else if (j == right + 1)       x[k] = array[i++];
        else if (array[i] <= array[j]) x[k] = array[i++];
        else                           x[k] = array[j++];
    }
 
    for (int k=0; k<n; k++)
        array[left + k] = x[k];
    delete[] x;
}
 
void merge_sort(int array[], int left, int right)
{
    if (left >= right) return;
 
    /* Divide */
    int mid = left + (right - left) / 2;
 
    /* Conquer */
    merge_sort(array, left, mid);
    merge_sort(array, mid+1, right);
 
    /* Combine */
    merge(array, left, right, mid);
}
 
void merge_sort(int array[], int n)
{
    merge_sort(array, 0, n-1);
}
```

### 範例：快速排序法（ Quicksort ）

![[Pasted image 20211016204348.png]]
Divide 階段：任意挑選一個數字當作基準（例如最右端），把資料分割成左右兩堆。左堆數字小於等於基準，右堆數字大於基準。

Conquer 階段：左右兩堆資料各自從事 Quicksort 。

Combine 階段：不做任何事。
```c
int partition(int array[], int left, int right)
{
    int pivot = array[right];   // 基準
 
    int i = left;
    for (int j = left; j < right; ++j)
        if (array[j] <= pivot)
        {
            swap(array[i], array[j]);
            i++;
        }
 
    swap(array[i], array[right]);
    return i;   // pivot的位置
}
 
void quicksort(int array[], int left, int right)
{
    if (left >= right) return;
 
    /* Divide */
    int k = partition(array, left, right);
 
    /* Conquer */
    quicksort(array, left, k-1);    // 左堆
    quicksort(array, k+1, right);   // 右堆
 
    /* Combine */
}
 
void quicksort(int array[], int n)
{
    quicksort(array, 0, n-1);
}
```

#### Prune-and-Search Method

「修剪搜尋法」是分治法的特例。去除不重要的子問題，只搜尋重要的子問題。
![[Pasted image 20211016204428.png]]
```
UVa 920
```

### 範例：二分搜尋法（ Binary Search ）
![[Pasted image 20211016204448.png]]

在已排序陣列裡面，尋找特定數字。

陣列由中央切成兩邊，一邊數字較小、一邊數字較大。這兩邊一定有一邊不是我們所要的，可以去除，只需要繼續尋找其中一邊。
```c
int binary_search(int array[], int n, int key)
{
    int left = 0, right = n-1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if      (array[mid] < key)  left = mid + 1;
        else if (array[mid] > key)  right = mid - 1;
        else if (array[mid] == key) return mid;
    }
    return -1;  // 找不到
}
UVa 10077
```

### 範例：快速選擇法（ Quickselect ）

![[Pasted image 20211016204516.png]]
在未排序陣列裡面，尋找第 k 小數字。

運用 Quicksort 的分割手法，把陣列切成兩邊，一邊數字較小、一邊數字較大。這兩邊一定有一邊不是我們所要的，可以去除，只需要繼續尋找其中一邊。
```c
int quickselect(int array[], int n, int k)
{
    int left = 0, right = n-1;
    while (left <= right)
    {
        int i = partition(array, left, right);
        if      (k < i)  right = i - 1;
        else if (k > i)  left = i + 1;
        else if (k == i) return array[i];
    }
    return -1;  // 找不到
}
```

### 範例：尋找假幣（ Counterfeit Coin Problem ）

一堆硬幣，當中一枚硬幣是假幣，重量比真幣輕，肉眼無法分辨差異。手邊的工具僅有一台天平，但沒有砝碼，該如何藉由天平判斷假幣？

當硬幣總數為一，那麼該幣就是假幣。當硬幣總數為二，則兩枚硬幣分別放在天平兩端秤重，較輕的一端就是假幣。當硬幣總數為三以上，一定有辦法找出假幣，以下介紹兩種策略。

採用遞增法。每次取兩枚硬幣，放在天平兩端秤重。當天平平衡，表示這兩枚硬幣都是真幣，接著繼續處理剩餘硬幣。當天平傾斜，比較輕的硬幣就是假幣。
![[Pasted image 20211016204545.png]]

採用分治法。兩枚硬幣放在天平兩端秤重，當天平平衡，表示這兩枚硬幣都是真幣。接著只剩下 N-2 枚硬幣要尋找假幣 ── 問題遞迴縮小了！

剩下 N-2 枚，太多了一點。一次取多一點硬幣，同時放在天平兩端秤，問題就能縮小更多了！

把所有硬幣平均分成三份，取兩份放在天平兩端秤重。當天平平衡，表示剩下的一份含有假幣，問題一次便縮小為 1/3 。當天平傾斜，表示比較輕的一份含有假幣，問題一次便縮小為 1/3 。
![[Pasted image 20211016204556.png]]

讀者可以想想看：如果硬幣數量不是三的倍數怎麼辦？如果一開始不知道假幣與真幣孰輕孰重怎麼辦？
```
UVa 12732 12733
```

# Scaling Algorithm

> 古之欲明明德於天下者，先治其國。　　　　
欲治其國者，先齊其家。　　　　
欲齊其家者，先修其身。　　　　
欲修其身者，先正其心。《禮記》

「縮放演算法」。將數值拆解為不同數量級，每個數量級分別計算一次答案，並且累計每次計算成果。

### 範例：乘法

數量級從小到大：乘數拆解為不同數量級，先以個位數相乘一次，再以十位數相乘一次， …… ，再以最高位數相乘一次，累加起來，得到正確結果。
![[Pasted image 20211016204704.png]]

### 範例：基數排序法（ Radix Sort ）

數量級從小到大：所有數字先以個位數排序一次，再以十位數排序一次， …… ，再以最高位數排序一次，得到正確結果。
![[Pasted image 20211016204725.png]]

數量級從大到小：所有數字先以最高位數排序一次，再以前兩高位數排序一次， …… ，再以全部位數排序一次，得到正確結果。
![[Pasted image 20211016204735.png]]

改善計數排序法的效率，不必建立一長串陣列。

### 範例：多重解析度字串搜尋（ Multiscale String Searching ）

從宏觀到微觀，從粗糙到細膩。短字串跳 N 格實施比對。若足夠相似，才跳 N/2 格實施比對。 …… 。若足夠相似，才跳 1 格實施比對。
![[Pasted image 20211016204753.png]]

改善字串搜尋的效率，不必每次都比對一大串字元。

### 範例： Shell 排序法（ Shell Sort ）

從宏觀到微觀，從粗糙到細膩。跳 N 個數字為同一組，每組分別實施插入排序法。跳 N/2 個數字為同一組，各組分別實施插入排序法。 …… 。跳 1 個數字為同一組，所有數字實施插入排序法。
![[Pasted image 20211016204809.png]]

改善插入排序法的效率，不必每次都挪動一大串數字。

# External Memory Algorithm

> 士農工商四民者，國之石，民也。　　　　　　
不可使雜處，雜處則其言哤，其事亂。《管子》

儲存容量大，存取時間長；儲存容量小，存取時間短。魚與熊掌不可兼得。自然而然形成階層架構：暫存器、快取、記憶體、硬碟，儲存容量越來越大，存取時間越來越久。

需要計算的變數，儲存在暫存器；不在暫存器，就找快取；不在快取，就找記憶體；不在記憶體，就找硬碟。

簡中譯作寄存器、缓存、内存、硬盘。
![[Pasted image 20211016204841.png]]

對中央處理器來說，最花時間的動作，不是運算，而是從記憶體讀入資料到快取、從快取寫出資料到記憶體。

每當變數不在快取，就從記憶體載入資料到快取，載入變數所在的那一個區塊。區塊大小等於通道容量，區塊位置似乎固定不變。
![[Pasted image 20211016204855.png]]

「快取無視演算法」目的是減少載入次數。實際的通道容量、快取容量，端看硬體規格，無法預知。我們只能盡量集中變數，以減少載入次數。

「快取無視演算法」的名稱由來是：考慮記憶體與快取，但是不知道通道容量、快取容量。以現代眼光來看，顯然詞不達意。

### 範例：陣列與串列

陣列在記憶體裡是連續的。串列在記憶體裡通常不是連續的。
![[Pasted image 20211016204913.png]]

枚舉陣列元素，偶爾載入區塊，不會重複載入，速度快。
![[Pasted image 20211016204921.png]]

枚舉串列元素，經常載入區塊，甚至重複載入，速度慢。
![[Pasted image 20211016204932.png]]

### 範例：變數型態

int = 4 byte ， short = 2 byte ，雖然儲存空間不一樣大，但是加法運算卻一樣快，都是一單位時間。

雖然兩數加法一樣快，但是多數總和就不一樣快。 short array 空間小，區塊少，速度快。
![[Pasted image 20211016204950.png]]
```c
short sum(short array[1000])
{
    // short array，空間小，區塊少，速度快。
    short n = 0;
    for (int i=0; i<1000; i++)
        n += array[i];
    return n;
}
int sum(int array[1000])
{
    // int array，空間大，區塊多，速度慢。
    int n = 0;
    for (int i=0; i<1000; i++)
        n += array[i];
    return n;
}
```

### 範例：二維陣列的總和

依序枚舉二維陣列的所有元素，累計總和。
![[Pasted image 20211016205008.png]]

枚舉橫條元素，偶爾載入區塊，不會重複載入，速度快。

枚舉直條元素，經常載入區塊，甚至重複載入，速度慢。
```c
int sum(int array[1000][1000])
{
    // 橫條為主，速度快。
    // 外層枚舉每一個橫條，內層枚舉一個橫條的每一個元素。
    int n = 0;
    for (int i=0; i<1000; i++)
        for (int j=0; j<1000; j++)
            n += array[i][j];
    return n;
}
int sum(int array[1000][1000])
{
    // 直條為主，速度慢。
    // 外層枚舉每一個直條，內層枚舉一個直條的每一個元素。
    int n = 0;
    for (int j=0; j<1000; j++)
        for (int i=0; i<1000; i++)
            n += array[i][j];
    return n;
}
```

### 範例：小畫家倒墨水（ Flood Fill Algorithm ）

建立二維陣列，一一對應盤面格子。區塊形成橫條。一個格子，左右通常是相同區塊，上下通常是不同區塊。墨水填充過程，經常載入區塊。

建立一維陣列，重新對應盤面格子。區塊從橫條變方塊，減少載入次數。
![[Pasted image 20211016205047.png]]

想要改變區塊形狀，就要改變陣列索引值與盤面格子的對應。
![[Pasted image 20211016205053.png]]

#### External Memory Algorithm

方才討論了快取與記憶體的讀寫。「外部記憶體演算法」則是考慮記憶體與硬碟的讀寫。

實務上，硬碟也可以是光碟、隨身碟、雲碟。簡中譯作光盘、闪存盘、云盘。

### 範例：動態陣列（ Dynamic Array ）

![[Pasted image 20211016205121.png]]
不知資料多寡，只好準備一塊記憶體空間，暫存資料。每當空間滿了，才擴充空間。

C++ 程式語言的標準函式庫的 vector ，即是動態陣列。
```c
void dynamic_array()
{
    vector<int> v;
    v.push(3);
    v.push(6);
    v.push(9);
    v.push(-8);
    v.push(1);
}
```

### 範例：緩衝區（ Buffer ）

![[Pasted image 20211016205208.png]]
不知資料生成時刻，只好準備一塊記憶體空間，暫存資料。每當資料夠了，才處理資料。

printf/scanf 、 cin/cout ，內含緩衝區。
```c
void print()
{
    printf("It's a pencil.");
    flush(stdout);          // 立即清空緩衝區
    setbuf(stdout, NULL);   // 不使用緩衝區
 
    cout << "It's a pencil.";
    cout << flush;          // 立即清空緩衝區
    cout << endl;           // 等同 cout << '\n' << flush;
    cout.unitbuf();         // 每次都清空緩衝區（不使用緩衝區）
};
```

### 範例：合併排序法（ Merge Sort ）

排序硬碟資料。

一、資料分段排序：每段資料符合記憶體容量，假設分成了 k 段。 k 段資料分別讀入、排序、寫出。
![[Pasted image 20211016205234.png]]

二、資料合併排序：記憶體配置 k 塊輸入、 1 塊輸出緩衝區。 k 段資料合併成排序資料。
![[Pasted image 20211016205242.png]]

在步驟一，當資料分段太多，則遞迴處理。
![[Pasted image 20211016205249.png]]

### 範例：桶子排序法（ Bucket Sort ）

排序硬碟資料。

![[Pasted image 20211016205309.png]]
一、資料分類排序：記憶體配置 1 塊輸入、 k 塊輸出緩衝區。一段資料分散於 k 個桶子，依照數字大小。

二、資料分段排序： k 段資料分別讀入、排序、寫出。

在步驟二，當一段資料太長，則遞迴處理。

### 範例：選擇排序法暨二分搜尋法（ Selection Sort & Binary Search ）

不排序硬碟資料，不使用其他硬碟空間，直接輸出排序結果。
![[Pasted image 20211016205324.png]]

篩選最小的數字們、排序、輸出。以二分搜尋法，調整篩選範圍。如果硬碟未讀完、緩衝區已滿溢，則減少篩選範圍，重新來過；如果硬碟已讀完，緩衝區未滿溢，則排序、輸出、更新篩選範圍。

小心處理同一數字數量非常多的情況。
```c
int MIN = -1000000000;  // 數字的最小值
int MAX = +1000000000;  // 數字的最大值
const int M = (1 << 18);
const int N = (1 << 19);
int in[M];              // 篩選前的數字
int out[N];             // 篩選後的數字
 
// 讀取檔案裡面所有數字，篩選大於等於L、小於等於R的數字。
int read(ifstream& fin, int L, int R)
{
    int n = 0;
    fin.clear();            // 回復讀寫狀態
    fin.seekg(0, fin.beg);  // 回到檔案開頭
 
    while (true)
    {
        // 讀取檔案裡面的數字
        fin.read((char*)in, sizeof(int)*M);
        int c = fin.gcount() / sizeof(int);
        if (c <= 0) break;  // 沒有數字就結束
 
        // 篩選數字
        for (int i = 0; i < c; i++)
            if (in[i] >= L && in[i] <= R)
                if (L == R)
                {
                    if (n < N) out[n++] = in[i];
                    else n++;   // 同一數字出現許多次
                }
                else
                {
                    if (n < N) out[n++] = in[i];
                    else return -1; // 存不下
                }
    }
    return n;
}
 
// 選擇排序法暨二分搜尋法
// 屢次從檔案裡面篩選最小的數字們、排序、輸出。
// 如果記憶體滿溢，則將篩選範圍減半，重新來過。
void sort_file()
{
    ifstream fin("number.in", ios::binary);
    ofstream fout("number.out", ios::binary);
 
    // 選擇排序法暨二分搜尋法
    for (int L = MIN, R = MAX; L <= R; )
    {
        int M = (L + R) / 2;
        int n = read(fin, L, M);
 
        if (n < 0)          // 記憶體滿溢。篩選範圍減半。
            R = M;
        else if (n == 0)    // 查無數字。處理另一半範圍。
            L = M + 1;
        else                // 記憶體未滿溢。排序。輸出。
        {
            if (L == M)
            {
                for ( ; n > N; n -= N)
                    fout.write((char*)out, sizeof(int)*N);
                if (n > 0)
                    fout.write((char*)out, sizeof(int)*n);
            }
            else
            {
                sort(out, out + n);
                fout.write((char*)out, sizeof(int)*n);
            }
 
            // 處理其餘範圍
            L = M + 1;
            R = MAX;
        }
    }
 
    fin.close();
    fout.close();
}
```

# Parallel Algorithm
（ Under Construction! ）

> 眾心成城，眾口鑠金。《國語》

「循序 Sequential 」就是逐一計算，「平行 Parallel 」就是一齊計算，兩者是相對概念。

「平行演算法」。當計算順序無所謂時，就可以使用多個計算器一齊計算。優點是減少計算時間，缺點是增加硬體、增加電力。

計算器有兩種類型：多個計算器只能一齊執行相同指令（例如 GPU ），多個計算器可以分頭執行不同指令（例如多核心 CPU ）。前者富含巧思，後者缺乏變化，所以我們只談前者。

```
kernel launch overhead
shared memory bank conflicts
branch divergence overhead
```

因為作業系統建立執行緒需要大量時間與空間，所以平行計算不一定比循序計算好。程式員必須自行取捨。

一份記憶體一齊傳遞資料給各個計算器，多個計算器一齊計算，多個計算器一齊傳遞資料給一份記憶體。


### 範例：複製字串

理論：各個字元分頭複製，時間複雜度從 O(N) 變 O(1) 。


實務：字串切成數段，分頭複製。

```c
void copy()
{
    char s[15] = "incremental";
    char t[15];
 
    int i;
    #pragma omp parallel for
    for (i=0; s[i]; i++)
        t[i] = s[i];
    t[i] = '\0';
 
    cout << "原本字串" << s;
    cout << "複製之後的字串" << t;
}
```

### 範例：加總數字

理論：數字雙雙相加，時間複雜度從 O(N) 變 O(logN) 。


實務：陣列切成數段，分頭計算總和。最後累加各段總和。

```c
void summation()
{
    int array[5] = {3, 6, 9, -8, 1};
 
    // 陣列切成兩段，分頭計算總和。
    int sum = 0;
    #pragma omp parallel for num_thread(2) schedule(static) reduction(+:sum)
    for (int i=0; i<5; i++)
        sum = sum + array[i];
 
    cout << "總和是" << sum;
}
```

### 範例：矩陣相乘

理論：簡單起見，討論 N×N 方陣。兩層的平行化，外層是乘積矩陣的每一個元素，內層是兩串數列相乘，時間複雜度從 O(N³) 變 O(1) 。

實務：執行緒數量高達 O(N³) ，不但跟循序計算沒兩樣，而且還得額外浪費設置執行緒的時間與空間，弄巧成拙、過猶不及。只平行化每一個元素，放棄平行化數列相乘。

```c
void matrix_multiply(float A[N*N], float B[N*N], float C[N*N])
{
    int i, j, k;
    #pragma omp parallel for collapse(2) private(k)
    for (i=0; i<N; i++)
        for (j=0; j<N; j++) 
        {
            // 放棄數列相乘的平行化
            for (k=0; k<N; k++)
                C[N*i+j] += A[N*i+k] * B[N*k+j];
        }
}
```
相同資料重複傳遞很多份到各個執行緒，改為每次計算一塊區域。

```c
const int N, P, M;      // matrix dimensions
float A[N*P], B[P*M], C[N*M];
int NB = 0;             // number of blocks
int Nb = N / NB;        // block dimensions
int Pb = P / NB;
int Mb = M / NB;
 
void clear_block(float* C, int gapC, int Nb, int Mb)
{
    for (int i=0; i<Nb; i++) 
        for (int j=0; j<Mb; j++)
            // C[i][j] = 0;
            C[i * gapC + j] = 0.0;
}
 
void multiply_block(float* A, float* B, float* C, int gapA, int gapB, int gapC)
{
    for (int i=0; i<N; i++)
        for (int j=0; j<M; j++)
        {
            // C[i][j] += A[i][k] * B[k][j];
            float t = C[i*gapC + j];
            for (int k=0; k<P; k++)
                t += A[i*gapA + k] * B[k*gapB + j];
            C[i*gapC + j] = t;
        }
}
 
void matrix_multiply()
{
    int ib, jb, kb;
    #pragma omp parallel for private(jb,kb) schedule(static)
    for (ib=0; ib<NB; ib++)
        for (jb=0; jb<NB; jb++)
        {
            // Cb[ib][jb] = 0;
            float* ptrC = C + ib * Nb * M + jb * Mb;
            clear_block(ptrC, M, Nb, Mb);
 
            // Cb[ib][jb] = Ab[ib][kb] * Bb[kb][jb];
            for (kb=0; kb<NB; kb++)
                multiply_block(
                    A + ib * Nb * P + kb * Pb,
                    B + kb * Pb * M + jb * Mb,
                    ptrC,
                    P, M, M
                );
        }
}
```

### 範例：生命遊戲

理論：兩層的平行化，外層是地圖的每一個細胞，內層是八個鄰居細胞數量總和，時間複雜度從 O(XY⋅8) 變 O(log8) 。

實務：只平行化每一個細胞，放棄平行化細胞求和。


### 範例： Hamilton Path

理論：如果能夠建立 N! 個執行緒，時間複雜度就從 O(N!) 變 O(N)── 可是要去哪裡生那麼多個執行緒？即便是平行化也無法快速解決 NP-complete 問題。


#### Distributed Algorithm

「分散式演算法」。 Parallel Algorithm 和 External Memory Algorithm 合體。

https://paper.dropbox.com/doc/Google-DCJ--MnMwtOSSmcM4ZaEzFOpNF

### 範例：哲學家用餐問題（ Dining Philosophers Problem ）

資源控管。

Paxos 。

### 範例：多工（ Multiplexing ）

通道控管。

CSMA

https://www.zhihu.com/question/26743389/answer/33983737

### 範例：共時（ Clock Synchronization ）

時間同步。

CAP theorem: Consistence, Availability, Partition Tolerance.

https://en.wikipedia.org/wiki/Clock_synchronization

### 範例：尚無正式翻譯（ Sketching ）

分配律。協作。

### 範例：尚無正式翻譯（ Placement ）

排程。


# Randomized Algorithm

> 有過物者必濟，故受之以既濟。《易傳》

> 致中和，天地位焉，萬物育焉。《禮記》

「隨機化演算法」。隨便的計算數值、計算順序。難得糊塗。

### 範例：隨機數字（ Random Number ）

隨機數字又稱亂數。亂七八糟、毫無章法、什麼都有可能。
![[Pasted image 20211016205747.png]]

如何製造亂數呢？沒人知道！數學家尚未釐清「亂」是什麼。計算學家則創造了形形色色的算式，偽造亂數，聊勝於無。

簡易算式：乘上一數、加上一數，遞推下去。
```c
int rand()
{
    // 使用unsigned int，即便溢位也不會當機。
    static unsigned int seed = 0;
    // 乘上一數、加上一數。
    seed = seed * 1103515245U + 12345U;
    // 符合int上限範圍，得到[0, 2³¹-1]之間的亂數。
    return int(seed % 2147483648U);
}
```
C 程式語言的內建函式庫，已經有亂數了。
```c
void random_number()
{
    // 設定亂數表，之後才能使用rand()。
    srand(time(0));
 
    // 印出10個亂數，範圍是整數0到整數4。
    for (int i=0; i<10; i++)
        cout << rand() % 5;
}
```

### 範例：雜湊函數（ Hash Function ）

一種特別的函數：數字變成特定範圍數字。
![[Pasted image 20211016205833.png]]

雜湊函數應用廣泛，衍生許多變化，其中一種經典變化是：數字變成特定範圍亂數。隨便導致分散 ── 亂數四散，不會太集中。
```c
int hash(int num, int range)
{
    // 以給定的資料，製造一個亂數，位於[0, range-1]。
    unsigned int hash = num;    // num是負數也沒關係
    hash = hash * 1103515245U + 12345U;
    return int(hash % 2147483648U) % range;
}
```
C++ 程式語言的內建函式庫，已經有雜湊函數了，但是不是亂數版本。不會變成亂數，而是變成原本數字，喜感十足。
```c
void hash_function()
{
    // 印出數字0到9的雜湊值，位於[0, 2³¹-1]。
    hash<int> int_hash;
    for (int i=0; i<10; i++)
        cout << int_hash(i);
 
    // 印出數字0到9的雜湊值，位於[0, 2³¹-1]。
    for (int i=0; i<10; i++)
        cout << hash<int>{}(i);
}
```

### 範例：雜湊表（ Hash Table ）

以簡短陣列儲存資料，以雜湊函數決定儲存位置。隨便導致分散 ── 資料四散，不會太集中。
![[Pasted image 20211016205911.png]]

優點是搜尋迅速，只需瀏覽少數資料，不必瀏覽全部資料。
```c
const int range = 5;
 
void add_number(vector<int>& table[range], int num)
{
    // 以雜湊函數決定存放位置
    int h = hash(num, range);
    // 儲存至陣列
    table[h].push_back(num);
}
 
bool find_number(vector<int>& table[range], int num)
{
    // 只需瀏覽少數資料，不必瀏覽全部資料。
    int h = hash(num, range);
    for (auto x: table[h])  // 窮舉
        if (x == num)       // 搜尋
            return true;
    return false;
}
```

### 範例：均勻隨機數字（ Uniform Random Number ）

亂數雖分散，卻不見得均勻。於是計算學家另行創造算式，偽造均勻亂數。由於需要背景知識，此處不多提。

又亂、又均勻，很匪夷所思吧！譯作亂數真的沒問題嗎？
![[Pasted image 20211016205942.png]]

C++ 程式語言的內建函式庫，已經有均勻亂數了。
```c
void random_number()
{
    // 亂數生成器
    default_random_engine g;
 
    // 均勻亂數，範圍[0, 5)。
    uniform_int_distribution<int> rand(0, 4);
 
    // 印出10個亂數，範圍是整數0到整數4。
    for (int i=0; i<10; i++)
        cout << rand(g);
}
```

### 範例：隨機抽樣（ Random Sampling ）

隨機挑選一物，機率均等。
![[Pasted image 20211016210047.png]]
```c
// 差勁的做法。不均勻。
int random_sampling(int array[], int n)
{
    srand(time(0));
    return array[rand() % n];
}
 
// 比較優秀的做法。比較均勻。
int random_sampling(int array[], int n)
{
    default_random_engine g;
    uniform_int_distribution<int> rand(0, n-1);
    return array[rand(g)];
}
```

### 範例：隨機混洗（ Random Shuffle ）

隨機排列，打亂順序，機率均等。
![[Pasted image 20211016210133.png]]
```c
void random_shuffle(int array[], int n)
{
    srand(time(0));
 
    // 數字0到n-1
    int permutate[n];
    for (int i=0; i<n; i++) permutate[i] = i;
 
    // 逐次挑出一個數字
    for (int i=0; i<n-1; i++)
    {
        // 剩下的數字，隨機挑出一個數字（的位置）。
        int j = i + rand() % (n - i);
        // 挑出的數字，挪至前面。
        swap(permutate[i], permutate[j]);
    }
 
    // 重新排列
    int temp[n];
    for (int i=0; i<n; i++) temp[i] = array[i];
    for (int i=0; i<n; i++) array[permutate[i]] = temp[i];
}
```
與其先排列再交換，不如直接交換。
![[Pasted image 20211016210153.png]]
```c
void random_shuffle(int array[], int n)
{
    srand(time(0));
 
    // 逐次挑出一個數字
    for (int i=0; i<n-1; i++)
    {
        // 剩下的數字，隨機挑出一個數字（的位置）。
        int k = i + rand() % (n - i);
        // 挑出的數字，挪至前面。
        swap(array[i], array[k]);
    }
}
```

### 範例：隨機化搜尋法（ Randomized Search ）

隨便挑一個位置，直到找到為止、直到無處可尋為止。程式可能永不結束。
![[Pasted image 20211016210251.png]]
```c
int randomized_search(int array[], int n, int num)
{
    srand(time(0));
 
    // 建立表格，記錄已經找過的位置。
    // 一開始所有位置皆未找過。
    bool visit[n] = {};
 
    // 錯誤的實作方式。
    // 程式可能永不結束，儘管機率趨近0。
    for (int i=0; i<n; i++)
    {
        int j;
        do j = rand() % n; while (visit[j]);
        if (array[j] == num) return j;
        visit[j] = true;
    }
    return -1;
}
```
從其餘位置當中隨便挑一個位置，直到找到為止、直到無處可尋為止。程式一定結束。
![[Pasted image 20211016210312.png]]
```c
int randomized_search(int array[], int n, int num)
{
    srand(time(0));
 
    for (int i=0; i<n-1; i++)
    {
        // 從其餘位置當中隨便挑一個位置
        int j = i + rand() % (n - i);
        if (array[j] == num) return j;
        // 已經找過的數字，挪至前面，永不再找。
        swap(array[i], array[j]);
    }
    return -1;
}
```
綜觀過程，是以一種順序讀取各個數字。因此隨機的計算順序，可以等價交換成隨機的輸入順序、循序的計算順序。
![[Pasted image 20211016210332.png]]
```c
int randomized_search(int array[], int n, int num)
{
    // 隨機排列
    random_shuffle(array, array+n);
 
    // 循序搜尋
    for (int i=0; i<n; i++)
        if (array[i] == num)
            return i;
    return -1;
}
int randomized_search(int array[], int n, int num)
{
    // 額外建立索引值、指標，避免改變陣列內容。
    int index[n];
    for (int i=0; i<n; i++)
        index[i] = i;
 
    // 隨機的計算順序
    random_shuffle(index, index+n);
 
    for (int i=0; i<n; i++)
        if (array[index[i]] == num)
            return i;
    return -1;
}
```

搜尋次數的期望值是 (n+1)/2 。
```
正確數字在每個位置的出現機率都一樣多，都是1/n。
正確數字出現在第1個位置，讀取第1個數字就能找到。
正確數字出現在第i個位置，讀取第i個數字才能找到。
  (1/n) × 1 + (1/n) × 2 + ... + (1/n) × n
= (1/n) × (1 + ... + n)
= (1/n) × (1+n)n/2
= (1+n)/2
```

### 範例：隨機化排序法（ Randomized Sort ）

隨便挑兩個位置，若數字順序不對則交換，直到無處可尋為止。
![[Pasted image 20211016210411.png]]

交換次數的期望值是多少呢？

只挑相鄰位置，期望值會比較少嗎？

儘管缺乏實用價值，但是如果你會分析，麻煩教我。

### 範例：矩陣乘法驗算（ Matrix Product Verification ）

矩陣乘法，通盤檢查太久，抽樣檢查較快。

第二個矩陣，隨機挑選一個向量來驗算。驗算一次，僥倖通過機率是 (n-1)/n ；驗算 k 次，僥倖通過機率是 (n-k)/n 。
![[Pasted image 20211016210434.png]]

第二個矩陣，隨機挑選多個向量，以向量總和來驗算。驗算一次，僥倖通過機率是 1/2 ；驗算 k 次，僥倖通過機率是 (1/2)ᵏ 。效果好多了。
![[Pasted image 20211016210439.png]]
```c
const int N = 10;
typedef double Matrix[N][N];
 
// Freivalds' Algorithm
bool verify_matrix_product(Matrix A, Matrix B, Matrix C)
{
    srand(time(0));
 
    // 驗算5次
    for (int t=0; t<5; t++)
    {
        // 第二個矩陣，隨機挑選多個向量。
        // 0是沒選中，1是選中。
        bool column[N] = {};
        for (int i=0; i<N; ++i)
            column[i] = rand() % 2;
 
        // 以向量總和來驗算
        // 逐次檢查各個元素
        for (int i=0; i<N; i++)
        {
            double sumAB = 0, sumC = 0;
            for (int j=0; j<N; j++)
                if (column[j])
                {
                    for (int k=0; k<N; k++)
                        sumAB += A[i][k] * B[k][j];
                    sumC += C[i][j];
                }
            if (sumAB != sumC) return false;
        }
    }
    return true;
}
```

### 範例：集合相似度（ Set Similarity ）

此處將集合相似度設為交聯比：交集大小除以聯集大小。

交集與聯集，通盤計算需額外記憶體，抽樣計算以節省記憶體。
![[Pasted image 20211016210508.png]]

集合有兩種資料結構：循序儲存、索引儲存。

如果是循序儲存，隨機挑選一個數字，判斷是不是交集元素、聯集元素。大量抽樣，統計比例。累計越多次，答案越準確。
![[Pasted image 20211016210515.png]]

陣列還可以改成雜湊表，節省搜尋時間。
```c
const int range = 10;
 
double set_similarity(vector<int>& A[range],
                      vector<int>& B[range])
{
    srand(time(0));
 
    int c = 0;  // 交集大小
    int d = 0;  // 聯集大小
 
    for (int i=0; i<5; i++) // 抽樣5次
    {
        int x = rand();
        bool inA = find_number(A, x);   // 搜尋雜湊表
        bool inB = find_number(B, x);
        if (inA && inB) c++;
        if (inA || inB) d++;
    }
 
    return (double)c / d;
}
```
如果是索引儲存，隨機抽樣改成隨機排列，然後挑選首個標記位置來比對。
![[Pasted image 20211016210535.png]]

隨機排列還可以改成雜湊函數，節省排列時間。
```c
// MinHash
double set_similarity(bool A[], bool B[], int range)
{
    int c = 0;  // 交集大小
    int d = 0;  // 聯集大小（和抽樣次數一樣，其實可以省略。）
 
    for (int i=0; i<5; i++) // 抽樣5次
    {
        // 創造新的雜湊函數（此處沒有實作，這是虛擬碼。）
        int (*hash)(int,int) = new_hash_function();
 
        int headA = 2147483647;
        for (int j=0; j<range; j++)
            if (A[j])
                headA = min(headA, hash(j, range));
 
        int headB = 2147483647;
        for (int j=0; j<range; j++)
            if (B[j])
                headB = min(headB, hash(j, range));
 
        if (headA == headB) c++;
        d++;
    }
 
    return (double)c / d;
}
```

### 範例：快速排序法（ Quicksort ）

挑選一個數字當作基準，所有數字分成大的一邊和小的一邊，遞迴下去。

無論挑選哪一個數字當作基準，最終都會得到正確結果。
![[Pasted image 20211016210600.png]]

然而，隨機挑選基準，不是最好的方式。挑選中位數當作基準，讓數字對半分，讓遞迴次數最少，才是最好的方式。

中位數無法預測。實務上是將陣列三等份，以三個中央數的中位數當作基準。因為上一層遞迴已經數字分成兩邊、大致排序過了，所以這種方式更容易接近中位數。

### 範例：平面上距離最近的兩個點（ Closest Pair ）

挑選一個點對距離當作方格寬度，建立方格紙。最近點對只會在相同方格、相鄰方格。窮舉田字，窮舉田字裡面所有點對，取距離最小者。

無論挑選哪一個距離當作寬度，最終都會得到正確結果。
![[Pasted image 20211016210618.png]]

然而，隨機挑選距離，不是最好的方式。實務上是挑選最近距離三倍以下的距離當作方格寬度。做法請參考：

https://www.cs.cmu.edu/~ckingsf/class/02713/lectures/lec31-random.pdf

### 範例：最小包圍圓（ Smallest Enclosing Circle ）

包圍所有點的圓，越小越好。做法請參考：

http://www.cs.uu.nl/docs/vakken/ga/slides4b.pdf

![[Pasted image 20211016210644.png]]
以遞增法求最小包圍圓，逐次添加一點，並且調整最小包圍圓。若新點在圓內，不做任何事；若新點在圓外，則新點一定在新圓上，但是本來的點就不一定在新圓上了。於是得到新問題：已知一點在圓上，求最小包圍圓。接著又得到新問題：已知兩點在圓上，求最小包圍圓。已知兩點時，以枚舉法掃描所有點，找到最遠的點。

添加一點的時間複雜度分成兩種情況：圓不變、圓變動。因為無法預測變動，所以窮舉各種結果、反推變動機率。各種結果是新圓上有兩點、有三點。現有 i 點、已知一點在圓上，因此新點導致新圓的機率是 (2-1)/i 、 (3-1)/i 。添加一點的平均時間複雜度是 O(1) ，添加 N 點的平均時間複雜度是 O(N) 。原始問題以此類推，平均時間複雜度 O(N) 。

#### Streaming Algorithm

現在是資訊爆炸的年代，資料不斷增加。「串流演算法」就是處理源源不絕的輸入資料。大家關注的有：
```
online：隨時處理資料，甚至隨時計算正確答案。
one-pass：只讀取一次資料，盡量計算正確答案。
memory-bounded：資料無法盡數儲存，盡量計算正確答案。
```

### 範例：統計數字數量

先排序，再統計。
![[Pasted image 20211016210720.png]]
```c
void histogram(int array[], int n)
{
    sort(array, array+n);
 
    int c = 1;
    for (int i=1; i<n; i++)
        if (array[i] != array[i-1])
        {
            // 印出統計結果
            cout << array[i-1] << ':' << c << '\n';
            // 重新計數
            c = 1;
        }
    // 印出統計結果
    cout << array[n-1] << ':' << c << '\n';
}
```
變成串流。建立陣列，根據數值大小，累計至對應位置。
![[Pasted image 20211016210742.png]]
```c
void histogram(istream& in)
{
    int c[1000000] = {};
 
    int num;
    while (in >> num)
    {
        c[num]++;
        cout << c[num];
    }
}
```
減少記憶體。格子少於數值範圍，只好使用雜湊函數。相異數字可能存入相同格子，無法精確統計。
![[Pasted image 20211016210800.png]]
```c
void histogram(istream& in)
{
    int c[10] = {}; // 統計表格，範圍0到9。
 
    int num;
    while (in >> num)
    {
        // 以雜湊函數決定累計位置。
        int h = hash(num, 10);
        c[h]++;
        cout << c[h];
    }
}
```
建立多個統計表格，使用不同雜湊函數，分散風險。推定最小值為統計結果。
![[Pasted image 20211016210819.png]]
```c
int hash1(int num) {return num % 10;}
int hash2(int num) {return num % 9;}
int hash3(int num) {return num * num % 10;}
 
// Count-Min Sketch
void histogram(istream& in)
{
    // 3個統計表格
    int c[3][10] = {};
    // 3種雜湊函數
    int (*hash[3])(int) = {hash1, hash2, hash3};
 
    int num;
    while (in >> num)
    {
        int count_min = 2147483647;
        for (int i=0; i<3; i++)
        {
            // 以雜湊函數決定累計位置，分散風險。
            int h = hash[i](num);
            c[i][h]++;
            // 取最小值
            count_min = min(count_min, c[i][h]);
        }
        cout << count_min;
    }
}
```

### 範例：相異數字個數

先排序，再統計。
![[Pasted image 20211016210841.png]]
```c
int count_distinct(int array[], int n)
{
    sort(array, array+n);
 
    int x = 0;
    if (n > 0) x = 1;
    for (int i=1; i<n; i++)
        if (array[i] != array[i-1])
            x++;
    return x;
}
```
變成串流。建立陣列，根據數值大小，累計至對應位置。
```c
void count_distinct(istream& in)
{
    int c[1000000] = {};
 
    int x = 0;
    int num;
    while (in >> num)
    {
        if (!c[num]) x++;
        c[num]++;
        cout << x;
    }
}
```
減少記憶體。格子少於數值範圍，只好使用雜湊函數。相異數字可能存入相同格子，無法精確統計。
```c
void count_distinct(istream& in)
{
    int c[10] = {}; // 統計表格，範圍0到9。
 
    int num;
    while (in >> num)
    {
        // 以雜湊函數決定累計位置。
        int h = hash(num, 10);
        if (!c[h]) x++;
        c[h]++;
        cout << x;
    }
}
```
再減少記憶體。建立二進位數值當作答案。每讀一個數字，最低位第 1 位改成 1 的機率是 1/2 ，第 i 位改成 1 的機率是 1/2ⁱ 。推定低位數連續的 1 再加一是答案。
```c
void count_distinct(istream& in)
{
    srand(time(0));
 
    unsigned int mask = 0;
    int num;
    while (in >> num)
    {
        for (int i=0; i<32; i++)
            if (rand() % (1 << i) < 1)
                mask |= (1U << i);
 
        int lsb0 = __builtin_ctz(mask + 1U);
        cout << (1 << lsb0);
    }
}
// Flajolet-Martin Sketch
void count_distinct(istream& in)
{
    unsigned int mask = 0;
    int num;
    while (in >> num)
    {
        // 簡化成每次只修改一個位數。
        // 數尾端有多少個零，修改對應位數。
        int h = hash(num, 32);
        int i = (h > 0 ? __builtin_ctz(h) : 32);
        mask |= (1U << i);
 
        // 經實驗發現除以0.77351效果很好。
        int lsb0 = __builtin_ctz(mask + 1U);
        cout << floor(double(1 << lsb0) / 0.77351));
    }
}
```

### 範例：尋找陣列裡的最小值

趁早找到最小值，不想看遍全部數字。
![[Pasted image 20211016210937.png]]

前 n/e 個，記錄最小值。第 n/e + 1 個以後，如果小於最小值，就推定為答案。

實際應用：找伴侶、買水果、炒短線。
```c
// Gilbert-Mosteller Strategy
int find_minimum(int array[], int n)
{
    int k = floor((double)n / exp(1));
    int min = 2147483647;
    for (int i=0; i<k; i++)
        if (array[i] < min)
            min = array[i];
 
    for (int i=k; i<n; i++)
        if (array[i] < min)
            return array[i];
    return min;
}
```

### 範例：隨機抽樣（ Random Sampling ）

隨機挑選一物，機率均等。
![[Pasted image 20211016211007.png]]
```c
int random_sampling(int array[], int n)
{
    srand(time(0));
    return array[rand() % n];
}
```
變成串流。使用動態陣列。
```c
void random_sampling(istream& in)
{
    vector<int> array;  // 動態陣列
 
    int num;
    for (int i=0; in >> num; i++)
    {
        array.push_back(num);
        cout << array[rand() % (i+1)];
    }
}
```
節省記憶體，只需儲存一物。從 1 開始編號，遭遇第 i 物時，儲存機率 1/i ，捨棄機率 1 - 1/i 。

最終得到第 i 物的條件是：保留第 i 物，捨棄第 i+1 物到第 n 物。機率恰是 1/n ：
```
   1           1             1                   1
  ——— × ( 1 - ——— ) × ( 1 - ——— ) × ... × ( 1 - ——— )
   i          i+1           i+2                  n 

   1     i    i+1         n-1    1
= ——— × ——— × ——— × ... × ——— = ———
   i    i+1   i+2          n     n
```   
   
最終得到各物的機率，推導過程如法炮製，機率均是 1/n 。
```c
// Reservoir Sampling
void random_sampling(istream& in)
{
    srand(time(0));
 
    int result = 0, num;
    for (int i=0; in >> num; i++)
    {
        if (rand() % (i+1) < 1)
            result = num;
        cout << result;
    }
}
```

### 範例：隨機混洗（ Random Shuffle ）

遭遇第 i 物時，第 i 物與後面挑一物對調。
![[Pasted image 20211016211108.png]]
```c
// 產生[0,x)的隨機整數。
inline int rand(int x) {return rand() % x;}
 
// 產生[x,y)的隨機整數。
inline int rand(int x, int y) {return x + rand(y - x);}
 
// Fisher-Yates Shuffle
void random_shuffle(int array[], int n)
{
    srand(time(0));
 
    for (int i=0; i<n-1; i++)
        swap(array[i], array[rand(i, n)]);
}
```
隨機混洗可以串流嗎？我也不知道。哎喲隨便啦。