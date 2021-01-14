import jieba

s = '大家好我是長博，我旁邊是博母，我常常看到他就勃起'
s1_list = jieba.cut(s,cut_all = True)
s2_list = jieba.cut(s,cut_all = False)
s3_list = jieba.cut(s)
s4_list = jieba.cut(s,cut_for_search(s))

print('|'.join(s1_list))
print('|'.join(s2_list))
print('|'.join(s3_list))
print('|'.join(s4_list))