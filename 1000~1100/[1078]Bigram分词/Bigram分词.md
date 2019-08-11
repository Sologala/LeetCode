![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`1078`]**Bigram分词**|**orrurrences-after-bigram**

*/

给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，third 紧随 second 出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

 

示例 1：

输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]
示例 2：

输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/occurrences-after-bigram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## **Solution** 

依次从`text`中读取一个单词，然后和`first` `second` 比较，并且我们是需要先有`frist` 之后再有`second`  因此我们需要使用一个 `tag` 来表示当前已经有了的单词的数量。

### **ac_code**
```c
class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        int tag  = 0 ;
        stringstream ss(text);
        string t;
        vector<string> ret;
        while(ss>>t){
            if(tag == 2) ret.push_back(t),tag = 0;
            
            if(t==first) tag = 1;
            else if(tag==1&&t==second) tag = 2;
            else tag = 0;
        }
        return ret;
    }
};
```