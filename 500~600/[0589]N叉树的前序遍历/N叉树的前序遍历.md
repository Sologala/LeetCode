![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git

   [589]N叉树的前序遍历
     |     n-ary-tree-preorder-traversal

*/

给定一个 N 叉树，返回其节点值的*前序遍历*。

例如，给定一个 `3叉树` :

 

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png)

 

返回其前序遍历: `[1,3,5,6,2,4]`。

## **Solution** 

递归办法很简单,非递归的时候我们要是到一个`stack`  这个`栈` 里面我们要装我们的根节点.

在循环里面主要做一下两件事情

```c
1.出栈根节点 非空即访问.
2.将该根节点所有的子树都压栈.
```

但是由于我们的栈保持一个 `先进后出` 的规律,因此我们需要反过来遍历`root->children`这个`vector`.

### **ac_code**
```c
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> ret;
        stack<Node* > s;
        s.push(root);
        while(!s.empty()){
            root = s.top();s.pop();
            if(!root) continue;
            ret.push_back(root->val);
            for(int i = root->children.size()-1;i>=0;--i){
                s.push(root->children[i]);
            }
        }
        return ret;
    }
};
```