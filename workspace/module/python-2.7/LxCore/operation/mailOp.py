# coding=utf-8
import smtplib
#
import traceback
#
from email.mime.text import MIMEText
#
from LxBasic import bscMtdCore, bscMethods

from LxPreset import prsOutputs, prsMethods
#
from email.header import Header
#
timeOut = 15
#
none = ''


#
def getPipeMail():
    mailEnabled = prsOutputs.Util.pipeMailEnabled
    if mailEnabled:
        mailServer = prsOutputs.Util.pipeMailServer
        mailPot = prsOutputs.Util.pipeMailPort
        mailAddress = prsOutputs.Util.pipeMailAddress
        mailPassword = prsOutputs.Util.pipeMailPassword
        return mailServer, int(mailPot), mailAddress, str(mailPassword)


#
def datum(toMails, summary, subject, information):
    user = bscMethods.OsPlatform.username()
    userMail = prsMethods.Personnel.userMail()
    cnName = prsMethods.Personnel.userChnname()
    team = prsMethods.Personnel.userTeam()
    #
    fromMessage = '''%s by %s Team's [ %s ( %s ) ] < %s >''' % (summary, team, user, cnName, userMail)
    message = MIMEText(information, 'html', 'utf-8')
    message["Accept-Language"] = 'zh-CN'
    message["Accept-Charset"] = 'ISO-8859-1,utf-8'
    message['Subject'] = Header(subject, 'utf-8').encode()
    message['From'] = fromMessage
    message['To'] = ';'.join(toMails)
    return message


#
def getToMails():
    userMail = prsMethods.Personnel.userMail()
    toMails = [userMail]
    teamLeaders = prsMethods.Personnel.usernamesFilterByPost('Team - Leader')
    if teamLeaders:
        for i in teamLeaders:
            mail = prsMethods.Personnel.userMail(i)
            toMails.append(mail)
    return toMails


#
def sendMail(toMails, summary, subject, information):
    mailData = getPipeMail()
    if mailData:
        mailServer, mailPort, mailAddress, mailPassword = mailData
        print 'Server : ', mailServer
        print 'Port : ', str(mailPort)
        print 'From : ', mailAddress
        print 'Password : ', mailPassword
        print 'To : ', toMails
        message = datum(toMails, summary, subject, information)
        smtplib.socket.setdefaulttimeout(timeOut)
        try:
            server = smtplib.SMTP_SSL()
            # server = smtplib.SMTP()
            server.connect(mailServer, mailPort)
            server.set_debuglevel(1)
            server.login(mailAddress, mailPassword)
            server.sendmail(mailAddress, toMails, message.as_string())
            server.quit()
            print 'Mail Send Complete'
            return True
        except Exception, e:
            print str(e)
            print traceback.format_exc()
            return False
