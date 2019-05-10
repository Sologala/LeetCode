![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   LRU�������
   |     lru-cache

*/

�����������յ����ݽṹ����ƺ�ʵ��һ��  [LRU (�������ʹ��) �������](https://baike.baidu.com/item/LRU)����Ӧ��֧�����²����� ��ȡ���� `get` �� д������ `put` ��

��ȡ���� `get(key)` - �����Կ (key) �����ڻ����У����ȡ��Կ��ֵ�����������������򷵻� -1��
д������ `put(key, value)` - �����Կ�����ڣ���д��������ֵ�������������ﵽ����ʱ����Ӧ����д��������֮ǰɾ���������ʹ�õ�����ֵ���Ӷ�Ϊ�µ�����ֵ�����ռ䡣

**����:**

���Ƿ������ **O(1)** ʱ�临�Ӷ�����������ֲ�����

**ʾ��:**

``` c
LRUCache cache = new LRUCache( 2 /* �������� */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // ����  1
cache.put(3, 3);    // �ò�����ʹ����Կ 2 ����
cache.get(2);       // ���� -1 (δ�ҵ�)
cache.put(4, 4);    // �ò�����ʹ����Կ 1 ����
cache.get(1);       // ���� -1 (δ�ҵ�)
cache.get(3);       // ����  3
cache.get(4);       // ����  4
```

##**˼·��** 

?	��ҪO(1)��ά���Ļ� ���ǿ���ʹ��һ��ѭ��˫�˶��У����˫�˶�������ά�����ݵ�˳�򣬶�������Ҫ���ٵļ�������Ҫ�Ľڵ��ʱ�� ������һ�� (`unordered_map<node*,int>`) ��ӳ��������һ����ϵ���Ϳ���O(1) ���õ�����ڵ㡣

?	����ʹ����һ����ͷ�ڵ��ѭ���б� ͷ���� `val` ֵ������� �������е� ���ȣ�ͨ��������ȵĲ�ͬ��������Ҫ������ͬ���жϣ����統���������ǿջ���û������ʱ�򣬾�ֱ�Ӳ��룬����Ѿ�������Ҫȥ������Ƿ�������ڵ㣬����оͽ�����ڵ��ƶ�����ͷ���������Ǿ���Ҫ�ó�����û��ʹ�õ��Ǹ��ڵ㣬���������ֵ�޸ģ��ٲ����ͷ��

### **ac_code**
```c
struct node{
    int val = 0;
    int key = 0;
    node* pre = NULL,*next = NULL;
};
class LRUCache {
public:
    unordered_map<int,node*> m;//����ӳ��
    node* head;
    int max_len = 0;
    LRUCache(int capacity) {
        max_len = capacity;
        head = new node();
        head->next = head;
        head->pre = head;
        head->val = 0;
    }
    int getlen(){
        return head->val;
    }
    int get(int key) {
        node * p = m[key];
        if(p==NULL||getlen()==0) return -1;//can`t find 
        //�Ͽ�
        p->pre->next = p->next;
        p->next->pre = p->pre;
        //���뵽�ʼ
        p->next = head->next;
        head->next->pre = p; 
        p->pre = head;
        head->next = p;
        return p->val;
    }
    void put(int key, int value) {
        node * p =m[key];
        if(p==NULL){//û��
            int len = getlen();
            if(len<max_len){//��û�����½�һ���ڵ�
                p = new node();
                head->val++;
            }
            else{//���ˣ�ȥ��������ʹ�õ�
                p = head->pre;
                m[p->key] = NULL;
                //�Ͽ�
                p->pre->next = p->next;
                p->next->pre = p->pre;
            }
        }
        else{//�Ѿ�����,�Ͽ�
            p->pre->next = p->next;
            p->next->pre = p->pre;
        }
        p->key = key;
        p->val = value;
        m[key] = p; 
        //���뵽�ʼ
        p->next = head->next;
        head->next->pre = p; 
        p->pre = head;
        head->next = p;
    }

    void show(){
        node * p = head->next;
        while(p&&p!=head){
            cout<<"["<<p->key<<":"<<p->val<<"] --> ";
            p = p ->next;
        }   
        cout<<endl;
    }
};
```