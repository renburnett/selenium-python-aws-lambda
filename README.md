## Selenium Python on AWS Lambda with chrome webdriver
### Forked from @ManivannanMurugavel

- All necessary files and dependencies for Python, Selenium and the Chrome webdriver were forked from @ManivannanMurugavel's repo 
- The implementation for the actual webscraper was written by yours truly (; 

1. Zip this all of these files together
2. Upload them to an AWS bucket 
3. When configuring your Lambda function, point it to the URL of the zip file
4. Configure the event object to hold your URL:  i.e.  event = {'url' : 'kexp.com/playlist'}
5. Test it!





