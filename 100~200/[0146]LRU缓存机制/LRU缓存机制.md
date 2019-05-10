![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   LRU缓存机制
   |     lru-cache

*/

运用你所掌握的数据结构，设计和实现一个  [LRU (最近最少使用) 缓存机制](https://baike.baidu.com/item/LRU)。它应该支持以下操作： 获取数据 `get` 和 写入数据 `put` 。

获取数据 `get(key)` - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 `put(key, value)` - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

**进阶:**

你是否可以在 **O(1)** 时间复杂度内完成这两种操作？

**示例:**

``` c
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
```

##**思路：** 

?	想要O(1)来维护的话 我们可以使用一个循环双端队列，这个双端队列用来维护数据的顺序，而我们想要快速的检索到想要的节点的时候 可以用一个 (`unordered_map<node*,int>`) 来映射这样的一个关系，就可以O(1) 的拿道这个节点。

?	这里使用了一个带头节点的循环列表 头结点的 `val` 值代表的是 整个队列的 长度，通过这个长度的不同，我们需要做出不同的判断，比如当整个队列是空或者没有满的时候，就直接插入，如果已经满就需要去查表找是否有这个节点，如果有就将这个节点移动到对头，否则，我们就需要拿出最早没有使用的那个节点，将他里面的值修改，再插入对头。

### **ac_code**
```c
struct node{
    int val = 0;
    int key = 0;
    node* pre = NULL,*next = NULL;
};
class LRUCache {
public:
    unordered_map<int,node*> m;//用于映射
    node* head;
    int max_len = 0;
    LRUCache(int capacity) {
        max_len = capacity;
        head = new node();
        head->next = head;
        head->pre = head;
        head->val = 0;
    }
    int getlen(){
        return head->val;
    }
    int get(int key) {
        node * p = m[key];
        if(p==NULL||getlen()==0) return -1;//can`t find 
        //断开
        p->pre->next = p->next;
        p->next->pre = p->pre;
        //插入到最开始
        p->next = head->next;
        head->next->pre = p; 
        p->pre = head;
        head->next = p;
        return p->val;
    }
    void put(int key, int value) {
        node * p =m[key];
        if(p==NULL){//没有
            int len = getlen();
            if(len<max_len){//还没有满新建一个节点
                p = new node();
                head->val++;
            }
            else{//满了，去拿最近最不常使用的
                p = head->pre;
                m[p->key] = NULL;
                //断开
                p->pre->next = p->next;
                p->next->pre = p->pre;
            }
        }
        else{//已经存在,断开
            p->pre->next = p->next;
            p->next->pre = p->pre;
        }
        p->key = key;
        p->val = value;
        m[key] = p; 
        //插入到最开始
        p->next = head->next;
        head->next->pre = p; 
        p->pre = head;
        head->next = p;
    }

    void show(){
        node * p = head->next;
        while(p&&p!=head){
            cout<<"["<<p->key<<":"<<p->val<<"] --> ";
            p = p ->next;
        }   
        cout<<endl;
    }
};
```