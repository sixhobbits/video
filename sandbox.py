import youtube_dl
title = "test"
link = "http://www.youtube.com/watch?v=a1Y73sPHKxw"

#print(youtube_dl.main(['-f', '85/84/83/82/38/37/22/18/120/35/34','-o','/home/gareth/video/uploads/' + title  + '.%(ext)s', link, '-s', '--get-filename']))
#youtube_dl.main([link, '--all-format', '--get-filename', '--get-format'])

print "-----------------"


print (youtube_dl.main([link, '--all-format',  '--get-format']))

print (12345)