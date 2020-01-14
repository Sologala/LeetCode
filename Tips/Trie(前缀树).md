# 前缀树(字典树)

​	通常我们使用 `hash`  来解决判断一个单词是否又出现，但是如果问题变成了判断一个单词的`前缀(prefix)` 是否又出现过，使用`hash` 就显得尤为棘手，要表示一个单词的`prefix` 显然我们应该想到树形结构。

​	如果我们把一些单词表现称为下列的形式：
​		

![Trie树](https://s2.ax1x.com/2019/07/10/ZckkJH.jpg)

​	当我们需要找寻一个前缀的时候只需要从根节点开始向下查询，但是我们儿还是需要标记一下这个节点是否是一个单词，还是一个前缀。

​	于是我们的`Trie` 的结构如下：

```c
struct Node{
    bool isWord = false;
    Node* next[26] = {};//指向26个下一个节点
    int cnt = 0； //表示当前节点有几个子节点
};	
```

##  基本操作

1. #### 插入

    	插入的时候我们只需要根据我们需要插入的单词的每一个字母，一直往下，如果是空结点我们就补上。

   ​	最后一个节点要注意我们要将他的 `isWord ` 置为 `true`;

   ```c
   void insert(Node* root,string s){
       for(int i = 0;i<s.size();++i){
           if(root->next[s[i]- 'a'] == NULL){
               root->next[s[i]- 'a'] = new Node();
               root->cnt++;//更新cnt
           }
           root = root->next[s[i]- 'a']; 
       }
       root->isWord  = true;
   }
   ```

2. #### 查询单词

   ​	查询单词可以写成一个递归的过程也可以是非递归的，下面是一个非递归的写法。

   ```c
   bool search(Node* root,string s){
       for(int i = 0;root&&i<s.size();i++){
           root = root->next[s[i]- 'a'];
       }
       return root!=NULL&&root->isWord;//查找的是一个单词
   }
   ```

   ​	那么要注意我们需要查询的是一个单词，如果只是到了一个 `isWord == false` 的节点 ，这仅仅表明这是一个前缀，而不是一个单词。

3. #### 查询前缀

   ​	与上面的查询一个单词很类似，只不过条件放松了很多，我们只需要判断最后一个是否是`NULL` 

   ```c
   bool search_prefix(Node* root, string s){
       for(int i = 0;root&&i<s.size();i++){
           root = root->next[s[i]- 'a'];
       }
       return root!=NULL;//查找一个前缀
   }
   ```

   

4. #### 删除单词

   ​	删除的时候一定是删除一个单词，而且我们不能删除一些公共的前缀，比如你要删除 `append` 那么前面的 `app` 你是不能删除的。

   ​	

   ```c
   void delete_word(Node* root,string s ){
       Node* stk[1000];
       int top = -1, j = s.size()-1;
       if(root->cnt== 0) return;
       //找寻要删除的节点
       for(int i = 0;root&&i<s.size();i++){
           stk[++top] = root;
           root = root->next[s[i]- 'a'];
       }
       if(root==NULL||root->isWord ==false) return;//没有找到
       stk[++top] = root;//最后一个节点没有入站
       while(top > 0){
           if((--(stk[top]->cnt) ) <= 0){//如果该节点没有孩子了
               delete stk[top];//释放空间
               stk[top-1]->next[s[j]-'a'] = NULL;//父节点指向空
           }
           top -- ;
           j--;
       }
   }
   ```

   

   ​	删除的过程我们需要记录下父节点的信息，于是这里我们使用了一个 `Node* stk[1000];`  来表示栈 ，然后去循环查询想要删除的单词，如果没有找到就直接 `return`。

   ​	找到之后就需要根据当前节点的`cnt` 来更新父节点的信息，如果删除一个之后他的 `cnt <=0 ` 了就表明这个当前节点需要释放掉。于是 `delete ` . 同时还需要更新 父节点的 `next`

   