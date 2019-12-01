![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`117`]**填充每个节点的下一个右侧节点指针 II**|**populating-next-right-pointers-in-each-node-ii**

*/

给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

示例：输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/117_sample.png)



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### **Solution** 

使用两个队列来对二叉树进行层次遍历，这里二叉树的结构里面包含了next指针，就可以直接使用二叉树的节点来作为队列的元素。

也就是链式队列。

### **ac_code**
```c
class Solution {
public:
    Node* connect(Node* root) {
        int cur = 0;
        Node q[2];
        q[cur].next =root;
        while(1){
            Node* p = q[cur%2].next;
            q[(cur+1) % 2].next = NULL;
            if(p == NULL) break;
            Node * t = &q[(cur+1) %2];
            while(p){
                if(p->left){
                    t->next =p->left;
                    t = t->next;
                }
                if(p->right){
                    t->next =p->right;
                    t = t->next;
                }
                p = p->next;
            }
            cur = cur + 1;
        }
        return root;
    }
};
```