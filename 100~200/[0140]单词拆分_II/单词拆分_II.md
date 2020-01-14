![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`140`]**单词拆分 II**|**word-break-ii**

*/



## **Solution** 

```c
“catsand”
["cat","cats","sand"]
```



#### Point 1：字典树

由于需要使用单词 `worddict` 来查询分割的单词，于是想到使用字典树对`worddict`进行重建，可以加速之后的查询。

<img src="https://tva1.sinaimg.cn/large/006tNbRwly1gakj2imwygj30gw0miab0.jpg" alt="image-20200104144701379" style="zoom:25%;" />

随后从第一个位置开始**dfs** 并且向后搜索，但是这样会超时，因为有大量重复的`aaa`

#### point 2：dp

由于直接**dfs**是不可取的，于是选择先对于字符串dp一次然后反过来**dfs**，至于为什么会反过来dfs 是因为

![image-20200104144539685](https://tva1.sinaimg.cn/large/006tNbRwly1gakj14xav3j30we09kab7.jpg)

对于**DFS**从前向后的搜索会在字典树上面进行搜索到下一个合适的位置然后递归再次寻找，这其中会重复查看很多步骤。`aaaaaaaaaaaaaaaaaaaaa`  `Dict : {"a","aaa",aaaa"}`这样去搜索会很费时间。

于是可以先`dp`一次计算出每个位置的前一个可能的位置，并且在dp的过程中也要记录下来是否能够到达第一个字符。只有能够到达第一个字符的才能够分割。

最后开始**dfs** 从最后一个字符开始搜索，可以看作一棵树。

### **ac_code**
```c
struct Node{
    bool isWord = false;
    Node* next[26] = {};//指向26个下一个节点
};	
void insert(Node* root ,string& s){
    for(int i = 0;i<s.size();++i){
        if(root->next[s[i]- 'a'] == NULL){
            root->next[s[i]- 'a'] = new Node();
        }
        root = root->next[s[i]- 'a']; 
    }
    root->isWord  = true;
}
class Solution {
public:
    Node * d = new Node;
    vector<string> ret;
    vector<vector<short>> dp;
    vector<string> st;
    void dfs(string & s, int i ){
        if(i<0){
            string res;
            for(int k =  0;k < st.size();++k){
                if(k) res =" " + res;
                res = st[k] + res;
            }
            ret.push_back(res);
            return;
        }
        for(int j = 0 ;j < dp[i].size();++j){
            st.push_back(s.substr(dp[i][j] , i - dp[i][j]+1));
            dfs(s,dp[i][j]-1);
            st.pop_back();
        }
    }
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        if(wordDict.size()  == 0||s.size() == 0) return {};
        //建立字典树 用来加速
      	for(auto w : wordDict){
            insert(d,w);
        }
        dp.resize(s.size()+1,vector<short>());
        //iscover 表示是否能够到达字符串首
        vector<bool> iscover(s.size(),false);
        iscover[0] = (d->next[s[0] - 'a']&&d->next[s[0] - 'a']->isWord);
        for(int i = 0 ; i< s.size() ; ++i){
            int j = i;
            Node * p = d->next[s[j] - 'a'];
            while(j<s.size()&&p){
                if(p->isWord == true && ((i==0)||(i>0&&iscover[i-1]))){
                    dp[j].push_back(i);
                    iscover[j] = true;
                }
                if(j+1<s.size())
                    p =  p -> next[s[++j] - 'a'];
                else break;
            }
        }
      	//判断是否可以完成分割
        if(iscover[s.size()-1] ==false ) return {};
        dfs(s,s.size()-1);
        return ret;
    }
};
```