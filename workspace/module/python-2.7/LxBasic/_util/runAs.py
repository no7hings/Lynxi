# coding:utf-8
import os, subprocess


#
class cmdRunAs(object):
    def __init__(self, commandExe, commandArgv):
        self._programExe = 'lsrunase.exe'
        self._user = 'dongchangbao'
        self._password = 'vQ=='
        self._domain = ''
        self._commandExe = commandExe
        self._commandDirectory = os.path.dirname(self._commandExe)
        self._commandArgv = commandArgv
    # User
    @property
    def user(self):
        return self._user
    #
    @user.setter
    def user(self, s):
        if s:
            if not isinstance(s, str) or isinstance(s, unicode):
                raise ValueError('UserName must be String or Unicode')
            #
            self._user = s
    # Password
    @property
    def password(self):
        return self._password
    #
    @password.setter
    def password(self, s):
        if s:
            if not isinstance(s, str) or isinstance(s, unicode):
                raise ValueError('Password must be String or Unicode')
            #
            self._password = s
    # Domain
    @property
    def domain(self):
        return self._domain
    #
    @domain.setter
    def domain(self, s):
        if s:
            if not isinstance(s, str) or isinstance(s, unicode):
                raise ValueError('Domain must be String or Unicode')
            #
            self._domain = s
    # Run Command
    def run(self):
        command = \
            '''"%s" /user:%s /password:%s /domain:%s /command:%s /runpath:%s''' % (
            self._programExe,
            self._user,
            self._password,
            self._domain,
            '''"%s %s"''' % (self._commandExe, ' '.join(self._commandArgv)),
            self._commandDirectory)
        #
        subprocess.call(command, shell=True)
