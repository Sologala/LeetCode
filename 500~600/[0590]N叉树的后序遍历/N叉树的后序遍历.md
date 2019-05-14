![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   N叉树的后序遍历
   |     n-ary-tree-postorder-traversal

*/

给定一个 N 叉树，返回其节点值的*后序遍历*。

例如，给定一个 `3叉树` :

 

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png)

 

返回其后序遍历: `[5,6,3,2,4,1]`.

 

**说明:** 递归法很简单，你可以使用迭代法完成此题吗?

##**思路** 

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
    vector<int> ret;
    void post(Node* root){
        if(root==NULL) return;
        for(int i = 0;i<root->children.size();++i){
            post(root->children[i]);
        }
        ret.push_back(root->val);
    }
    vector<int> postorder(Node* root) {
        post(root);
        return ret;        
    }
};
```

#### 非递归版本

```c++
#define par pair<Node*,int> // 0: travel 1: output
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> ret;
        if(!root) return ret;        
        stack<par> s;
        s.push(par(root,0));
        while(!s.empty()){
            par cur = s.top();s.pop();
            if(cur.second==1){
                ret.push_back(cur.first->val);
                continue;
            }
            s.push(par(cur.first,1));
            for(int i = cur.first->children.size()-1;i>=0;--i){
                s.push(par(cur.first->children[i],0));
            }
        }
        return ret;        
    }
};
```

