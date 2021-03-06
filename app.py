from flask import Flask,render_template,request,url_for
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests





def sendDiscordAlertMEDS(phnum, cityname, dets):
	webhook = DiscordWebhook(url="https://discord.com/api/webhooks/837944145652875294/FXQNLdBNkDjMcsAHrpYSAKRQUii7sucKAxmCWkeXGcboydghjCJTXiTnWpRPC3J4GwZJ", username="CoVBot")
	embed = DiscordEmbed(
		title="Resource Request", description="Hello Peeps! We just received a request on our portal for MEDICINES!", color='03b2f8'
	)
	embed.set_author(
		name="CoVBot",
		url="https://www.edctiet.com/",
		icon_url="https://freedesignfile.com/upload/2017/12/Alert-Icon.jpg",
	)
	embed.set_footer(text="Let's try to find the above mentioned resources as soon as possible!")
	embed.set_timestamp()
	# Set `inline=False` for the embed field to occupy the whole line
	embed.add_embed_field(name="Contact Number", value=phnum)
	embed.add_embed_field(name="City", value=cityname)
	embed.add_embed_field(name="Requirement", value=dets, inline=False)


	webhook.add_embed(embed)
	response1 = webhook.execute()
	return response1

def sendDiscordAlertOXY(phnum, cityname):
	webhook1 = DiscordWebhook(url="https://discord.com/api/webhooks/837944145652875294/FXQNLdBNkDjMcsAHrpYSAKRQUii7sucKAxmCWkeXGcboydghjCJTXiTnWpRPC3J4GwZJ", username="CoVBot")
	embed = DiscordEmbed(
		title="Resource Request", description="Hello Peeps! We just received a request on our portal for OXYGEN!", color='03b2f8'
	)
	embed.set_author(
		name="CoVBot",
		url="https://www.edctiet.com/",
		icon_url="https://freedesignfile.com/upload/2017/12/Alert-Icon.jpg",
	)
	embed.set_footer(text="Let's try to find the above mentioned resources as soon as possible!")
	embed.set_timestamp()
	# Set `inline=False` for the embed field to occupy the whole line
	embed.add_embed_field(name="Contact Number", value=phnum)
	embed.add_embed_field(name="City", value=cityname)


	webhook1.add_embed(embed)
	response2 = webhook1.execute()
	return response2

def sendDiscordAlertCON(phnum, deets):
	webhook2 = DiscordWebhook(url="https://discord.com/api/webhooks/837944145652875294/FXQNLdBNkDjMcsAHrpYSAKRQUii7sucKAxmCWkeXGcboydghjCJTXiTnWpRPC3J4GwZJ", username="CoVBot")
	embed = DiscordEmbed(
		title="Resource Request", description="Hello Peeps! We just received a request on our portal for CONSULTATION!", color='03b2f8'
	)
	embed.set_author(
		name="CoVBot",
		url="https://www.edctiet.com/",
		icon_url="https://freedesignfile.com/upload/2017/12/Alert-Icon.jpg",
	)
	embed.set_footer(text="Let's try to find the above mentioned resources as soon as possible!")
	embed.set_timestamp()
	# Set `inline=False` for the embed field to occupy the whole line
	embed.add_embed_field(name="Contact Number", value=phnum)
	embed.add_embed_field(name="Query", value=deets,inline=False)


	webhook2.add_embed(embed)
	response3 = webhook2.execute()
	return response3

application = app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/medicines', methods=['POST',  'GET'])
def medicines():
	msg = ""
	lable = ""
	phoneNum = request.form['medPhoneNum']
	usrCity = request.form.get('medCity')
	
	medDet = request.form['medDetails']
	if (phoneNum == "" or usrCity == None):
		msg = "Please enter all nesessary Details!"
		lable = "danger"
		return hello_world()
	else:
		msg = "Thank You! We get back to you with the resource details!"
		lable = "info"
	usrCity = usrCity.replace(" ", "")
	sendDiscordAlertMEDS(phoneNum, usrCity, medDet)
	return render_template("index.html", msg=msg, lable=lable)

@app.route('/oxygen', methods=['POST',  'GET'])
def oxygen():
	msg = ""
	lable = ""
	phoneNum1 = request.form['oxyPhoneNum']
	usrCity1 = request.form.get('oxyCity')
	

	if (phoneNum1 == "" or usrCity1 == None):
		msg = "Please enter all nesessary Details!"
		lable = "danger"
		return render_template("index.html", msg=msg, lable=lable)
	else:
		msg = "Thank You! We get back to you with the resource details!"
		lable = "info"
	usrCity1 = usrCity1.replace(" ", "")
	sendDiscordAlertOXY(phoneNum1, usrCity1)

	return render_template("index.html", msg=msg, lable=lable)

@app.route('/consultation', methods=['POST',  'GET'])
def consultation():
	msg = ""
	lable = ""
	phoneNum2 = request.form['consultNum']
	medDet2 = request.form['queryCon']
	if (phoneNum2 == ""):
		msg = "Please enter all nesessary Details!"
		lable = "danger"
		return render_template("index.html", msg=msg, lable=lable)
	else:
		msg = "Thank You! We get back to you with the resource details!"
		lable = "info"
	sendDiscordAlertCON(phoneNum2, medDet2)

	return render_template("index.html", msg=msg, lable=lable)

@app.errorhandler(404)
def page_not_found(e):
    return(render_template('404.html'), 404)

@app.errorhandler(500)
def page_error(e):
    return(render_template('404.html'), 500)
if __name__ == '__main__':
	app.run(debug=False)
