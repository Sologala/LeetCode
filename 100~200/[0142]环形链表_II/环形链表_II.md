![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   环形链表 II
   |     linked-list-cycle-ii

*/

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 `null`。

为了表示给定链表中的环，我们使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 `pos` 是 `-1`，则在该链表中没有环。

**说明：**不允许修改给定的链表。

 

**示例 1：**

```
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

**示例 2：**

```
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

**示例 3：**

```
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

##**思路：** 

#### 做法1

?	hash打表来判断访问的第二次

?	我们访问一个节点就将该节点值标记为访问过，当第二次访问到已经访问过的节点的时候，就表明这个节点是循环的起点

```c
   ListNode *detectCycle(ListNode *head) {
        unordered_map<ListNode*,int> m;
        int idx = 1;
        while(head!=NULL){
            if(m[head]!=0){return head;}
            m[head] = idx++;
            head = head->next;
        }
        return NULL;
    }
```



### **思路2**

##### 快慢指针

我们通过一个快慢 指针来检测是否有循环，之后我们同时移动满指针以及从头结点开始移动，当两个相遇的时候就是第一个循环的节点。

```c
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* f = head,*s = head;
        while(1){
            if( !f||!f->next) return NULL;
            s = s->next;
            f = f->next->next;
            if(s==f) break;
        }
        
        f = head;
        while(s != f){
            s = s->next;
            f = f->next;
        }
        return s;
    }
};
```