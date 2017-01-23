

of = 'dnsmasq.conf.hosts'

# 读取hosts文件
infile = open('hosts.2015-10-17','r')

# 写入dnsmasq配置文件
outfile = open(of,'w')

for ipline in infile:
    print ipline




