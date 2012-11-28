
import re

def insert(context, body, match, after):
    i = body.find(match)
    if i < 0:
        context.log("could not insert!")
        return body
    else:
        return body[:(i+len(match))] + after + body[(i+len(match)):]
    

def response(context, flow):
    if re.match('^/books/OL[0-9]+[MW]/.*', flow.request.path):
        context.log("matched page")
        body = flow.response.content
        m = re.search('http://worldcat.org/isbn/([0-9]+)', body)
        if m:
            isbn = m.groups()[0]
            context.log("found isbn: %s" % isbn)
            flow.response.content = insert(context,
                body,
                '<span class="icon read"></span>',
"""
        <span class="head">Read Locally</span>
    </h3>
    <div class="panel">
        <p><strong><a href="http://libgen.org/search?req=%s&nametype=orig&column%%5B%%5D=identifier">Search libgen</a></strong><br></p>
    </div>
</div>
<div>
    <h3 class="header">
        <span class="icon read"></span>""" % isbn)
        else:
            context.log("no isbn found")
