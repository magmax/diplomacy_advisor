#!/usr/bin/env python

import httplib
import HTMLParser
import re
from datetime import datetime, timedelta
import ConfigParser
import smtplib
from email.mime.text import MIMEText

def retrieve_page(config):
    conn = httplib.HTTPConnection(config.get('game', 'host'))
    try:
        conn.request("GET", config.get('game', 'uri'))
        response = conn.getresponse()
        return response.read()
    finally:
        conn.close()


def send_email(config, to, subject, body):
    if not to:
        print "Skipped mail to ", subject
        return
    print (config, to, subject, body)
    msg = MIMEText(body)

    me = config.get('smtp', 'user')

    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = to
    msg['List-Id'] = "Diplomacy advisor"

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP(config.get('smtp', 'host'))
    s.ehlo()
    s.starttls()
    s.login(me, config.get('smtp', 'password'))
    s.sendmail(me, to, msg.as_string())
    s.quit()

config = ConfigParser.ConfigParser()
config.read('advisor.cfg')


left = None
countries = {}
for line in retrieve_page(config).splitlines():
    m = re.match('.*timeremaining.*\sunixtime="(\d+)".*\sunixtimefrom="(\d+)"', line)
    if m:
        current = datetime.fromtimestamp(int(m.group(2)))
        end = datetime.fromtimestamp(int(m.group(1)))
        left = end - current
        continue
    m = re.match('.*memberCountryName.*\salt="([^\"]+)".*\smemberStatusPlaying"\s*>([A-Za-z]+)<', line)
    if m:
        countries[m.group(2)] = m.group(1)


if left.total_seconds() < int(config.get('game', 'hours')) * 3600:
    for country, status in countries.items():
        if status == 'Not received':
            message = (
                "Hello, {}.\n\nYou are getting out of time for the game in http://{}{}.\n\n"
                "You only have {} to move!!"
                .format(country, config.get('game', 'host'), config.get('game', 'url'), left)
            )
            send_email(config, config.get('email', country), "[Diplomacy] You are getting out of time!", message)
            print 'Hurry up, {}!!'.format(config.get('email', country))
print "Only {} left!".format(left)
