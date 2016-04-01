CREATE TABLE `user_agents` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `agent_cd` varchar(40) UNIQUE NOT NULL,
  `agent_name` varchar(40),
  `category` varchar(40),
  `name` varchar(40),
  `version` varchar(40),
  `os_name` varchar(40),
  `vendor` varchar(40),
  `os_version` varchar(40),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=144 DEFAULT CHARSET=utf8;
