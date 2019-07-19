# So this is what I have so far.  Issue being the for loop:


    @app.route("/")
    def index():
        url = "https://www.wsj.com/"
        req = requests.get(url)

        soup = BeautifulSoup(req.text, "html.parser")
        container = soup.find("div", {"layout": "LS-NO-IMAGE-SPOTLIGHT-SEVEN"})
        containers = container.find_all("article")

        article_content = dict()
        article_content["headline"] = container.find("h3").find("a").text

        article_info = dict()
        for i in containers:
            article_info[i.find("h3").find("a").text] = i.find_all(
                "p", {"class": "WSJTheme--summary--12br5Svc"}
            )
        return render_template(
            "index.html", article_content=article_content["headline"], content=article_info
        )

    
This is the HTML Flask code I'm using for the site:

    <ul class="list-simple-styled">
                    {% for k in content %}
                    <li>
                        <span>{{k}}</span>
                    </li>
                    <li>
                        {{content[k]}}
                    </li><br><br>
                    {% endfor %}
                </ul>
 
 As it stands the code produces a list of all the headlines and their summaries which is what I'm going for.
 
    Iran Rebuffs Trump Assertion That U.S. Ship Downed Drone
    [<p class="WSJTheme--summary--12br5Svc ">Iran denied that the U.S. Navy downed one of its drones in the Strait of Hormuz,
    a day after several close encounters between American warships and the Iranian military in the vital oil shipping route 
    further raised tensions.<span class="WSJTheme--stats--2waJk-ql ">
    <span class="WSJTheme--timestamp--21reayKL WSJTheme--red-timestamp--qefOYS5r WSJTheme--red-timestamp--qefOYS5r ">2 minutes 
    ago</span></span></p>] 

***I've put the code on new lines for reading sake***
 
 The problem is trying to get the text from the 'p' tag. When I add .text() .getText() :
 
      article_info[i.find("h3").find("a").text] = i.find_all(
            "p", {"class": "WSJTheme--summary--12br5Svc"}
        ).text
 
 It gives me this errorr:
      AttributeError: 'NoneType' object has no attribute 'text'
      
 The odd thing is also when I try using find() and find_all, it sometimes gives me this error:
      AttributeError: ResultSet object has no attribute 'text'. 
      You're probably treating a list of items like a single item. 
      Did you call find_all() when you meant to call find()?
      
 I can't find anything on Stackoverflow or anywhere about this problem.
 Even when searching how to get the text from 'p' tags, implement that code,
 the same errors pop up.
