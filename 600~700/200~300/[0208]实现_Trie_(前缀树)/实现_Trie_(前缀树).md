![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)

/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git

   [208]实现 Trie (前缀树)
     |     implement-trie-prefix-tree

*/

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true



## **Solution** 

前缀树的结构

```c
struct Node{
    bool isWord = false;
    Node* next[26] = {};
};
```

用指针来标志着是那个字母。

使用之前我们新建一个节点作为`root` 

查询的时候就是直接根据单词的每个字母一层一层往下搜索就行了，当半路断掉之后机会证明没有这个单词，或者如果遇到的最后一个节点的 `isWord== false` 那么也证明不是一个单词 只是一个前缀而已。

### **ac_code**
```c
struct Node{
    bool isWord = false;
    Node* next[26] = {};
};
class Trie {
public:

    Node* root ;
    Trie() {
       root = new Node();
    }

    void insert(string word) {
        Node* p = root;
        for(int i = 0;i<word.size();++i){
            if(p->next[word[i]- 'a'] == NULL){
                p->next[word[i]- 'a'] = new Node();
            }
            p = p->next[word[i]- 'a']; 
        }
        p->isWord  = true;
    }
   
    bool search(string word) {
        Node* p = root;
        for(int i = 0;p&&i<word.size();i++){
            p = p->next[word[i]- 'a'];
        }
        return p!=NULL&&p->isWord;
    }

    bool startsWith(string prefix) {
        Node* p = root;
        for(int i = 0;p&&i<prefix.size();i++){
            p = p->next[prefix[i]- 'a'];
        }
        return p!=NULL;
    }
};

```