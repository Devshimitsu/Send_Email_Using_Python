import smtplib 
  
semailid = input("\nSender Email ID: ")

spass = input("\nSender Email ID PassWord: ")

remailid = input("\nReceiver Email ID: ")

mess = input("\nType Your Message Here: ")

try:
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login(semailid, spass) 
	s.sendmail(semailid, remailid, mess) 
	s.quit() 
	

except:
	print("Something Went Wrong!")

#BY_DEVSHIMITSU