import urllib2
contents = urllib2.urlopen("https://databros.uksouth.cloudapp.azure.com/cron/daily").read()
print contents