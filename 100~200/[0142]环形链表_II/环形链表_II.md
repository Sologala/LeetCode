![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   �������� II
   |     linked-list-cycle-ii

*/

����һ��������������ʼ�뻷�ĵ�һ���ڵ㡣 ��������޻����򷵻� `null`��

Ϊ�˱�ʾ���������еĻ�������ʹ������ `pos` ����ʾ����β���ӵ������е�λ�ã������� 0 ��ʼ���� ��� `pos` �� `-1`�����ڸ�������û�л���

**˵����**�������޸ĸ���������

 

**ʾ�� 1��**

```
���룺head = [3,2,0,-4], pos = 1
�����tail connects to node index 1
���ͣ���������һ��������β�����ӵ��ڶ����ڵ㡣
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

**ʾ�� 2��**

```
���룺head = [1,2], pos = 0
�����tail connects to node index 0
���ͣ���������һ��������β�����ӵ���һ���ڵ㡣
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

**ʾ�� 3��**

```
���룺head = [1], pos = -1
�����no cycle
���ͣ�������û�л���
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

##**˼·��** 

#### ����1

?	hash������жϷ��ʵĵڶ���

?	���Ƿ���һ���ڵ�ͽ��ýڵ�ֵ���Ϊ���ʹ������ڶ��η��ʵ��Ѿ����ʹ��Ľڵ��ʱ�򣬾ͱ�������ڵ���ѭ�������

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



### **˼·2**

##### ����ָ��

����ͨ��һ������ ָ��������Ƿ���ѭ����֮������ͬʱ�ƶ���ָ���Լ���ͷ��㿪ʼ�ƶ���������������ʱ����ǵ�һ��ѭ���Ľڵ㡣

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