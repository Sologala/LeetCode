![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   两数之和 IV - 输入 BST
   |     two-sum-iv-input-is-a-bst

*/

给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

**案例 1:**

```
输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
```

##**Solution** 

二叉搜索树寻找两个数字之和等于 `target`,由二叉搜索树 的中序遍历已经排好序,并且满足 左子树的所有节点一定小于父节点,右子树的所有结点一定大于父节点. 

我们可以在找寻根节点的时候先去找 `target - root->val`  并且在查询的时候要把所有遇到的节点都放到一个 `hashmap ` 里面存储起来.并且会判断当前这个节点 的值 是否在之前出现过 `target -  root->val` 如果出现过就 `return true` 否则 就去遍历左子树, 这种时候就只需要判断是否出想过与当前节点相对应的值.

### **ac_code**
```c

class Solution {
public:
    unordered_map<int,int> m;
    
    bool find(TreeNode* root,int k,int rig){
        if(!root) return false;
        
        if(k>0){
            if(root->val == k) return true;
        }
        if(m[rig-root->val]) return true;
        m[root->val] ++;
        return find(root->left,k,rig)||find(root->right,k,rig);
    }
    
    bool findTarget(TreeNode* root, int k) {
        if(!root) return false;
        int f = k-root->val;
        m[root->val] ++;
        if(f>root->val){
            if(find(root->right,f,k)) //右边找 f
                return true;
            else
                return find(root->left,-1,k);//左边看是否又配对
        }
        else{
            if(find(root->left,f,k))//左边找与 root  对应的 f
                return true;
            else 
                return find(root->right,-1,k);//右边是否有对应的.
        }
        return false;            
    }
};
```