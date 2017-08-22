# user

|字段|类型|含义|
|----|----|---|
|_id| Object||
|name| str|名字|
|password|md5|密码
|sport|list|运动列表|
|sport_log|list|运动日志|


# log

|字段|类型|含义|
|----|----|---|
|_id| Object||
|day|time|记录时间|
|time|time|运动时间
|sport|id|运动|
|counts|int,str|总数|
|remarks|str|备注|
|group_nums|list|运动分组次

# sport

|字段|类型|含义|
|----|----|---|
|_id| Object||
|name|str|运动名|
|group_num|int|建议次数
|guide|str|指导url|
|img_url|str|标准指导图
