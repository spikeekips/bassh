import re


class Config (object, ) :
    RE_HOST = re.compile('^host[\s][\s]*(?P<name>.*)$')

    def __init__ (self, f, ) :
        self._f = f

    def parse (self, ) :
        if type(self._f, ) in (str, unicode, ) :
            _f = file(self._f, )
        else :
            _f = self._f

        _f.seek(0, 0, )
        _found = dict()

        _name = None
        for i in _f :
            _i = i.strip()
            if not _i :
                continue

            _r = self.RE_HOST.search(_i, )
            if not _name and not _r :
                continue

            if _name and not _r :
                _found[_name] += i
                continue

            _name = self._parse_host(_r.groupdict().get('name'), )
            _found[_name] = str()

        return _found

    def _parse_host (self, s, ) :
        if '#' not in s :
            return s

        return s[:s.index('#')].strip()



if __name__ == '__main__' :
    import StringIO

    _config_content = """
#ControlMaster auto
ControlPath /tmp/ssh_mux_%h_%p_%r
TCPKeepAlive no
ServerAliveInterval 120

host 127.0.0.1
    StrictHostKeyChecking=no
    UserKnownHostsFile=/dev/null
host localhost
    StrictHostKeyChecking=no
    UserKnownHostsFile=/dev/null

host seolin-office
    Hostname localhost
    StrictHostKeyChecking=no
    UserKnownHostsFile=/dev/null
    Port 2200

host home
    Hostname 192.168.0.2
    """

    _config = Config(StringIO.StringIO(_config_content, ), )
    _d = _config.parse()
    for k, v in _d.items() :
        print '...........................'
        print '>', k
        print v


