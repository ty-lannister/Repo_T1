ADD NEW BELOW:


A) Input: 1|aaa|111|2|bbb|222|3|ccc|333
output: 
1 aaa 111
2 bbb 222
3 ccc 333


|Product|Amount|Country|
+-------+------+-------+
| Banana| 1000| USA|
|Carrots| 1500| USA|
| Beans| 1600| USA|
| Orange| 2000| USA|
| Orange| 2000| USA|
| Banana| 400| China|
|Carrots| 1200| China|
| Beans| 1500| China|
| Orange| 4000| China|
| Banana| 2000| Canada|
|Carrots| 2000| Canada|
| Beans| 2000| Mexico|
+-------+-----+-------+
Output
+-------+------+-----+------+----+
|Product|Canada|China|Mexico| USA|
+-------+------+-----+------+----+
| Orange| null| 4000| null|4000|
| Beans| null| 1500| 2000|1600|
| Banana| 2000| 400| null|1000|
|Carrots| 2000| 1200| null|1500| 

Given two strings of equal length, map each unique character in str1 to the character at the same index in str2 (preserving existing mappings), and use this mapping to transform str1 into a new string final_output.

str1 = 'hljljq'
str2 = 'abcdef'


final = list(zip(str1,str2))

mapping = {}

for x in final:
    if x[0] in mapping:
        pass
    else:
        mapping[x[0]] = x[1]




final_output = ''
for x in str1:
    final_output = final_output + mapping[x]

print(final_output)



Get a column ""isProficient"" and add 1 if sum of the skills from below table > 3 else add 0 
name | skills
-----------------
John | {""s0"": ""0.0"", ""s1"": ""1.0"",""s2"": ""0.0"", ""s3"": ""1.0""}
Mary | {""s0"": ""1.0"", ""s1"": ""1.0"",""s2"": ""1.0"", ""s3"": ""1.0""}
Alex | {""s0"": ""1.0"", ""s1"": ""0,0"",""s2"": ""0.0"", ""s3"": ""1.0""}
## Client Interview Round:
