from flask import Flask, render_template, request

app = Flask(__name__)
#file name = storage
@app.route("/")
def index():
    global dir
    dir = "root/files/"
    val = request.args.get("name")
    meth = request.args.get("choice")
    text = request.args.get("textarea")
    dir = dir + str(val)
    if dir != "root/files/None" and text != None:
        print(dir)
        if meth == "read":
            print("I am going to read the text file")
            print(text)
            print(type(text))
            with open(str(val), "r") as file:
                return render_template("index.html", output=file.read())
        if meth == "write":
            print(text)
            print(type(text))            
            with open(str(val), "w") as file:
                file.write(str(text))
                return render_template("index.html")
            print("I am going to write to the text file")
    
    return render_template("index.html", value=val)

#I am incredibly close, i just need to make it so the text area is changed to not none, so make it in the same form
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
