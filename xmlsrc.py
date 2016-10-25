class xmlsrc:
    confile = ""
    KEY="key"
    ATTR="attr"
    ELEM="elem"
    NEXT_CONF="next_conf"
    CSV_ASSOCIATE_FIELD="csv_associate_field"

    def __init__(self, filename):
        self.confile = filename

    def read_conf(self):
        import ConfigParser
        cfg = ConfigParser.ConfigParser()
        cfg.read(self.confile)
        return cfg

    def get_node_list(self):
        cfg = self.read_conf()
        nodestr = cfg.get('node','nodelist')
        nodelist = nodestr.split(',')
        return nodelist

    def get_section_list(self):
        cfg = self.read_conf()
        section_fieldstr = cfg.get('node','section_field')
        section_fieldlist = section_fieldstr.split(',')
        return section_fieldlist

    def get_section_info(self,section):
        cfg = self.read_conf()
        info = {}
        section_fieldlist = self.get_section_list()
        for option in section_fieldlist:
            value = cfg.get(section, option)
            if option == 'attr' or option == 'elem':
                ret = [] if value == '' else value.split(',')
                info.setdefault(option, ret)
            else:
                info.setdefault(option, value)
        return  info

    def get_associate_node_list(self):
        nodelist = self.get_node_list()
        associate_node_list = []
        cfg = self.read_conf()
        for nodestr in nodelist:
            if cfg.has_section(nodestr):
                associate_node_list.append(nodestr)
        return associate_node_list

    def has_section(self,section):
        cfg = self.read_conf()
        return cfg.has_section(section)

    def gen_node_index_map(self):
        nodelist = self.get_node_list()
        n = 0
        node_index_map = {}
        for nodestr in nodelist:
            node_index_map[nodestr] = n
            n += 1
        return node_index_map

    def parse_dict_str(self, ele_str):
        if ele_str.find(':') == -1:
            return {}
        if ele_str.find('{') == -1 and ele_str.find('}') == -1:
            ele_str = '{' + ele_str
            ele_str += '}'
        import math
        d = eval(ele_str)
        print(d)
        return d


if __name__ == '__main__':
    from xmlsrc import xmlsrc
    xmlconf = xmlsrc("xml.conf")
    ele_str = '{"1401":5}'
    xmlconf.parse_dict_str(ele_str)
    exit(0)
    print(xmlconf.get_node_list())
    print(xmlconf.get_section_list())
    print(xmlconf.get_section_info('fb'))
