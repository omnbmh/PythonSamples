import coweibo.mysql
import coweibo.redis
import coweibo.http

print coweibo.mysql.search("SELECT  `uid`,  `name`,  `email`,  LEFT(`password`, 256),  `gender`,  LEFT(`head_url`, 256),  LEFT(`description`, 256),  `register_at`,  `credit_accumulate`,  `credit_effective`,  `grade_id` FROM `sos`.`user` LIMIT 1000")