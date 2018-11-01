## play-with-data-structures

Python implementation of imooc course [玩转数据结构](https://coding.imooc.com/class/207.html), thanks for that great course (instructor [liuyubobobo](https://github.com/liuyubobobo)) !

Any pull-request is welcome:)

Any quesitons please email to wangzhe.dut@gmail.com


### Included data structures

Array 数组
Stack 栈
Queue 队列
Linked List 链表
Binary Search Tree 二分搜索树
Heap 堆

Segment Tree 线段树
Trie
Union Find 并查集

AVL
Red Black Tree 红黑树
Hash Table 哈希表


### Some course notes

二叉堆：
- 堆中任意节点的值一定小于等于其父节点的值（最大堆）
- 用数组实现即可
- 对于任意节点i，左孩子是2 * i + 1, 右孩子是2 * i + 2，父节点(i - 1) // 2 （因为索引从0开始）
- 添加元素时候，先在最下面的最左边添加一个元素，再执行sift_up操作
- sift_up: 新添加的节点和父亲节点比较，交换，再递归重复（因为如果新节点的值比父亲节点大，则一定比父亲节点的另一个节点大，大于号保持不变性）
- extract_max_heap: 取出堆顶的值，并将最小层最左边的元素移到堆顶，再执行sift_down
- sift_down: 每次要下沉的元素和两个孩子比较，和两个孩子中最大的交换位置，再递归重复
- replace: 取出一个最大的，再放入一个新元素，set 0 index，再从0开始sift_down
- heapify: 将任意数组整理成堆的形状, 从最后一个非叶子节点开始计算，倒着从后向前sift_down即可 (算法复杂度是O(n)的！！！)
- 最后一个非叶子节点：先拿到最后一个节点的索引，计算它的父亲节点的索引即可(再递归所有非叶子节点)！！！
- d叉堆 d-ary heap
- 索引堆：可以看到堆中间的元素（最短路径和Dijkstra中可能用到）
- 二项堆，斐波那契堆
- 广义队列（普通队列，优先队列，随机队列，栈也可以理解成一个队列）

线段树：O(logn)
- 区间染色
- 区间查询(动态不停的更新和查询), 区间本身固定
- 线段树不是完全二叉树，但是是一棵平衡二叉树（任何节点的左右深度之差小于等于1）
- 第h层（h从0开始）：h层有2 ** h - 1个节点
- 如果区间有n个元素，则4n的空间足以

Trie:
- 重点应用是查询前缀

UnionFind
- 连接问题
- union(e1, e2), query(e1, e2)
- use array for implementation
- 可以基于size优化
- 可以基于rank优化
- 路径压缩(发生在find操作中顺便进行)
- 查询合并都是O(h)
- 并查集的优势是在合并查询都有的场景

AVL
- G.M.Adelson-Velsky and E.M.Landis
- 自平衡二分搜索树
- 对于任意一个节点，左子树和右子树的高度差不能超过1
- 平衡因子：叶子节点为0，非叶子节点左右子树高度差
- 左旋转，右旋转，在插入节点的时候造成了不平衡 LL, RR
- 插入的元素在不平衡的节点的左侧的左侧 -> 右旋转，将下图的B作为新节点
```
          A
        /
      B
    /
new node
```
- LR和RL LR -> LL, RL -> RR
```
          A
         /
        B
         \
      new node
```

红黑树
- 红黑树也是平衡二分搜索树，统计性能更好
- 1. 每个节点要么是红色，要么是黑色
- 2. 根节点是黑色的
- 3. 每一个叶子节点（最后的空节点）是黑色的(空节点既是根节点，又是叶子节点，是黑色的)
- 4. 如果一个节点是红色的，那么他的孩子节点都是黑色的(why? because red node's parent MUST BE BLACK!!!, so a red node can not be the parent node of another red node)
- 5. 从任意一个节点到叶子节点，经过的黑色节点数目是一样的(红色节点不一定一样多)，因为1）绝对平衡，高度一致，2）不算红色节点
- 算法4（作者Robert Sedgewick即红黑树发明人之一）
- Donald Knuth的弟子(The art of computer Programming, TAOCP)
- 23树：节点可以存放一个元素或者两个元素, 2节点，3节点, 2-3树是一棵绝对平衡的树(从根节点到任意一个叶子节点经过的节点数目都是相同的)
- 23树永远不会添加新节点到一个空的位置上(找最后一个叶子节点)
- why 23 tree === r-b tree? 红色节点相当于表示它和它父亲节点等效于23树种的3节点！！！所有的红色节点都是左倾斜的。
- 23树中的2节点即黑节点，3节点即红-黑节点（红在左边）
- 如果经常添加，删除，红黑树性能高于AVL
- 所有的红节点都是向左倾斜的
- 红黑树中添加新元素：左旋转 -> 右旋转 -> 颜色翻转
- 红黑树删除节点（太复杂）

哈希表
- 设计哈希函数，key通过哈希函数得到的index分布越均匀越好
- 哈希冲突处理
- 大整数：取模（可能造成分布不均匀，直接丢弃了部分数字的信息）-> 模一个素数
- 空间换时间
- 一致性，高效性，均匀性
- hash冲突可以使用链地址法解决 (seperate chaining)
- hash(-121211) & 0x7fffffff % M  0x7fffffff (f == 1111, 7 == 111，一共是31个1 == 2147483647，相当于抹去了最高位符号位的1)
- 哈希表开了M个空间，对于冲突的元素以链表（或者TreeMap, TreeSet）形式插入
- 平均每个地址承载的元素多过一定程度，即扩容 N/M >= upper_tol
- 平均每个地址承载的元素少过一定程序，即缩容 N/M < lower_tol
- 开放地址法，不必马上插入相同hash的链表中，放入下一个空白的位置即可(线性探测，平方探测，二次哈希),这样可以使得数组整体被使用率比较高（负载率高，均匀度高）
- 再哈希法（rehashing）
- coalesced hashing（综合了sperate chaining和open addressing）


### Miscellaneous

平摊分析：Amortized Analysis, resize时候会引入。
remove_last时resize太过着急，出现复杂度震荡，使用lazy方案：
扩容2倍，缩容1/4（错开）

删除任意节点：
1. 叶子节点
2. 只有左孩子或者只有右孩子
3. 既有做孩子又有右孩子（* Hibbard Deletion *）:找被删节点右子树中方的最左节点（最小值）来代替

完全二叉树：不一定是满二叉树，但是缺失的节点一定是在树的右下侧

满二叉树：除了叶子节点，所有节点既有左孩子又有右孩子

图结构：邻接表和邻接矩阵（建图比较简单，但是可以应用图的存储结构的一些性质做一些很好的应用）

抽象数据结构：类似于接口的思想