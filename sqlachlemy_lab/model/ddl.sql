create table py_orm (
    `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '唯一id',
    `name` varchar(255) NOT NULL DEFAULT '' COMMENT '名称',
    `attr` JSON NOT NULL COMMENT '属性',
    `ct` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `ut` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON update CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY(`id`)
)ENGINE=InnoDB COMMENT '测试表';
